"""
# File: aitrics_cnn_lstm.py
# Project: Trabajo de graduación

CNN2D + LSTM real-time seizure detector (Lee et al., CHIL 2022), adapted to this repo.
Includes binary and multilabel classification according to the input.
Handles feature extraction flatten for Classic ML.
"""
import json
import time
from pathlib import Path

import numpy as np
import pandas as pd
import torch
import torch.nn as nn
from sklearn.metrics import roc_auc_score
from torch.utils.data import DataLoader

# Configuraciones globales y de preprocesamiento
from src.core.data_config import (
    NORMALIZE_CLIP, 
    SFREQ, 
    ENC_CHOICES, 
    N_CHANNELS, 
    PSD_BANDS, 
    RAW_SCALE_UV,
    SPEC_FRAME, 
    SPEC_HOP, 
    SPEC_NFFT, 
    WINDOWS_REQUESTS_SEIZURES
)

# Utilidades de ventanas y extracción desde el caché
from src.core.windowing import taxonomy_intervals, mask_from_intervals, window_labels
from src.utils.session_cache import get_or_compute_session

def n_windows(L, win, shift):
    """Calcula el número de ventanas posibles dadas la longitud de la señal, la ventana y el salto."""
    return (L - win) // shift + 1 if L >= win else 0

def get_device():
    return torch.device("cuda" if torch.cuda.is_available() else "cpu")

def _conv(i, o, k, s, p, drop=0.1):
    layers = [nn.Conv2d(i, o, k, s, p), nn.BatchNorm2d(o), nn.ReLU(inplace=True)]
    if drop:
        layers.append(nn.Dropout(drop))
    return nn.Sequential(*layers)

