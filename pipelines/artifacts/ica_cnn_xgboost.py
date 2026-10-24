"""
# File: ica_cnn_xg.py
# Project: Trabajo de graduación
# Author: Maria Fernanda Andrade Recinos

End-to-end pipeline for 'artifact' corpus, process:
Windowing -> split -> features (ICA+ICLabel agregado) -> 
Hiperparameter optimization (Random Search, Grid Search y Honey Badger) -> 
Training of several XGBoost, one per artifact -> validation -> saves work.
"""
# file: ica_cnn_xgboost.py (pipeline)

# Data managment libraries
import math
import pandas as pd
from pathlib import Path
from scipy.stats import randint, uniform

# Data integration libraries / project modules
from src.core.windowing import get_or_build_windows
from src.core.data_loader import build_annotations_index, find_project_root
from src.core.data_config import ARTIFACT_KEYWORDS, WINDOW_REQUESTS_ARTIFACTS, RATIOS, VERSION, LEAKAGE_COLS, OUTPUTS_DIR, NORMALIZE, COMPARISON
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

FORCE_RETRAIN = True
POS_THR, IGN_THR = 0.5, 0.2
OPTIMIZER_IDX = 2  # 0: grid, 1: random, 2: optuna

### ----------------------------------------------------------------------
if COMPARISON:
    DATASET_DIR = CORPUS_OUTPUTS_DIR / Path("dataset/_comparison") 
    MODELS_DIR = CORPUS_OUTPUTS_DIR / Path("models/_comparison")

for d in (ICA_CACHE_DIR, SESSION_CACHE_DIR, WINDOWS_CACHE_DIR, FEATURES_DIR, DATASET_DIR, SPLIT_CACHE_DIR, ANNOTATIONS_DIR):
    d.mkdir(parents=True, exist_ok=True)

PARAM_GRID = {
    "n_estimators": [200, 400],
    "max_depth": [None, 20]
}
RANDOM_SPACE = {
    "n_estimators": randint(100, 600),
    "max_depth": randint(3, 10),
    "learning_rate": uniform(0.01, 0.29),      
    "subsample": uniform(0.4, 0.6),
    "colsample_bytree": uniform(0.5, 0.5),     
    "min_child_weight": randint(1, 7),
    "gamma": uniform(0.0, 2.0),
    "reg_alpha": uniform(0.0, 2.0),
    "reg_lambda": uniform(0.0, 2.0),
    "scale_pos_weight": [0.0],
}
OPTUNA_SPACE = {
    "n_estimators": ("int", 100, 600),
    "max_depth": ("int", 3, 10),
    "learning_rate": ("float", 0.01, 0.30, True),      
    "subsample": ("float", 0.4, 0.6),
    "colsample_bytree": ("float", 0.5, 0.5),     
    "min_child_weight": ("int", 1, 7),
    "gamma": ("float", 0.0, 2.0),
    "reg_alpha": ("float", 0.0, 2.0),
    "reg_lambda": ("float", 0.0, 2.0),
    "scale_pos_weight": ("float", 1.0, 5.0),
}

AVAILABLE_OPTIMIZERS = ["grid", "random", "optuna", "hba"]
OPTIMIZER_SETTINGS = [PARAM_GRID, RANDOM_SPACE, OPTUNA_SPACE]

CURRENT_OPTIMIZER = AVAILABLE_OPTIMIZERS[OPTIMIZER_IDX]
CURRENT_SPACE_BASE = OPTIMIZER_SETTINGS[OPTIMIZER_IDX]

for name, val in RANDOM_SPACE.items():
    has_rvs = hasattr(val, "rvs")
    has_len = hasattr(val, "__len__")
    print(f"{name}: {val!r} | tiene .rvs()? {has_rvs} | tiene __len__? {has_len}")

CONFIG_ARTIFACT = {
    "eye": {
        "max_fp_per_day": 50,
        "n_iter": 60,
    },
    "muscle": {
        "max_fp_per_day": 300,
        "n_iter": 60,
    },
    "non_physiological": {
        "max_fp_per_day": 1000,
        "n_iter": 60,
    },
}


