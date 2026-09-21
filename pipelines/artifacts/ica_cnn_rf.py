"""
# File: ica_cnn_rf.py
# Project: Trabajo de graduación
# Author: Maria Fernanda Andrade Recinos

End-to-end pipeline for 'artifact' corpus, process:
Windowing -> split -> features (ICA+ICLabel agregado) -> 
Hiperparameter optimization (Grid Search y Honey Badger) -> 
Training of multi-output RF -> validation -> saves work.
"""
# file: ica_cnn_rf.py (pipeline)

# Data managment libraries
import pandas as pd
from pathlib import Path

# Utils libraries
from scipy.stats import randint

# Data integration libraries / project modules
from src.core.windowing import get_or_build_windows
from src.core.data_loader import build_annotations_index, find_project_root
from src.core.data_config import ARTIFACT_KEYWORDS, WINDOW_REQUESTS_ARTIFACTS, RATIOS, VERSION, LEAKAGE_COLS
from src.core.data_splitter import get_or_compute_labeled_split, split_balance_report, drop_inconsistent_channel_columns
from src.utils.patient_registry import load_registry, forced_for
from src.core.feature_extractor import build_feature_dataset, build_ml_dataset

# Data visualization and search libraries
from IPython.display import display

# Pipeline directions
BASE_DIR = find_project_root("src")
CORPUS_OUTPUTS_DIR = BASE_DIR / Path("outputs/artifact")

ICA_CACHE_DIR = CORPUS_OUTPUTS_DIR / Path("cache/ica")
SESSION_CACHE_DIR = CORPUS_OUTPUTS_DIR / Path("cache/sessions")
WINDOWS_CACHE_DIR = CORPUS_OUTPUTS_DIR / Path("windows")
FEATURES_DIR = CORPUS_OUTPUTS_DIR / Path("features")
SPLIT_CACHE_DIR = CORPUS_OUTPUTS_DIR / Path("splits")
ANNOTATIONS_DIR = find_project_root("src") / "outputs" / "artifact" /  "annotations"

MODELS_DIR = CORPUS_OUTPUTS_DIR / Path("models")

for d in (FEATURES_DIR, ICA_CACHE_DIR, SESSION_CACHE_DIR, SPLIT_CACHE_DIR, MODELS_DIR, WINDOWS_CACHE_DIR):
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

print("\nLoading all dataset for training...")
database_corpus_patient = build_annotations_index("artifact", paths=True, CACHE_DIR=ANNOTATIONS_DIR)
display(database_corpus_patient.head(5))

results = {}
reg = load_registry()
if not reg["patients"]:
    raise RuntimeError("Empty fixed registry, run patient registry first.")
FORCED = forced_for(reg, database_corpus_patient["Patient"].unique(), source_prefix=("folder:", "shared:"))
print(pd.Series(FORCED).value_counts().to_dict())

