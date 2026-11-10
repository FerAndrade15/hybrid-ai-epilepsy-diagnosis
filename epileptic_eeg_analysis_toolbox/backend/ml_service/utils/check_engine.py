import numpy as np
from backend.pipelines.data_loader import load_raw_edf
from backend.ml_service.utils.preprocessing import raw_data_preproccesing
from backend.ml_service.utils.windowing import slice_raw_into_windows
from backend.ml_service.inference_engine import ClinicalInferenceEngine
from backend.ml_service.utils.data_loader import build_annotations_index
from backend.ml_service.utils.data_config import OUTPUTS_DIR

KEY = ("aaaaaajy", "s003", "t003")
ann = build_annotations_index(
    "seizure", n_patients=None, paths=True,
    CACHE_DIR=OUTPUTS_DIR / "seizure" / "annotations")
g = ann[(ann.Patient == KEY[0]) & (ann.Session == KEY[1])
        & (ann.Section == KEY[2])]
raw = load_raw_edf(g.EDF.iloc[0], preloaD=True)
prep = raw_data_preproccesing(
    raw_data=raw, l_freq=1.0, h_freq=100.0, notch_freq=60.0,
    bipolar_montage=False, resampling_freq=256)
wins = slice_raw_into_windows(raw=prep, window_size_sec=60.0, stride_sec=60.0)
print("claves de ventana:", list(wins[0].keys()))

engine = ClinicalInferenceEngine("models_weights/seizure_transformer.pth")
print("posproceso:", engine.postprocess)
ev = engine.predict_study_windows(wins)
ev_raw = engine.predict_study_windows(wins, raw=True)
print("eventos ajustado:", len(ev), "| crudo:", len(ev_raw))
for e in ev:
    print("  %.1f - %.1f s  conf=%.2f"
          % (e["start_time"], e["stop_time"], e["confidence"]))

z = np.load(OUTPUTS_DIR / "seizure" / "pp_probs" / ("_".join(KEY) + ".npz"))
p = engine.last_probs
print("largo app/guardado:", len(p), len(z["probs"]),
      "| diferencia maxima:", float(np.abs(p - z["probs"]).max()))
