"""Pipeline: replicación agnóstica de Lee et al. (CHIL 2022) para detección de crisis en TUSZ.

    uv run python -u -m pipelines.seizures.aitrics_cnn_lstm --smoke
    uv run python -u -m pipelines.seizures.aitrics_cnn_lstm --enc psd
    uv run python -u -m pipelines.seizures.aitrics_cnn_lstm --enc psd --tune 15
    uv run python -u -m pipelines.seizures.aitrics_cnn_lstm --enc all
"""
import argparse
import shutil

import numpy as np
import pandas as pd

from src.core.data_config import (
    OUTPUTS_DIR, VERSION, ENC_CHOICES,
    WINDOWS_REQUESTS_SEIZURES, SEIZURE_MULTILABELS, SEIZURE_SESSION_CACHE,
    PARTITION_TO_SPLIT,
)
from src.core.windowing import split_compound_label
from src.core.data_loader import build_annotations_index
from src.utils.patient_registry import load_registry, forced_for
from src.utils.seizure_dataset import HybridSeizureDataset
from src.utils.seizure_eval import full_report, window_metrics
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
ap.add_argument("--tune", type=int, default=0, help="n trials de Optuna (0 = parámetros del paper)")
ap.add_argument("--force-retrain", action="store_true")
ap.add_argument("--smoke", action="store_true", help="Prueba rápida de fontanería")
ap.add_argument("--tune-epochs", type=int, default=8, help="épocas por intento de Optuna")
args = ap.parse_args()

if args.smoke:
    args.n_patients, args.epochs, args.steps, args.val_max_sessions, args.workers = 40, 1, 20, 3, 2

CORPUS_OUT = OUTPUTS_DIR / "seizure" / ("smoke" if args.smoke else "full")
ANN_DIR = OUTPUTS_DIR / "seizure" / "annotations"
TUNE_DIR = CORPUS_OUT / "tune"
for d in (CORPUS_OUT, ANN_DIR, TUNE_DIR):
    d.mkdir(parents=True, exist_ok=True)

device = get_device()
print(f"[INFO] Dispositivo: {device}")

TAXONOMY = {"seiz": SEIZURE_MULTILABELS}
N_CLASSES = len(TAXONOMY)

ann_df = build_annotations_index("seizure", n_patients=None, paths=True, CACHE_DIR=ANN_DIR)
ann_df["EDF_path"] = ann_df["EDF"]
ann_df["is_positive"] = ann_df["label"].map(
    lambda l: int(bool(split_compound_label(str(l)) & SEIZURE_MULTILABELS))
)

forced = forced_for(load_registry(), ann_df["Patient"].unique(), source_prefix="folder:seizure")
ann_df["split"] = ann_df["Patient"].map(forced)

off = ann_df["Partition"].map(PARTITION_TO_SPLIT)       # solo informativo
print(f"[CHECK] registro == partición oficial: {(ann_df['split'] == off).mean():.1%}")
print(f"[CHECK] pacientes sin regla (se excluyen): {ann_df.loc[ann_df['split'].isna(), 'Patient'].nunique()}")
ann_df = ann_df[ann_df["split"].notna()].reset_index(drop=True)