class SeizureCNNLSTM(nn.Module):
    def __init__(self, enc="psd", n_ch=N_CHANNELS, sfreq=SFREQ, 
                 win_s=WINDOWS_REQUESTS_SEIZURES["win_sec"], shift_s=WINDOWS_REQUESTS_SEIZURES["shift_sec"],
                 hidden=256, n_layers=2, dropout=0.1, n_out=1, flatten_for_ml=False):
        super().__init__()
        assert enc in ENC_CHOICES, enc
        self.enc, self.n_ch = enc, n_ch
        self.win, self.shift = int(win_s * sfreq), int(shift_s * sfreq)
        self.n_fft, self.hop, self.frame = SPEC_NFFT, SPEC_HOP, SPEC_FRAME
        self.flatten_for_ml = flatten_for_ml

        if enc not in ("raw", "downsampled"):
            assert self.n_fft == int(sfreq), "bins de 1 Hz: n_fft debe ser igual a sfreq"
            assert self.frame <= self.n_fft
            assert shift_s * sfreq > self.hop, "si shift == hop, unfold devuelve Nw+1 ventanas"

        assert self.win % self.hop == 0 and self.shift % self.hop == 0, "windows must align to the STFT hop"
        self.fpw, self.fps = self.win // self.hop, self.shift // self.hop
        self.register_buffer("stft_win", torch.hamming_window(self.frame))

        d = dropout
        if enc == "raw":
            self.features = nn.Sequential(_conv(1, 64, (1, 51), (1, 4), (0, 25), d), nn.MaxPool2d((1, 4)),
                                          _conv(64, 128, (1, 21), (1, 2), (0, 10), d),
                                          _conv(128, 256, (1, 9), (1, 2), (0, 4), d))
        elif enc == "downsampled":
            self.branches = nn.ModuleList([_conv(1, 32, (1, 51), (1, 4), (0, 25), 0),
                                           _conv(1, 16, (1, 51), (1, 2), (0, 25), 0),
                                           _conv(1, 16, (1, 51), (1, 1), (0, 25), 0)])
            self.features = nn.Sequential(nn.MaxPool2d((1, 4)), _conv(64, 128, (1, 21), (1, 2), (0, 10), d),
                                          _conv(128, 256, (1, 9), (1, 1), (0, 4), d))
        elif enc == "psd":
            k = len(PSD_BANDS)
            self.features = nn.Sequential(_conv(1, 64, (k, 21), (k, 2), (0, 10), d),
                                          _conv(64, 128, (1, 21), (1, 2), (0, 10), d), nn.MaxPool2d((1, 2)),
                                          _conv(128, 256, (1, 9), (1, 1), (0, 4), d))
        else:                                                # stft1 / stft2
            nb = 50 if enc == "stft1" else 100
            self.features = nn.Sequential(_conv(1, 64, (nb, 3), (nb, 1), (0, 1), d),
                                          _conv(64, 128, (1, 51), (1, 2), (0, 25), d), nn.MaxPool2d((1, 4)),
                                          _conv(128, 256, (1, 9), (1, 1), (0, 4), d))
        self.pool = nn.AdaptiveAvgPool2d((1, 1))
        
        if not self.flatten_for_ml:
            self.lstm = nn.LSTM(256, hidden, n_layers, batch_first=True, dropout=d if n_layers > 1 else 0.0)
            
        self.classifier = nn.Sequential(nn.Linear(hidden if not self.flatten_for_ml else 256, 64), 
                                        nn.BatchNorm1d(64), nn.ReLU(inplace=True),
                                        nn.Linear(64, n_out))

    def _windows(self, x):
        """x [B, C, L] (uV) -> windows [B*Nw, 1, H, W], Nw. L = (Nw-1)*shift + win."""
        B, C, L = x.shape
        if self.enc in ("raw", "downsampled"):
            xs = (x / RAW_SCALE_UV).clamp(-NORMALIZE_CLIP, NORMALIZE_CLIP)
            w = xs.unfold(2, self.win, self.shift)                       # [B, C, Nw, win]
            Nw = w.shape[2]
            return w.permute(0, 2, 1, 3).reshape(B * Nw, 1, C, self.win), Nw
        spec = torch.stft(x.reshape(B * C, L), n_fft=self.n_fft, hop_length=self.hop, win_length=self.frame,
                          window=self.stft_win, center=True, return_complex=True).abs()
        spec = torch.log(spec + 1e-10)                                   # [B*C, F, Ft], 1 Hz bins
        if self.enc == "psd":
            spec = torch.stack([spec[:, a:b].mean(1) for a, b in PSD_BANDS], dim=1)       # [B*C, 7, Ft]
        else:
            spec = spec[:, :50 if self.enc == "stft1" else 100]
        K = spec.shape[1]
        w = spec.unfold(2, self.fpw, self.fps)                           # [B*C, K, Nw, fpw]
        Nw = w.shape[2]
        w = w.reshape(B, C, K, Nw, self.fpw).permute(0, 3, 1, 2, 4).reshape(B * Nw, 1, C * K, self.fpw)
        return w, Nw

    def _encode(self, w):
        if self.enc == "downsampled":
            w = torch.cat([self.branches[0](w), self.branches[1](w[..., ::2]), self.branches[2](w[..., ::4])], 1)
        return self.pool(self.features(w)).flatten(1)                    # [B*Nw, 256]

    def forward(self, x, state=None):
        B = x.shape[0]
        w, Nw = self._windows(x)
        h = self._encode(w).reshape(B, Nw, -1)
        
        if self.flatten_for_ml:
            return h.reshape(B * Nw, -1)
            
        out, state = self.lstm(h, state)                                 # LSTM over consecutive windows
        logits = self.classifier(out.reshape(B * Nw, -1)).reshape(B, Nw, -1)
        return logits, state


def build_model(enc="psd", **kw):
    return SeizureCNNLSTM(enc=enc, **kw)


