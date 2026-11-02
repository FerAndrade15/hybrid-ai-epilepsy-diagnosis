"""
# File: inference_engine.py
# Project: Trabajo de graduación
# Author: Maria Fernanda Andrade Recinos
#
# Main orchestrator for clinical predictions
#   - Loads checkpoints
#   - Get predictions from continuos windows
#   - Structure data for GUI events
"""
# inference_engine.py
# Imports models 
import joblib
import json
import torch
import pickle
import numpy as np
import pandas as pd
from pathlib import Path
from dataclasses import dataclass
from typing import Optional, List, Dict,  Any, Protocol

# Internal functions
from config.app_config import CHECKPOINTS_DIR
from config.data_config import SFREQ
from backend.ml_service.models_registry import get_model_config
from backend.ml_service.utils.postprocess import probs_to_events, DEFAULT_PP
from backend.ml_service.models_registry import get_model_config
from backend.ml_service.utils.feature_extractor import extract_features_from_window_payload

PP_DIR = Path(r"C:\Users\ferch\Documents\Various\EngineeringDesignAndInnovation\hybrid-ai-epilepsy-diagnosis\epileptic_eeg_analysis_toolbox\backend\ml_service\postprocessing")
RAW_PP = dict(smooth_sec=0.0, thr_on=0.5, thr_off_ratio=1.0,
              merge_gap_sec=0.0, min_dur_sec=0.0)

@dataclass
class ProbTrack:
    values: np.ndarray
    sfreq: float
    t0: float = 0.0
    kind: str = "data"
    name: str = ""

# Protocol
class TraditionalMLModel(Protocol):
    def predict(self, X:Any)->Any:...
    def predict_proba(self, X:Any)->Any:...

