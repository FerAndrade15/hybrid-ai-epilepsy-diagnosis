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
import numpy as np
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

    rng = np.random.default_rng(seed)
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

    # El assignment se mapea sobre el df ORIGINAL sin filtrar,
    # para que las ventanas excluidas/ambiguas también queden marcadas
    # (para medir falsos positivos en val/test)
    windowed_df = windowed_df.copy()
    windowed_df["split"] = windowed_df[group_col].map(assignment)

    report = pd.DataFrame(split_totals).T
    report["n_patients"] = pd.Series(assignment).value_counts()
    print(report)
    return windowed_df, assignment


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
    with open(json_path, "w") as f:
        json.dump(metadata, f, indent=2)

    print(f"Guardado: {csv_path}")
    print(f"Guardado: {json_path}")
    return csv_path, json_path

if __name__ == "__main__":
    from implementation.core.data_config import ARTIFACT_KEYWORDS, ARTIFACT_ADDITIONAL_TOKENS, BACKGROUND_LABEL, WINDOW_REQUESTS
    from implementation.core.data_loader import build_annotations_index
    from implementation.core.windowing import label_windowing
    
    database_corpus_patient = build_annotations_index("artifact", paths=True) # n_patients=10, max_sessions=1,
    windowed_annotations_corpus_patient = label_windowing(database_corpus_patient, 
                                                          WINDOW_REQUESTS["rf_artifact_class"], 
                                                          ARTIFACT_KEYWORDS, 
                                                          unreviewd_tokens=True)

    ratios_ = {"train": 0.7, "val": 0.15, "test": 0.15}
    windowed_df, assignment = grouped_multilabel_split(windowed_annotations_corpus_patient, target_taxonomy=ARTIFACT_KEYWORDS)

    save_split_outputs(
        windowed_df=windowed_df,
        assignment=assignment,
        target_taxonomy=ARTIFACT_KEYWORDS,
        ratios=ratios_,         # currently used, default
        seed=42,                # default
        window_request_name="rf_artifact_class",
        version="v1",
        notes="",
    )
    
    """pd.set_option("display.max_columns", None)
    pd.set_option("display.width", 120)  
    pd.set_option("display.expand_frame_repr", True)
    pd.set_option("display.max_colwidth", 25)
    print(windowed_df.head())
    print(windowed_df.shape)"""
    
    # Para entrenamiento, ahí sí filtrás excluidas/ambiguas
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