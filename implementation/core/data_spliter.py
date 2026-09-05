"""
# File: data_spliter.py
# Project: Trabajo de graduación
# Author: Maria Fernanda Andrade Recinos

Distribute the data from the original dataset to create a uniform partition 
based on the parameters extracted from the EDA.
"""

# Data managment libraries
import json
from datetime import datetime
import pandas as pd

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


def save_split_outputs(windowed_df, assignment, target_taxonomy, ratios, seed,
                        window_request_name, out_dir="splits", version="v1",
                        notes=""):
    out_dir = Path(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    basename = f"windowed_df_{window_request_name}_{version}"
    csv_path = out_dir / f"{basename}.csv"
    json_path = out_dir / f"{basename}.json"
    

    # 1. Dataframe completo con la columna split ya pegada
    windowed_df.to_csv(csv_path, index=False)

    # 2. Sidecar con lo necesario para reproducir/auditar
    n_patients = pd.Series(assignment).value_counts().to_dict()
    metadata = {
        "source_window_request": window_request_name,
        "target_taxonomy_keys": list(target_taxonomy.keys()),
        "seed": seed,
        "ratios": ratios,
        "n_patients": n_patients,
        "n_windows_total": len(windowed_df),
        "generated_at": datetime.now().strftime("%Y-%m-%d"),
        "notes": notes,
    }


    print(f"Guardado: {csv_path}")
    print(f"Guardado: {json_path}")
    return csv_path, json_path

def get_or_compute_split(windowed_df, target_taxonomy, group_col="Patient",
                        include_clean=True, drop_excluded=True, drop_ambiguous=True, 
                        ratios={"train": 0.7, "val": 0.15, "test": 0.15}, seed=42, 
                        dataset_division_dir="splits", version="v1"):
    
    saving_dir = Path(dataset_division_dir)
    saving_dir.mkdir(parents=True, exist_ok=True)
    saving_parquet = saving_dir / f"test{ratios['train']}_val{ratios['val']}_train{ratios['test']}_{version}.pkl"
    saving_json = saving_dir / f"test{ratios['train']}_val{ratios['val']}_train{ratios['test']}_{version}.json"

    current_config = {
        "target_taxonomy_keys": list(target_taxonomy.keys()),
        "target_taxonomy_values": list(target_taxonomy.values()),
        "seed": seed,
        "ratios": ratios,
        "n_windows_total": len(windowed_df),
        "patients": sorted(windowed_df[group_col].unique().tolist()),
        "version": version,
    }
    
    compute_new_split = True

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
            print(f"[INFO] Loading existing split from {saving_parquet} and {saving_json}")
            windowed_df = pd.read_parquet(saving_parquet)
            assignment = saved_metadata.get("patient_assignments", {})
            report = pd.DataFrame(saved_metadata.get("split_report", {})).T
            compute_new_split = False
        else:
            print(f"[INFO] Existing split metadata does not match current configuration.")

    if compute_new_split:
        print(f"[INFO] Existing split metadata does not match current configuration.")
        print(f"[INFO] Computing and saving new split...")
        windowed_df, assignment, report = grouped_multilabel_split(windowed_df, target_taxonomy, group_col, include_clean,
                                                                    drop_excluded, drop_ambiguous, 
                                                                    ratios, seed)
        with open(saving_json, "w") as f:
            metadata_to_save = current_config.copy()
            metadata_to_save["generated_at"] = datetime.now().strftime("%Y-%m-%d")
            metadata_to_save["n_patients"] = pd.Series(assignment).value_counts().to_dict()
            metadata_to_save["patient_assignments"] = assignment
            metadata_to_save["split_report"] = report.to_dict()
            json.dump(metadata_to_save, f, indent=4)
        windowed_df.to_parquet(saving_parquet, index=False)
        print(f"[INFO] Saved new split to {str(saving_parquet)} and {str(saving_json)}")

    return windowed_df, assignment, report

if __name__ == "__main__":
    
    # Data integration libraries / project modules
    from implementation.core.data_config import ARTIFACT_KEYWORDS, ARTIFACT_ADDITIONAL_TOKENS, BACKGROUND_LABEL, WINDOW_REQUESTS
    from implementation.core.data_loader import build_annotations_index
    from implementation.core.windowing import label_windowing
    from implementation.core.data_config import find_project_root

    # Data visualization libraries
    from IPython.display import display
    from pathlib import Path


    # Paths for loading and saving data
    BASE_DIR = find_project_root()
    CORPUS_OUTPUTS_DIR = BASE_DIR / "outputs" / "artifact"
    SPLIT_CACHE_DIR = CORPUS_OUTPUTS_DIR / "individual_tests" / "splits"
    
    database_corpus_patient = build_annotations_index("artifact", paths=True, n_patients=50, max_sessions=1)
    display(database_corpus_patient)

    windowed_annotations_corpus_patient = label_windowing(database_corpus_patient, 
                                                          WINDOW_REQUESTS["rf_artifact_class"], 
                                                          ARTIFACT_KEYWORDS, 
                                                          unreviewd_tokens=True)

    display(windowed_annotations_corpus_patient)

    ratios_ = {"train": 0.7, "val": 0.15, "test": 0.15}
    # windowed_df, assignment, report = grouped_multilabel_split(windowed_annotations_corpus_patient, target_taxonomy=ARTIFACT_KEYWORDS)
    windowed_df, assignment, report = get_or_compute_split(windowed_annotations_corpus_patient, target_taxonomy=ARTIFACT_KEYWORDS, dataset_division_dir=SPLIT_CACHE_DIR, version="v1", ratios=ratios_)
    
    print("[DEBUG] Report with ratios:", ratios_, "\n", report)
    print("[DEBUG] Assignment value:", assignment)

    print("Windowed dataframe:")
    display(windowed_df.head(5))
    print(windowed_df.columns.tolist())
    print("[DEBUG] is_excluded_unreviewed: ",len(windowed_df[(windowed_df["is_excluded_unreviewed"]==1)]))
    print("[DEBUG] is_clean_window: ",len(windowed_df[(windowed_df["is_clean_window"]==1)]))
    print("[DEBUG] is_unreviewed: ",len(windowed_df[(windowed_df["is_unreviewed"]==1)]))
    print("[DEBUG] is_excluded: ",len(windowed_df[(windowed_df["is_excluded"]==1)]))
        
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