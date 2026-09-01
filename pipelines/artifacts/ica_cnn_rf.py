"""
# File: ica_cnn_rf.py
# Project: Trabajo de graduación
# Author: Maria Fernanda Andrade Recinos

End-to-end pipeline for 'artifact' corpus, process:
Windowing -> split -> features (ICA+ICLabel agregado) -> 
Hiperparameter optimization (Grid Search y Honey Badger) -> 
Training of multi-output RF -> validation -> saves work.
"""

import pickle
import pandas as pd
from pathlib import Path
from pickle import dump
from sklearn.metrics import classification_report

from implementation.core.data_config import ARTIFACT_KEYWORDS, WINDOW_REQUESTS
from implementation.core.data_loader import build_annotations_index
from implementation.core.windowing import label_windowing
from implementation.core.data_spliter import grouped_multilabel_split, save_split_outputs
from implementation.core.features_extractor import build_feature_dataset
from implementation.models.rf_model import (
    optimize_rf_hba, optimize_rf_gridsearch, train_rf, DEFAULT_TARGETS,
)

# Configurations and taxonomy ---------------------------------------------------------------------
CORPUS_NAME = "artifact"
TARGET_TAXONOMY = ARTIFACT_KEYWORDS
WINDOW_REQUEST_NAME = "rf_artifact_class"
SPLIT_VERSION = "v1"
RUN = {
    "windowing": True,
    "gridsearch": True,
    "hba": False,
    "comparison": True,
}

# Location of project path to prevent rupture due to cmd running
def find_project_root(marker="implementation"):
    current = Path(__file__).resolve()
    for parent in current.parents:
        if (parent / marker).is_dir():
            return parent
    raise RuntimeError(f"No se encontró la raíz del proyecto (buscando carpeta '{marker}')")

BASE_DIR = find_project_root()

# Isolated outputs - path directions
CORPUS_OUTPUTS_DIR = BASE_DIR / "outputs" / CORPUS_NAME
SPLIT_DIR = CORPUS_OUTPUTS_DIR / "splits"
FEATURES_DIR = CORPUS_OUTPUTS_DIR / "features"
MODELS_DIR = CORPUS_OUTPUTS_DIR / "models"
ICA_CACHE_DIR = CORPUS_OUTPUTS_DIR / "cache" / "ica"
for d in (SPLIT_DIR, FEATURES_DIR, MODELS_DIR, ICA_CACHE_DIR):
    d.mkdir(parents=True, exist_ok=True)
context_cols = ["Patient", "Session", "Start", "split", "sample_weight"] + list(DEFAULT_TARGETS)

# Hyperparameters optimization methods ---------------------------------------------------------------------------
## Hyperparameters optimization by Grid Search ********************************************************************
def Run_GridSearch(process_number, total_number_process, X_train, y_train, groups_train):
    gs_path = MODELS_DIR / f"gridsearch_result_{SPLIT_VERSION}.pkl"
    if gs_path.exists():
        print(f"[{process_number}/{total_number_process}] Grid search results already generated in {gs_path}, loading...")
        with open(gs_path, "rb") as f:
            gs_result = pickle.load(f)
        gs_params, gs_score = gs_result["params"], gs_result["score"]
    else:
        print("[{process_number}/{total_process}] Running Grid Search Optimization [this can take a while]")
        param_grid = {
            "estimator__n_estimators": [200, 400],
            "estimator__max_depth": [None, 20],
            "estimator__min_samples_split": [2, 10],
            "estimator__max_features": ["sqrt"],
        }
        _, gs_params, gs_score = optimize_rf_gridsearch(
            X_train, y_train, groups_train, param_grid=param_grid, cv_splits=5, n_jobs=16, m_jobs=1
        )   
        with open(gs_path, "wb") as f:
            dump({"params": gs_params, "score": gs_score}, f)

    print(f"\t\tGridSearch -> params={gs_params}, F1 macro CV={gs_score:.4f}")
    return gs_params, gs_score

## Hyperparameters optimization by Honey Badger Algorithm *********************************************************
##   HBA (Hashim et al., 2022) — metaheurístico
def Run_HBA(process_number, total_number_process, X_train, y_train, groups_train):
    hba_path = MODELS_DIR / f"hba_result_{SPLIT_VERSION}.pkl"
    if hba_path.exists():
        print(f"[{process_number}/{total_number_process}] Honey Badger Algorithm results already generated in {hba_path}, loading...")
        with open(hba_path, "rb") as f:
            hba_result = pickle.load(f)
        hba_params, hba_score = hba_result["params"], hba_result["score"]
    else:
        print(f"{process_number}/{total_number_process} Running Honey Badger Algorithm Optimization, this can take a while...")
        hba_params, hba_score, hba_history = optimize_rf_hba(
            X_train, y_train, groups_train, max_iter=15, n_agents=10, seed=42,
        )
        with open(hba_path, "wb") as f:
            dump({"params": hba_params, "score": hba_score, "history": hba_history}, f)

    print(f"\t\tHBA -> params={hba_params}, F1 macro CV={hba_score:.4f}")
    return hba_params, hba_score    

