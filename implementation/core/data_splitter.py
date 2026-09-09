"""
# File: data_spliter.py
# Project: Trabajo de graduación
# Author: Maria Fernanda Andrade Recinos

Distribute the data from the original dataset to create a uniform partition 
based on the parameters extracted from the EDA.
"""
## file: data_spliter.py

# Data managment libraries
import json
from datetime import datetime
import pandas as pd
from pathlib import Path

def grouped_multilabel_split(windowed_df, target_taxonomy, group_col="Patient", include_clean=True, 
                             drop_excluded=True, drop_ambiguous=True, 
                             ratios={"train": 0.7, "val": 0.15, "test": 0.15}, seed=42):
                             
    df = windowed_df.copy()

    if drop_excluded and "is_excluded" in df.columns:
        df = df[df["is_excluded"] == 0]
    if drop_ambiguous and "is_ambiguous" in df.columns:
        df = df[df["is_ambiguous"] == 0]

    label_cols = list(target_taxonomy.keys())
    if include_clean:
        label_cols = label_cols + ["is_clean_window"]

    patient_counts = df.groupby(group_col)[label_cols].sum()
    patient_counts["total_weight"] = patient_counts.sum(axis=1)
    order = patient_counts.sample(frac=1, random_state=seed).sort_values(
        "total_weight", ascending=False
    ).index

    target_totals = patient_counts[label_cols].sum()
    split_totals = {s: pd.Series(0, index=label_cols, dtype=float) for s in ratios}
    split_target = {s: target_totals * r for s, r in ratios.items()}
    assignment = {}

    for patient in order:
        counts = patient_counts.loc[patient, label_cols]
        def deficit(split_name):
            projected = split_totals[split_name] + counts
            return ((projected - split_target[split_name]) / (split_target[split_name] + 1e-9)).max()
        best_split = min(ratios.keys(), key=deficit)
        assignment[patient] = best_split
        split_totals[best_split] += counts

    windowed_df = windowed_df.copy()
    windowed_df["split"] = windowed_df[group_col].map(assignment)

    report = pd.DataFrame(split_totals).T
    report["n_patients"] = pd.Series(assignment).value_counts()
    return windowed_df, assignment, report


def grouped_split_from_labels(windowed_df, target_col="is_positve", group_col="Patient", 
                              include_clean=True, drop_excluded=True, drop_ambiguous=True, 
                             ratios={"train": 0.7, "val": 0.15, "test": 0.15}, seed=42):

    df = windowed_df.copy()

    if drop_excluded and "is_excluded" in df.columns:
        df = df[df["is_excluded"] == 0]
    if drop_ambiguous and "is_ambiguous" in df.columns:
        df = df[df["is_ambiguous"] == 0]
        
    counts = df.groupby(group_col)[target_col].sum()
    order = counts.sample(frac=1, random_state=seed).sort_values(ascending=False).index

    target_total = counts.sum()
    split_totals = {s: 0.0 for s in ratios}
    split_target = {s: target_total * r for s, r in ratios.items()}
    assignment = {}

    for patient in order:
        c = counts.loc[patient]
        def deficit(split_name):
            projected = split_totals[split_name] + c
            return ((projected - split_target[split_name]) / (split_target[split_name] + 1e-9))
        best_split = min(ratios.keys(), key=deficit)
        assignment[patient] = best_split
        split_totals[best_split] += c

    windowed_df = windowed_df.copy()
    windowed_df["split"] = windowed_df[group_col].map(assignment)

    for split_name, total in split_totals.items():
        if total == 0:
            raise ValueError(f"[ERROR] Invalid split '{split_name}' has 0 real positives.")

    report = pd.DataFrame(split_totals).T
    report["n_patients"] = pd.Series(assignment).value_counts()
    return windowed_df, assignment, report


def get_or_compute_labeled_split(windowed_df, label_col, group_col="Patient",
                        include_clean=True, drop_excluded=True, drop_ambiguous=True, 
                        ratios={"train": 0.7, "val": 0.15, "test": 0.15}, seed=42, 
                        dataset_division_dir="splits", version=1, target="all"):
    
    current_config = {
        "target_taxonomy": label_col,
        "ratios": ratios,
        "n_windows_total": len(windowed_df),
        "patients": sorted(windowed_df[group_col].unique().tolist()),
        "version": version,
    }

    saving_dir = Path(dataset_division_dir)
    saving_dir.mkdir(parents=True, exist_ok=True)
    base_name = f"split_train{ratios['train']*100}_val{ratios['val']*100}_test{ratios['test']*100}_p{len(sorted(windowed_df[group_col].unique().tolist()))}_v{version}_{target}"
    saving_parquet = saving_dir / f"{base_name}.parquet"
    saving_json = saving_dir / f"{base_name}.json"

    if saving_parquet.exists() and saving_json.exists():
        with open(saving_json, "r") as f:
            saved_metadata = json.load(f)
            comp_metadata = saved_metadata.copy()
            comp_metadata.pop("generated_at", None)
            comp_metadata.pop("notes", None)
            comp_metadata.pop("n_patients", None)
            comp_metadata.pop("patient_assignments", None)
            comp_metadata.pop("split_report", None)

        if comp_metadata == current_config:
            print(f"[INFO] Loading existing split from {str(base_name)} parquet and json")
            return pd.read_parquet(saving_parquet), saved_metadata.get("patient_assignments", {}), pd.DataFrame(saved_metadata.get("split_report", {})).T
        else:
            print(f"[INFO] Existing split metadata does not match current configuration.")
            raise ValueError(
                f"\n[PELIGRO] El archivo {str(base_name)} ya existe, pero la configuración actual "
                f"ha cambiado \n"
                f"Para no sobreescribir tus datos anteriores, cambia el parámetro "
                f"'version={version + 1}' (o mayor) en tu script principal."
            )
           
    print(f"[INFO] Existing split metadata does not match current configuration.")
    print(f"[INFO] Computing and saving new split...")
    windowed_df, assignment, report = grouped_split_from_labels(windowed_df, label_col, group_col, include_clean,
                                                                drop_excluded, drop_ambiguous, 
                                                                ratios, seed)
    with open(saving_json, "w") as f:
        metadata_to_save = current_config.copy()
        metadata_to_save["generated_at"] = datetime.now().strftime("%Y-%m-%d")
        metadata_to_save["n_patients"] = pd.Series(assignment).value_counts().to_dict()
        metadata_to_save["patient_assignments"] = assignment
        metadata_to_save["split_report"] = report.to_dict()
        json.dump(metadata_to_save, f, indent=4)

    if "EDF_path" in windowed_df.columns:
        windowed_df["EDF_path"] = windowed_df["EDF_path"].astype(str)
        
    # Si la columna 'CSV' (que vi en tu log) también tiene rutas Path, agrégala:
    if "CSV" in windowed_df.columns:
        windowed_df["CSV"] = windowed_df["CSV"].astype(str)

    windowed_df.to_parquet(saving_parquet, index=False)
    print(f"[INFO] Saved new split to {str(base_name)}")

    return windowed_df, assignment, report

