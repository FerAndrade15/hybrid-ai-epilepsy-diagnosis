"""
# File: extract_probs.py
# Project: Trabajo de graduación
"""
import argparse, numpy as np, pandas as pd
from pathlib import Path
from backend.pipelines.data_loader import load_raw_edf
from backend.pipelines.preprocessing import raw_data_preproccesing
from backend.pipelines.windowing import slice_raw_into_windows
from backend.ml_service.inference_engine import ClinicalInferenceEngine
from backend.ml_service.utils.data_loader import build_annotations_index
from backend.ml_service.utils.data_config import OUTPUTS_DIR
from backend.ml_service.utils.patient_registry import load_registry, forced_for

ap = argparse.ArgumentParser()
ap.add_argument("--model", required=True)
ap.add_argument("--n-sz", type=int, default=20)       # sesiones con crisis por split
ap.add_argument("--n-bg", type=int, default=20)       # sesiones sin crisis por split
ap.add_argument("--splits", nargs="+", default=["val", "test"])
args = ap.parse_args()

OUT = OUTPUTS_DIR / "seizure" / "pp_probs"; OUT.mkdir(parents=True, exist_ok=True)
ann = build_annotations_index("seizure", n_patients=None, paths=True,
                              CACHE_DIR=OUTPUTS_DIR / "seizure" / "annotations")
ann["split"] = ann["Patient"].map(forced_for(load_registry(), ann["Patient"].unique(),
                                             source_prefix="folder:seizure"))
ann = ann[ann["split"].isin(args.splits)]
# ajusta estos nombres si tus columnas difieren (ann.columns)
ann["is_positive"] = ann["is_positive"] if "is_positive" in ann else 0

sess = (ann.groupby(["Patient", "Session", "Section"])
           .agg(split=("split", "first"), edf=("EDF", "first"), sz=("is_positive", "max"))
           .reset_index())
pick = []
for s in args.splits:
    for flag, n in ((1, args.n_sz), (0, args.n_bg)):
        sub = sess[(sess.split == s) & (sess.sz == flag)]
        pick.append(sub.sample(n=min(n, len(sub)), random_state=0))
pick = pd.concat(pick)

engine = ClinicalInferenceEngine(args.model)
for r in pick.itertuples():
    f = OUT / f"{r.Patient}_{r.Session}_{r.Section}.npz"
    if f.exists():
        continue
    raw = load_raw_edf(r.edf, preload=True)
    prep = raw_data_preproccesing(raw_data=raw, l_freq=1.0, h_freq=100.0, notch_freq=60.0,
                                  bipolar_montage=False, resampling_freq=256)  # = al worker
    sfreq = float(prep.info["sfreq"])
    wins = slice_raw_into_windows(raw=prep, window_size_sec=60.0, stride_sec=60.0)
    probs = np.concatenate([engine.predict_probs(w["data"]) for w in wins])
    np.savez_compressed(f, probs=probs.astype(np.float16), sfreq=sfreq)
    print("[OK]", f.name, f"{len(probs)/sfreq/60:.1f} min")
pick.to_csv(OUT / "sessions.csv", index=False)