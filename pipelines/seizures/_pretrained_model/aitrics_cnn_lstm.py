"""Pipeline: replicación agnóstica de Lee et al. (CHIL 2022) para detección de crisis en TUSZ.

Run (from the repo root, inside WSL / server):
    uv run python -u -m pipelines.seizure.cnn_lstm_paper --smoke     # 1) Prueba rápida end-to-end
    uv run python -u -m pipelines.seizure.cnn_lstm_paper --enc psd   # 2) Corrida completa (mejor encoder)
    uv run python -u -m pipelines.seizure.cnn_lstm_paper --enc all   # 3) Evaluar todos los encoders
"""
import argparse
from pathlib import Path

import pandas as pd

# Importaciones de tu configuración unificada
from src.core.data_config import (
    OUTPUTS_DIR, 
    VERSION, 
    ENC_CHOICES, 
    WINDOWS_REQUESTS_SEIZURES, 
    SEIZURE_BINARY_KEYBOARD
)
from src.core.data_loader import build_annotations_index
from src.core.data_splitter import get_or_compute_labeled_split
from src.utils.seizure_dataset import HybridSeizureDataset
from src.utils.seizure_eval import full_report
from src.models.aitrics_cnn_lstm import build_model, get_device, predict_sessions, train_model_aitrics

ap = argparse.ArgumentParser()
ap.add_argument("--enc", default="psd", help=f"{ENC_CHOICES} or 'all'")
ap.add_argument("--epochs", type=int, default=20)
ap.add_argument("--batch", type=int, default=8)
ap.add_argument("--steps", type=int, default=500, help="optimizer steps per epoch")
ap.add_argument("--lr", type=float, default=1e-3)
ap.add_argument("--workers", type=int, default=8)
ap.add_argument("--n-patients", type=int, default=None)
ap.add_argument("--val-max-sessions", type=int, default=None)
ap.add_argument("--force-retrain", action="store_true")
ap.add_argument("--smoke", action="store_true", help="Prueba rápida de fontanería")
args = ap.parse_args()

if args.smoke:
    args.n_patients, args.epochs, args.steps, args.val_max_sessions, args.workers = 40, 1, 20, 3, 2

CORPUS_OUT = OUTPUTS_DIR / "seizure" / ("smoke" if args.smoke else "full")
CACHE_DIR, ANN_DIR = CORPUS_OUT / "cache", OUTPUTS_DIR / "seizure" / "annotations"
for d in (CACHE_DIR, ANN_DIR):
    d.mkdir(parents=True, exist_ok=True)

device = get_device()
print(f"[INFO] Dispositivo: {device}")

# 1. Configuración de Taxonomía Dinámica
TAXONOMY = SEIZURE_BINARY_KEYBOARD
N_CLASSES = len(TAXONOMY.keys())

# 2. Indexación y División de Datos usando tu infraestructura agnóstica
print("[INFO] Construyendo índice y splits...")
ann_df = build_annotations_index("seizure", n_patients=args.n_patients, paths=True)
windowed_df, _, _ = get_or_compute_labeled_split(
    ann_df, label_col="is_positive", ratios={"train": 0.7, "val": 0.15, "test": 0.15}
)

train_ds = HybridSeizureDataset(windowed_df, "train", target_taxonomy=TAXONOMY)
val_index = windowed_df[windowed_df["split"] == "val"].reset_index(drop=True)
test_index = windowed_df[windowed_df["split"] == "test"].reset_index(drop=True)

encs = list(ENC_CHOICES) if args.enc == "all" else [args.enc]
all_reports = []

for enc in encs:
    print("\n" + "=" * 60 + f"\nFRONT-END: {enc}\n" + "=" * 60)
    model_dir = CORPUS_OUT / "models" / f"cnn2d_lstm_{enc}_v{VERSION}"
    
    # Instanciamos el modelo dinámico multiclase
    model = build_model(enc=enc, n_out=N_CLASSES, flatten_for_ml=False)

    model, hist = train_model_aitrics(
        model=model, train_ds=train_ds, val_index=val_index, target_taxonomy=TAXONOMY, 
        out_dir=model_dir, device=device, epochs=args.epochs,
        batch_size=args.batch, steps_per_epoch=args.steps, lr=args.lr,
        num_workers=args.workers, val_max_sessions=args.val_max_sessions,
        force=args.force_retrain
    )

    cap = 3 if args.smoke else None
    paths = {s: model_dir / f"preds_{s}.parquet" for s in ("val", "test")}
    
    for s, idx in (("val", val_index), ("test", test_index)):
        if paths[s].exists() and not args.force_retrain:
            continue
        print(f"[INFO] Prediciendo {s} ({len(idx)} secciones)...")
        preds_df = predict_sessions(model, idx, TAXONOMY, device, max_sessions=cap)
        preds_df.to_parquet(paths[s], index=False)

    # 3. Evaluación Clínica Final
    report = full_report(
        val_preds=pd.read_parquet(paths["val"]), 
        test_preds=pd.read_parquet(paths["test"]), 
        margin_sec=5,
        window_size_sec=WINDOWS_REQUESTS_SEIZURES["win_sec"],
        shift_sec=WINDOWS_REQUESTS_SEIZURES["shift_sec"]
    )
    report.insert(0, "enc", enc)
    report.to_csv(model_dir / "report.csv", index=False)
    all_reports.append(report)
    print(report.round(3).to_string(index=False))

pd.concat(all_reports).to_csv(CORPUS_OUT / f"report_all_v{VERSION}.csv", index=False)
print(f"\n[OK] cnn_lstm_paper | reports en {CORPUS_OUT}")