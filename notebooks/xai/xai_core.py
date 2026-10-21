"""
# File: xai_core.py
XAI general methods implementation:
    - Saliency
    - IG
    - Occlusion
    - SHAP
"""
# General required libraries
from pathlib import Path
import json
import numpy as np


def validate_inputs(inputs):
    xs = tuple(np.asarray(x, dtype=np.float32) for x in inputs)
    if not xs or any(x.ndim < 2 for x in xs):
        raise ValueError('Use una tupla de entradas (batch, ...), incluso con una sola entrada.')
    if not len(xs[0]) or any(len(x) != len(xs[0]) for x in xs):
        raise ValueError('Las entradas deben tener el mismo batch no vacío.')
    if any(not np.isfinite(x).all() for x in xs):
        raise ValueError('Hay valores no finitos.')
    return xs


def predict(score, inputs, batch_size=32):
    xs = validate_inputs(inputs)
    if batch_size < 1:
        raise ValueError('batch_size debe ser positivo.')
    parts = []
    for start in range(0, len(xs[0]), batch_size):
        batch = tuple(x[start:start + batch_size] for x in xs)
        y = np.asarray(score(*batch))
        if y.shape != (len(batch[0]),) or not np.isfinite(y).all():
            raise ValueError('score debe devolver un valor finito por muestra: (batch,).')
        parts.append(y)
    return np.concatenate(parts)


# --------------------------------------------------------------------------------
# Oclussion method
# --------------------------------------------------------------------------------
def occlusion(score, inputs, input_index, axis=-1, baseline=0.0, batch_size=32):
    """Una caída firmada por canal/característica. axis excluye el eje batch.

    Las otras entradas permanecen fijas. No recalcula características derivadas.
    baseline debe estar en el espacio de entrada del modelo (p. ej., escalado).
    """
    xs = validate_inputs(inputs)
    x = xs[input_index]
    axis %= x.ndim
    if axis == 0:
        raise ValueError('No se puede ocluir el eje batch.')
    ref = np.broadcast_to(np.asarray(baseline, dtype=x.dtype), x.shape)
    base_score = predict(score, xs, batch_size)
    drops = np.empty((len(x), x.shape[axis]))
    for j in range(x.shape[axis]):
        masked = x.copy()
        region = [slice(None)] * x.ndim
        region[axis] = j
        masked[tuple(region)] = ref[tuple(region)]
        changed = list(xs)
        changed[input_index] = masked
        drops[:, j] = base_score - predict(score, changed, batch_size)
    return drops, base_score

# --------------------------------------------------------------------------------
# SHAP method
# --------------------------------------------------------------------------------
def kernel_shap(score, inputs, input_index, background, nsamples=100, seed=13):
    """SHAP tabular: mantiene las OTRAS entradas de CADA muestra correspondiente.

    Retorna values (B,F), expected_values (B,) y residual aditivo (B,).
    No equivale a SHAP conjunto de señal + características derivadas.
    """
    import shap
    xs = validate_inputs(inputs)
    x = xs[input_index]
    bg = np.asarray(background, dtype=np.float32)
    if x.ndim != 2 or bg.ndim != 2 or not len(bg) or bg.shape[1:] != x.shape[1:]:
        raise ValueError('SHAP requiere entrada (B,F) y background (N,F).')
    if not np.isfinite(bg).all():
        raise ValueError('Background no finito.')
    values, expected = [], []
    rng_state = np.random.get_state()
    try:
        np.random.seed(seed)
        for i in range(len(x)):
            def forward(features):
                batch = [np.repeat(v[i:i+1], len(features), axis=0) for v in xs]
                batch[input_index] = features
                return predict(score, tuple(batch))
            explainer = shap.KernelExplainer(forward, bg)
            phi = np.asarray(explainer.shap_values(x[i:i+1], nsamples=nsamples))
            if phi.shape == (1, x.shape[1], 1):
                phi = phi[..., 0]
            if phi.shape != (1, x.shape[1]):
                raise ValueError(f'SHAP devolvió una forma inesperada: {phi.shape}')
            values.append(phi[0])
            expected.append(float(np.asarray(explainer.expected_value).item()))
    finally:
        np.random.set_state(rng_state)
    values, expected = np.asarray(values), np.asarray(expected)
    residual = predict(score, xs) - expected - values.sum(axis=1)
    return values, expected, residual


class TorchAdapter:
    """Adaptador diferenciable. selector transforma la salida a un score (B,).

    El usuario elige probabilidad/logit/clase. No aplica sigmoid implícitamente.
    """
    def __init__(self, model, selector, device='cpu'):
        import torch
        self.device = torch.device(device)
        self.model = model.to(self.device).eval()
        self.selector = selector

    def forward(self, *inputs):
        y = self.selector(self.model(*inputs))
        if y.ndim != 1 or y.shape[0] != inputs[0].shape[0]:
            raise ValueError('selector debe devolver un tensor (B,).')
        return y

    def tensors(self, inputs):
        import torch
        return tuple(torch.as_tensor(x, dtype=torch.float32, device=self.device)
                     for x in validate_inputs(inputs))

    def predict(self, *inputs):
        import torch
        with torch.no_grad():
            return self.forward(*self.tensors(inputs)).cpu().numpy()