if args.n_patients:     # smoke: pacientes con crisis, repartidos entre los tres splits
    per_split = {"train": args.n_patients // 2, "val": args.n_patients // 4, "test": args.n_patients // 4}
    sz = ann_df.groupby("Patient").agg(split=("split", "first"), sz=("is_positive", "sum"))
    keep = [p for s, n in per_split.items() for p in sz[(sz.split == s) & (sz.sz > 0)].index[:n]]
    ann_df = ann_df[ann_df["Patient"].isin(keep)].reset_index(drop=True)

windowed_df = ann_df
print(ann_df.drop_duplicates("Patient")["split"].value_counts())
print(ann_df["label"].value_counts().head(8))
sz = ann_df.groupby("Patient")["is_positive"].sum()
print(f"pacientes: {len(sz)} | con crisis: {(sz > 0).sum()} | filas de crisis: {int(sz.sum())}")
print(sz.groupby(ann_df.drop_duplicates("Patient").set_index("Patient")["split"]).agg(["count", "sum"]))

train_ds = HybridSeizureDataset(windowed_df, "train", target_taxonomy=TAXONOMY,
                                session_cache_dir=str(SEIZURE_SESSION_CACHE))

has_sz = windowed_df.groupby(["Patient", "Session", "Section"])["is_positive"].transform("max") > 0
pool = windowed_df[has_sz] if args.smoke else windowed_df
val_index = pool[pool["split"] == "val"].reset_index(drop=True)          # evaluación final
test_index = pool[pool["split"] == "test"].reset_index(drop=True)

# Subconjunto fijo de val (solo sesiones con crisis) para elegir hiperparámetros con Optuna
val_sz = windowed_df[has_sz & (windowed_df["split"] == "val")]
sess_keys = val_sz[["Patient", "Session", "Section"]].drop_duplicates()
sess_keys = sess_keys.sample(n=min(20, len(sess_keys)), random_state=0)
tune_val_index = val_sz.merge(sess_keys, on=["Patient", "Session", "Section"]).reset_index(drop=True)

encs = list(ENC_CHOICES) if args.enc == "all" else [args.enc]
all_reports = []

for enc in encs:
    print("\n" + "=" * 60 + f"\nFRONT-END: {enc}\n" + "=" * 60)

    # ---------- Búsqueda de hiperparámetros ----------
    HP = {}
    if args.tune:
        import gc
        import torch
        import optuna

        STUDY_NAME = f"seiz_{enc}_v{VERSION}"
        DB_URL = f"sqlite:///{TUNE_DIR / (STUDY_NAME + '.db')}"     # separado por smoke/full

        def objective(trial):
            p = dict(
                lr=trial.suggest_float("lr", 1e-4, 3e-3, log=True),
                weight_decay=trial.suggest_float("weight_decay", 1e-7, 1e-3, log=True),
                dropout=trial.suggest_float("dropout", 0.0, 0.3),
                hidden=trial.suggest_categorical("hidden", [128, 256]),
                n_layers=trial.suggest_int("n_layers", 1, 2),
                pos_frac=trial.suggest_float("pos_frac", 0.3, 0.7),
            )
            tdir = TUNE_DIR / enc / f"trial_{trial.number}"
            m = build_model(enc=enc, n_out=N_CLASSES, hidden=p["hidden"],
                            n_layers=p["n_layers"], dropout=p["dropout"])
            try:
                _, hist = train_model_aitrics(
                    m, train_ds, tune_val_index, TAXONOMY, tdir, device,
                    epochs=args.tune_epochs, batch_size=args.batch, steps_per_epoch=150,
                    lr=p["lr"], weight_decay=p["weight_decay"], pos_frac=p["pos_frac"],
                    num_workers=args.workers, force=True,
                    session_cache_dir=str(SEIZURE_SESSION_CACHE), trial=trial)
                vals = [h["val_auroc"] for h in hist if not np.isnan(h["val_auroc"])]
                return max(vals) if vals else 0.0
            except RuntimeError as e:
                if "out of memory" in str(e):
                    print(f"[OOM] Intento {trial.number}: sin memoria en GPU, se poda.")
                    raise optuna.TrialPruned()
                raise
            finally:
                shutil.rmtree(tdir, ignore_errors=True)       # no llenar el disco con best.pt
                del m
                gc.collect()
                if torch.cuda.is_available():
                    torch.cuda.empty_cache()

        study = optuna.create_study(
            direction="maximize", study_name=STUDY_NAME, storage=DB_URL,
            load_if_exists=True,        # si el pod se apaga, retoma donde quedó
            sampler=optuna.samplers.TPESampler(seed=42),
            pruner=optuna.pruners.MedianPruner(n_startup_trials=5, n_warmup_steps=2))

        print(f"[TUNE] {enc}: intentos previos en el estudio: {len(study.trials)}")
        study.optimize(objective, n_trials=args.tune, gc_after_trial=True)

        HP = study.best_params
        print(f"[TUNE] {enc} best val AUROC={study.best_value:.4f} params={HP}")
    # ---------- Entrenamiento final ----------
    tag = "_tuned" if HP else ""
    model_dir = CORPUS_OUT / "models" / f"cnn2d_lstm_{enc}_v{VERSION}{tag}"

    model = build_model(enc=enc, n_out=N_CLASSES, flatten_for_ml=False,
                        hidden=HP.get("hidden", 256), n_layers=HP.get("n_layers", 2),
                        dropout=HP.get("dropout", 0.1))

    model, hist = train_model_aitrics(
        model=model, train_ds=train_ds, val_index=val_index, target_taxonomy=TAXONOMY,
        out_dir=model_dir, device=device, epochs=args.epochs,
        batch_size=args.batch, steps_per_epoch=args.steps,
        lr=HP.get("lr", args.lr), weight_decay=HP.get("weight_decay", 1e-6),
        pos_frac=HP.get("pos_frac", 0.5),
        num_workers=args.workers, val_max_sessions=args.val_max_sessions,
        force=args.force_retrain, session_cache_dir=str(SEIZURE_SESSION_CACHE)
    )

    # ---------- Predicciones y evaluación ----------
    cap = 3 if args.smoke else None
    paths = {s: model_dir / f"preds_{s}.parquet" for s in ("val", "test")}

    for s, idx in (("val", val_index), ("test", test_index)):
        if paths[s].exists() and not args.force_retrain:
            continue
        print(f"[INFO] Prediciendo {s} ({len(idx)} filas de anotación)...")
        preds_df = predict_sessions(model, idx, TAXONOMY, device, max_sessions=cap,
                                    session_cache_dir=str(SEIZURE_SESSION_CACHE))
        preds_df.to_parquet(paths[s], index=False)

    report = full_report(
        val_preds=pd.read_parquet(paths["val"]),
        test_preds=pd.read_parquet(paths["test"]),
        margin_sec=5,
        window_size_sec=WINDOWS_REQUESTS_SEIZURES["win_sec"],
        shift_sec=WINDOWS_REQUESTS_SEIZURES["shift_sec"]
    )
    report.insert(0, "enc", enc)
    report.insert(1, "tuned", bool(HP))
    report.to_csv(model_dir / "report.csv", index=False)
    all_reports.append(report)
    print(report.round(3).to_string(index=False))

    wm = window_metrics(
        pd.read_parquet(paths["test"]),
        dict(zip(report["Class"], report["Best_Threshold"])),
        shift_sec=WINDOWS_REQUESTS_SEIZURES["shift_sec"],
    )
    wm.insert(0, "enc", enc)
    wm.to_csv(model_dir / "window_metrics.csv", index=False)
    print(wm.round(3).to_string(index=False))

pd.concat(all_reports).to_csv(CORPUS_OUT / f"report_all_v{VERSION}.csv", index=False)
print(f"\n[OK] aitrics_cnn_lstm | reports en {CORPUS_OUT}")