# Inference engine
class ClinicalInferenceEngine:
    def __init__(self, model_filename: Optional[str] = None, threshold: int = 0.5) -> None:
        self.model: Any = None
        self.model_type = None
        self.output_type = None
        self.feature_columns: Optional[List[str]] = None
        self.scaler = None
        self.threshold = threshold
        self.norm = "zscore"
        self.transpose = False
        self.data_scale = 1e6

        if model_filename:
            self.load_model(model_filename)

    def track_from_data(probs, sfreq, t0):
        return ProbTrack(np.asarray(probs, np.float32), sfreq, t0, "data")

    def _as_channels_first(self, data, n_ch, idx=None):
        """(n_ch, samples) or ERROR"""
        d = np.asarray(data)
        if d.ndim != 2:
            raise ValueError(f"ventana {idx}: se esperaba 2D, llegó {d.shape}")
        if d.shape[0] == n_ch:
            return d
        if d.shape[1] == n_ch:
            return d.T
        raise ValueError(f"ventana {idx}: forma {d.shape} no tiene {n_ch} canales")

    def track_from_windows(win_probs, win_starts, win_len_s, n, sfreq, t0):
        """win_starts en segundos absolutos; promedia donde hay solape."""
        acc = np.zeros(n, np.float32); cnt = np.zeros(n, np.float32)
        for p, st in zip(win_probs, win_starts):
            s = max(0, int((st - t0) * sfreq))
            e = min(n, int((st - t0 + win_len_s) * sfreq))
            acc[s:e] += p; cnt[s:e] += 1
        out = np.full(n, np.nan, np.float32)
        m = cnt > 0
        out[m] = acc[m] / cnt[m]
        return ProbTrack(out, sfreq, t0, "window")

    def track_from_events(events, n, sfreq, t0, outside=0.0):
        """events: [(start_abs, stop_abs, conf)]. Fuera de evento = `outside` (0), no NaN."""
        out = np.full(n, outside, np.float32)
        for s, e, c in events:
            i, j = max(0, int((s - t0) * sfreq)), min(n, int((e - t0) * sfreq))
            out[i:j] = np.fmax(out[i:j], c)
        return ProbTrack(out, sfreq, t0, "event")

    def _prepare_input(self, signal_window):
        sig = np.asarray(signal_window, dtype=np.float64)
        if self.norm == "zscore":
            sig = (sig - sig.mean(1, keepdims=True)) / (sig.std(1, keepdims=True) + 1e-8)
        else:                                   # "scale"
            sig = sig * self.data_scale
        if self.transpose:
            sig = sig.T
        return torch.tensor(sig, dtype=torch.float32).unsqueeze(0)

    def _forward_dl(self, signal_window, features=None) -> np.ndarray:
        """Devuelve un ndarray 1D con la salida del modelo (probabilidades)."""
        x = self._prepare_input(signal_window)

        x_feat = None
        if self.feature_columns and self.scaler is not None and features is not None:
            vals = [features.get(c, 0.0) for c in self.feature_columns]
            arr = self.scaler.transform(np.array([vals], dtype=np.float32))
            x_feat = torch.tensor(arr, dtype=torch.float32)

        with torch.no_grad():
            out = self.model(x, x_feat) if x_feat is not None else self.model(x)

        if hasattr(out, "probabilities"):
            p = out.probabilities
        elif hasattr(out, "logits"):
            lg = out.logits
            p = torch.sigmoid(lg) if lg.shape[-1] == 1 else torch.softmax(lg, dim=-1)
        else:
            p = out
        return p.detach().cpu().numpy().reshape(-1)

    def _window_prob(self, signal_window, ch_names, sfreq=SFREQ,
                 positive_label=1, **kw) -> float:
        """Devuelve P(crisis) de una ventana, como float en [0,1]."""
        if self.model_type == "traditional_ml":
            features = extract_features_from_window_payload(
                channel_data=signal_window, ch_names=ch_names, sfreq=sfreq, **kw)
            df = pd.DataFrame([features])
            if self.feature_columns is not None:
                df = df.reindex(columns=self.feature_columns, fill_value=0.0)
            if hasattr(self.model, "predict_proba"):
                proba = self.model.predict_proba(df)[0]
                return float(proba[list(self.model.classes_).index(positive_label)])
            return float(self.model.predict(df)[0] == positive_label)

        # deep learning con salida por ventana
        p = self._forward_dl(signal_window)          # tu bloque actual, devuelto como ndarray
        if p.size == 1:
            return float(p[0])
        if p.size == 2:
            return float(p[1])                       # softmax de 2 clases: índice 1 = crisis
        return float(p.max())                        # curva: resume la ventana por su máximo

    def _predict_events(self, windows, thr=0.5, **kw):
        L = self.window_size_sec
        segs = []
        for w in windows:
            p = self._window_prob(w["data"], w["ch_names"], **kw)
            if p >= thr:
                s, e = w["start"], w["start"] + L
                if segs and s <= segs[-1][1] + 1e-6:
                    segs[-1][1] = e
                    segs[-1][2].append(p)
                else:
                    segs.append([s, e, [p]])
        return [(s, e, float(np.mean(ps))) for s, e, ps in segs]


    def predict_probs(self, signal_window):
        """Devuelve las probabilidades por muestra, sin posprocesado."""
        sig = np.asarray(signal_window, dtype=np.float64)
        sig = (sig - sig.mean(1, keepdims=True)) / (sig.std(1, keepdims=True) + 1e-8)
        x = torch.tensor(np.transpose(sig) if self.transpose else sig,
                         dtype=torch.float32).unsqueeze(0)
        with torch.no_grad():
            out = self.model(x)
        p = out.probabilities if hasattr(out, "probabilities") else out
        p = p.detach().cpu().numpy().reshape(-1)
        if p.min() < 0 or p.max() > 1:
            raise ValueError("La salida no está en [0,1]: aplica sigmoid o revisa el modelo")
        return p

    def load_model(self, model_filename:str):
        model_path = Path(model_filename)
        print(model_filename)
        if not model_path.exists():
            raise FileNotFoundError(f"No se encontró el modelo en {model_path.resolve()}")

        ext = model_path.suffix.lower()
        if ext in ['.joblib', '.pkl']:
            self._load_traditional_ml(model_path)
        elif ext in ['.pth', '.pt']:
            self._load_deep_learning(model_path, model_filename)
        else:
            raise ValueError(f"Formato del modelo no soportado: {ext}")

    def _load_traditional_ml(self, model_path: Path):
        self.model_type = "traditional_ml"
        self.output_type = "global_classification"
        
        checkpoint = joblib.load(model_path)

        # Paquets support with metadata
        if isinstance(checkpoint, dict) and "model" in checkpoint:
            loaded_model = checkpoint["model"]
            self.feature_columns = checkpoint.get("features", None)
        else:
            loaded_model = checkpoint
            self.feature_columns = getattr(self.model, "feature_names_in_", None)
            if self.feature_columns is not None:
                self.feature_columns = list(self.feature_columns)

        if not hasattr(loaded_model, "predict"):
            raise TypeError(f"El modelo {model_path.name} es inválido, no tiene método predict.")

        self.model = loaded_model

    def _load_deep_learning(self, model_path: Path, filename: str):
            self.model_type = "deep_learning"

            # Relation document and registry
            config = get_model_config(filename)

            self.output_type = config.get("output_type", "binary_segmentation")
            self.window_size_sec = config.get("window_size_sec", 60.0)
            self.stride_sec = config.get("stride_sec", 60.0)
            self.transpose = config.get("transpose", False)
            self.data_scale = config.get("scale", 1e6)
            self.data_units = config.get("classification_output", "window")
            self.postprocess = config.get("postprocess")
            self.pp_source = config.get("postprocess_source")

            architecture_class = config["class"]
            parameters = config["parameters"]

            # Dynamic instance
            self.feature_columns = parameters.get("selected_features", [])
            self.model = architecture_class(**parameters)

            # Loading weights
            state = torch.load(model_path, map_location=torch.device('cpu'))
            state_dict = state.get("state_dict") or state
            self.model.load_state_dict(state)
            self.model.eval()

            scaler_path = model_path.parent / "feature_scaler.pkl"
            if scaler_path.exists() and self.feature_columns:
                with open(scaler_path, "rb") as fp:
                    self.scaler = pickle.load(fp)

            model_key = Path(filename).stem
            pp_file = PP_DIR / f"{model_key}.json"
            if pp_file.exists():
                self.postprocess = json.loads(pp_file.read_text())["postprocess"]
            else:
                self.postprocess = config.get("postprocess") or DEFAULT_PP
                print(f"[AVISO] {model_key}: sin PP ajustado, usando DEFAULT_PP")

    def predict_study_windows(self, windows, sfreq=SFREQ, components_full=None,
                              mixing_matrix=None, ic_probs=None, raw=False, ch_names=None):
        self.last_probs = None
        self.last_track = None
        if not windows:
            return []
        
        kw = dict(mixing_matrix=mixing_matrix, ic_probs=ic_probs)
        t0 = windows[0]["start"]
        last = windows[-1]
        n = int(round((last["start"] - t0) * sfreq)) + np.asarray(last["data"]).shape[-1]

        n_ch = len(ch_names) if ch_names else getattr(self.model, "in_channels", None)
        if n_ch is None:
            raise ValueError("No se pudo determinar el número de canales: pasa ch_names")
        windows = [dict(w, data=self._as_channels_first(w["data"], n_ch, i))
                        for i, w in enumerate(windows)]

        def to_dicts(evs):
            return [{"start_time": s, "stop_time": e, "duration": round(e - s, 2),
                        "label": "Crisis", "confidence": c} for s, e, c in evs]

        # Time-step
        if self.model_type == "deep_learning" and self.data_units == "data":
            probs = np.concatenate([self.predict_probs(w["data"]) for w in windows])
            self.last_probs = probs                  # curva cruda, siempre
            pp = RAW_PP if raw else self.postprocess
            t0 = windows[0]["start"]
            return [{"start_time": t0 + s, "stop_time": t0 + e,
                     "duration": round(e - s, 2), "label": "Crisis", "confidence": c}
                    for s, e, c in probs_to_events(probs, sfreq, pp)]

        # Windows
        if self.data_units == "window":
            wp = [self._window_prob(w, **kw) for w in windows]      # float por ventana
            self.last_track = self.track_from_windows(
                wp, [w["start"] for w in windows], self.window_size_sec, n, sfreq, t0)
            return []

        # Events
        if self.data_units == "event":
            events = []
            #events = self.{self._predict_events}(windows, **kw)            # [(s, e, conf)] absolutos
            self.last_track = self.track_from_events(events, n, sfreq, t0)
            return [{"start_time": s, "stop_time": e, "duration": round(e - s, 2),
                    "label": "Crisis", "confidence": c} for s, e, c in events]
        
        return []
if __name__ == "__main__":
    engine = ClinicalInferenceEngine()
    print("inference_engine.py module instanced and integrated correctly")