"""
# File: inference_engine.py
# Project: Trabajo de graduación
# Author: Maria Fernanda Andrade Recinos
#
# Compilation of all models code to import all at the inference engine
"""

from .seizure_transformer import SeizureTransformer

MODELS_REGISTER = {
    "seizure_transformer": {
        "class": SeizureTransformer,
        "output_type": "binary_segmentation",
        "window_size_sec": 60.0,
        "stride_sec": 60.0,
        "transpose": False,
        "scale": 1e6,
        "classification_output": "data",
        "parameters": {},
        "postprocess": dict(smooth_sec=2.0, thr_on=0.5, thr_off_ratio=0.6,
                            merge_gap_sec=12.0, min_dur_sec=10.0),
    },
}

def  get_model_config(model_name: str):
    name = model_name.lower()
    for keyword, config in MODELS_REGISTER.items():
        if keyword in name:
            return config

    raise ValueError(f"No hay ninguna arquitectura para el archivo: {name}")