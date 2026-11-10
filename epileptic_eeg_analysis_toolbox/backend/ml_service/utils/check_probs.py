import numpy as np, pandas as pd
from backend.ml_service.utils.data_config import OUTPUTS_DIR
from backend.ml_service.utils.data_loader import build_annotations_index

PP = OUTPUTS_DIR / "seizure" / "pp_probs"
sess = pd.read_csv(PP / "sessions.csv")
sess["ok"] = [(PP / f"{r.Patient}_{r.Session}_{r.Section}.npz").exists()
              for r in sess.itertuples()]
print(sess.groupby(["split", "sz", "ok"]).size().unstack(fill_value=0))

ann = build_annotations_index("seizure", n_patients=None, paths=True,
                              CACHE_DIR=OUTPUTS_DIR / "seizure" / "annotations")
ann["is_positive"] = (~ann["label"].astype(str).str.strip().str.lower().eq("bckg")).astype(int)
G = {k: g for k, g in ann.groupby(["Patient", "Session", "Section"])}

for r in sess[sess.ok].itertuples():
    z = np.load(PP / f"{r.Patient}_{r.Session}_{r.Section}.npz")
    p, sf = z["probs"], float(z["sfreq"])
    g = G[(r.Patient, r.Session, r.Section)]
    pos = g[g.is_positive == 1]
    m = np.zeros(len(p), bool)
    for s, e in zip(pos.start_time, pos.stop_time):
        m[int(s * sf):int(e * sf)] = True
    p_in = p[m].mean() if m.any() else float("nan")
    print(f"{r.split:4s} {r.Patient}_{r.Session}_{r.Section}: "
          f"proc={len(p)/sf/60:5.1f} min anot={g.Duration.iloc[0]/60:5.1f} min "
          f"crisis={m.mean()*100:5.1f}% p_dentro={p_in:.2f} p_fuera={p[~m].mean():.3f}")
