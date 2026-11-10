import json
import numpy as np
import pandas as pd
from backend.ml_service.utils.data_config import OUTPUTS_DIR
from backend.ml_service.utils.data_loader import build_annotations_index
from backend.ml_service.utils.postprocess import probs_to_events
from backend.ml_service.utils.postprocess import merge_intervals

PP = OUTPUTS_DIR / "seizure" / "pp_probs"
best = json.loads((PP / "postprocess_frozen.json").read_text())["postprocess"]
print("params:", best)
sess = pd.read_csv(PP / "sessions.csv")
ann = build_annotations_index(
    "seizure", n_patients=None, paths=True,
    CACHE_DIR=OUTPUTS_DIR / "seizure" / "annotations")
lab = ann["label"].astype(str).str.strip().str.lower()
ann["is_positive"] = (lab != "bckg").astype(int)
G = {k: g for k, g in ann.groupby(["Patient", "Session", "Section"])}


def ov(a, b):
    return a[1] > b[0] and a[0] < b[1]


recs = []
for r in sess[sess.split == "val"].itertuples():
    f = PP / f"{r.Patient}_{r.Session}_{r.Section}.npz"
    if not f.exists():
        continue
    z = np.load(f)
    g = G[(r.Patient, r.Session, r.Section)]
    g = g[g.is_positive == 1]
    ref = merge_intervals(zip(g.start_time, g.stop_time))
    recs.append((r, z["probs"].astype(np.float32), float(z["sfreq"]), ref))

hours = sum(len(p) / sf for _, p, sf, _ in recs) / 3600
print("horas val:", round(hours, 2), "sesiones:", len(recs))

print("--- falsas alarmas (params congelados) ---")
for r, p, sf, ref in recs:
    for s, e, c in probs_to_events(p, sf, best):
        if not any(ov((s, e), x) for x in ref):
            print(r.Patient, r.Session, r.Section,
                  "FA %.0f-%.0f s conf=%.2f" % (s, e, c))

print("--- eventos perdidos ---")
for r, p, sf, ref in recs:
    ev = probs_to_events(p, sf, best)
    for x in ref:
        if any(ov((s, e), x) for s, e, _ in ev):
            continue
        seg = p[int(x[0] * sf):int(x[1] * sf)]
        if seg.size == 0:
            print(r.Patient, r.Session, "fuera del rango procesado")
            continue
        print(r.Patient, r.Session, "dur=%.0fs pmax=%.2f pmean=%.2f"
              % (x[1] - x[0], seg.max(), seg.mean()))

print("--- curva variando solo thr_on ---")
for thr in (0.3, 0.5, 0.7, 0.8, 0.9, 0.95):
    q = dict(best)
    q["thr_on"] = thr
    hit = n = fa = 0
    for r, p, sf, ref in recs:
        ev = probs_to_events(p, sf, q)
        n += len(ref)
        hit += sum(any(ov((s, e), x) for s, e, _ in ev) for x in ref)
        fa += sum(not any(ov((s, e), x) for x in ref) for s, e, _ in ev)
    print("thr=%.2f sens=%.3f FA=%d FA/dia=%.1f"
          % (thr, hit / max(n, 1), fa, fa / (hours / 24)))
