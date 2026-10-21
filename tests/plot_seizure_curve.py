"""Dibuja la salida del SeizureTransformer contra las anotaciones .csv_bi, fuera de tu herramienta.

Uso:
    python plot_seizure_curve.py \
        --model-file src/models/large_eeg_u_transformer.py \
        --weights ruta/a/pesos.pt \
        --tensor ventana.npy \
        --csv-bi ruta/al/archivo.csv_bi \
        --window-start 120 \
        --out curva.png

--tensor : .npy con la MISMA ventana que le da tu herramienta al modelo, forma (19, 15360)
           (guardala desde tu herramienta con np.save justo antes de llamar al modelo).
--window-start : segundo del archivo donde empieza esa ventana (0 si es el inicio).
"""
import argparse
import importlib.util

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import torch

SFREQ = 256


def load_model_class(path):
    spec = importlib.util.spec_from_file_location("seizure_model_module", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.SeizureTransformer


def read_csv_bi(path):
    """Devuelve lista de (inicio, fin) en segundos para las filas 'seiz'."""
    events = []
    with open(path) as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#") or line.lower().startswith("channel"):
                continue
            parts = line.split(",")
            if len(parts) >= 4 and parts[3].strip() == "seiz":
                events.append((float(parts[1]), float(parts[2])))
    return events


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--model-file", required=True)
    ap.add_argument("--weights", required=True)
    ap.add_argument("--tensor", required=True)
    ap.add_argument("--csv-bi", default=None)
    ap.add_argument("--window-start", type=float, default=0.0)
    ap.add_argument("--threshold", type=float, default=0.5)
    ap.add_argument("--out", default="curva.png")
    args = ap.parse_args()

    # 1) Modelo: carga ESTRICTA (si las capas no coinciden, falla aqui y es la pista)
    model = load_model_class(args.model_file)()
    state = torch.load(args.weights, map_location="cpu")
    if isinstance(state, dict) and "state_dict" in state:
        state = state["state_dict"]
    result = model.load_state_dict(state, strict=True)
    print("Carga de pesos:", result)
    model.eval()

    # 2) Entrada: la misma ventana que usa tu herramienta
    x = np.load(args.tensor).astype(np.float32)
    assert x.shape == (19, 15360), f"Forma inesperada {x.shape}, se esperaba (19, 15360)"
    print(f"Entrada: min={x.min():.3f} max={x.max():.3f} media={x.mean():.3f} std={x.std():.3f}")

    # 3) Inferencia: la salida YA son probabilidades (el modelo aplica sigmoide)
    with torch.no_grad():
        prob = model(torch.from_numpy(x).unsqueeze(0))[0].numpy()
    print(f"Salida: forma={prob.shape} min={prob.min():.3f} max={prob.max():.3f} "
          f"media={prob.mean():.3f} fraccion>umbral={(prob >= args.threshold).mean():.3f}")

    # 4) Grafica
    t = args.window_start + np.arange(prob.size) / SFREQ
    fig, (ax_sig, ax) = plt.subplots(2, 1, figsize=(14, 6), sharex=True,
                                     gridspec_kw={"height_ratios": [1, 1]})
    ax_sig.plot(t, x[0], lw=0.4, color="gray")
    ax_sig.set_ylabel("canal 0")
    ax.plot(t, prob, lw=0.9, color="tab:blue", label="probabilidad del modelo")
    ax.axhline(args.threshold, color="red", ls="--", lw=0.8, label=f"umbral {args.threshold}")
    if args.csv_bi:
        events = read_csv_bi(args.csv_bi)
        for i, (s, e) in enumerate(events):
            for a in (ax_sig, ax):
                a.axvspan(s, e, color="orange", alpha=0.3,
                          label="seiz (csv_bi)" if (i == 0 and a is ax) else None)
        print(f"Eventos seiz en el CSV: {len(events)}")
    ax.set_ylim(-0.02, 1.02)
    ax.set_xlim(t[0], t[-1])
    ax.set_xlabel("segundos desde el inicio del archivo")
    ax.set_ylabel("P(convulsion)")
    ax.legend(loc="upper right")
    fig.savefig(args.out, dpi=130, bbox_inches="tight")
    print("Guardado:", args.out)


if __name__ == "__main__":
    main()