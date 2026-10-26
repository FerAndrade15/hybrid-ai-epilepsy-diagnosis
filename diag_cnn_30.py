from IPython.display import display
from pathlib import Path
import pandas as pd

from src.core.data_config import (
    ARTIFACT_KEYWORDS,
    BIPOLAR_MONTAGE,
    WINDOW_REQUESTS_ARTIFACTS,
    SFREQ,
    RATIOS,
    VERSION,
    OUTPUTS_DIR,
    find_project_root,
)
from src.core.data_loader import build_annotations_index
from src.core.windowing import get_or_build_windows
from src.core.data_splitter import get_or_compute_labeled_split, split_balance_report
from src.models.cnn_artifact_detector import binary_cnn
from src.utils.patient_registry import load_registry, forced_for
from src.utils.split_cache import load_selected_sw, save_selected_sw

BASE_DIR = find_project_root("src")
CORPUS_OUTPUTS_DIR = OUTPUTS_DIR / Path("artifact")

ICA_CACHE_DIR = CORPUS_OUTPUTS_DIR / Path("cache/ica")
SESSION_CACHE_DIR = CORPUS_OUTPUTS_DIR / Path("cache/sessions")
WINDOWS_CACHE_DIR = CORPUS_OUTPUTS_DIR / Path("windows")
FEATURES_DIR = CORPUS_OUTPUTS_DIR / Path("features")
DATASET_DIR = CORPUS_OUTPUTS_DIR / Path("dataset")
SPLIT_CACHE_DIR = CORPUS_OUTPUTS_DIR / Path("splits")
ANNOTATIONS_DIR = OUTPUTS_DIR / Path("artifact/annotations")

MODELS_DIR = CORPUS_OUTPUTS_DIR / Path("models")
SPLIT_REGISTRY_PATH = SPLIT_CACHE_DIR / "split_registry.json"

for d in (ICA_CACHE_DIR, SESSION_CACHE_DIR, WINDOWS_CACHE_DIR, FEATURES_DIR, DATASET_DIR, SPLIT_CACHE_DIR, ANNOTATIONS_DIR):
    d.mkdir(parents=True, exist_ok=True)

# [CAMBIO 1] Subimos la capacidad de la red (cambia "standard" por el nombre de tu arquitectura principal si es diferente)
CNN_CONFIG = {
    "eye": {"model_type": "standard", "max_fp_per_day": 50, "epochs": 100},
    "muscle": {"model_type": "standard", "max_fp_per_day": 300, "epochs": 100},
    "non_physiological": {"model_type": "standard", "max_fp_per_day": 1000, "epochs": 100},
}

# [CAMBIO 2] Activamos Focal Loss para ejemplos difíciles (gamma=2.0) manteniendo alpha neutro
FOCAL_PARAMS = {"alpha": 0.5, "gamma": 2.0}
LR = 3e-4

N_CHANNELS = len(BIPOLAR_MONTAGE["names"])

print("\n[PASO 1] Loading ENTIRE dataset to guarantee consistent patient ordering...")
database_corpus_patient = build_annotations_index(
    "artifact",
    n_patients=None,  
    paths=True,
    CACHE_DIR=ANNOTATIONS_DIR,
    refresh=False     # Usamos el caché rápido porque ya lo tienes bien generado
)

print("\n[PASO 2] Sorting alphabetically and filtering first 30 patients (Windows mimic)...")
all_patients = sorted(database_corpus_patient["Patient"].unique())
selected_patients = all_patients[:30]

database_corpus_patient = database_corpus_patient[database_corpus_patient["Patient"].isin(selected_patients)].reset_index(drop=True)

display(database_corpus_patient.head(5))
n_patients = len(database_corpus_patient["Patient"].unique())
print(f"Pacientes reales filtrados para la CNN: {n_patients}")

results = {}
reg = load_registry()
if not reg["patients"]:
    raise RuntimeError("Empty fixed registry, run patient registry first.")
FORCED = forced_for(reg, database_corpus_patient["Patient"].unique(), source_prefix=("folder:", "shared:"))
print("Patient registry allocation counts (Debería ser 12 y 2):", pd.Series(FORCED).value_counts().to_dict())

base_forced = FORCED.copy()

# ==========================================
# CONFIGURACIÓN DE PRUEBA RÁPIDA
TARGET_ARTIFACT = "eye"  
print(f"\n[INFO] Modo de prueba rápida: Solo se procesará el artefacto '{TARGET_ARTIFACT}'")
# ==========================================

