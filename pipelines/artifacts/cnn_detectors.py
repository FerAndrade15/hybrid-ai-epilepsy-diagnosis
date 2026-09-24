"""
# File: cnn_detectors.py
# Project: Trabajo de graduación
# Author: Maria Fernanda Andrade Recinos

Pipeline to train 1D CNN for each artifact
"""
# file: cnn_detectors.py

from IPython.display import display
from pathlib import Path
import pandas as pd

from src.core.data_config import (  ARTIFACT_KEYWORDS, BIPOLAR_MONTAGE,
                                    WINDOW_REQUESTS_ARTIFACTS, SFREQ,
                                    RATIOS, VERSION, OUTPUTS_DIR,
                                    find_project_root,
                                )
from src.core.data_loader import build_annotations_index
from src.core.windowing import get_or_build_windows
from src.core.data_splitter import get_or_compute_labeled_split, split_balance_report
from src.models.cnn_artifact_detector import binary_cnn
from src.utils.patient_registry import load_registry, forced_for
from src.utils.split_cache import load_selected_sw

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

CNN_CONFIG = {
    "eye": {"model_type": "standard", "max_fp_per_day": 50, "epochs": 100},
    "muscle": {"model_type": "lightweight", "max_fp_per_day": 300, "epochs": 100},
    "non_physiological": {"model_type": "lightweight", "max_fp_per_day": 1000, "epochs": 100},
}

# Configurations for the model according to general settings
N_CHANNELS = len(BIPOLAR_MONTAGE["names"])

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
        print(f">> {artifact} | windows: {window['window_size_sec']}s ({window['stride_sec']}s stride)")

        """ ANNOTATIONS WINDOWS """
        print("\n"+("*"*60))
        print("Generating windows...")
        windowed_annotations_corpus_patient = get_or_build_windows( annotations_df=database_corpus_patient, 
                                                                    window=window, 
                                                                    taxonomy=ARTIFACT_KEYWORDS, 
                                                                    cache_dir=WINDOWS_CACHE_DIR,
                                                                    artifact_umbral=window['artifact_umbral'],
                                                                    refresh=False
                                                                )
        display(windowed_annotations_corpus_patient.head(5))
        print(windowed_annotations_corpus_patient.columns.tolist())

        win_annotations_corpus_patient = windowed_annotations_corpus_patient.loc[windowed_annotations_corpus_patient["is_ambiguous"] == 0, ["Patient", "Session", "Section", "Start", artifact]].reset_index(drop=True)
        print(f"Windows: {len(windowed_annotations_corpus_patient)} -> without ambiguous: {len(win_annotations_corpus_patient)} | positive: {int(win_annotations_corpus_patient[artifact].sum())}") 
        #display(win_annotations_corpus_patient.head(25))
        print(win_annotations_corpus_patient.columns.tolist())

        selected_sw = load_selected_sw(SPLIT_REGISTRY_PATH, artifact, window, n_patients, VERSION)

        if selected_sw is None:
            raise ValueError("Not available register, searched at RF models cache files")
            """ SIZE WEIGHT SWEEP 
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
            """

        else:
            print(f"[INFO] Best suggested and saved size weight for {artifact}: {selected_sw}")        

        splitted_dataset, assignment, report = get_or_compute_labeled_split(  windowed_annotations_corpus_patient, 
                                                                                label_col=artifact, 
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

        #display(splitted_dataset.head(10))
        #print(splitted_dataset.columns.to_list())
  
        split_counts = splitted_dataset["split"].value_counts(dropna=False)
        print("[INFO] Split distribution: ", split_counts)

        print("\n" + ("="*50))
        print(f"Starting training of CNN_{artifact}")

        config = CNN_CONFIG[artifact]

        results.setdefault(artifact, []).append( binary_cnn(
                                                            windowed_df=splitted_dataset, 
                                                            target_col=artifact, 
                                                            model_name=f"cnn_{artifact}_w{window['window_size_sec']}_s{window['stride_sec']}",
                                                            window_size_sec=window["window_size_sec"], 
                                                            sfreq=SFREQ, 
                                                            n_channels=N_CHANNELS,
                                                            session_cache_dir=str(SESSION_CACHE_DIR), 
                                                            ica_cache_dir=str(ICA_CACHE_DIR),
                                                            models_dir=str(MODELS_DIR), 
                                                            model_type=config["model_type"],
                                                            epochs=config["epochs"], 
                                                            max_fp_per_day=config["max_fp_per_day"],
                                                            force_retrain=True,
                                                            checkpoints_dir=str(CORPUS_OUTPUTS_DIR / "checkpoints" / f"{artifact}_w{window['window_size_sec']}_s{window['stride_sec']}"),
                                                        )
                                                )

print("\n"+"*-" * 25)
print("Final report")
for artifact, res_list in results.items():
    print(('-'*10), artifact, ('-'*10))
    for res in res_list:
        print(f"\t\t Threshold: {res['chosen_threshold']:.3f} ({res['chosen_mode']})")
        print(f"\t\t Confusion matrix:\n{res['confusion_matrix']}")
        print(f"\t\t Metrics results: {res['metrics_results']}")