@torch.no_grad()
def predict_sessions(model, index_df, target_taxonomy, device, block_windows=WINDOWS_REQUESTS_SEIZURES["chunk_windows"], infer_batch=8, max_sessions=None, session_cache_dir="cache/sessions"):    
    """Predice P(seizure) o P(clase) para cada ventana, extrayendo la señal desde el caché .npz
    y construyendo la etiqueta real (y_true) para el cálculo de métricas de validación."""
    model.eval().to(device)
    win_sec = WINDOWS_REQUESTS_SEIZURES["win_sec"]
    shift_sec = WINDOWS_REQUESTS_SEIZURES["shift_sec"]
    min_pos_sec = WINDOWS_REQUESTS_SEIZURES["min_pos_sec"]
    
    win = int(win_sec * SFREQ)
    shift = int(shift_sec * SFREQ)
    
    group_cols = ["Patient", "Session", "Section", "EDF_path", "Duration"]
    frames, n_done = [], 0
    classes = list(target_taxonomy.keys())
    skipped = []

    for keys, group in index_df.groupby(group_cols, dropna=False):   # group = TODAS las anotaciones de la sesión
        if max_sessions and n_done >= max_sessions:
            break
        patient, session, section, edf_path, duration_s = keys

        try:
            sess_data = get_or_compute_session(
                patient=patient, session=session, section=section, path_edf=edf_path, 
                use_ica=False, bipolar_montage=True, cache_dir=session_cache_dir
            )
            
        except ValueError as e:
            if "Missing channels" in str(e) or "Short signal" in str(e):
                print(f"[WARNING] Saltando sesión: {e}") # Opcional, para no saturar tu consola
                continue
            raise e

        n_done += 1      
        x = sess_data["data"]
        total_samples = x.shape[1]          # longitud real tras el remuestreo; la del header puede diferir
        N = n_windows(x.shape[1], win, shift)
        if N <= 0:
            continue
            
        # Generar etiquetas reales agnósticas (y_true)
        intervals_dict = taxonomy_intervals(group, target_taxonomy)
        y_true_list = []
        for cat in classes:
            iv = intervals_dict[cat]
            y_mask = mask_from_intervals(iv, total_samples, SFREQ)
            wl = window_labels(y_mask, SFREQ, win_sec, shift_sec, min_pos_sec)
            y_true_list.append(wl[:N])
        y_true = np.column_stack(y_true_list) # [N, N_clases]
        
        probs = np.zeros((N, len(classes)), np.float32)

        def run(blocks):
            xs = np.stack([x[:, w0 * shift:(w0 + nw - 1) * shift + win] for w0, nw in blocks]).astype(np.float32)
            logits, _ = model(torch.from_numpy(xs).to(device))
            p = torch.sigmoid(logits).cpu().numpy() # Sigmoid para multilabel/BCE
            for (w0, nw), pp in zip(blocks, p):
                probs[w0:w0 + nw] = pp

        blocks = [(w0, min(block_windows, N - w0)) for w0 in range(0, N, block_windows)]
        full = [b for b in blocks if b[1] == block_windows]
        for i in range(0, len(full), infer_batch):
            run(full[i:i + infer_batch])
        for b in blocks:
            if b[1] != block_windows:
                run([b])
                
        df_res = pd.DataFrame({
            "key": f"{patient}_{session}_{section}", "Patient": patient, "Session": session, 
            "Section": section, "win_idx": np.arange(N),
            "start_s": np.arange(N) * shift_sec, "end_s": np.arange(N) * shift_sec + win_sec
        })
        
        for idx, cat in enumerate(classes):
            df_res[f"p_{cat}"] = probs[:, idx]
            df_res[f"y_{cat}"] = y_true[:, idx]
            
        frames.append(df_res)

    if skipped:
        print(f"[WARNING] {len(skipped)} sesiones omitidas por canales faltantes: {skipped[:5]}...")
        
    return pd.concat(frames, ignore_index=True) if frames else pd.DataFrame()


def _val_auroc(preds, target_taxonomy):
    """Calcula el AUROC promedio a través de todas las clases dinámicas."""
    if preds.empty:
        return float("nan")
        
    aurocs = []
    for cat in target_taxonomy.keys():
        y_true = preds[f"y_{cat}"]
        y_pred = preds[f"p_{cat}"]
        if y_true.nunique() > 1:
            aurocs.append(roc_auc_score(y_true, y_pred))
            
    return float(np.mean(aurocs)) if aurocs else float("nan")