for artifact, window_settings in WINDOW_REQUESTS_ARTIFACTS.items():
    if artifact != TARGET_ARTIFACT:
        continue

    print("\n" + "="*50)
    print(f"ARTIFACT: {artifact}")
    print("="*50)

    current_forced = base_forced.copy()

    for i, window in enumerate(window_settings):
        print("*"*50)
        print(f">> {artifact} | windows: {window['window_size_sec']}s ({window['stride_sec']}s stride)")

        windowed_annotations_corpus_patient = get_or_build_windows(
            annotations_df=database_corpus_patient,
            window=window,
            taxonomy=ARTIFACT_KEYWORDS,
            cache_dir=WINDOWS_CACHE_DIR,
            artifact_umbral=window['artifact_umbral'],
            refresh=False # Reutilizamos las ventanas que calculamos exitosamente en el paso anterior
        )

        win_annotations_corpus_patient = windowed_annotations_corpus_patient.loc[
            windowed_annotations_corpus_patient["is_ambiguous"] == 0,
            ["Patient", "Session", "Section", "Start", artifact]
        ].reset_index(drop=True)
        print(f"Windows: {len(windowed_annotations_corpus_patient)} -> without ambiguous: {len(win_annotations_corpus_patient)} | positive: {int(win_annotations_corpus_patient[artifact].sum())}")

        selected_sw = load_selected_sw(SPLIT_REGISTRY_PATH, artifact, window, n_patients, VERSION)

        if selected_sw is None:
            print(f"[WARN] No split found in registry for {artifact} (p={n_patients}). Running size weight sweep...")
            sweep_results = []
            for sw in [0.0, 0.3, 0.5, 0.7, 1.0]:
                candidate_dataset, assignment, report = get_or_compute_labeled_split(
                    windowed_annotations_corpus_patient,
                    label_col=artifact,
                    group_col="Patient",
                    ratios=RATIOS,
                    size_weight=sw,
                    dataset_division_dir=SPLIT_CACHE_DIR,
                    version=VERSION,
                    target=str(artifact),
                    forced=current_forced,
                    artifact_umbral=window['artifact_umbral'],
                    window_size_sec=window['window_size_sec'],
                    stride_sec=window['stride_sec'],
                )
                balance = split_balance_report(candidate_dataset, target_col=artifact)
                spread = balance["positive_rate"].max() - balance["positive_rate"].min()
                size_pct = balance["n_total"] / balance["n_total"].sum()
                size_dev = (size_pct - pd.Series(RATIOS)).abs().max()

                sweep_results.append({
                    "size_weight": sw,
                    "combined_score": spread + size_dev,
                })

            sweep_report = pd.DataFrame(sweep_results).set_index("size_weight")
            selected_sw = sweep_report["combined_score"].idxmin()
            print(f"[INFO] Optimal size weight computed and selected: {selected_sw}")
            save_selected_sw(SPLIT_REGISTRY_PATH, artifact, window, n_patients, VERSION, selected_sw)
        else:
            print(f"[INFO] Best suggested and saved size weight for {artifact}: {selected_sw}")

        splitted_dataset, assignment, report = get_or_compute_labeled_split(
            windowed_annotations_corpus_patient,
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
            print(f"[INFO] Saving patient assignment for {artifact}")
            current_forced.update(assignment)

        balance = split_balance_report(splitted_dataset, target_col=artifact)
        print("[DEBUG] Split balance (positive rate):\n", balance)

        bad = {p: (s, assignment[p]) for p, s in FORCED.items() if p in assignment and assignment[p] != s}
        print("Broken rules:", len(bad), "| splits per patient:", pd.Series(assignment).value_counts().to_dict())

        split_counts = splitted_dataset["split"].value_counts(dropna=False)
        print("[INFO] Split distribution:\n", split_counts)

        print("\n" + "="*50)
        print(f"Starting training of CNN_{artifact}")

        config = CNN_CONFIG[artifact]

        results.setdefault(artifact, []).append(binary_cnn(
            windowed_df=splitted_dataset,
            target_col=artifact,
            model_name=f"diag_cnn_{artifact}_w{window['window_size_sec']}_s{window['stride_sec']}",
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
            lr=LR,
            focal_params=FOCAL_PARAMS,
            checkpoints_dir=str(CORPUS_OUTPUTS_DIR / "checkpoints_diag" / f"{artifact}_w{window['window_size_sec']}_s{window['stride_sec']}"),
        ))

print("\n" + "*-" * 25)
print(f"Final report (n_patients={n_patients})")
for artifact, res_list in results.items():
    print(("-"*10), artifact, ("-"*10))
    for res in res_list:
        print(f"\t\t Threshold: {res['chosen_threshold']:.3f} ({res['chosen_mode']})")
        print(f"\t\t Confusion matrix:\n{res['confusion_matrix']}")
        print(f"\t\t Metrics results: {res['metrics_results']}")
