"""
# File: xai_deep_core.py
# Project: Trabajo de Graduación
# Author: María Fernanda Andrade
#
# Confusion mapping and selection of top variables.
"""
# General imports
import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F
from captum.attr import IntegratedGradients
 
# ---------------------------------------------------------------------------
# Wrapper: (B,T,C) + feat (B,16) -> un escalar por ventana (B,)
# ---------------------------------------------------------------------------
class ModelWrapper(nn.Module):
    def __init__(self, model, output_fn=None, activation=None,
                 target_class=None, reduce=None):
        super().__init__()
        self.model = model.eval()
        self.output_fn = output_fn or (lambda o: o)
        self.activation = activation
        self.target_class = target_class
        self.reduce = reduce

    def forward(self, *inputs):
        out = self.output_fn(self.model(*inputs))

        if self.activation == "sigmoid":
            out = torch.sigmoid(out)
        elif self.activation == "softmax":
            out = torch.softmax(out, dim=-1)

        if self.target_class is not None:
            out = out[..., self.target_class]
        elif out.ndim > 1 and out.shape[-1] == 1:
            out = out[..., 0]

        if out.ndim > 1:
            if callable(self.reduce):
                out = self.reduce(out)
            elif self.reduce == "mean":
                out = out.flatten(1).mean(1)
            elif self.reduce == "max":
                out = out.flatten(1).max(1).values
            else:
                raise ValueError(
                    f"Output {tuple(out.shape)}: usa reduce='mean'/'max' o target_class")

        if out.ndim != 1 or out.shape[0] != inputs[0].shape[0]:
            raise ValueError("El wrapper debe devolver un valor por ventana (B,).")
        return out


def make_wrap(model, reduce="max"):
    # Logits (activation=None): evita saturación del sigmoide al atribuir
    return ModelWrapper(model, output_fn=lambda o: o.logits,
                        activation=None, reduce=reduce)


# ---------------------------------------------------------------------------
# 1) Integrated Gradients sobre (x, feat)
# ---------------------------------------------------------------------------
def explain_ig(model, x, feat, x_base=None, feat_base=None,
               n_steps=32, reduce="max"):
    """
    x: (B,T,C)   feat: (B,16)
    Devuelve:
      attr_x  (B,T,C)  atribución completa con signo
      channel (B,C)    importancia por canal de entrada
      time    (B,T)    importancia por instante
      feat    (B,16)   atribución por feature (+ empuja a crisis)
      delta   (B,)     error de convergencia (pequeño = fiable)
    """
    model.eval()
    x_base = torch.zeros_like(x) if x_base is None else x_base
    feat_base = torch.zeros_like(feat) if feat_base is None else feat_base
    ig = IntegratedGradients(make_wrap(model, reduce))
    (ax, af), delta = ig.attribute(
        (x, feat),
        baselines=(x_base, feat_base),
        n_steps=n_steps,
        internal_batch_size=n_steps,
        return_convergence_delta=True,
    )
    return {
        "attr_x": ax,
        "channel": ax.abs().sum(1),
        "time": ax.abs().sum(2),
        "feat": af,
        "delta": delta,
    }


# ---------------------------------------------------------------------------
# 2) Atención x gradiente (Chefer et al., ICCV 2021, versión genérica)
# ---------------------------------------------------------------------------
def explain_attn_grad(model, x, feat, reduce="max"):
    """Mapa temporal (B,T) en [0,1]. 1 forward + 1 backward."""
    model.eval()
    for b in model.blocks:
        b.attn.capture = True
    model.zero_grad()
    make_wrap(model, reduce)(x, feat).sum().backward()

    R = None
    for b in model.blocks:
        A, G = b.attn.last_attn, b.attn.last_attn_grad      # (B,H,N,N)
        Ab = (A * G).clamp(min=0).mean(1)                   # (B,N,N)
        if R is None:
            R = torch.eye(Ab.size(-1), device=Ab.device).expand_as(Ab).clone()
        R = R + Ab @ R
    for b in model.blocks:
        b.attn.capture = False

    # token 0 = CLS. time_step: aporte de cada token como fuente; ventana: fila del CLS
    tok = R[:, 1:, 1:].sum(1) if model.time_step else R[:, 0, 1:]   # (B,T')
    tok = tok / tok.amax(-1, keepdim=True).clamp_min(1e-8)
    return F.interpolate(tok[:, None], size=x.size(1), mode="linear",
                         align_corners=False)[:, 0]                  # (B,T)


