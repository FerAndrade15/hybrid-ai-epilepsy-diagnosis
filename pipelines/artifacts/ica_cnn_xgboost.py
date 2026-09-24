"""
# File: ica_cnn_rf.py
# Project: Trabajo de graduación
# Author: Maria Fernanda Andrade Recinos

End-to-end pipeline for 'artifact' corpus, process:
Windowing -> split -> features (ICA+ICLabel agregado) -> 
Hiperparameter optimization (Random Search, Grid Search y Honey Badger) -> 
Training of several XGBoost, one per artifact -> validation -> saves work.
"""
# file: ica_cnn_xgboost.py (pipeline)

# Data managment libraries
import pandas as pd
from pathlib import Path

# Utils libraries
from scipy.stats import randint

# Data integration libraries / project modules
from src.core.windowing import get_or_build_windows
from src.core.data_loader import build_annotations_index, find_project_root
from src.core.data_config import ARTIFACT_KEYWORDS, WINDOW_REQUESTS_ARTIFACTS, RATIOS, VERSION, LEAKAGE_COLS, OUTPUTS_DIR, NORMALIZE
from src.core.data_splitter import get_or_compute_labeled_split, split_balance_report, drop_inconsistent_channel_columns
from src.core.feature_extractor import build_ml_dataset, get_or_build_features
from src.models.xgboost_model import build_xgb_model
from src.models.ml_models import train_binary_model
from src.utils.split_cache import load_selected_sw, save_selected_sw
from src.utils.patient_registry import load_registry, forced_for

# Data visualization and search libraries
from IPython.display import display

# Pipeline directions
BASE_DIR = find_project_root("src")
CORPUS_OUTPUTS_DIR = OUTPUTS_DIR / Path("artifact")

ICA_CACHE_DIR = CORPUS_OUTPUTS_DIR / Path("cache/ica")
SESSION_CACHE_DIR = CORPUS_OUTPUTS_DIR / Path("cache/sessions")
WINDOWS_CACHE_DIR = CORPUS_OUTPUTS_DIR / Path("windows")
FEATURES_DIR = CORPUS_OUTPUTS_DIR / Path("features")
DATASET_DIR = CORPUS_OUTPUTS_DIR / Path("dataset")
SPLIT_CACHE_DIR = CORPUS_OUTPUTS_DIR / Path("splits")
ANNOTATIONS_DIR = OUTPUTS_DIR/ Path("artifact/annotations")

MODELS_DIR = CORPUS_OUTPUTS_DIR / Path("models")
SPLIT_REGISTRY_PATH = SPLIT_CACHE_DIR / "split_registry.json"

for d in (ICA_CACHE_DIR, SESSION_CACHE_DIR, WINDOWS_CACHE_DIR, FEATURES_DIR, DATASET_DIR, SPLIT_CACHE_DIR, ANNOTATIONS_DIR):
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
database_corpus_patient = build_annotations_index("artifact", n_patients=50, paths=True, CACHE_DIR=ANNOTATIONS_DIR)
display(database_corpus_patient.head(5))
n_patients = len(database_corpus_patient["Patient"].unique())

results = {}
reg = load_registry()
if not reg["patients"]:
    raise RuntimeError("Empty fixed registry, run patient registry first.")
FORCED = forced_for(reg, database_corpus_patient["Patient"].unique(), source_prefix=("folder:", "shared:"))
print(pd.Series(FORCED).value_counts().to_dict())

base_forced = FORCED.copy()

