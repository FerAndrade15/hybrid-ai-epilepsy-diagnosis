import numpy as np
import pandas as pd
import torch
from scipy.stats import rankdata
from backend.pipelines.data_loader import load_raw_edf
from backend.ml_service.utils.preprocessing import raw_data_preproccesing
from backend.ml_service.inference_engine import ClinicalInferenceEngine
from backend.ml_service.utils.data_loader import build_annotations_index
from backend.ml_service.utils.data_config import OUTPUTS_DIR

N = 15360
PP = OUTPUTS_DIR / "seizure" / "pp_probs"
sess = pd.read_csv(PP / "sessions.csv")
sess = sess[(sess.split == "val") & (sess.sz == 1)]
ok = [(PP / f"{r.Patient}_{r.Session}_{r.Section}.npz").exists()
      for r in sess.itertuples()]
sess = sess[ok].head(8)
ann = build_annotations_index(
    "seizure", n_patients=None, paths=True,
    CACHE_DIR=OUTPUTS_DIR / "seizure" / "annotations")
lab = ann["label"].astype(str).str.strip().str.lower()
ann["is_positive"] = (lab != "bckg").astype(int)
G = {k: g for k, g in ann.groupby(["Patient", "Session", "Section"])}
engine = ClinicalInferenceEngine("models_weights/seizure_transformer.pth")


def zs(d):
    return (d - d.mean(1, keepdims=True)) / (d.std(1, keepdims=True) + 1e-8)


def run(d):
    out = []
    for i in range(d.shape[1] // N):
        x = torch.tensor(d[:, i * N:(i + 1) * N], dtype=torch.float32)
        with torch.no_grad():
            y = engine.model(x.unsqueeze(0))
        out.append(y.cpu().numpy().reshape(-1))
    return np.concatenate(out)


def auroc(p, m):
    n1 = int(m.sum())
    n0 = len(m) - n1
    if n1 == 0 or n0 == 0:
        return float("nan")
    r = rankdata(p)
    return (r[m].sum() - n1 * (n1 + 1) / 2) / (n1 * n0)


names = ["win 1-100", "rec 1-100", "win .5-120", "rec .5-120"]
rows = []
for r in sess.itertuples():
    raw = load_raw_edf(r.edf, preloaD=True)
    g = G[(r.Patient, r.Session, r.Section)]
    pos = g[g.is_positive == 1]
    res = []
    for lf, hf in ((1.0, 100.0), (0.5, 120.0)):
        prep = raw_data_preproccesing(
            raw_data=raw, l_freq=lf, h_freq=hf, notch_freq=60.0,
            bipolar_montage=False, resampling_freq=256)
        if len(prep.ch_names) != 19 or prep.n_times < N:
            continue
        sf = float(prep.info["sfreq"])
        n = (prep.n_times // N) * N
        d = prep.get_data()[:, :n]
        m = np.zeros(n, bool)
        for s, e in zip(pos.start_time, pos.stop_time):
            m[int(s * sf):int(e * sf)] = True
        dwin = np.concatenate(
            [zs(d[:, i * N:(i + 1) * N]) for i in range(n // N)], axis=1)
        for dd in (dwin, zs(d)):
            p = run(dd)
            res.append(auroc(p[::8], m[::8]))
    rows.append(res)
    print(r.Patient, r.Session, r.Section,
          " ".join("%.3f" % v for v in res), flush=True)

print("--- AUROC medio ---")
for nm, v in zip(names, np.nanmean(np.array(rows), axis=0)):
    print(nm, "%.3f" % v)
