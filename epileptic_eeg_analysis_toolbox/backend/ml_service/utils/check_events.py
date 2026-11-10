import numpy as np
import pandas as pd
from backend.ml_service.utils.data_config import OUTPUTS_DIR
from backend.ml_service.utils.data_loader import build_annotations_index
from backend.ml_service.utils.postprocess import merge_intervals

PP = OUTPUTS_DIR / "seizure" / "pp_probs"
sess = pd.read_csv(PP / "sessions.csv")
ann = build_annotations_index(
    "seizure", n_patients=None, paths=True,
    CACHE_DIR=OUTPUTS_DIR / "seizure" / "annotations")
lab = ann["label"].astype(str).str.strip().str.lower()
ann["is_positive"] = (lab != "bckg").astype(int)
G = {k: g for k, g in ann.groupby(["Patient", "Session", "Section"])}

rows = []
for r in sess[sess.split == "val"].itertuples():
    f = PP / f"{r.Patient}_{r.Session}_{r.Section}.npz"
    if not f.exists():
        continue
    z = np.load(f)
    p, sf = z["probs"], float(z["sfreq"])
    g = G[(r.Patient, r.Session, r.Section)]
    g = g[g.is_positive == 1]
    for lb, gl in g.groupby("label"):
        for s, e in merge_intervals(zip(gl.start_time, gl.stop_time)):
            seg = p[int(s * sf):int(e * sf)]
            if seg.size == 0:
                continue
            rows.append(dict(label=lb, dur=e - s, patient=r.Patient,
                             pmax=float(seg.max()), pmean=float(seg.mean())))

df = pd.DataFrame(rows)
df["dur_bin"] = pd.cut(df.dur, [0, 20, 60, 180, 1e9],
                       labels=["<20s", "20-60s", "60-180s", ">180s"])


def summ(x):
    return pd.Series(dict(n=len(x), pmax_ge_05=(x.pmax >= 0.5).mean(),
                          pmax_ge_08=(x.pmax >= 0.8).mean(),
                          pmean_mediana=x.pmean.median()))


print(df.groupby("label").apply(summ).round(2))
print(df.groupby("dur_bin", observed=True).apply(summ).round(2))
print(df.groupby("patient").apply(summ).round(2).sort_values("pmax_ge_05"))