for artifact, window_settings in WINDOW_REQUESTS_ARTIFACTS.items():
    print("\n" + "="*50)
    print(f"ARTIFACT: {artifact}")
    print("\n" + "="*50)

    current_forced = base_forced.copy()

    for i, window in enumerate(window_settings):
        print("*"*50)
        print(f">> {artifact} | patients:{n_patients} | windows: {window['window_size_sec']}s ({window['stride_sec']}s stride)")

        rf_dataset_path = DATASET_DIR / (
            f"rf_dataset_{artifact}_w{window['window_size_sec']}_s{window['stride_sec']}"
            f"_ua{window['artifact_umbral']}_p{n_patients}_v{VERSION}.parquet"
        )
        if rf_dataset_path.exists():
            print(f"[INFO] Existing dataset, loading: {rf_dataset_path}")
            rf_features_dataset = pd.read_parquet(rf_dataset_path)
        else:
            """ ANNOTATIONS WINDOWS """
            print("\n"+("*"*60))
            print("Generating windows...")
            windowed_annotations_corpus_patient = get_or_build_windows(annotations_df=database_corpus_patient, 
                                                                    window=window, 
                                                                    taxonomy=ARTIFACT_KEYWORDS, 
                                                                    cache_dir=WINDOWS_CACHE_DIR,
                                                                    artifact_umbral=window['artifact_umbral'],
                                                                    refresh=False
                                                                    )
            display(windowed_annotations_corpus_patient.head(5))
            print(windowed_annotations_corpus_patient.columns.tolist())

            win_annotations_corpus_patient = windowed_annotations_corpus_patient.loc[windowed_annotations_corpus_patient["is_ambiguous"] == 0, ["Patient", "Session", "Section", "Start", artifact]].reset_index(drop=True)
            print(f"Ventanas: {len(windowed_annotations_corpus_patient)} -> sin ambiguas: {len(win_annotations_corpus_patient)} | positivas: {int(win_annotations_corpus_patient[artifact].sum())}") 
            #display(win_annotations_corpus_patient.head(25))
            print(win_annotations_corpus_patient.columns.tolist())

            selected_sw = load_selected_sw(SPLIT_REGISTRY_PATH, artifact, window, n_patients, VERSION)

            if selected_sw is None:
                """ SIZE WEIGHT SWEEP """
                print("\n"+("*"*60))
                sweep_results = []
                for sw in [0.0, 0.3, 0.5, 0.7, 1.0]:
                    print(f"Size weight: {sw}")
                    candidate_dataset, assignment, report = get_or_compute_labeled_split(
                        windowed_annotations_corpus_patient, 
                        artifact, 
                        group_col="Patient",
                        ratios=RATIOS,
                        size_weight=sw, 
                        dataset_division_dir=SPLIT_CACHE_DIR, 
                        version=VERSION, 
                        artifact_umbral=window['artifact_umbral'],
                        window_size_sec=window['window_size_sec'],
                        stride_sec=window['stride_sec'],
                        target=str(artifact),
                        forced=current_forced,
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
                save_selected_sw(SPLIT_REGISTRY_PATH, artifact, window, n_patients, VERSION, selected_sw)

            else:
                print(f"[INFO] Best suggested and saved size weight for {artifact}: {selected_sw}")
            

            splitted_dataset, assignment, report = get_or_compute_labeled_split(  windowed_annotations_corpus_patient, 
                                                                                    artifact, 
                                                                                    group_col="Patient",
                                                                                    ratios=RATIOS,
                                                                                    size_weight=selected_sw, 
                                                                                    dataset_division_dir=SPLIT_CACHE_DIR, 
                                                                                    version=VERSION, 
                                                                                    target=str(artifact),
                                                                                    forced=current_forced,
                                                                                    artifact_umbral=window['artifact_umbral'],
                                                                                    window_size_sec=window['window_size_sec'],
                                                                                    stride_sec=window['stride_sec'],
                                                                                )

            if i == 0:
                print(f"[INFO] Saving patient asignation for {artifact}")
                current_forced.update(assignment)

            balance = split_balance_report(splitted_dataset, target_col=artifact)
            spread = balance["positive_rate"].max() - balance["positive_rate"].min()
            size_pct = balance["n_total"]/balance["n_total"].sum()
            size_dev = (size_pct - pd.Series(RATIOS)).abs().max()
            print("[DEBUG] Split balance (positive rate):\n", balance)
            bad = {p: (s, assignment[p]) for p, s in FORCED.items() if p in assignment and assignment[p] != s}
            print("Broken rules:", len(bad), "| splits per patient:", pd.Series(assignment).value_counts().to_dict())
            display(splitted_dataset.head(10))
            print(splitted_dataset.columns.to_list())


            """ FEATURES EXTRACTION """
            print("\nStarting features extraction from channels and ICA components...")
            featured_windows = get_or_build_features(   splitted_dataset,
                                                        target_labels=list(ARTIFACT_KEYWORDS.keys()),
                                                        bipolar_montage=False,
                                                        artifact=artifact,
                                                        window_size_sec=window['window_size_sec'],
                                                        stride_sec=window['stride_sec'],
                                                        use_ica=True,
                                                        cache_dir=FEATURES_DIR,
                                                        ica_cache_dir=str(ICA_CACHE_DIR),
                                                        session_cache_dir=str(SESSION_CACHE_DIR),
                                                        version=VERSION,
                                                        refresh=False,
                                                    )
            display(featured_windows.head(25))

            if not featured_windows.empty:
                print("[INFO] Successful features extraction")
                rf_features_dataset = build_ml_dataset(featured_windows, target_artifact=artifact, output_path=rf_dataset_path)
            else:
                raise ValueError(f"Error: Resulting empty dataset")

            rf_features_dataset = drop_inconsistent_channel_columns(rf_features_dataset, protect_cols=LEAKAGE_COLS + ["is_positive", "split"] )
            print(rf_features_dataset.head(5))
            print(rf_features_dataset.columns.tolist())

            if NORMALIZE:
                exclude_cols_to_feats = ['ic_index', 'ic_raw_label', 'ic_target_label', 'ic_iclabel_prob']
                feature_col = [c for c in rf_features_dataset.columns
                               if (c.startswith('ic_') and c not in exclude_cols_to_feats) or c.endswith(('_variance', '_line_length', '_peak_to_peak'))]

                rf_features_dataset[feature_col] = rf_features_dataset.groupby('Session')[feature_col].transform(
                    lambda x: (x - x.median()) / (x.quantile(0.75) - x.quantile(0.25) + 1e-8)
                )
                print(f"[INFO] Normalization applied to: {feature_col}")

            print("[INFO] Positive count:")
            print(rf_features_dataset["is_positive"].value_counts())


        split_counts = rf_features_dataset["split"].value_counts(dropna=False)
        print("[INFO] Split distribution: ", split_counts)

        print("\n" + ("="*50))
        print(f"Starting training of Random Forest - {artifact}")

        config = RANDOM_SPACE[artifact]
        results.setdefault(artifact, []).append(  train_binary_model(   df=rf_features_dataset,
                                                                        model_name=f"rf_{artifact}_w{window['window_size_sec']}s{window['stride_sec']}_{VERSION}",
                                                                        window_size_sec=window,
                                                                        build_model_fn=build_rf_model,
                                                                        search_data=config["space"],
                                                                        models_dir=str(MODELS_DIR),
                                                                        leakage_cols=LEAKAGE_COLS,
                                                                        search_method="random",
                                                                        search_kwargs={"n_iter": config["n_iter"]},
                                                                        force_retrain=False,
                                                                        balanced=True,
                                                                        max_fp_per_day=config["max_fp_per_day"] 
                                                                    )
                                                 )

print("\n"+"*-" * 25)
print("Final report")
for artifact, res_list in results.items():
    print(('-'*10), artifact, ('-'*10))
    for res in res_list:
        print(f"\t\t F1(val)={res['val_f1']:.4f}")
        print(f"\t\t best_params={res['params']}")
        print("\t\t Confusion matrix:", res['confusion_matrix'])
        print("\t\t Metrics results:", res['metrics_results'])