# ---------------------------------------------------------------------------
# 3) Fidelidad: curva de deleción (x con batch=1)
# ---------------------------------------------------------------------------
@torch.no_grad()
def deletion_curve(model, x, feat, imp_time,
                   fracs=(0.1, 0.2, 0.3, 0.5), reduce="max"):
    """Anula el top-k% de instantes 'importantes' y mide la caída del logit;
    compara con anular al azar. Devuelve [(fracción, caída_top, caída_azar)]."""
    w = make_wrap(model, reduce)
    base = w(x, feat).item()
    order = imp_time[0].argsort(descending=True)
    rnd = torch.randperm(order.numel())
    out = []
    for f in fracs:
        k = max(1, int(f * order.numel()))
        row = [f]
        for idx in (order[:k], rnd[:k]):
            xm = x.clone()
            xm[0, idx, :] = 0
            row.append(base - w(xm, feat).item())
        out.append(tuple(row))
    return out


# ---------------------------------------------------------------------------
# PARCHE en MultiHeadSelfAttentionRoPE.forward, justo tras el softmax:
#
#     attn = self.softmax(logits)
#     if getattr(self, "capture", False):
#         self.last_attn = attn
#         if attn.requires_grad:
#             attn.register_hook(lambda g: setattr(self, "last_attn_grad", g))
#     attn = self.dropout(attn)
# ---------------------------------------------------------------------------

def as_tuple(inputs):
    return (inputs,) if torch.is_tensor(inputs) else tuple(inputs)

def reduce_logit_of_mean_prob(z):   # z: (B, T')
    return torch.logsumexp(F.logsigmoid(z), dim=1) - torch.logsumexp(F.logsigmoid(-z), dim=1)

# Model wrapper
class ModelWrapper:
    def __init__(self, model, output_fn=None, activation=None,
                 target_class=None, reduce=None) -> None:
        """
        (B, C, T) ->    B: Probabilidad de crisis

        """
        self.model = model.eval()
        self.output_fn = output_fn or (lambda o: o)
        self.activation = activation
        self.target_class = target_class
        self.reduce = reduce
        self.device = next(model.parameters()).device

    def __call__(self, *inputs):
        out = self.output_fn(self.model(*inputs))

        if self.activation == "sigmoid":
            out = torch.sigmoid(out)
        elif self.activation == "softmax":
            out = torch.softmax(out, dim=-1)
        
        if self.target_class is not None:
            out = out[..., self.target_class]
        elif out.ndim > 1 and out.shape[-1] == 1:
            out = out[..., 0]

        if out.ndim > 1:
            if callable(self.reduce):
                out = self.reduce(out)
            elif self.reduce == "mean":
                out = out.flatten(1).mean(1)
            elif self.reduce == "max":
                out = out.flatten(1).max(1).values
            else:
                raise ValueError(f"Output {tuple(out.shape)}: reduce='mean'/'max' o target_class")
        
        if out.ndim != 1 or out.shape[0] != inputs[0].shape[0]:
            raise ValueError("Wrapper returns no value for the window (B,).")
        
        return out

# Prediction
@torch.no_grad()
def predict_proba(wrapper, inputs, batch_size=32):
    args = as_tuple(inputs)
    n = args[0].shape[0] 
    outs = []
    for i in range(0, n, batch_size):
        batch = [t[i:i+batch_size].to(wrapper.device).float() for t in args]
        outs.append(wrapper(*batch).cpu().numpy())
    return np.concatenate(outs)

# Saliency method
def saliency(wrapper, inputs, explain_idx=0, absolute=True):
    args = [t.detach().to(wrapper.device).float() for t in as_tuple(inputs)]
    x  = args[explain_idx].clone().requires_grad_(True)
    args[explain_idx] = x
    wrapper.model.zero_grad(set_to_none=True)
    wrapper(*args).sum().backward()
    g = x.grad.abs() if absolute else x.grad
    return g.detach().cpu().numpy()