def train_model_aitrics(
        model, train_ds, val_index, target_taxonomy, out_dir, device, epochs=20, batch_size=8, steps_per_epoch=500,
        lr=1e-3, weight_decay=1e-6, pos_weight=1.0, num_workers=8, patience=5, val_max_sessions=None,
        seed=42, force=False, session_cache_dir="cache/sessions"
    ):
    out_dir = Path(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    ckpt, hist_path = out_dir / "best.pt", out_dir / "history.json"
    model.to(device)
    cfg = dict(enc=model.enc, n_ch=model.n_ch, epochs=epochs, batch_size=batch_size,
           steps_per_epoch=steps_per_epoch, lr=lr, weight_decay=weight_decay,
           pos_weight=pos_weight, patience=patience, seed=seed, val_max_sessions=val_max_sessions)
    cfg_path = out_dir / "config.json"
    if ckpt.exists() and not force:
        old = json.loads(cfg_path.read_text()) if cfg_path.exists() else None
        if old != cfg:
            raise RuntimeError(f"best.pt en {out_dir} es de otra configuración: {old}. Usa force=True u otro out_dir.")
        print(f"[INFO] Checkpoint found, loading: {ckpt}")
        model.load_state_dict(torch.load(ckpt, map_location=device))
        return model, (json.loads(hist_path.read_text()) if hist_path.exists() else [])
    cfg_path.write_text(json.dumps(cfg, indent=2))

    torch.manual_seed(seed)
    np.random.seed(seed)
    loader = DataLoader(train_ds, batch_size=batch_size, sampler=train_ds.make_sampler(steps_per_epoch * batch_size),
                        num_workers=num_workers, pin_memory=device.type == "cuda", drop_last=True,
                        persistent_workers=num_workers > 0)
    opt = torch.optim.Adam(model.parameters(), lr=lr, weight_decay=weight_decay)
    sched = torch.optim.lr_scheduler.OneCycleLR(opt, max_lr=lr, total_steps=epochs * len(loader), pct_start=0.1)
    
    # BCEWithLogitsLoss para multilabel/multiclase agnóstico
    loss_fn = nn.BCEWithLogitsLoss(pos_weight=torch.tensor([pos_weight], device=device))

    best, bad, history = -1.0, 0, []
    for ep in range(1, epochs + 1):
        model.train()
        t0, losses = time.time(), []
        for step, (x, y) in enumerate(loader, 1):
            x, y = x.to(device, non_blocking=True), y.to(device, non_blocking=True)
            logits, _ = model(x)
            
            # Las dimensiones deben coincidir: (Batch*Nw, Clases)
            loss = loss_fn(logits.reshape(-1, logits.shape[-1]), y.reshape(-1, y.shape[-1]))
            
            opt.zero_grad(set_to_none=True)
            loss.backward()
            nn.utils.clip_grad_norm_(model.parameters(), 5.0)
            opt.step()
            sched.step()
            losses.append(loss.item())
            if step % 50 == 0:
                print(f"  ep{ep} step {step}/{len(loader)} loss={np.mean(losses[-50:]):.4f}", flush=True)
                
        val_preds = predict_sessions(model, val_index, target_taxonomy, device, max_sessions=val_max_sessions,
                                     session_cache_dir=session_cache_dir)        
        auroc = _val_auroc(val_preds, target_taxonomy)
        history.append({"epoch": ep, "train_loss": float(np.mean(losses)), "val_auroc": auroc,
                        "sec": round(time.time() - t0, 1)})
        print(f"[EPOCH {ep}/{epochs}] loss={history[-1]['train_loss']:.4f} val_AUROC={auroc:.4f} "
              f"({history[-1]['sec']} s)", flush=True)
        hist_path.write_text(json.dumps(history, indent=2))
        score = auroc if not np.isnan(auroc) else -0.5
        if score > best:
            best, bad = score, 0
            torch.save(model.state_dict(), ckpt)
        else:
            bad += 1
            if bad >= patience:
                print(f"[INFO] Early stop (no val AUROC gain in {patience} epochs)")
                break
    if not ckpt.exists():
        torch.save(model.state_dict(), ckpt)
    model.load_state_dict(torch.load(ckpt, map_location=device))
    return model, history


if __name__ == "__main__":
    # Shape / backward smoke test for every front-end (random data, 4 windows)
    dev = get_device()
    Nw = 4
    L = (Nw - 1) * int(WINDOWS_REQUESTS_SEIZURES["shift_sec"] * SFREQ) + int(WINDOWS_REQUESTS_SEIZURES["win_sec"] * SFREQ)
    for enc in ENC_CHOICES:
        # Probamos instanciar el modelo de manera agnóstica con n_out=3 clases de ejemplo
        m = build_model(enc, n_out=3).to(dev)
        x = torch.randn(2, N_CHANNELS, L, device=dev) * 30
        logits, st = m(x)
        assert logits.shape == (2, Nw, 3), (enc, logits.shape)
        logits.sum().backward()
        print(f"[OK] {enc:<12} logits {tuple(logits.shape)} params={sum(p.numel() for p in m.parameters())/1e6:.2f}M")
    print("[OK] seizure_cnn_lstm")