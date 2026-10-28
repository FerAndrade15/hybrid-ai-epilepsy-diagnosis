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
pick.to_csv(OUT / "sessions.csv", index=False)

n_ch, n_s = engine.model.in_channels, engine.model.in_samples   # 19, 15360
failed = []
for r in pick.itertuples():
    f = OUT / f"{r.Patient}_{r.Session}_{r.Section}.npz"
    if f.exists():
        continue
    try:
        raw = load_raw_edf(r.edf, preloaD=True)
        prep = raw_data_preproccesing(raw_data=raw, l_freq=1.0, h_freq=100.0,
                                      notch_freq=60.0, bipolar_montage=False,
                                      resamplig_freq=256)
        sfreq = float(prep.info["sfreq"])
        wins = slice_raw_into_windows(raw=prep, window_size_sec=60.0, stride_sec=60.0)

        parts = []
        for i, w in enumerate(wins):
            d = np.asarray(w["data"])
            if d.shape[0] != n_ch and d.shape[1] == n_ch:
                d = d.T
            assert d.shape[0] == n_ch, f"ventana {i}: {d.shape}"
            n = d.shape[1]
            if n != n_s:
                print(f"[AVISO] {f.stem} ventana {i}/{len(wins)}: {n} muestras")
            if n > n_s:
                d, n = d[:, :n_s], n_s
            elif n < n_s:
                d = np.pad(d, ((0, 0), (0, n_s - n)))
            parts.append(engine.predict_probs(d)[:n])

        probs = np.concatenate(parts)
        np.savez_compressed(f, probs=probs.astype(np.float32), sfreq=sfreq)
        print("[OK]", f.name, f"{len(probs)/sfreq/60:.1f} min")
    except (ValueError, AssertionError) as e:
        print(f"[FALLA] {f.stem}: {e}")
        failed.append(f.stem)

print(f"Terminado. Fallidas: {len(failed)}")