# IG method
def integrated_gradients(wrapper, inputs, explain_idx=0, baseline=None,
                         n_steps=50, return_delta=False):
    args = [t.detach().to(wrapper.device).float() for t in as_tuple(inputs)]
    x = args[explain_idx]

    if baseline is None:
        base = torch.zeros_like(x)
    else:
        base = baseline.to(x.device).float().expand_as(x)

    total = torch.zeros_like(x)
    for a in (torch.arange(n_steps, device=x.device) + 0.5) / n_steps:
        xi = (base + a *(x - base)).requires_grad_(True)
        steps_args = list(args)
        steps_args[explain_idx] = xi
        wrapper.model.zero_grad(set_to_none=True)
        total += torch.autograd.grad(wrapper(*steps_args).sum(), xi)[0]

    attr = (x-base) * total/n_steps
    attr_np = attr.detach().cpu().numpy()

    if not return_delta:
        return attr_np

    with torch.no_grad():
        b_args = list(args)
        b_args[explain_idx] = base
        diff = (wrapper(*args) -  wrapper(*b_args)).cpu().numpy()
    delta = attr_np.reshape(len(attr_np), -1).sum(1) - diff
    return attr_np, delta

# Occlusion
@torch.no_grad()
def occlusion(wrapper, inputs, explain_idx=0, axis=1, window=1, baseline_value=0.0):
    args = [t.detach().to(wrapper.device).float() for t in as_tuple(inputs)]
    x = args[explain_idx]

    ax = axis % x.dim()
    if ax == 0:
        raise ValueError("axis can't be 0 (batch size equals 0)")
    base = wrapper(*args)
    starts = range(0, x.shape[ax], window)
    drop = torch.zeros(x.shape[0], len(starts), device=x.device)

    for k, s in enumerate(starts):
        xm = x.clone()
        sl = [slice(None)] * x.dim()
        sl[ax] = slice(s, min(s + window, x.shape[ax]))
        xm[tuple(sl)] = baseline_value
        m_args = list(args)
        m_args[explain_idx] = xm
        drop[:, k] = base - wrapper(*m_args)

    return drop.cpu().numpy(), base.cpu().numpy()

 
# ---------------------------------------------------------------------------
# 1) Integrated Gradients CONJUNTO sobre (señal, features)
# ---------------------------------------------------------------------------
def explain_ig(wrap, x, feat, x_base=None, feat_base=None,
               n_steps=100, internal_bs=25):
    """
    x: (B,T,C)  feat: (B,F)  (en el mismo device que el modelo)
    Devuelve dict:
      attr_x    (B,T,C)  atribución con signo sobre la señal
      attr_feat (B,F)    atribución con signo sobre las features
      delta     (B,)     error de completitud (unidades del logit)
      gap       (B,)     f(x) - f(baseline); sirve para delta relativo
    Completitud: sum(attr_x)+sum(attr_feat) ≈ gap.
    """
    x_base = torch.zeros_like(x) if x_base is None else x_base
    feat_base = torch.zeros_like(feat) if feat_base is None else feat_base
    ig = IntegratedGradients(wrap)
    (ax, af), delta = ig.attribute(
        (x, feat),
        baselines=(x_base, feat_base),
        n_steps=n_steps,
        internal_batch_size=internal_bs,
        return_convergence_delta=True,
    )
    with torch.no_grad():
        gap = wrap(x, feat) - wrap(x_base, feat_base)
    return {"attr_x": ax.detach(), "attr_feat": af.detach(),
            "delta": delta.detach(), "gap": gap.detach()}
 
 