# Main
if __name__ == "__main__":
    # Staring values
    results = {}
    total_active = sum(RUN.values())
    step = 1

    # Windowing, split and feature extraction ***********************************************************************
    if RUN["windowing"]:
        feature_paths = {s: FEATURES_DIR / f"features_{s}.parquet" for s in ("train", "val", "test")}

        if all(p.exists() for p in feature_paths.values()):
            print(f"[{step}/{total_active}] Features alterady generated in {FEATURES_DIR}, loading...")
            datasets = {s: pd.read_parquet(p) for s, p in feature_paths.items()}
        else:
            print(f"[{step}/{total_active}] Incompleted or not founded features for '{CORPUS_NAME}' corpus, generating...")
            csv_path = SPLIT_DIR / f"windowed_df_{WINDOW_REQUEST_NAME}_{SPLIT_VERSION}.csv"
            if csv_path.exists():
                print(f"      Using existing split: {csv_path}")
                windowed_df = pd.read_csv(csv_path)
                windowed_df["EDF_path"] = windowed_df["EDF_path"].apply(Path)
            else:
                print("      Staring windowing and splitting...")
                database = build_annotations_index(CORPUS_NAME, paths=True)
                windowed_df = label_windowing(
                    database, WINDOW_REQUESTS[WINDOW_REQUEST_NAME],
                    TARGET_TAXONOMY, unreviewd_tokens=True,
                )
                ratios = {"train": 0.7, "val": 0.15, "test": 0.15}
                windowed_df, assignment = grouped_multilabel_split(
                    windowed_df, target_taxonomy=TARGET_TAXONOMY, ratios=ratios, seed=42,
                )
                save_split_outputs(
                    windowed_df=windowed_df, assignment=assignment, target_taxonomy=TARGET_TAXONOMY,
                    ratios=ratios, seed=42, window_request_name=WINDOW_REQUEST_NAME,
                    out_dir=SPLIT_DIR, version=SPLIT_VERSION,
                )

            clean_df = windowed_df[(windowed_df["is_excluded"] == 0) & (windowed_df["is_ambiguous"] == 0)]

            datasets = {}
            for split_name, out_path in feature_paths.items():
                print(f"      Extracting features for split {split_name}...")
                subset = clean_df[clean_df["split"] == split_name]
                feats = build_feature_dataset(subset, use_ica=True, ica_cache_dir=str(ICA_CACHE_DIR))
                merged = feats.merge(subset[context_cols], on=["Patient", "Session", "Start"], how="left")
                merged.to_parquet(out_path, index=False)
                datasets[split_name] = merged

        train_df, val_df = datasets["train"], datasets["val"]
        feature_cols = [c for c in train_df.columns if c not in context_cols]

        print(f"      train={train_df.shape}, val={val_df.shape}, test={datasets['test'].shape}")
        print(f"      n_features={len(feature_cols)}")

        X_train, y_train = train_df[feature_cols], train_df[DEFAULT_TARGETS]
        w_train = train_df["sample_weight"]
        groups_train = train_df["Patient"]

    # Optimization ---------------------------------------------------------------------------------------------------
    if RUN["gridsearch"]:
        step += 1
        params, score = Run_GridSearch(step, total_active, X_train, y_train, groups_train)
        results["gridsearch"] = {"params": params, "score": score}

    if RUN["hba"]:
        step += 1
        params, score = Run_HBA(step, total_active, X_train, y_train, groups_train)
        results["hba"] = {"params": params, "score": score}

    # Train and validation of the final model ************************************************************************
    step += 1
    if RUN["comparison"]:
        final_model_path = MODELS_DIR / f"rf_ica_iclabel_{CORPUS_NAME}_{SPLIT_VERSION}.pkl"

        best_method = max(results, key=lambda m: results[m]["score"])
        best_params = results[best_method]["params"]
        best_score = results[best_method]["score"]

        print(f"[{step}/{total_active}] Best method: {best_method} (F1={best_score:.4f})")

        if best_method == "gridsearch":
            clean_params = {k.replace("estimator__", ""): v for k, v in best_params.items()}
        else:
            clean_params = best_params

        final_model = train_rf(X_train, y_train, sample_weight=w_train, **clean_params)

        X_val, y_val = val_df[feature_cols], val_df[DEFAULT_TARGETS]
        y_pred = final_model.predict(X_val)

        print(f"\n===== Validation report (val) — corpus='{CORPUS_NAME}' =====")
        for i, target in enumerate(DEFAULT_TARGETS):
            print(f"--- {target} ---")
            print(classification_report(y_val[target], y_pred[:, i], zero_division=0))

        with open(final_model_path, "wb") as f:
            dump({
                "model": final_model,
                "feature_cols": feature_cols,
                "params": best_params,
                "best_method": best_method,
                "score": best_score,
                "corpus": CORPUS_NAME,
            }, f)

        print(f"\nFinal model saved in: {final_model_path}")