# pipelines/artifacts/ica_cnn_pipeline.py

import pandas as pd
from pathlib import Path
from IPython.display import display

from implementation.core.data_config import (
    ARTIFACT_KEYWORDS, WINDOW_REQUESTS_ARTIFACTS, RATIOS, VERSION, find_project_root,
)
from implementation.core.data_loader import build_annotations_index
from implementation.core.windowing import label_windowing
from implementation.core.data_splitter import get_or_compute_labeled_split, split_balance_report
from implementation.models.cnn_artifact_detector import binary_cnn

BASE_DIR = find_project_root()
CORPUS_OUTPUTS_DIR = BASE_DIR / "outputs" / "artifact"
SESSION_CACHE_DIR = CORPUS_OUTPUTS_DIR / "cache" / "sessions"
ICA_CACHE_DIR = CORPUS_OUTPUTS_DIR / "cache" / "ica"
SPLIT_CACHE_DIR = CORPUS_OUTPUTS_DIR / "splits"
MODELS_DIR = CORPUS_OUTPUTS_DIR / "models_cnn"
for d in (SESSION_CACHE_DIR, ICA_CACHE_DIR, SPLIT_CACHE_DIR, MODELS_DIR):
    d.mkdir(parents=True, exist_ok=True)


CNN_CONFIG = {
    "eye": {"model_type": "standard", "max_fp_per_day": 50, "epochs": 100},
    "muscle": {"model_type": "lightweight", "max_fp_per_day": 300, "epochs": 100},
    "non_physiological": {"model_type": "lightweight", "max_fp_per_day": 1000, "epochs": 100},
}

SFREQ = 256     
N_CHANNELS = 21  

print("\nCargando dataset completo de anotaciones...")
database_corpus_patient = build_annotations_index("artifact", paths=True)
display(database_corpus_patient.head(5))

results = {}

for artifact, window in WINDOW_REQUESTS_ARTIFACTS.items():
    print("\n" + "-" * 60)
    print(f"CNN - ARTIFACT: {artifact} | window: {window['window_size_sec']}s")
    print("-" * 60)

    print("Generando ventanas...")
    windowed_df = label_windowing(
        database_corpus_patient, WINDOW_REQUESTS_ARTIFACTS[artifact],
        ARTIFACT_KEYWORDS, unreviewd_tokens=True,
    )

    target_col = f"tuar_{artifact}" if not f"tuar_{artifact}" in windowed_df.columns else artifact
    target_col = artifact

    print(f"Distribución de {target_col}:")
    print(windowed_df[target_col].value_counts())

    print("Calculando split (por paciente, mismo criterio que el RF)...")
    windowed_df_split, assignment, report = get_or_compute_labeled_split(
        windowed_df, target_col, group_col="Patient",
        ratios=RATIOS, dataset_division_dir=str(SPLIT_CACHE_DIR),
        version=VERSION, target=f"cnn_{artifact}",
    )

    balance = split_balance_report(windowed_df_split, target_col=target_col)
    print(f"[INFO] Balance del split para {artifact}:\n{balance}")

    config = CNN_CONFIG[artifact]
    results[artifact] = binary_cnn(
        windowed_df_split, target_col=target_col, model_name=f"cnn_{artifact}",
        window_size_sec=window["window_size_sec"], sfreq=SFREQ, n_channels=N_CHANNELS,
        session_cache_dir=str(SESSION_CACHE_DIR), ica_cache_dir=str(ICA_CACHE_DIR),
        models_dir=str(MODELS_DIR), model_type=config["model_type"],
        epochs=config["epochs"], max_fp_per_day=config["max_fp_per_day"],
        force_retrain=True,
    )

print("\n" + "=" * 60)
print("RESUMEN FINAL — CNN por artefacto")
for artifact, res in results.items():
    print(f"\n{artifact}:")
    print(f"  Threshold: {res['chosen_threshold']:.3f} ({res['chosen_mode']})")
    print(f"  Métricas: {res['metrics_results']}")