# ---------------------------------------------------------------------------
# 2) Atención x gradiente (Chefer et al., ICCV 2021, versión genérica)
# ---------------------------------------------------------------------------
def explain_attn_grad(model, wrap, x, feat):
    """Mapa temporal (B,T) en [0,1]. 1 forward + 1 backward. Solo tiempo."""
    for b in model.blocks:
        b.attn.capture = True
    model.zero_grad(set_to_none=True)
    try:
        wrap(x, feat).sum().backward()
        R = None
        for b in model.blocks:
            A, G = b.attn.last_attn, b.attn.last_attn_grad       # (B,H,N,N)
            Ab = (A * G).clamp(min=0).mean(1)                    # (B,N,N)
            if R is None:
                R = torch.eye(Ab.size(-1), device=Ab.device).expand_as(Ab).clone()
            R = R + Ab @ R
    finally:
        for b in model.blocks:
            b.attn.capture = False
 
    # token 0 = CLS. time_step: aporte de cada token como fuente; ventana: fila del CLS
    tok = R[:, 1:, 1:].sum(1) if model.time_step else R[:, 0, 1:]   # (B,T')
    tok = tok / tok.amax(-1, keepdim=True).clamp_min(1e-8)
    out = F.interpolate(tok[:, None], size=x.size(1), mode="linear",
                        align_corners=False)[:, 0]                   # (B,T)
    return out.detach()
 
 
# ---------------------------------------------------------------------------
# 3) Fidelidad: deleción (top-importancia vs azar), x con batch=1
# ---------------------------------------------------------------------------
@torch.no_grad()
def deletion_scores(wrap, x, feat, imp, fracs=(0.1, 0.2, 0.3, 0.5)):
    """
    imp: (T,) importancia temporal. Anula (=0) el top-k% de instantes y mide
    la caída media del valor explicado (logit) respecto a la ventana original.
    Devuelve (caída_media_top, caída_media_azar). Una sola pasada por lotes.
    """
    T = x.size(1)
    base = wrap(x, feat)                                   # (1,)
    order = imp.to(x.device).argsort(descending=True)
    rnd = torch.randperm(T, device=x.device)
    xs = x.repeat(2 * len(fracs), 1, 1)
    for i, f in enumerate(fracs):
        k = max(1, int(f * T))
        xs[i, order[:k], :] = 0
        xs[len(fracs) + i, rnd[:k], :] = 0
    out = wrap(xs, feat.repeat(2 * len(fracs), 1))          # (2n,)
    drops = base - out
    n = len(fracs)
    return drops[:n].mean().item(), drops[n:].mean().item()


