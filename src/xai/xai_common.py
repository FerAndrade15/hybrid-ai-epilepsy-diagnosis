"""
# File: xai_common.py
# Project: Trabajo de Graduación
# Author: María Fernanda Andrade
#
# Confusion mapping and selection of top variables.
"""
# Data management libraries
import numpy as np

# Visualization
import matplotlib.pyplot as plt

def confusion_groups(y_true, probs, threshold=0.5):
    y = np.asarray(y_true).astype(int)
    pred = np.asarray(probs) >= threshold
    return {
        "TP": np.where((y==1) & pred)[0],
        "FP": np.where((y==0) & pred)[0],
        "TN": np.where((y==0) & ~pred)[0],
        "FN": np.where((y==1) & ~pred)[0],
    }

def select_top(indices, probs, n, highest=True):
    indices = np.asarray(indices).reshape(-1)
    if len(indices) == 0:
        return np.array([], dtype=int)
    order = indices[np.argsort(np.asarray(probs)[indices])]
    return (order[::-1] if highest else order)[:n].copy()

# Visualization
def plot_saliency_window(
    sal_sig, fs, channel_names=None, title="Saliency"
):
    sal_sig = np.asarray(sal_sig)

    if sal_sig.ndim != 2:
        raise ValueError("Se espera sal_sig con forma (tiempo, canales).")
    if not np.isfinite(sal_sig).all():
        raise ValueError("El saliency contiene NaN o infinitos.")

    n_t, n_ch = sal_sig.shape

    if channel_names is None:
        channel_names = [f"Canal {j}" for j in range(n_ch)]
    if len(channel_names) != n_ch:
        raise ValueError("Los nombres no coinciden con el número de canales.")

    # Mismos valores y escala para todos los canales.
    channel_score = sal_sig.mean(axis=0)
    order = np.argsort(channel_score)[::-1]
    vmax = float(sal_sig.max()) or 1.0

    fig, axes = plt.subplots(
        1, 2,
        figsize=(16, 8),
        gridspec_kw={"width_ratios": [3, 1.4]},
        constrained_layout=True,
    )

    im = axes[0].imshow(
        sal_sig.T,  # (canales, tiempo)
        origin="lower",
        aspect="auto",
        interpolation="nearest",
        extent=[0, n_t / fs, -0.5, n_ch - 0.5],
        cmap="magma",
        vmin=0,
        vmax=vmax,
    )

    axes[0].set_yticks(np.arange(n_ch))
    axes[0].set_yticklabels(channel_names)
    axes[0].set_xlabel("Tiempo dentro de la ventana (s)")
    axes[0].set_ylabel("Canal")
    axes[0].set_title("Sensibilidad por tiempo y canal")
    fig.colorbar(im, ax=axes[0], label="|∂P(crisis)/∂señal|")

    axes[1].barh(
        np.arange(n_ch),
        channel_score[order],
        color="darkorange",
    )
    axes[1].set_yticks(np.arange(n_ch))
    axes[1].set_yticklabels([channel_names[j] for j in order])
    axes[1].invert_yaxis()
    axes[1].set_xlabel("Gradiente absoluto medio")
    axes[1].set_title("Resumen por canal")
    axes[1].ticklabel_format(axis="x", style="sci", scilimits=(0, 0))

    fig.suptitle(title)
    plt.show()


def _norm(v):
    v = np.asarray(v, dtype=float)
    return v / max(v.max(), 1e-8)