# --------------------------------------------------------------------------------
# Saliency method
# --------------------------------------------------------------------------------
def saliency(adapter, inputs, input_index, absolute=True):
    """Gradiente parcial: las otras entradas permanecen fijas."""
    import torch
    xs = list(adapter.tensors(inputs))
    x = xs[input_index].detach().clone().requires_grad_(True)
    xs[input_index] = x
    with torch.enable_grad():
        grad, = torch.autograd.grad(adapter.forward(*xs).sum(), x)
    if absolute:
        grad = grad.abs()
    return grad.detach().cpu().numpy()


# --------------------------------------------------------------------------------
# IG method
# --------------------------------------------------------------------------------
def integrated_gradients(adapter, inputs, input_index, baseline=0.0,
                         n_steps=50, internal_batch_size=None):
    """IG parcial, con emparejamiento correcto de muestras y delta conservado."""
    import torch
    from captum.attr import IntegratedGradients
    xs = adapter.tensors(inputs)
    x = xs[input_index]
    others = tuple(v for j, v in enumerate(xs) if j != input_index)
    def forward(changed, *fixed):
        args = list(fixed)
        args.insert(input_index, changed)
        return adapter.forward(*args)
    base = torch.broadcast_to(torch.as_tensor(baseline, dtype=x.dtype,
                                             device=x.device), x.shape).clone()
    if n_steps < 2:
        raise ValueError('n_steps debe ser al menos 2.')
    with torch.enable_grad():
        attrs, delta = IntegratedGradients(forward).attribute(
            x, baselines=base, additional_forward_args=others or None,
            n_steps=n_steps, internal_batch_size=internal_batch_size,
            return_convergence_delta=True)
    return attrs.detach().cpu().numpy(), delta.detach().cpu().numpy()


def binary_groups(labels, probabilities, threshold=0.5, n=3):
    """Casos extremos para inspección, NO muestra representativa de rendimiento."""
    y, p = np.asarray(labels), np.asarray(probabilities)
    if y.ndim != 1 or p.shape != y.shape or not np.isin(y, [0, 1]).all():
        raise ValueError('Etiquetas binarias y probabilidades deben tener forma (N,).')
    if not np.isfinite(p).all() or np.any((p < 0) | (p > 1)):
        raise ValueError('Se requieren probabilidades en [0,1].')
    if n < 1 or not 0 <= threshold <= 1:
        raise ValueError('n o threshold inválidos.')
    pred = p >= threshold
    groups = {}
    for name, truth, decision in [('TP', 1, True), ('FP', 0, True),
                                  ('TN', 0, False), ('FN', 1, False)]:
        idx = np.flatnonzero((y == truth) & (pred == decision))
        idx = idx[np.argsort(p[idx], kind='stable')]
        groups[name] = (idx[::-1] if decision else idx)[:n].copy()
    return groups


# --------------------------------------------------------------------------------
# Save and plot results
# --------------------------------------------------------------------------------
def save_results(directory, arrays, metadata):
    path = Path(directory)
    path.mkdir(parents=True, exist_ok=True)
    if any(np.asarray(v).dtype.hasobject for v in arrays.values()):
        raise ValueError('Guarde solo arrays numéricos, no objetos/tensores GPU.')
    np.savez_compressed(path / 'attributions.npz', **arrays)
    (path / 'metadata.json').write_text(json.dumps(metadata, indent=2,
                                                 ensure_ascii=False), encoding='utf-8')


def plot_importance(values, names, output, title='Importancia', absolute=True):
    import matplotlib.pyplot as plt
    values = np.asarray(values)
    if values.ndim != 2 or values.shape[1] != len(names):
        raise ValueError('values debe ser (B,F) y names tener longitud F.')
    mean = (np.abs(values) if absolute else values).mean(axis=0)
    order = np.argsort(np.abs(mean))
    fig, ax = plt.subplots(figsize=(7, max(3, len(names) * .28)))
    ax.barh(np.asarray(names)[order], mean[order], color='#6A8BA2')
    ax.set(title=title, xlabel='Media de magnitudes' if absolute else 'Media firmada')
    fig.tight_layout()
    Path(output).parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(output, bbox_inches='tight')
    plt.close(fig)


def plot_signal_map(values, channel_names, fs, output, title='Atribución'):
    """Mapa por ventana (T,C), sin divisibilidad por bins fijos."""
    import matplotlib.pyplot as plt
    a = np.asarray(values)
    if a.ndim != 2 or a.shape[1] != len(channel_names) or fs <= 0:
        raise ValueError('Se requiere (T,C), C nombres y fs positivo.')
    fig, ax = plt.subplots(figsize=(9, max(3, len(channel_names) * .25)))
    vmax = max(float(np.max(np.abs(a))), 1e-12)
    im = ax.imshow(a.T, aspect='auto', cmap='RdBu_r', vmin=-vmax, vmax=vmax,
                   extent=(0, len(a) / fs, len(channel_names)-.5, -.5))
    ax.set_yticks(range(len(channel_names)), channel_names)
    ax.set(xlabel='Tiempo (s)', title=title)
    fig.colorbar(im, ax=ax, label='Atribución')
    fig.tight_layout()
    Path(output).parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(output, bbox_inches='tight')
    plt.close(fig)