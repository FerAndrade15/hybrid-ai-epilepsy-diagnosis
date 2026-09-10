import pandas as pd
from random import randint
from pathlib import Path

# Data integration libraries / project modules
from implementation.core.data_config import ARTIFACT_KEYWORDS, WINDOW_REQUESTS_ARTIFACTS, RATIOS, VERSION, LEAKAGE_COLS
from implementation.core.data_loader import build_annotations_index, find_project_root
from implementation.core.windowing import label_windowing
from implementation.core.data_splitter import get_or_compute_labeled_split, split_features_target
from implementation.core.feature_extractor import build_feature_dataset, build_rf_dataset

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
RANDOM_SPACE = {
    "eye": {
        "space":{
            "n_estimators": randint(150, 600),
            "max_depth": randint(5, 30),
            "min_samples_split": randint(5, 30),
            "min_samples_leaf": randint(2, 15),
            "max_features": ["sqrt", "log2", 0.3, 0.5],
            "sampling_strategy": [0.3, 0.5, 0.7, 1.0],
        },
        "max_fp_per_day": 50,
        "n_iter": 60,
    },
    "muscle": {
        "space":{
            "n_estimators": randint(150, 600),
            "max_depth": randint(5, 30),
            "min_samples_split": randint(2, 15),
            "min_samples_leaf": randint(1, 8),
            "max_features": ["sqrt", "log2", 0.3, 0.5],
            "sampling_strategy": [0.3, 0.5, 0.7, 1.0],
        },
        "max_fp_per_day": 300,
        "n_iter": 60,
    },
    "non_physiological": {
        "space":{
            "n_estimators": randint(150, 600),
            "max_depth": randint(5, 35),
            "min_samples_split": randint(2, 15),
            "min_samples_leaf": randint(1, 8),
            "max_features": ["sqrt", "log2", 0.3, 0.5],
            "sampling_strategy": [0.3, 0.5, 0.7, 1.0],
        },
        "max_fp_per_day": 1000,
        "n_iter": 60,
    },
}

print("\nLoading 30 artifact patients, 1 sessions per patient for testing...")
database_corpus_patient = build_annotations_index("artifact", n_patients=30, max_sessions=1, paths=True)
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
        display(rf_dataset.head(5))
        print(rf_dataset.columns.tolist())
    else:
        print("\nGenerating windows...")
        windowed_annotations_corpus_patient = label_windowing(
                        database_corpus_patient, WINDOW_REQUESTS_ARTIFACTS[artifact],
                        ARTIFACT_KEYWORDS, unreviewd_tokens=True,
                    )
        display(windowed_annotations_corpus_patient.head(5))


        print("\nStarting features extraction from channels and ICA components...")
        featured_windows = build_feature_dataset(windowed_annotations_corpus_patient, use_ica=True, ica_cache_dir=str(ICA_CACHE_DIR), session_cache_dir=str(SESSION_CACHE_DIR))
        display(featured_windows.head(5))

        featured_windows.to_excel("Features_analysis.xlsx", index=False)

      
        """ 
        print("\nStarting features extraction from channels and ICA components...")
        featured_windows = build_feature_dataset(windowed_annotations_corpus_patient, use_ica=True, ica_cache_dir=str(ICA_CACHE_DIR), session_cache_dir=str(SESSION_CACHE_DIR))
        display(featured_windows.head(5))

        if not featured_windows.empty:
            print("[INFO] Successful features extraction")

                    windowed_annotated_splited, assignment, report = get_or_compute_labeled_split(windowed_annotations_corpus_patient, artifact, "is_positive", group_col="Patient",
                                                        include_clean=True, drop_excluded=True, drop_ambiguous=True, 
                                                        ratios={"train": 0.7, "val": 0.15, "test": 0.15}, seed=42, 
                                                        dataset_division_dir=SPLIT_CACHE_DIR, version=1):

            rf_features_dataset = build_rf_dataset(featured_windows, target_artifact=artifact, features_dir=str(FEATURES_DIR))
            print(rf_features_dataset.head(5))
            print(rf_features_dataset.columns.tolist())
            print("[INFO] Positive count:")
            print(rf_features_dataset["is_positive"].value_counts())
        else:
            raise ValueError(f"Error: Resulting empty dataset")

        rf_dataset = build_rf_dataset(featured_windows, target_artifact=artifact, features_dir=str(FEATURES_DIR))

        rf_dataset, assignment, report = get_or_compute_labeled_split(rf_dataset, "is_positive", group_col="Patient",
                                                                        ratios=RATIOS, dataset_division_dir=SPLIT_CACHE_DIR, version=VERSION, target="all")

    split_counts = rf_dataset["split"].value_counts(dropna=False)
    print("[INFO] Split distribution: ", split_counts)

    print(f"\nStarting training of Random Forest ({artifact})")

    config = RANDOM_SPACE[artifact]
    results[artifact] = binary_rf(rf_dataset, window_size_sec=WINDOW_REQUESTS_ARTIFACTS[artifact], model_name=f"rf_{artifact}", 
                                    models_dir=str(MODELS_DIR), leakage_cols= LEAKAGE_COLS,
                                    search_method="random",
                                    search_data=config["space"],
                                    search_kwargs={"n_iter": config["n_iter"]},
                                    force_retrain=True, balanced_bootstrap=True,
                                    max_fp_per_day=config["max_fp_per_day"]
                                    )

print("\n"+"*-" * 25)
print("Final report")
for artifact, res in results.items():
    print(('-'*10),artifact,('-'*10))
    print(f"\t\t F1(val)={res['val_f1']:.4f}")
    print(f"\t\t best_params={res['params']}")
    print("\t\t Confusion matrix:", res['confusion_matrix'])
    print("\t\t Metrics results:", res['metrics_results'])"""