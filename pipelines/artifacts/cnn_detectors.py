"""
# File: cnn_detectors.py
# Project: Trabajo de graduación
# Author: Maria Fernanda Andrade Recinos

Pipeline to train 1D CNN for each artifact
"""

# pipelines/artifacts/ica_cnn_pipeline.py


from IPython.display import display
from pathlib import Path
import pandas as pd

from src.core.data_config import (  ARTIFACT_KEYWORDS, BIPOLAR_MONTAGE,
                                    WINDOW_REQUESTS_ARTIFACTS, SFREQ,
                                    RATIOS, VERSION, find_project_root,
                                )
from src.core.data_loader import build_annotations_index
from src.core.windowing import get_or_build_windows
from src.core.data_splitter import get_or_compute_labeled_split, split_balance_report
from src.models.cnn_artifact_detector import binary_cnn
from src.utils.patient_registry import load_registry, forced_for

BASE_DIR = find_project_root("src")
CORPUS_OUTPUTS_DIR = BASE_DIR / "outputs" / "artifact"

SESSION_CACHE_DIR = CORPUS_OUTPUTS_DIR / Path("cache/sessions")
WINDOWS_CACHE_DIR = CORPUS_OUTPUTS_DIR / Path("windows")
SPLIT_CACHE_DIR = CORPUS_OUTPUTS_DIR / Path("splits")
ANNOTATIONS_DIR = find_project_root("src") / "outputs" / "artifact" /  "annotations"

MODELS_DIR = CORPUS_OUTPUTS_DIR / Path("models")

for d in (SESSION_CACHE_DIR, WINDOWS_CACHE_DIR, SPLIT_CACHE_DIR, ANNOTATIONS_DIR):
    d.mkdir(parents=True, exist_ok=True)


CNN_CONFIG = {
    "eye": {"model_type": "standard", "max_fp_per_day": 50, "epochs": 100},
    "muscle": {"model_type": "lightweight", "max_fp_per_day": 300, "epochs": 100},
    "non_physiological": {"model_type": "lightweight", "max_fp_per_day": 1000, "epochs": 100},
}

# Configurations for the model according to general settings
N_CHANNELS = len(BIPOLAR_MONTAGE["names"])

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

        splitted_dataset, assignment, report = get_or_compute_labeled_split(  windowed_annotations_corpus_patient, 
                                                                                artifact, 
                                                                                group_col="Patient",
                                                                                ratios=RATIOS,
                                                                                size_weight=selected_sw,        # tendré que dejar un registro json para poder verificar esta categoría para que solo se calcule en rf y ya solo se lea en cnn
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

        split_counts = splitted_dataset["split"].value_counts(dropna=False)
        print("[INFO] Split distribution: ", split_counts)


        print("\n" + ("="*50))
        print(f"Starting training of CNN_{artifact}")

        results.setdefault(artifact, []).append(  train_binary_model(   df=rf_features_dataset,
                                                                        model_name=f"rf_{artifact}_w{window['window_size_sec']}s{window['stride_sec']}_{VERSION}",
                                                                        window_size_sec=window,
                                                                        build_model_fn=build_rf_model,
                                                                        search_data=config["space"],
                                                                        models_dir=str(MODELS_DIR),
                                                                        leakage_cols=LEAKAGE_COLS,
                                                                        search_method="random",
                                                                        search_kwargs={"n_iter": config["n_iter"]},
                                                                        force_retrain=True,
                                                                        balanced=True,
                                                                        max_fp_per_day=config["max_fp_per_day"] 
                                                                    )
                                                 )


        config = CNN_CONFIG[artifact]
        results.setdefault(artifact, []).append( binary_cnn(
                                                            windowed_df_split, target_col=target_col, model_name=f"cnn_{artifact}",
                                                            window_size_sec=window["window_size_sec"], sfreq=SFREQ, n_channels=N_CHANNELS,
                                                            session_cache_dir=str(SESSION_CACHE_DIR), ica_cache_dir=str(ICA_CACHE_DIR),
                                                            models_dir=str(MODELS_DIR), model_type=config["model_type"],
                                                            epochs=config["epochs"], max_fp_per_day=config["max_fp_per_day"],
                                                            force_retrain=True,
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








------


    config = CNN_CONFIG[artifact]
    results[artifact] = binary_cnn(
        windowed_df_split, target_col=target_col, model_name=f"cnn_{artifact}",
        window_size_sec=window["window_size_sec"], sfreq=SFREQ, n_channels=N_CHANNELS,
        session_cache_dir=str(SESSION_CACHE_DIR), ica_cache_dir=str(ICA_CACHE_DIR),
        models_dir=str(MODELS_DIR), model_type=config["model_type"],
        epochs=config["epochs"], max_fp_per_day=config["max_fp_per_day"],
        force_retrain=True,
    )

print("\n" + "=" * 60)
print("RESUMEN FINAL — CNN por artefacto")
for artifact, res in results.items():
    print(f"\n{artifact}:")
    print(f"  Threshold: {res['chosen_threshold']:.3f} ({res['chosen_mode']})")
    print(f"  Métricas: {res['metrics_results']}")