def plot_explanation(x, feat, ig, am, fs, prob=None, ch_names=None,
                     feat_names=None, path="explicacion.png"):
    xs = x[0].detach().cpu().numpy()                    # (T, C)
    T, C = xs.shape
    t = np.arange(T) / fs
    ch_names = ch_names or [f"ch{i}" for i in range(C)]
    feat_names = feat_names or [f"f{i}" for i in range(feat.size(1))]
    t_ig = _norm(ig["time"][0].detach().cpu())
    t_at = _norm(am[0].detach().cpu())

    fig = plt.figure(figsize=(13, 10))
    gs = GridSpec(4, 2, height_ratios=[2.2, 1.6, 1, 1.2], figure=fig)

    # Panel 1: EEG con la importancia temporal de IG como fondo rojo
    ax1 = fig.add_subplot(gs[0, :])
    z = (xs - xs.mean(0)) / (xs.std(0) + 1e-8)
    for i in range(C):
        ax1.plot(t, z[:, i] * 0.4 + i * 2, lw=0.6, color="k")
    ax1.imshow(t_ig[None], aspect="auto", cmap="Reds", alpha=0.35,
               extent=[0, t[-1], -1, C * 2])
    ax1.set_yticks(np.arange(C) * 2)
    ax1.set_yticklabels(ch_names, fontsize=7)
    ax1.set_title("EEG + importancia temporal (IG)"
                  + (f"  |  P(crisis)={prob:.2f}" if prob is not None else ""))

    # Panel 2: mapa canal x tiempo de IG
    ax2 = fig.add_subplot(gs[1, :], sharex=ax1)
    a = ig["attr_x"][0].abs().detach().cpu().numpy().T   # (C, T)
    ax2.imshow(a, aspect="auto", cmap="magma", extent=[0, t[-1], C, 0])
    ax2.set_yticks(np.arange(C) + 0.5)
    ax2.set_yticklabels(ch_names, fontsize=7)
    ax2.set_title("IG |atribución| por canal de entrada y tiempo")

    # Panel 3: IG vs atención x gradiente
    ax3 = fig.add_subplot(gs[2, :], sharex=ax1)
    ax3.plot(t, t_ig, label="IG")
    ax3.plot(t, t_at, label="Atención×grad", alpha=0.8)
    ax3.set_ylabel("importancia (norm.)")
    ax3.set_xlabel("tiempo (s)")
    ax3.legend(loc="upper right")

    # Panel 4a: importancia por canal
    ax4 = fig.add_subplot(gs[3, 0])
    ax4.bar(range(C), _norm(ig["channel"][0].detach().cpu()))
    ax4.set_xticks(range(C))
    ax4.set_xticklabels(ch_names, rotation=90, fontsize=7)
    ax4.set_title("Importancia por canal")

    # Panel 4b: features (rojo empuja a crisis, azul en contra)
    ax5 = fig.add_subplot(gs[3, 1])
    f = ig["feat"][0].detach().cpu().numpy()
    ax5.bar(range(len(f)), f, color=np.where(f >= 0, "tab:red", "tab:blue"))
    ax5.set_xticks(range(len(f)))
    ax5.set_xticklabels(feat_names, rotation=90, fontsize=7)
    ax5.set_title("Features (rojo: hacia crisis, azul: en contra)")

    fig.tight_layout()
    fig.savefig(path, dpi=130)
    plt.show()


if __name__ == "__main__":
    from model import build_transformer          # AJUSTA: módulo con tu modelo
    T, C, fs = 256, 19, 256                      # AJUSTA: muestras, canales, Hz
    cfg = dict(feat_input_dim=16)                # AJUSTA: hiperparámetros del entrenamiento

    model = build_transformer(input_shape=(T, C), **cfg)
    # model.load_state_dict(torch.load("ckpt.pt", map_location="cpu"))  # descomenta con tus pesos
    model.eval()

    x = torch.randn(1, T, C)                     # reemplaza por una ventana real
    feat = torch.randn(1, 16)
    feat_base = torch.zeros(1, 16)               # mejor: media de ventanas sin crisis

    with torch.no_grad():
        prob = torch.sigmoid(model(x, feat).logits).max().item()
    ig = explain_ig(model, x, feat, torch.zeros_like(x), feat_base, n_steps=16)
    am = explain_attn_grad(model, x, feat)
    print("delta IG:", ig["delta"].item(), "| P(crisis):", prob)
    plot_explanation(x, feat, ig, am, fs, prob)


