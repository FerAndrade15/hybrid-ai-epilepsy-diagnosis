"""
# File: corpus_inventory.py
# Project: Trabajo de graduación
# Author: Maria Fernanda Andrade Recinos

Data distribution according to corpus splits and required divisions for
application of machine learning algorithms.
"""
# corpus_inventory.py

# General imports
import re
import os
import json
import pandas as pd
from pathlib import Path

from src.core.data_config import BASE_PATH, CORPUS_PATHS, PARTITION_TO_SPLIT, DEBUG_DIR

DEFAULT_CORPORA = [ "artifact", 
                    "epilepsy", 
                    "seizure", 
                    #"events", 
                    ]
CACHE_DIR = DEBUG_DIR / "inventory"

def _token(stem, test):
    return next((t for t in stem.split("_") if test(t)), None)

def scan_corpus(corpus_name, refresh=True):
    cache = CACHE_DIR / f"{corpus_name}.parquet"
    if cache.exists() and not refresh:
        return pd.read_parquet(cache)
    
    root = BASE_PATH / CORPUS_PATHS[corpus_name]
    if not root.exists():
        print(f"[INFO] {root} not found")
        return pd.DataFrame()
    
    rows = []
    for dirpath, _, files in os.walk(root):
        names = set(files)
        rel = Path(dirpath).relative_to(root).parts
        for f in files:
            if not f.endswith(".edf"):
                continue
            stem = f[:-4]
            rows.append({
                "corpus": corpus_name,
                "partition": next((p for p in rel if p in PARTITION_TO_SPLIT), ""),
                "top_folder": rel[0] if rel else "",
                "montage": rel[-1] if rel else "",
                "patient": _token(stem, lambda t: len(t) == 8 and t.isalpha()),
                "session": _token(stem, lambda t: t.startswith("s") and t[1:].isdigit()),
                "edf": str(Path(dirpath)/f),
                "has_csv": f"{stem}.csv" in names,
                "has_rec": f"{stem}.rec" in names,
                "has_lab": f"{stem}.lab" in names,
            })
    df = pd.DataFrame(rows)
    if df.empty:
        return df
    df["split"] = df["partition"].map(PARTITION_TO_SPLIT).fillna("no_folder")
    df["annotated"] = df[["has_csv", "has_rec", "has_lab"]].any(axis=1)
    df["session_key"] = df["patient"].astype(str) + "_" + df["session"].astype(str)
    CACHE_DIR.mkdir(parents=True, exist_ok=True)
    df.to_parquet(cache, index=False)
    return df

def scan_all(corpora=DEFAULT_CORPORA, refresh=False):
    frames = [scan_corpus(c, refresh) for c in corpora]
    return pd.concat([f for f in frames if len(f)], ignore_index=True)

def summarize(inv):
    return inv.groupby(["corpus", "split"]).agg(
        n_files = ("edf", "size"),
        n_annotated = ("annotated", "sum"),
        n_patients = ("patient", "nunique"),
        n_sessions = ("session_key", "nunique"),
    )

def patient_overlap(inv):
    sets = {f"{c}/{s}": set(g["patient"].dropna()) for (c,s), g in inv.groupby(["corpus", "split"])}
    keys = sorted(sets)
    return pd.DataFrame([[len(sets[a] & sets[b]) for b in keys] for a in keys], index=keys, columns=keys)

def audit_saved_split(json_path, inv, corpus):
    assignment = json.load(open(json_path))["patient_assignments"]
    mine = pd.DataFrame({"patient":list(assignment), "my_split": list(assignment.values())})
    other = inv[inv["corpus"] != corpus][["patient", "corpus", "split"]].drop_duplicates()
    m = mine.merge(other, on="patient")
    print(f"Patients saved in split: {len(mine)} | Saved in other corpus: {m['patient'].nunique()}")
    if m.empty:
        print("[INFO] No patient matching between splits.")
        return m
    print(f"\nRows = Corpus folder | Columns = Common with {corpus}")
    print(pd.crosstab([m["corpus"], m["split"]], m["my_split"]).to_string())
    return m

def load_tuep_lists(list_dir):
    rows = []
    for name, in_tusz in (("sessions_common_with_tusz.list", True),
                          ("sessions_unique_to_tuep.list", False)):
        for line in (Path(list_dir) / name).read_text().split():
            parts = line.strip().split("/")
            rows.append({"patient": parts[-2], "session": parts[-1].split("_")[0], "in_tusz": in_tusz})
    return pd.DataFrame(rows)

### Run functions
if __name__ == "__main__":
    from src.core.patient_registry import load_registry
    inv = scan_all()

    print("All corpus structure (By folders)")
    print(inv.groupby(["corpus", "top_folder"]).size().to_string())

    print("\n" + ("="*60) + "\n")
    print("Available splits by corpus")
    print(summarize(inv).to_string())

    print("\n" + ("="*60) + "\n")
    print("EDF without parsed patient:", int(inv["patient"].isna().sum()))
    #print(inv[inv["patient"].isna() == True])
    print("EDF without annotations (.csv, .rec or .lab):", int((~inv["annotated"]).sum()))

    # Verification of data extracted according to documentation
    sz = summarize(inv[inv["corpus"] == "seizure"]).droplevel(0) if "seizure" in inv["corpus"].values else None
    if sz is not None:
        print("\nTUSZ according to README -> train 5057/578, dev 2203/53, eval 880/43 (archivos/pacientes)")
        print(sz[["n_files", "n_patients"]].to_string())

    print("\n" + ("="*60) + "\n")
    print("Shared patients accross corpus")
    print(patient_overlap(inv).to_string())

    splits = sorted((DEBUG_DIR.parent / "splits").glob("*.json"))
    print("\n" + ("="*60) + "\n")
    for corpus in DEFAULT_CORPORA:
        if splits:
            print(f"\nRevision of {splits[-1].name} - {corpus}")
            audit_saved_split(splits[-1], inv, corpus)

    print("\n" + ("="*60) + "\n")
    lists = load_tuep_lists("/mnt/d/tuh_eeg/tuh_eeg_epilepsy/v3.1.0/DOCS")
    ep = inv[inv["corpus"] == "epilepsy"].merge(lists, on=["patient", "session"], how="left")
    ep["tuep_class"] = ep["top_folder"].str.split("/").str[0]          # 00_epilepsy / 01_no_epilepsy
    assert ep["in_tusz"].notna().all(), "sesiones del disco que no están en ninguna lista"
    print(ep.groupby(["tuep_class", "in_tusz"])["session_key"].nunique())

    tusz_keys = set(inv.loc[inv["corpus"] == "seizure", "session_key"])
    common_keys = set(ep.loc[ep["in_tusz"], "session_key"])
    print("Common not found in TUSZ:", len(common_keys - tusz_keys))

    tusz_keys = set(inv.loc[inv["corpus"] == "seizure", "session_key"])
    missed = ep[~ep["in_tusz"] & ep["session_key"].isin(tusz_keys)]
    print("TUSZ marked as unique:", len(common_keys - tusz_keys))

    inv = scan_all()
    reg = load_registry()
    ar, ep = (set(inv.loc[inv["corpus"] == c, "patient"].dropna()) for c in ("artifact", "epilepsy"))
    libres = (ar & ep) - set(reg["patients"])
    print("compartidos artifact∩epilepsy:", len(ar & ep), "| sin regla todavía:", len(libres))