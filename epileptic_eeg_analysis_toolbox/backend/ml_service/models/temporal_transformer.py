"""
Sanchez Transformer - versión autocontenida (un solo archivo).

Une layers.py + sanchez_transformer_model.py sin imports relativos.
Los nombres de módulos/atributos son idénticos al original, así que el
state_dict de sanchez_transformer_final_model.pt carga sin cambios.

Config por defecto = sanchez_transformer_config_used.json:
  window 10 s @ 256 Hz -> 2560 muestras, clasificación por ventana
  (time_step=False), 16 features con FiLM, sin SE / Koopman / recon.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, Optional

import torch
from torch import nn
from torch.nn import functional as F


# ----------------------------------------------------------------- layers
class SEBlock1d(nn.Module):
    def __init__(self, channels: int, se_ratio: int = 16) -> None:
        super().__init__()
        reduced = max(1, channels // se_ratio)
        self.pool = nn.AdaptiveAvgPool1d(1)
        self.fc1 = nn.Linear(channels, reduced)
        self.fc2 = nn.Linear(reduced, channels)

    def forward(self, x: torch.Tensor) -> torch.Tensor:  # x: (B, T, C)
        z = self.pool(x.transpose(1, 2)).squeeze(-1)
        z = F.relu(self.fc1(z))
        z = torch.sigmoid(self.fc2(z)).unsqueeze(1)
        return x * z


class FiLM1d(nn.Module):
    def __init__(self, channels: int, feat_dim: int | None = None) -> None:
        super().__init__()
        feat_dim = int(feat_dim or channels)
        self.g = nn.Linear(feat_dim, channels)
        self.b = nn.Linear(feat_dim, channels)

    def forward(self, x: torch.Tensor, feat: torch.Tensor) -> torch.Tensor:
        gamma = self.g(feat).unsqueeze(1)
        beta = self.b(feat).unsqueeze(1)
        return gamma * x + beta


class AttentionPooling1d(nn.Module):
    def __init__(self, channels: int) -> None:
        super().__init__()
        self.score = nn.Linear(channels, 1)

    def forward(self, x: torch.Tensor) -> torch.Tensor:  # x: (B, T, C)
        w = torch.softmax(self.score(x), dim=1)
        return torch.sum(w * x, dim=1)


# ----------------------------------------------------------------- model
@dataclass
class TransformerOutputs:
    logits: torch.Tensor
    probabilities: torch.Tensor
    aux_losses: Dict[str, torch.Tensor]


class SeparableConv1d(nn.Module):
    def __init__(self, in_channels: int, out_channels: int, kernel_size: int, stride: int = 1) -> None:
        super().__init__()
        padding = kernel_size // 2
        self.depthwise = nn.Conv1d(in_channels, in_channels, kernel_size, stride=stride,
                                   padding=padding, groups=in_channels, bias=False)
        self.pointwise = nn.Conv1d(in_channels, out_channels, kernel_size=1, bias=False)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        return self.pointwise(self.depthwise(x))


class AddCLSToken(nn.Module):
    def __init__(self, embed_dim: int) -> None:
        super().__init__()
        self.cls = nn.Parameter(torch.zeros(1, 1, embed_dim))
        nn.init.trunc_normal_(self.cls, std=0.02)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        return torch.cat([self.cls.expand(x.size(0), -1, -1), x], dim=1)


def _apply_rotary_embedding(q: torch.Tensor, k: torch.Tensor):
    if q.size(-1) % 2 != 0:
        raise ValueError("head_dim debe ser par para RoPE.")
    _, _, t, d = q.shape
    half_dim = d // 2
    positions = torch.arange(t, device=q.device, dtype=q.dtype).unsqueeze(-1)
    idx = torch.arange(half_dim, device=q.device, dtype=q.dtype).unsqueeze(0)
    inv_freq = 1.0 / (10000.0 ** (idx / half_dim))
    angles = positions * inv_freq
    sin = torch.sin(angles).unsqueeze(0).unsqueeze(0)
    cos = torch.cos(angles).unsqueeze(0).unsqueeze(0)

    def _rotate(x: torch.Tensor) -> torch.Tensor:
        x1, x2 = torch.chunk(x, 2, dim=-1)
        return torch.cat([x1 * cos - x2 * sin, x1 * sin + x2 * cos], dim=-1)

    return _rotate(q), _rotate(k)


class MultiHeadSelfAttentionRoPE(nn.Module):
    def __init__(self, embed_dim: int, num_heads: int, attn_dropout: float = 0.1) -> None:
        super().__init__()
        if embed_dim % num_heads != 0:
            raise ValueError("embed_dim debe ser divisible por num_heads.")
        self.embed_dim = embed_dim
        self.num_heads = num_heads
        self.head_dim = embed_dim // num_heads
        self.scale = self.head_dim ** -0.5
        self.wq = nn.Linear(embed_dim, embed_dim)
        self.wk = nn.Linear(embed_dim, embed_dim)
        self.wv = nn.Linear(embed_dim, embed_dim)
        self.wo = nn.Linear(embed_dim, embed_dim)
        self.dropout = nn.Dropout(attn_dropout)
        self.softmax = nn.Softmax(dim=-1)
        self.mask_value = -1e9

    def _split_heads(self, x: torch.Tensor) -> torch.Tensor:
        b, t, _ = x.shape
        return x.view(b, t, self.num_heads, self.head_dim).permute(0, 2, 1, 3).contiguous()

    def _combine_heads(self, x: torch.Tensor) -> torch.Tensor:
        b, h, t, d = x.shape
        return x.permute(0, 2, 1, 3).reshape(b, t, h * d)

    def forward(self, x: torch.Tensor, mask: torch.Tensor | None = None) -> torch.Tensor:
        q = self._split_heads(self.wq(x))
        k = self._split_heads(self.wk(x))
        v = self._split_heads(self.wv(x))
        q, k = _apply_rotary_embedding(q, k)
        logits = torch.matmul(q, k.transpose(-1, -2)) * self.scale
        if mask is not None:
            if mask.dim() == 2:
                mask = mask.unsqueeze(1).unsqueeze(1)
            mask = mask.to(dtype=logits.dtype)
            logits = logits + (1.0 - mask) * self.mask_value
        attn = self.dropout(self.softmax(logits))
        return self.wo(self._combine_heads(torch.matmul(attn, v)))


class TransformerBlock(nn.Module):
    def __init__(self, embed_dim: int, num_heads: int, mlp_dim: int, dropout_rate: float) -> None:
        super().__init__()
        self.attn = MultiHeadSelfAttentionRoPE(embed_dim, num_heads, attn_dropout=dropout_rate)
        self.attn_dropout = nn.Dropout(dropout_rate)
        self.attn_norm = nn.LayerNorm(embed_dim)
        self.mlp = nn.Sequential(
            nn.Linear(embed_dim, mlp_dim),
            nn.GELU(),
            nn.Dropout(dropout_rate),
            nn.Linear(mlp_dim, embed_dim),
        )
        self.mlp_dropout = nn.Dropout(dropout_rate)
        self.mlp_norm = nn.LayerNorm(embed_dim)

    def forward(self, x: torch.Tensor, mask: torch.Tensor | None = None) -> torch.Tensor:
        x = self.attn_norm(x + self.attn_dropout(self.attn(x, mask=mask)))
        return self.mlp_norm(x + self.mlp_dropout(self.mlp(x)))


class TransformerClassifier(nn.Module):
    """Entrada: x (B, T, C) y feat (B, feat_input_dim). Salida: TransformerOutputs."""

    def __init__(
        self,
        input_dim: int = 19,          # canales EEG (montaje AR) -> verifica con tu checkpoint
        *,
        num_classes: int = 1,
        embed_dim: int = 128,
        num_layers: int = 4,
        num_heads: int = 4,
        mlp_dim: int = 256,
        dropout_rate: float = 0.1,
        time_step_classification: bool = False,
        use_se: bool = False,
        se_ratio: int = 16,
        feat_input_dim: Optional[int] = 16,
    ) -> None:
        super().__init__()
        if embed_dim % num_heads != 0:
            raise ValueError("'num_heads' debe dividir 'embed_dim'.")

        self.num_classes = num_classes
        self.time_step = time_step_classification
        self.feat_dim = feat_input_dim if feat_input_dim and feat_input_dim > 0 else None

        # CNN frontend (T/4)
        self.conv1 = SeparableConv1d(input_dim, 64, kernel_size=7, stride=2)
        self.bn1 = nn.BatchNorm1d(64)
        self.conv2 = SeparableConv1d(64, 128, kernel_size=7, stride=2)
        self.bn2 = nn.BatchNorm1d(128)
        self.se_after_cnn = SEBlock1d(128, se_ratio=se_ratio) if use_se else None

        self.proj = nn.Linear(128, embed_dim)
        self.proj_dropout = nn.Dropout(dropout_rate)
        self.cls_token = AddCLSToken(embed_dim)
        self.initial_film = FiLM1d(embed_dim, self.feat_dim) if self.feat_dim else None

        self.blocks = nn.ModuleList(
            [TransformerBlock(embed_dim, num_heads, mlp_dim, dropout_rate) for _ in range(num_layers)]
        )
        self.block_se = nn.ModuleList(
            [SEBlock1d(embed_dim, se_ratio=se_ratio) if use_se and i in (0, num_layers - 1) else nn.Identity()
             for i in range(num_layers)]
        )
        self.block_films = (
            nn.ModuleList([FiLM1d(embed_dim, self.feat_dim) for _ in range(num_layers)]) if self.feat_dim else None
        )

        # No se usan en el forward (solo servían a las pérdidas auxiliares),
        # pero se conservan para que el state_dict cargue con strict=True.
        self.latent_proj = nn.Linear(embed_dim, embed_dim)
        self.latent_norm = nn.LayerNorm(embed_dim)

        if self.time_step:
            self.ts_head = None
            self.ts_classifier = nn.Linear(embed_dim, num_classes)
        else:
            self.attention_pool = AttentionPooling1d(embed_dim)
            self.win_dropout = nn.Dropout(dropout_rate)
            self.win_head = None
            self.win_classifier = nn.Linear(embed_dim * 2, num_classes)

    def forward(self, x: torch.Tensor, feat: Optional[torch.Tensor] = None) -> TransformerOutputs:
        if x.dim() != 3:
            raise ValueError("La entrada debe tener forma (B, T, C).")
        if self.feat_dim and feat is None:
            raise RuntimeError("Se requieren features para FiLM.")

        y = x.transpose(1, 2)
        y = F.gelu(self.bn1(self.conv1(y)))
        y = F.gelu(self.bn2(self.conv2(y)))
        y = y.transpose(1, 2)
        if self.se_after_cnn is not None:
            y = self.se_after_cnn(y)

        z = self.cls_token(self.proj_dropout(self.proj(y)))
        if self.initial_film is not None:
            z = self.initial_film(z, feat)

        for i, block in enumerate(self.blocks):
            z = block(z)
            if self.block_films is not None:
                z = self.block_films[i](z, feat)
            z = self.block_se[i](z)

        if self.time_step:
            logits = self.ts_classifier(z[:, 1:, :])
        else:
            pooled = torch.cat([z[:, 0, :], self.attention_pool(z[:, 1:, :])], dim=-1)
            pooled = self.win_dropout(pooled)
            logits = self.win_classifier(pooled).unsqueeze(1)  # (B, 1, num_classes)

        return TransformerOutputs(logits=logits, probabilities=torch.sigmoid(logits), aux_losses={})


def load_model(ckpt_path: str, input_dim: int = 19, device: str = "cpu") -> TransformerClassifier:
    model = TransformerClassifier(input_dim=input_dim)
    state = torch.load(ckpt_path, map_location=device)
    if isinstance(state, dict):  # por si viene envuelto
        for key in ("model_state_dict", "state_dict", "model"):
            if key in state and isinstance(state[key], dict):
                state = state[key]
                break
    model.load_state_dict(state, strict=True)
    return model.to(device).eval()


if __name__ == "__main__":
    model = TransformerClassifier(input_dim=19).eval()
    x = torch.randn(2, 2560, 19)   # (B, T=10s*256Hz, C)
    feat = torch.randn(2, 16)      # 16 features seleccionadas (escaladas)
    with torch.no_grad():
        out = model(x, feat)
    print("logits:", out.logits.shape, "probs:", out.probabilities.squeeze().tolist())
    print("params:", sum(p.numel() for p in model.parameters()))