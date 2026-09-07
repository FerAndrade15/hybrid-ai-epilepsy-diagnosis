"""
# File: ica_cnn_rf.py
# Project: Trabajo de graduación
# Author: Maria Fernanda Andrade Recinos

End-to-end pipeline for 'artifact' corpus, process:
Windowing -> split -> features (ICA+ICLabel agregado) -> 
Hiperparameter optimization (Grid Search y Honey Badger) -> 
Training of multi-output RF -> validation -> saves work.
"""
# Data managment libraries
import pandas as pd
from pathlib import Path

# Data integration libraries / project modules
from implementation.core.data_config import ARTIFACT_KEYWORDS, WINDOW_REQUESTS_ARTIFACTS, RATIOS, VERSION, LEAKAGE_COLS
from implementation.core.data_loader import build_annotations_index, find_project_root
from implementation.core.windowing import label_windowing
from implementation.core.data_splitter import get_or_compute_split
from implementation.core.feature_extractor import build_feature_dataset, build_rf_dataset
from implementation.models.rf_model import binary_rf

# Data visualization and search libraries
from IPython.display import display

BASE_DIR = find_project_root()
CORPUS_OUTPUTS_DIR = BASE_DIR / Path("outputs/artifact")
ICA_CACHE_DIR = CORPUS_OUTPUTS_DIR / Path("individual_tests/cache/ica")
SESSION_CACHE_DIR = CORPUS_OUTPUTS_DIR / Path("individual_tests/cache/sessions")
FEATURES_DIR = CORPUS_OUTPUTS_DIR / Path("individual_tests/features")
SPLIT_CACHE_DIR = CORPUS_OUTPUTS_DIR / Path("individual_tests/splits")
MODELS_DIR = CORPUS_OUTPUTS_DIR / Path("individual_tests/models")

for d in (FEATURES_DIR, ICA_CACHE_DIR, SPLIT_CACHE_DIR):
    d.mkdir(parents=True, exist_ok=True)

PARAM_GRID = {
    "n_estimators": [200, 400],
    "max_depth": [None, 20]
}

print("\nLoading 25 artifact patients, 1 sessions per patient for testing...")
database_corpus_patient = build_annotations_index("artifact", n_patients=25, max_sessions=1, paths=True)
display(database_corpus_patient.head(5))

results = {}

for artifact, window in WINDOW_REQUESTS_ARTIFACTS.items():
    print("\n" + "-"*50)
    print(f"ARTIFACT: {artifact} | windows: {window ['window_size_sec']}s")
    print("\n" + "-"*50)

    rf_dataset_path = FEATURES_DIR/f"rf_dataset_{artifact}.parquet"
    if rf_dataset_path.exists():
        print(f"[INFO] Existing dataset, loading: {rf_dataset_path}")
        rf_dataset = pd.read_parquet(rf_dataset_path)
    else:
        print("\nGenerating windows...")
        windowed_annotations_corpus_patient = label_windowing(
                        database_corpus_patient, WINDOW_REQUESTS_ARTIFACTS[artifact],
                        ARTIFACT_KEYWORDS, unreviewd_tokens=True,
                    )
        display(windowed_annotations_corpus_patient.head(5))

        windowed_annotated_splited, assignment, report = get_or_compute_split(windowed_annotations_corpus_patient, 
                                                                                target_taxonomy=ARTIFACT_KEYWORDS, 
                                                                                dataset_division_dir=str(SPLIT_CACHE_DIR), 
                                                                                ratios=RATIOS, 
                                                                                version=VERSION,
                                                                                target=artifact)
        print("[INFO] Split report")
        print(report)

        print("\nStarting features extraction from channels and ICA components...")
        featured_windows = build_feature_dataset(windowed_annotated_splited, use_ica=True, ica_cache_dir=str(ICA_CACHE_DIR), session_cache_dir=str(SESSION_CACHE_DIR))
        display(featured_windows.head(5))
        print(featured_windows.columns.tolist())

        if not featured_windows.empty:
            print("[INFO] Successful features extraction")
            rf_features_dataset = build_rf_dataset(featured_windows, target_artifact=artifact, features_dir=str(FEATURES_DIR))
            print(rf_features_dataset.head(5))
            print("[INFO] Positive count:")
            print(rf_features_dataset["is_positive"].value_counts())
        else:
            raise ValueError(f"Error: Resulting empty dataset")

        rf_dataset = build_rf_dataset(featured_windows, target_artifact=artifact, features_dir=str(FEATURES_DIR))

    split_counts = rf_dataset["split"].value_counts(dropna=False)
    print("[INFO] Split distribution: ", split_counts)

    print(f"\nStarting training of Random Forest ({artifact})")

    results[artifact] = binary_rf(rf_dataset, window_size_sec=WINDOW_REQUESTS_ARTIFACTS[artifact], model_name=f"rf_{artifact}", 
                                    param_grid=PARAM_GRID, models_dir=str(MODELS_DIR), leakage_cols= LEAKAGE_COLS
                                    )

print("\n"+"*-" * 25)
print("Final report")
for artifact, res in results.items():
    print(('-'*10),artifact,('-'*10))
    print(f"\t\t F1(val)={res['val_f1']:.4f}")
    print(f"\t\t best_params={res['params']:.4f}")
    print("\t\t Confusion matrix:", res['confusion_matrix'])
    print("\t\t Metrics results:", res['metrics_results'])