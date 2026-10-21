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
# Imports models 
import joblib
import torch
import pickle
import numpy as np
import pandas as pd
from pathlib import Path
from typing import Optional, List, Dict,  Any, Protocol

# Internal functions
from config.app_config import CHECKPOINTS_DIR
from config.data_config import SFREQ
from backend.ml_service.models_registry import get_model_config
from backend.ml_service.feature_extractor import extract_features_from_window_payload

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
            ic_probs: Optional[np.ndarray] = None
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
                    print("[DEBUG] General use (check here)")

            if probs.ndim > 1:
                if self.data_units == "window":
                    confidence = float(np.max(probs))
                    print("[DEBUG] List of probs")
                elif self.data_units == "data":
                    binary_output = (probs > self.threshold).astype(int)
                    padded = np.pad(binary_output, (1, 1), 'constant', constant_values=0)
                    cambios = np.diff(padded)
                    inicios = np.where(cambios == 1)[0]
                    fines = np.where(cambios == -1)[0]

                    eventos_exactos = []
                    for start_idx, end_idx in zip(inicios, fines):
                        # Convertimos índices (muestras) a segundos
                        start_sec = start_idx / sfreq
                        end_sec = end_idx / sfreq
                        duracion = end_sec - start_sec

                        # Filtramos eventos demasiado cortos (ej. menores a 2 segundos)
                        if duracion >= 2.0:
                            confianza_promedio = float(np.mean(probs[start_idx:end_idx]))
                            eventos_exactos.append({
                                "offset_start": start_sec,
                                "offset_end": end_sec,
                                "confidence": confianza_promedio
                            })

            else:
                confidence = float(probs[0])
                print("[DEBUG] Single prob")
                print(f"[DEBUG] Shape de salida: {probs.shape} | Max Confianza: {confidence:.4f}" + "\n" + 50*"-")

                pred_label = "Crisis" if confidence >= self.threshold else "Fondo"

        else:
            raise RuntimeError(f"Tipo de modelo no soportado: {self.model_type}")

        return {
                "prediction": "Crisis" if len(eventos_exactos) > 0 else "Fondo",
                "confidence": float(np.max(probs)), # Solo para referencia global
                "features": features,
                "exact_events": eventos_exactos
            }

    def predict_study_windows(
            self,
            windows: List[Dict[str, Any]],
            sfreq: float = SFREQ,
            components_full: Optional[np.ndarray] = None,
            mixing_matrix: Optional[np.ndarray] = None,
            ic_probs: Optional[np.ndarray] = None
        ) -> List[Dict[str, Any]]:
        """
        Function to process a list of windows and generate detection list to feed events output into the UI
        """
        detections = []

        for win in windows:
            data = win["data"]
            t_start = win["start"]
            t_end = win["end"]
            ch_names = win.get("channels", [])

            comp_win = None
            if components_full is not None:
                start_samp = int(round(t_start * sfreq))
                end_samp = int(round(t_end * sfreq))
                comp_win = components_full[:, start_samp:end_samp]

            res = self.predict_window(
                signal_window=data,
                ch_names=ch_names,
                sfreq=sfreq,
                component_window=comp_win,
                mixing_matrix=mixing_matrix,
                ic_probs=ic_probs
            )

            if "exact_events" in res and res["exact_events"]:
                for ev in res["exact_events"]:
                    abs_start = t_start + ev["offset_start"]
                    abs_end = t_start + ev["offset_end"]
                    detections.append({
                        "start_time": abs_start,
                        "stop_time": abs_end,
                        "duration": round(abs_end - abs_start, 2),
                        "label": "Crisis",
                        "confidence": ev["confidence"]
                    })

        return detections

if __name__ == "__main__":
    engine = ClinicalInferenceEngine()
    print("inference_engine.py module instanced and integrated correctly")

        
