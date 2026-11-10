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
K = ["Patient", "Session", "Section"]
mont = ann.drop_duplicates(K).set_index(K)["Montage"].to_dict()
G = {k: g for k, g in ann.groupby(K)}

rows = []
for r in sess[sess.split == "val"].itertuples():
    f = PP / f"{r.Patient}_{r.Session}_{r.Section}.npz"
    if not f.exists():
        continue
    z = np.load(f)
    p, sf = z["probs"], float(z["sfreq"])
    key = (r.Patient, r.Session, r.Section)
    g = G[key]
    g = g[g.is_positive == 1]
    for s, e in merge_intervals(zip(g.start_time, g.stop_time)):
        seg = p[int(s * sf):int(e * sf)]
        if seg.size == 0:
            continue
        rows.append(dict(patient=r.Patient, montage=mont[key],
                         dur=e - s, pmax=float(seg.max())))

df = pd.DataFrame(rows)
df["det"] = df.pmax >= 0.5
print(df.groupby("montage").agg(n=("pmax", "size"), det=("det", "mean"),
                                pmax_med=("pmax", "median")).round(2))
print(df.groupby("patient").agg(
    montage=("montage", lambda x: ",".join(sorted(set(x)))),
    n=("pmax", "size"), det=("det", "mean"),
    pmax_med=("pmax", "median"), dur_med=("dur", "median")
).round(2).sort_values("det"))
