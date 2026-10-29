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
import torch
import pickle
import numpy as np
import pandas as pd
from pathlib import Path
from typing import Optional, List, Dict,  Any, Protocol
from scipy.ndimage import binary_closing, binary_opening

# Internal functions
from config.app_config import CHECKPOINTS_DIR
from config.data_config import SFREQ
from backend.ml_service.models_registry import get_model_config
from backend.ml_service.feature_extractor import extract_features_from_window_payload
from backend.ml_service.utils.postprocess import probs_to_events    # el postprocess.py de antes

RAW_PP = dict(smooth_sec=0.0, thr_on=0.5, thr_off_ratio=1.0,
              merge_gap_sec=0.0, min_dur_sec=0.0)

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

        if model_filename:
            self.load_model(model_filename)

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

    def predict_window(
            self,
            signal_window: np.ndarray,
            ch_names: List[str],
            sfreq: float = SFREQ,
            component_window: Optional[np.ndarray] = None,
            mixing_matrix: Optional[np.ndarray] = None,
            ic_probs: Optional[np.ndarray] = None,
            history: Optional[np.ndarray] = None,
        ) -> Dict[str, Any]:
        """
        Features extractor and inference execution over a single temporal window.
        """
        if self.model is None:
            raise RuntimeError("No se ha cargado ningún modelo en el motor de inferencia.")

        # Features
        features = extract_features_from_window_payload(
            channel_data=signal_window,
            ch_names=ch_names,
            sfreq=sfreq,
            component_data=component_window,
            mixing_matrix=mixing_matrix,
            ic_probs=ic_probs
        )

        # ML ------------------------------------------------------------------------------
        if self.model_type == "traditional_ml":
            df_feat = pd.DataFrame([features])

            # Align columns with standard configuration used in training (TUH dataset settings)
            if self.feature_columns is not None:
                for col in self.feature_columns:
                    if col not in df_feat.columns:
                        df_feat[col] = 0.0
                df_feat = df_feat[self.feature_columns]

            # Prediction
            pred_label = self.model.predict(df_feat)[0]
            confidence = 1.0
            if hasattr(self.model, "predict_proba"):
                probs = self.model.predict_proba(df_feat)[0]
                confidence = float(np.max(probs))

        # DL ---------------------------------------------------------------------------------
        elif self.model_type == "deep_learning":
            sig_norm = signal_window * self.data_scale
            """mean_vals = np.mean(signal_window, axis=1, keepdims=True)
            std_vals = np.std(signal_window, axis=1, keepdims=True)
            sig_norm = (signal_window - mean_vals) / (std_vals + 1e-8)"""

            if self.transpose:
                tensor_signal = torch.tensor(np.transpose(sig_norm), dtype=torch.float32).unsqueeze(0)
            else:
                tensor_signal = torch.tensor(sig_norm, dtype=torch.float32).unsqueeze(0)

            print(f"[DEBUG] Shape del tensor de entrada: {tensor_signal.shape}")

            tensor_feat = None
            if self.feature_columns and self.scaler:
                print("[DEBUG] Features and scaler analysis applied.")
                feat_values = [features.get(col, 0.0) for col in self.feature_columns]
                feat_array = np.array([feat_values], dtype=np.float32)

                if self.scaler:
                    feat_array = self.scaler.transform(feat_array)

                tensor_feat = torch.tensor(feat_array, dtype=torch.float32)

            with torch.no_grad():
                if tensor_feat is not None:
                    outputs = self.model(tensor_signal, tensor_feat)
                else: 
                    outputs = self.model(tensor_signal)

                if hasattr(outputs, "probabilities"):
                    probs = outputs.probabilities.detach().cpu().numpy()
                    print("[DEBUG] Probs")
                elif hasattr(outputs, "logits"):
                    probs = torch.softmax(outputs.logits, dim=-1).detach().cpu().numpy()
                    print("[DEBUG] Logits")
                else:
                    probs = outputs.detach().cpu().numpy()
                    print("[DEBUG] General use")


            probs = np.asarray(probs).reshape(-1)      # (1, N) -> (N,)
            print("[DEBUG] Samples:", probs.size, "| seconds:", probs.size / sfreq)
            print("[DEBUG] Dimensions: ", probs.ndim)

            if probs.size > 1:
                print("[DEBUG] Lenght probs for time analysis: ", len(probs))

                if self.data_units == "window":
                    confidence = float(np.max(probs))
                    print("[DEBUG] List of probs")                
                elif self.data_units == "data":
                    time_lapse = probs.size/sfreq
                    min_gap = int(time_lapse*0.025)         # Cerrar/unir huecos    < 0.025 * 60s   = 1.20s
                    min_dur = int(time_lapse*0.050)          # Descartar huecos     < 0.050 * 60s   = 3.00s 

                    binary_output = (probs > self.threshold)
                    binary_output = binary_closing(binary_output, structure=np.ones(min_gap))
                    binary_output = binary_opening(binary_output, structure=np.ones(min_dur))

                    padded = np.pad(binary_output.astype(int), (1, 1), 'constant', constant_values=0)
                    changes = np.diff(padded)
                    starts = np.where(changes == 1)[0]
                    ends = np.where(changes == -1)[0]
                    
                    print("[DEBUG] START AND ENDS AFTER PROCESSING: ", starts, ends)

                    eventos_exactos = []
                    for start_idx, end_idx in zip(starts, ends):
                        start_sec, end_sec = start_idx / sfreq, end_idx / sfreq
                        duracion = end_sec - start_sec
                        print("[DEBUG] Duration: ", duracion)

                        if duracion >= 1.0:
                            print("[DEBUG] Start and end: ", start_idx, end_idx)
                            confianza_promedio = float(np.mean(probs[start_idx:end_idx]))
                            eventos_exactos.append({
                                "offset_start": start_sec,
                                "offset_end": end_sec,
                                "confidence": confianza_promedio
                            })
            """

            else:
                confidence = float(probs[0])
                print("[DEBUG] Single prob")
                print(f"[DEBUG] Shape de salida: {probs.shape} | Max Confianza: {confidence:.4f}" + "\n" + 50*"-")

                pred_label = "Crisis" if confidence >= self.threshold else "Fondo"

                return {
                        "prediction": "Crisis" if len(eventos_exactos) > 0 else "Fondo",
                        "confidence": float(np.max(probs)), # Solo para referencia global
                        "features": features,
                        "exact_events": eventos_exactos
                }"""

        else:
            raise RuntimeError(f"Tipo de modelo no soportado: {self.model_type}")

    def predict_study_windows(self, windows, sfreq=SFREQ, components_full=None,
                              mixing_matrix=None, ic_probs=None, raw=False):
        self.last_probs = None
        if self.model_type == "deep_learning" and self.data_units == "data":
            probs = np.concatenate([self.predict_probs(w["data"]) for w in windows])
            self.last_probs = probs                  # curva cruda, siempre
            pp = RAW_PP if raw else self.postprocess
            t0 = windows[0]["start"]
            return [{"start_time": t0 + s, "stop_time": t0 + e,
                     "duration": round(e - s, 2), "label": "Crisis", "confidence": c}
                    for s, e, c in probs_to_events(probs, sfreq, pp)]
        return []
if __name__ == "__main__":
    engine = ClinicalInferenceEngine()
    print("inference_engine.py module instanced and integrated correctly")