def split_features_target(df, split_name, leakage_columns, exclude_probs=False):
    """
    Function to filter the split configuration separating features and target (input for training and  output to validate)
    """
    subset = df[df["split"]== split_name].copy()

    #Columns
    tuar_cols = [c for c in subset.columns if c.startswith("tuar_")]
    if exclude_probs:
        iclabel_prob_col = ["ic_iclabel_prob"]
    else:
        iclabel_prob_col = []

    drop_cols = [c for c in leakage_columns + tuar_cols + iclabel_prob_col]
    X = subset.drop(columns=drop_cols)
    y = subset["is_positive"]
    return X, y

if __name__ == "__main__":
    
    # Data integration libraries / project modules
    from implementation.core.data_config import ARTIFACT_KEYWORDS, ARTIFACT_ADDITIONAL_TOKENS, BACKGROUND_LABEL, WINDOW_REQUESTS
    from implementation.core.data_loader import build_annotations_index
    from implementation.core.windowing import label_windowing
    from implementation.core.data_config import find_project_root

    # Data visualization libraries
    from IPython.display import display


    # Paths for loading and saving data
    BASE_DIR = find_project_root()
    CORPUS_OUTPUTS_DIR = BASE_DIR / "outputs" / "artifact"
    SPLIT_CACHE_DIR = CORPUS_OUTPUTS_DIR / "individual_tests" / "splits"
    
    database_corpus_patient = build_annotations_index("artifact", paths=True, n_patients=25, max_sessions=1)
    display(database_corpus_patient)

    windowed_annotations_corpus_patient = label_windowing(database_corpus_patient, 
                                                          WINDOW_REQUESTS["rf_artifact_class"], 
                                                          ARTIFACT_KEYWORDS, 
                                                          unreviewd_tokens=True)

    display(windowed_annotations_corpus_patient)

    ratios_ = {"train": 0.7, "val": 0.15, "test": 0.15}
    # windowed_df, assignment, report = grouped_multilabel_split(windowed_annotations_corpus_patient, target_taxonomy=ARTIFACT_KEYWORDS)
    windowed_df, assignment, report = get_or_compute_labeled_split(windowed_annotations_corpus_patient, target_taxonomy=ARTIFACT_KEYWORDS, dataset_division_dir=str(SPLIT_CACHE_DIR), ratios=ratios_)
    
    print("[DEBUG] Report with ratios:", ratios_, "\n", report)
    print("[DEBUG] Assignment value:", assignment)

    print("Windowed dataframe:")
    display(windowed_df.head(5))
    print(windowed_df.columns.tolist())
    print("[DEBUG] is_excluded_unreviewed: ",len(windowed_df[(windowed_df["is_excluded_unreviewed"]==1)]))
    print("[DEBUG] is_clean_window: ",len(windowed_df[(windowed_df["is_clean_window"]==1)]))
    print("[DEBUG] is_unreviewed: ",len(windowed_df[(windowed_df["is_unreviewed"]==1)]))
    print("[DEBUG] is_excluded: ",len(windowed_df[(windowed_df["is_excluded"]==1)]))
    print("[DEBUG] is_ambiguous: ",len(windowed_df[(windowed_df["is_ambiguous"]==1)]))
        
    # Para entrenamiento, con filtro de excluidas/ambiguas
    train_df = windowed_df[
        (windowed_df["split"] == "train") &
        (windowed_df["is_excluded"] == 0) &
        (windowed_df["is_ambiguous"] == 0)
    ]
    train_df_rest = windowed_df[
        (windowed_df["split"] == "train") & 
        ((windowed_df["is_excluded"] == 1) | (windowed_df["is_ambiguous"] == 1))
    ]
    val_df = windowed_df[
        (windowed_df["split"] == "val") &
        (windowed_df["is_excluded"] == 0) &
        (windowed_df["is_ambiguous"] == 0)
    ]
    test_df = windowed_df[
        (windowed_df["split"] == "test") &
        (windowed_df["is_excluded"] == 0) &
        (windowed_df["is_ambiguous"] == 0)
    ]
    print(len(train_df), len(train_df_rest), len(val_df), len(test_df))