if __name__ == "__main__":

    x, f = torch.randn(6, 100, 4), torch.randn(6, 3)

    # Modelos de prueba
    class Planted(nn.Module):
        """Solo depende del canal 2 de la señal y de la feature 0."""
        def __init__(self):
            super().__init__()
            self.dummy = nn.Parameter(torch.zeros(1))   

        def forward(self, x, f):
            z = x[:, :, 2].pow(2).mean(1) + 2 * f[:, 0] - 1
            return torch.sigmoid(z).unsqueeze(-1)
        
    # Modelo donde saliency falla pero IG no
    class PlantedSat2(Planted):
        def forward(self, x, f):
            z = 50 * x[:, :, 2].pow(2).mean(1) - 20      # baseline: p≈0 | entrada: p≈1
            return torch.sigmoid(z).unsqueeze(-1)

    # Tiempo: un modelo que solo mira los últimos 20 puntos
    class PlantedTime(Planted):
        def forward(self, x, f):
            z = 5 * x[:, 80:, 0].pow(2).mean(1) - 5
            return torch.sigmoid(z).unsqueeze(-1)

    wp = ModelWrapper(Planted())
    print("Shape: ", wp(x, f).shape)

    w2 = ModelWrapper(PlantedSat2())
    f0 = torch.zeros_like(f)

    wt = ModelWrapper(PlantedTime())

    # Saliency
    sal_sig  = saliency(wp, (x, f), explain_idx=0)
    sal_feat = saliency(wp, (x, f), explain_idx=1)

    print("Channels: ", sal_sig.mean(axis=(0, 1)))  # canal 2 > 0, los demás exactamente 0
    print("Features: ",sal_feat.mean(axis=0))       # feature 0 > 0, las demás exactamente 0

    assert wp(x, f).shape == (6,)
    assert sal_sig.shape == x.shape
    assert sal_feat.shape == f.shape
    assert sal_sig.std() > 0                        # el gradiente sí fluye

    with torch.no_grad():
        p = wp(x, f)                                # (6,)
    dp = p * (1 - p)                                # σ'(z)
    T = x.shape[1]

    expected_sig = torch.zeros_like(x)
    expected_sig[:, :, 2] = dp[:, None] * 2 * x[:, :, 2] / T
    expected_sig = expected_sig.abs().numpy()

    expected_feat = torch.zeros_like(f)
    expected_feat[:, 0] = 2 * dp
    expected_feat = expected_feat.abs().numpy()

    assert np.allclose(sal_sig,  expected_sig,  atol=1e-6)
    assert np.allclose(sal_feat, expected_feat, atol=1e-6)
    print("saliency coincide con el gradiente analítico ✓")

    # Integrated Gradients
    # Completitud y dirección correcta, con Planted (canal 2 y feature 0)
    attr_sig, delta = integrated_gradients(wp, (x, f), explain_idx=0, n_steps=100, return_delta=True)
    print("delta:", delta)                           # ≈ 0
    print(np.abs(attr_sig).mean(axis=(0, 1)))        # solo canal 2 > 0; los demás exactamente 0
    assert attr_sig.shape == x.shape
    assert np.allclose(delta, 0, atol=1e-3)
    assert np.all(attr_sig[:, :, [0, 1, 3]] == 0)

    attr_feat = integrated_gradients(wp, (x, f), explain_idx=1, n_steps=100)
    assert np.all(attr_feat[:, 1:] == 0)             # solo la feature 0 recibe atribución

    print("prob:", predict_proba(w2, (x, f0)))                       # ≈ 1
    sal2 = saliency(w2, (x, f0), explain_idx=0)
    ig2  = integrated_gradients(w2, (x, f0), explain_idx=0, n_steps=200)

    print("saliency canal:", sal2.sum(axis=1).mean(0))               # ≈ 0 en todos
    print("IG canal:      ", ig2.sum(axis=1).mean(0))                # ≈ 1 en canal 2, 0 en el resto
    assert ig2[:, :, 2].sum() / ig2.sum() > 0.99

    # OCLUSSION: 
    # Canales: solo el canal 2 debe tener caída
    occ_ch, base = occlusion(wp, (x, f), explain_idx=0, axis=2)     # (6, 4)
    print(occ_ch.mean(axis=0))                                      # solo el canal 2 ≠ 0

    # Esperado: p(x) - p(x con canal 2 en cero) = p - sigmoide(2*f0 - 1)
    p = torch.sigmoid(x[:, :, 2].pow(2).mean(1) + 2*f[:, 0] - 1)
    exp_ch2 = (p - torch.sigmoid(2*f[:, 0] - 1)).numpy()
    assert np.allclose(occ_ch[:, 2], exp_ch2, atol=1e-6)
    assert np.all(occ_ch[:, [0, 1, 3]] == 0)

    # Features: solo la feature 0
    occ_f, _ = occlusion(wp, (x, f), explain_idx=1, axis=1)         # (6, 3)
    exp_f0 = (p - torch.sigmoid(x[:, :, 2].pow(2).mean(1) - 1)).numpy()
    assert np.allclose(occ_f[:, 0], exp_f0, atol=1e-6)
    assert np.all(occ_f[:, 1:] == 0)
    print("occlusion canales/features ✓")

    occ_t, _ = occlusion(wt, (x, f), explain_idx=0, axis=1, window=20)   # (6, 5)
    print(occ_t.mean(axis=0))                 # solo el último trozo ≠ 0
    assert np.all(occ_t[:, :4] == 0)
    assert np.all(occ_t[:, 4] > 0)            # promedio de x² > 1 ⇒ z > 0 ⇒ borrar baja p

    ig_ch = attr_sig.sum(axis=1)             # (6, 4): IG sumado sobre el tiempo, por canal0    
    print(np.allclose(ig_ch[:, 2], occ_ch[:, 2], atol=1e-3))   # True en Planted
