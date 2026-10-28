"""
# File: analysis_worker.py
# Project: Trabajo de graduación
# Author: Maria Fernanda Andrade Recinos

Interactive canvas for high performace EEG visualization and annotation.
"""
# analysis_worker.py
from pathlib import Path
from typing import Optional, Dict, Any
from PySide6.QtCore import Signal, Slot, QThread

# Backend functions
from backend.pipelines.data_loader import load_raw_edf, get_edf_metadata
from backend.pipelines.preprocessing import raw_data_preproccesing
from backend.pipelines.windowing import slice_raw_into_windows
from backend.ml_service.ica_module import classification_iclabel

# Thread from data (backend) into UI
class AnalysisWorker(QThread):
    progress_updated = Signal(int, str)     # 0 to 100 percentage
    analysis_finished = Signal(dict)        # Results payload
    analysis_failed = Signal(str)           # Failure message
    done = Signal()

    def __init__(
            self, 
            edf_path: Path | str,
            preprocessing_params: Optional[Dict[str, Any]] = None,
            window_size_sec: float = 1.0,
            stride_sec: float = 1.0,
            use_ica: bool = False,
            model_filename: Optional[str] = None
        ):
        super().__init__()
        self.edf_path = Path(edf_path)
        self.prep_params = preprocessing_params or {}
        self.window_size_sec = window_size_sec
        self.stride_sec = stride_sec
        self.use_ica = use_ica
        self.model_filename = model_filename

    @Slot()
    def run(self):
        """
        Execution focal entry point for execution, running in the background
        """
        #print("Running worker")
        try:
            # Loading file
            self.progress_updated.emit(10, "Cargando archivo EDF...")
            metadata = get_edf_metadata(self.edf_path)
            raw = load_raw_edf(self.edf_path, preloaD=True)

            # Signal preprocessing
            self.progress_updated.emit(30, "Aplicando filtros y montajes...")
            preprocessed_raw = raw_data_preproccesing(
                raw_data=raw,
                l_freq=self.prep_params.get("l_freq", 1.0),
                h_freq=self.prep_params.get("h_freq", 100.0),
                notch_freq=self.prep_params.get("notch_freq", 60.0),
                bipolar_montage=self.prep_params.get("bipolar_montage", False),
                resampling_freq=self.prep_params.get("resampling_freq", 256)
            )

            # ICA and ICLAbel
            components_full = None
            mixing_matrix = None
            ic_probs = None

            if self.use_ica:
                self.progress_updated.emit(50, "Calculando descomposición ICA e ICLabel...")
                ica, ic_labels, ic_probs = classification_iclabel(preprocessed_raw)
                # Temporal features
                sources = ica.get_sources(preprocessed_raw)
                components_full, _ = sources[:, :]
                mixing_matrix = ica.mixing_matrix_

            engine = None
            if self.model_filename:
                import importlib
                import backend.ml_service.feature_extractor as fe
                import backend.ml_service.models_registry as mr
                import backend.ml_service.inference_engine as ie
                for m in (fe, mr, ie):
                    importlib.reload(m)

                self.progress_updated.emit(80, "Cargando arquitectura de IA...")
                engine = ie.ClinicalInferenceEngine(self.model_filename)
                self.window_size_sec = engine.window_size_sec
                self.stride_sec = engine.stride_sec

            # Windows temporal segmentation
            self.progress_updated.emit(85, f"Segmentando señal ({self.window_size_sec}s)...")
            windows = slice_raw_into_windows(
                raw=preprocessed_raw,
                window_size_sec=self.window_size_sec,
                stride_sec=self.stride_sec
            )

            # AI inference
            detections = []
            if engine is not None:
                self.progress_updated.emit(90, "Ejecutando inferencia clínica...")
                detections = engine.predict_study_windows(
                    windows = windows,
                    sfreq = float(preprocessed_raw.info["sfreq"]),
                    components_full = components_full,
                    mixing_matrix = mixing_matrix,
                    ic_probs = ic_probs
                )


            # Clossing / Ending
            self.progress_updated.emit(100, "Procesamiento completo con éxito")

            # Data
            signal_matrix_uv = preprocessed_raw.get_data() * 1e6
            ch_names = list(preprocessed_raw.ch_names)
            sfreq = float(preprocessed_raw.info["sfreq"])
            duration_sec = float(preprocessed_raw.n_times / sfreq)

            # Results
            results = {
                "metadata": metadata,
                "raw": preprocessed_raw,
                "signal_matrix": signal_matrix_uv, 
                "ch_names": ch_names,              
                "sfreq": sfreq,                    
                "duration_sec": duration_sec,      
                "windows": windows,
                "events": detections,              
                "ica_used": self.use_ica
            }
            self.analysis_finished.emit(results)

        except Exception as e:
            self.analysis_failed.emit(str(e))

        finally:
            self.done.emit()