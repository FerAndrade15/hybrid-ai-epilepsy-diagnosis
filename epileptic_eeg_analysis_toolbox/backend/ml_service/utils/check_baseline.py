import numpy as np
import pandas as pd
from scipy.ndimage import uniform_filter1d
from sklearn.metrics import roc_auc_score, average_precision_score
from backend.ml_service.utils.data_config import OUTPUTS_DIR
from backend.ml_service.utils.data_loader import build_annotations_index

PP = OUTPUTS_DIR / "seizure" / "pp_probs"
sess = pd.read_csv(PP / "sessions.csv")
ann = build_annotations_index(
    "seizure", n_patients=None, paths=True,
    CACHE_DIR=OUTPUTS_DIR / "seizure" / "annotations")
lab = ann["label"].astype(str).str.strip().str.lower()
ann["is_positive"] = (lab != "bckg").astype(int)
G = {k: g for k, g in ann.groupby(["Patient", "Session", "Section"])}

DEC = 8
variants = {"crudo": [], "menos mediana sesion": [],
            "menos media 5 min": [], "menos media 10 min": []}
ms = []
for r in sess[sess.split == "val"].itertuples():
    f = PP / f"{r.Patient}_{r.Session}_{r.Section}.npz"
    if not f.exists():
        continue
    z = np.load(f)
    p, sf = z["probs"].astype(np.float32), float(z["sfreq"])
    g = G[(r.Patient, r.Session, r.Section)]
    g = g[g.is_positive == 1]
    m = np.zeros(len(p), bool)
    for s, e in zip(g.start_time, g.stop_time):
        m[int(s * sf):int(e * sf)] = True
    p, m = p[::DEC], m[::DEC]
    fs = sf / DEC
    variants["crudo"].append(p)
    variants["menos mediana sesion"].append(p - np.median(p))
    for name, sec in (("menos media 5 min", 300), ("menos media 10 min", 600)):
        w = max(1, int(sec * fs))
        variants[name].append(p - uniform_filter1d(p, size=w, mode="nearest"))
    ms.append(m)

m = np.concatenate(ms)
for name, parts in variants.items():
    p = np.concatenate(parts)
    print("%-22s AUROC=%.3f AP=%.3f" % (name, roc_auc_score(m, p),
                                        average_precision_score(m, p)))
