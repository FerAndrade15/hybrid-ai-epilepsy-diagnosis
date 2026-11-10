import numpy as np
import pandas as pd
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

for split in ("val",):
    ps, ms = [], []
    for r in sess[sess.split == split].itertuples():
        f = PP / f"{r.Patient}_{r.Session}_{r.Section}.npz"
        if not f.exists():
            continue
        z = np.load(f)
        p, sf = z["probs"], float(z["sfreq"])
        g = G[(r.Patient, r.Session, r.Section)]
        g = g[g.is_positive == 1]
        m = np.zeros(len(p), bool)
        for s, e in zip(g.start_time, g.stop_time):
            m[int(s * sf):int(e * sf)] = True
        ps.append(p[::8])
        ms.append(m[::8])
    p, m = np.concatenate(ps), np.concatenate(ms)
    print(split, "muestras=%d prevalencia=%.3f AUROC=%.3f AP=%.3f"
          % (len(p), m.mean(), roc_auc_score(m, p), average_precision_score(m, p)))
