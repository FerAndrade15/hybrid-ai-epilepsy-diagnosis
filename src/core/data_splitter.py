"""
# File: data_splitter.py
# Project: Trabajo de graduación
# Author: Maria Fernanda Andrade Recinos

Distribute the data from the original dataset to create a uniform partition 
based on the parameters extracted from the EDA.
"""
## file: data_splitter.py

# Data managment libraries
import json
from datetime import datetime
import pandas as pd
from pathlib import Path

# Import modules
from src.utils.patient_registry import load_registry, forced_for, REG_PATH

def split_balance_report(windowed_df, target_col="is_positive", split_col="split"):
    summary = windowed_df.groupby(split_col).agg(
        n_total=(target_col, "size"),
        n_positive=(target_col, "sum"),
    )
    summary["n_negative"] = summary["n_total"] - summary["n_positive"]
    summary["positive_rate"] = summary["n_positive"]/summary["n_total"]
    return summary

def drop_inconsistent_channel_columns(df, verbose=True, protect_cols=None):
    """
	Drop  columns containing NaN values caused by incosisntent montages.
    """
    protect_cols = set(protect_cols or [])
    candidate_cols = [col for col in df.columns if col not in protect_cols]
    cols_with_nan = df[candidate_cols].columns[df[candidate_cols].isna().any()].tolist()
    if verbose and cols_with_nan:
        print(f"[INFO] Dropping {cols_with_nan} due to montage variations")
        print(cols_with_nan)
    return df.drop(columns=cols_with_nan)

def resolve_forced_split(forced, patients, ratios, registry_path=None):
    patients = set(patients)
    if forced is None:
        reg = load_registry(registry_path or REG_PATH)
        if not reg["patients"]:
            print("[INFO] Empty or non-existent register")
        forced = forced_for(reg, patients)
        print(f"[INFO] Fixed per register: {len(forced)} / {len(patients)} patients.")
    forced = {p: s for p, s in forced.items() if p in patients}
    bad = set(forced.values()) - set(ratios)
    if bad:
        raise ValueError(f"Invalid forced splits: {bad}")
    return forced

def grouped_multilabel_split(windowed_df, target_taxonomy, group_col="Patient", include_clean=True, 
                             drop_excluded=True, drop_ambiguous=True, 
                             ratios={"train": 0.7, "val": 0.15, "test": 0.15}, seed=42,
                             forced=None, registry_path=None):
                             
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

    forced = resolve_forced_split(forced, windowed_df[group_col].unique(), ratios, registry_path)
    for p, s in forced.items():
        assignment[p] = s
        if p in patient_counts.index:
            split_totals[s] += patient_counts.loc[p, label_cols]

    for patient in order:
        if patient in assignment:
            continue
        
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


def grouped_split_from_labels(windowed_df, target_col="is_positive", group_col="Patient", 
                              include_clean=True, drop_excluded=True, drop_ambiguous=True, 
                             ratios={"train": 0.7, "val": 0.15, "test": 0.15}, seed=42,
                             size_weight=1, forced=None, registry_path=None):

    df = windowed_df.copy()

    if drop_excluded and "tuar_is_excluded" in df.columns:
        df = df[df["tuar_is_excluded"] == 0]
    if drop_ambiguous and "tuar_is_ambiguous" in df.columns:
        df = df[df["tuar_is_ambiguous"] == 0]
        
    counts = df.groupby(group_col)[target_col].sum()
    sizes = df.groupby(group_col).size()
    order = counts.sample(frac=1, random_state=seed).sort_values(ascending=False).index

    target_total = counts.sum()
    size_total = sizes.sum()
    split_totals = {s: 0.0 for s in ratios}
    split_sizes = {s: 0.0 for s in ratios}
    split_target = {s: target_total * r for s, r in ratios.items()}
    split_size_target = {s: size_total * r for s, r in ratios.items()}
    assignment = {}

    forced = resolve_forced_split(forced, windowed_df[group_col].unique(), ratios, registry_path)
    for p, s in forced.items():
        assignment[p] = s
        if p in counts.index:
            split_totals[s] += counts.loc[p]
            split_sizes[s] += sizes.loc[p]

    for patient in order:
        if patient in assignment:
            continue

        c = counts.loc[patient]
        n = sizes.loc[patient]

        def deficit(split_name):
            pos_deficit = ((split_totals[split_name] + c) - split_target[split_name])/(split_target[split_name]+1e-9)
            size_deficit = ((split_sizes[split_name] + n) - split_size_target[split_name])/(split_size_target[split_name]+1e-9)
            return (1- size_weight) * pos_deficit + size_weight * size_deficit

        best_split = min(ratios.keys(), key=deficit)
        assignment[patient] = best_split
        split_totals[best_split] += c
        split_sizes[best_split] += n

    windowed_df = windowed_df.copy()
    windowed_df["split"] = windowed_df[group_col].map(assignment)

    for split_name, total in split_totals.items():
        if total == 0:
            raise ValueError(f"[ERROR] Invalid split '{split_name}' has 0 real positives.")

    report = pd.Series(split_totals, name="n_positive").to_frame()
    report["n_patients"] = pd.Series(assignment).value_counts()
    return windowed_df, assignment, report