print("\nLoading all dataset for training...")
database_corpus_patient = build_annotations_index("artifact", paths=True, CACHE_DIR=ANNOTATIONS_DIR)
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

        xg_dataset_path = DATASET_DIR / (
            f"rf_dataset_{artifact}_w{window['window_size_sec']}_s{window['stride_sec']}"
            f"_ua{window['artifact_umbral']}_p{n_patients}_v{VERSION}"
            f"_pt{POS_THR}_it{IGN_THR}_norm{int(NORMALIZE and not COMPARISON)}.parquet"
        )

        #print("[DEBUG] Looking for {xg_dataset_path}, it is {xg_dataset_path.exists()} it exists")
        if xg_dataset_path.exists():
            print(f"[INFO] Existing dataset, loading: {xg_dataset_path}")
            xg_features_dataset = pd.read_parquet(xg_dataset_path)
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
                                                                                    manually_checked=COMPARISON
                                                                                )

            if i == 0 and not COMPARISON:
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
                                                        manually_checked=COMPARISON
                                                    )
            display(featured_windows.head(25))

            if not featured_windows.empty:
                print("[INFO] Successful features extraction")
                xg_features_dataset = build_ml_dataset(featured_windows, target_artifact=artifact,
                                                       output_path=xg_dataset_path.with_suffix(".raw.parquet"),
                                                       pos_thr=POS_THR, ign_thr=IGN_THR)
            else:
                raise ValueError(f"Error: Resulting empty dataset")
            
            xg_features_dataset = drop_inconsistent_channel_columns(xg_features_dataset, protect_cols=LEAKAGE_COLS + ["is_positive", "split"] )
            print(xg_features_dataset.head(5))
            print(xg_features_dataset.columns.tolist())

            if NORMALIZE and not COMPARISON:
                exclude_cols_to_feats = ['ic_index', 'ic_raw_label', 'ic_target_label', 'ic_iclabel_prob']
                feature_col = [c for c in xg_features_dataset.columns
                               if (c.startswith('ic_') and c not in exclude_cols_to_feats) or c.endswith(('_variance', '_line_length', '_peak_to_peak'))]

                xg_features_dataset[feature_col] = xg_features_dataset.groupby('Session')[feature_col].transform(
                    lambda x: (x - x.median()) / (x.quantile(0.75) - x.quantile(0.25) + 1e-8)
                )
                print(f"[INFO] Normalization applied to: {feature_col}")

            print("[INFO] Positive count:")
            print(xg_features_dataset["is_positive"].value_counts())
            xg_features_dataset.to_parquet(xg_dataset_path, index=False)

        split_counts = xg_features_dataset["split"].value_counts(dropna=False)
        print("[INFO] Split distribution: ", split_counts)

        train_mask = xg_features_dataset["split"] == "train"
        
        n_pos = (train_mask & (xg_features_dataset["is_positive"] == 1)).sum()
        n_neg = (train_mask & (xg_features_dataset["is_positive"] == 0)).sum()
        raw_weight = n_neg / n_pos if n_pos > 0 else 1.0
        scale_pos_weight_base = min(raw_weight, 10.0)
        print("[INFO] Scale positive weight (excluding -1):", scale_pos_weight_base)

        current_xgb_space = CURRENT_SPACE_BASE.copy()
        if CURRENT_OPTIMIZER in ["grid", "random"]:
            current_xgb_space["scale_pos_weight"] = [scale_pos_weight_base]

        print("\n" + ("="*50))
        print(f"Starting training of XGBoost - {artifact}")

        # Reemplaza config = RANDOM_SPACE[artifact] por tu configuración de iteraciones
        config = CONFIG_ARTIFACT[artifact] # Asegúrate de tener este diccionario definido arriba

        # 3. Llamar al entrenamiento con build_xgb_model
        results.setdefault(artifact, []).append(  train_binary_model(   df=xg_features_dataset,
                                                                        model_name=f"xgb_{artifact}_w{window['window_size_sec']}s{window['stride_sec']}_{VERSION}_run2",
                                                                        window_size_sec=window,
                                                                        build_model_fn=build_xgb_model,
                                                                        search_data=current_xgb_space,
                                                                        models_dir=str(MODELS_DIR),
                                                                        leakage_cols=LEAKAGE_COLS,
                                                                        search_method=CURRENT_OPTIMIZER,
                                                                        search_kwargs={"n_iter": config["n_iter"]},
                                                                        force_retrain=FORCE_RETRAIN,
                                                                        balanced=False, 
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