for artifact, window in WINDOW_REQUESTS_ARTIFACTS.items():
    print("\n" + "-"*50)
    print(f"ARTIFACT: {artifact} | windows: {window['window_size_sec']}s ({window['stride_sec']} s overlap)")
    print("\n" + "-"*50)

    rf_dataset_path = FEATURES_DIR / (
        f"rf_dataset_{artifact}_w{window['window_size_sec']}_s{window['stride_sec']}_v{VERSION}.parquet"
    )
    if rf_dataset_path.exists():
        print(f"[INFO] Existing dataset, loading: {rf_dataset_path}")
        rf_features_dataset = pd.read_parquet(rf_dataset_path)
    else:
        print("\n"+("*"*60))
        print("Generating windows...")
        windowed_annotations_corpus_patient = get_or_build_windows(annotations_df=database_corpus_patient, 
                                                                   window=window, 
                                                                   taxonomy=ARTIFACT_KEYWORDS, 
                                                                   cache_dir=WINDOWS_CACHE_DIR,
                                                                   refresh=False
                                                                   )
        display(windowed_annotations_corpus_patient.head(5))
        #print(windowed_annotations_corpus_patient.columns.tolist())

        win_annotations_corpus_patient = windowed_annotations_corpus_patient.loc[windowed_annotations_corpus_patient["is_ambiguous"] == 0, ["Patient", "Session", "Section", "Start", artifact]].reset_index(drop=True)
        print(f"Ventanas: {len(windowed_annotations_corpus_patient)} -> sin ambiguas: {len(win_annotations_corpus_patient)} | positivas: {int(win_annotations_corpus_patient[artifact].sum())}") 

        display(win_annotations_corpus_patient.head(25))

        
        print("\n"+("*"*60))
        sweep_results = []
        for sw in [0.0, 0.3, 0.5, 0.7, 1.0]:
            print(f"Size weight: {sw}")
            candidate_dataset, assignment, report = get_or_compute_labeled_split(
                win_annotations_corpus_patient, 
                artifact, 
                group_col="Patient",
                ratios=RATIOS,
                size_weight=sw, 
                dataset_division_dir=SPLIT_CACHE_DIR, 
                version=VERSION, 
                target=str(artifact),
                forced=FORCED,
            )
            # print("[DEBUG] Report with ratios:", RATIOS, "\n", report)
            # print("[DEBUG] Assigment value:", assignment)
            balance = split_balance_report(candidate_dataset, target_col=artifact)
            spread = balance["positive_rate"].max() - balance["positive_rate"].min()
            size_pct = balance["n_total"]/balance["n_total"].sum()
            size_dev = (size_pct - pd.Series(RATIOS)).abs().max()
            # print("[DEBUG] Split balance (positive rate):\n", balance)

            sweep_results.append({
                "size_weight": sw,
                "test_rate": balance.loc["test", "positive_rate"],
                "train_rate": balance.loc["train", "positive_rate"],
                "val_rate": balance.loc["val", "positive_rate"],
                "rate_spread": spread,
                "train_pct": size_pct["train"],
                "val_pct": size_pct["val"],
                "test_pct": size_pct["test"],
                "size_dev": size_dev,
                "combined_score": spread + size_dev,
            })

        print("\n"+("*"*60))
        sweep_report = pd.DataFrame(sweep_results).set_index("size_weight")
        print(f"\n[INFO] Sweep size weight results for {artifact}:")
        print(sweep_report.round(4).sort_values("rate_spread"))
        selected_sw = sweep_report['combined_score'].idxmin()
        print(f"[INFO] Best suggested size weight for {artifact}: {selected_sw}")

        rf_dataset, assignment, report = get_or_compute_labeled_split(  win_annotations_corpus_patient, 
                                                                        artifact, 
                                                                        group_col="Patient",
                                                                        ratios=RATIOS,
                                                                        size_weight=selected_sw, 
                                                                        dataset_division_dir=SPLIT_CACHE_DIR, 
                                                                        version=VERSION, 
                                                                        target=str(artifact),
                                                                        forced=FORCED,
                                                                )
        balance = split_balance_report(rf_dataset, target_col=artifact)
        spread = balance["positive_rate"].max() - balance["positive_rate"].min()
        size_pct = balance["n_total"]/balance["n_total"].sum()
        size_dev = (size_pct - pd.Series(RATIOS)).abs().max()
        print("[DEBUG] Split balance (positive rate):\n", balance)

        bad = {p: (s, assignment[p]) for p, s in FORCED.items() if p in assignment and assignment[p] != s}
        print("Reglas violadas:", len(bad), "| pacientes por split:", pd.Series(assignment).value_counts().to_dict())

"""

        print("\nStarting features extraction from channels and ICA components...")
        featured_windows = build_feature_dataset(   windowed_annotations_corpus_patient, 
                                                    target_labels=list(ARTIFACT_KEYWORDS.keys()), 
                                                    bipolar_montage=False, 
                                                    use_ica=True, 
                                                    ica_cache_dir=str(ICA_CACHE_DIR), 
                                                    session_cache_dir=str(SESSION_CACHE_DIR))
        display(featured_windows.head(5))

        if not featured_windows.empty:
            print("[INFO] Successful features extraction")
            rf_features_dataset = build_ml_dataset(featured_windows, target_artifact=artifact, bipolar_montage=False, features_dir=str(FEATURES_DIR))
        else:
            raise ValueError(f"Error: Resulting empty dataset")

        rf_features_dataset = drop_inconsistent_channel_columns(rf_features_dataset, protect_cols=LEAKAGE_COLS + ["is_positive", "split"] )
        print(rf_features_dataset.head(5))
        print(rf_features_dataset.columns.tolist())
        print("[INFO] Positive count:")
        print(rf_features_dataset["is_positive"].value_counts())


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
    print("\t\t Metrics results:", res['metrics_results'])  
    """