def get_or_compute_labeled_split(windowed_df, label_col, group_col="Patient",
                                include_clean=True, drop_excluded=True, drop_ambiguous=True, 
                                ratios={"train": 0.7, "val": 0.15, "test": 0.15}, seed=42, size_weight=0, 
                                dataset_division_dir="splits", version=1, artifact_umbral=0.7,
                                target="all", forced=None, registry_path=None
                                ):
    
    forced = resolve_forced_split(forced, windowed_df[group_col].unique(), ratios, registry_path)

    current_config = {
        "target_taxonomy": label_col,
        "ratios": ratios,
        "n_windows_total": len(windowed_df),
        "patients": sorted(windowed_df[group_col].unique().tolist()),
        "version": version,
        "size_weight": size_weight,
        "forced": dict(sorted(forced.items())),
        "columns": list(windowed_df.columns),
        "content_hash": int(pd.util.hash_pandas_object(windowed_df[[group_col, label_col]], index=False).sum()),
    }

    saving_dir = Path(dataset_division_dir)
    saving_dir.mkdir(parents=True, exist_ok=True)
    base_name = (
        f"split_train{ratios['train']*100}_val{ratios['val']*100}_test{ratios['test']*100}"
        f"_p{len(sorted(windowed_df[group_col].unique().tolist()))}_v{version}_{target}"
        f"_sw{size_weight}_ua{artifact_umbral}"
    )
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
            return pd.read_parquet(saving_parquet), saved_metadata.get("patient_assignments", {}), pd.DataFrame(saved_metadata.get("split_report", {}))
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
                                                                ratios, seed, size_weight, forced=forced)
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
    channel_cols = [c for c in subset.columns if ("_channels_") in c]
    if exclude_probs:
        iclabel_prob_col = ["ic_iclabel_prob"]
    else:
        iclabel_prob_col = []

    drop_cols = [c for c in leakage_columns + tuar_cols + iclabel_prob_col + channel_cols]
    X = subset.drop(columns=drop_cols)
    y = subset["is_positive"]
    return X, y

# General data splitter functions tests
if __name__ == "__main__":
    import tempfile
    import numpy as np
    from src.core.data_config import LEAKAGE_COLS, RATIOS

    rng = np.random.default_rng(0)
    frames = []
    # Sintetic dataset to test
    for i in range(40):                                   
        n, rate = int(rng.integers(200, 1500)), rng.uniform(0.002, 0.03)
        frames.append(pd.DataFrame({
            "Patient": f"p{i:02d}", "Session": "s001", "Section": "t000",
            "Start": np.arange(n, dtype=float), "ic_index": rng.integers(0, 15, n),
            "ic_raw_label": "brain", "ic_target_label": "clean",
            "is_positive": (rng.random(n) < rate).astype(int),
            "tuar_eye": 0, "tuar_is_ambiguous": 0, "tuar_is_excluded": 0,
            "monopolar_channels_eye": [["FP1"] for _ in range(n)],
            "feat_a": rng.normal(size=n), "feat_b": rng.normal(size=n),
        }))
    df = pd.concat(frames, ignore_index=True)

    # Split per patient
    out, assignment, report = grouped_split_from_labels(df, "is_positive", size_weight=0.5)
    assert (out.groupby("Patient")["split"].nunique() == 1).all(), "one patient is in more than one split"
    print(split_balance_report(out).round(4).to_string())
    dev = (out["split"].value_counts(normalize=True) - pd.Series(RATIOS)).abs().max()
    print(f"Max dev. of size vs RATIOS: {dev:.3f}")

    # Split per feature and target
    X, y = split_features_target(out, "train", LEAKAGE_COLS)
    assert list(X.columns) == ["feat_a", "feat_b"], list(X.columns)
    assert y.sum() == out[out["split"] == "train"]["is_positive"].sum()

    # Saved data into cache
    with tempfile.TemporaryDirectory() as tmp:
        kw = dict(group_col="Patient", ratios=RATIOS, size_weight=0.5,
                  dataset_division_dir=tmp, version=1, target="smoke")
        a, asg_a, _ = get_or_compute_labeled_split(df, "is_positive", **kw)
        b, asg_b, _ = get_or_compute_labeled_split(df, "is_positive", **kw)
        assert asg_a == asg_b and a["split"].reset_index(drop=True).equals(b["split"].reset_index(drop=True))

        df2 = df.copy()
        df2["is_positive"] = rng.permutation(df2["is_positive"].to_numpy())  
        try:
            get_or_compute_labeled_split(df2, "is_positive", **kw)
            print("[INFO] labels changed and loading old split ('content_hash' to current_config)")
        except ValueError:
            print("[OK] Labels change detected")

    # File functions verification
    current_script = Path(__file__).name
    print(f"\n[OK] {current_script}")