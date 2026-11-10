import numpy as np
from backend.pipelines.data_loader import load_raw_edf
from backend.ml_service.utils.preprocessing import raw_data_preproccesing
from backend.ml_service.utils.windowing import slice_raw_into_windows
from backend.ml_service.inference_engine import ClinicalInferenceEngine
from backend.ml_service.utils.data_loader import build_annotations_index
from backend.ml_service.utils.data_config import OUTPUTS_DIR

KEY = ("aaaaaajy", "s003", "t003")
engine = ClinicalInferenceEngine("models_weights/seizure_transformer.pth")
orig_scale = engine.data_scale
print("training mode:", engine.model.training, "| scale:", orig_scale)

ann = build_annotations_index(
    "seizure", n_patients=None, paths=True,
    CACHE_DIR=OUTPUTS_DIR / "seizure" / "annotations")
g = ann[(ann.Patient == KEY[0]) & (ann.Session == KEY[1])
        & (ann.Section == KEY[2])]
print("Duracion real:", g.Duration.iloc[0], "s")
pos = g[g.label != "bckg"]
cols = ["channel", "start_time", "stop_time", "label"]
print(pos[cols].drop_duplicates().head(12).to_string())
print("--- CSV original ---")
print(open(g.CSV.iloc[0]).read()[:900])

raw = load_raw_edf(g.EDF.iloc[0], preloaD=True)
prep = raw_data_preproccesing(
    raw_data=raw, l_freq=1.0, h_freq=100.0, notch_freq=60.0,
    bipolar_montage=False, resampling_freq=256)
sf = float(prep.info["sfreq"])
wins = slice_raw_into_windows(raw=prep, window_size_sec=60.0, stride_sec=60.0)
mask = np.zeros(len(wins) * 15360, bool)
for s, e in zip(pos.start_time, pos.stop_time):
    mask[int(s * sf):int(e * sf)] = True


def zs(d):
    return (d - d.mean(1, keepdims=True)) / (d.std(1, keepdims=True) + 1e-8)


def ident(d):
    return d


variants = {"actual": (ident, orig_scale), "zscore": (zs, 1.0)}
for name, (fn, sc) in variants.items():
    engine.data_scale = sc
    parts = [engine.predict_probs(fn(np.asarray(w["data"]))) for w in wins]
    p = np.concatenate(parts)
    m = mask[:len(p)]
    print(name, "p_dentro=%.3f p_fuera=%.3f max=%.2f"
          % (p[m].mean(), p[~m].mean(), p.max()))
