"""
# File: _xai.py
# Project: Trabajo de Graduación
#
# Application of explainable methods to the temporal 
# transformer developed and trained by Santiago Sanchez
# as part of a UVG research line.
#
# Required files - Extracted from Sanchez repository:
# sanchez_transformer_final_model.pt        -> Trained weights
# sanchez_transformer_config_used.json      -> Hyperparameters
# sanchez_transformer_feature_scaler.pkl    -> Features normalizer
# sanchez_transformer_model.py              -> Architecture
#
"""
import json
import random
import re
from pathlib import Path
from collections import defaultdict
 
import numpy as np
import pandas as pd
import torch
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
from scipy.stats import spearmanr
 
from src.xai.xai_common import confusion_groups
from src.xai.xai_deep_core import (
    ModelWrapper,
    reduce_logit_of_mean_prob,
    predict_proba,
    occlusion,
)
from src.xai.models.temporal_transformer.sanchez_transformer_utils import (
    load_config,
    validate_config,
)
from src.xai.models.temporal_transformer.sanchez_transformer_pipeline import (
    make_model,
    _transformer_params_from_config,
)
from src.xai.models.temporal_transformer._data.data_extractor import load_dataset
from src.xai.xai_deep_core import (
    explain_ig,
    explain_attn_grad,
    deletion_scores,
)
 
# ----------------------------------------------------------------------------
# Settings
# ----------------------------------------------------------------------------
XAI_OPTIONS = ["ig", "occlusion"]
XAI_METHOD = XAI_OPTIONS[0]
COMPUTE_ABLATION = True
 
BATCH_SIZE = 4
THRESHOLD = 0.5
 
IG_STEPS = 100            # línea base = 0 (features z-score: 0 = media; señal normalizada)
IG_INTERNAL_BS = 25       # baja si te quedas sin memoria
DELTA_REL_TOL = 0.05      # |delta| / |f(x)-f(base)|; sube IG_STEPS si se supera
 
COMPUTE_ATTN = True       # atención×gradiente + fidelidad (solo con XAI_METHOD="ig")
FID_FRACS = (0.1, 0.2, 0.3, 0.5)
 
MAX_PER_GROUP = 300       # tope fijo de ventanas por grupo (VP/FP/VN/FN)
BOOT_N = 2000             # remuestreos bootstrap (sobre PACIENTES)
OCC_WINDOW_SEC = 0.5
BASELINE_VALUE = 0.0
 
FORCE_RECALCULATE = True
PLOT_RESULTS = True
FORCE_REPLOT = False
 
COLOR_POSITIVE = "#0D232F"
COLOR_NEGATIVE = "#6A8BA2"
 
L = {
    "occ_title":   "Oclusión temporal: todos los canales, por bloque de tiempo",
    "ig_cbar":     "IG con signo (línea base = 0)",
    "map_title":   "Tiempo × canal (escala de color propia de esta ventana)",
    "time_title":  "Importancia temporal: IG vs atención×gradiente",
    "channels":    "Canales",
    "features":    "Características (features)",
    "note_signed": "Mediana con signo de las medianas por paciente; barras de error: "
                   "IC95% bootstrap sobre pacientes. Ver top3_freq en los CSV.",
    "pdf_title":   "Resultados",
}
METHOD_LABEL = {"ig": "Gradientes integrados (IG)", "occlusion": "Oclusión"}
GROUP_LABEL = {"TP": "VP", "FP": "FP", "TN": "VN", "FN": "FN"}
 
PLOT_ORIG_IDXS = None     # None: primera de cada grupo; o p. ej. [415, 165, 0, 127]
 
RUN_ID = "sanchez_v2"
settings_tag = f"threshold_{THRESHOLD:g}"
 
CHANNEL_NAMES = [
    "FP1-F7", "F7-T3", "T3-T5", "T5-O1",
    "FP2-F8", "F8-T4", "T4-T6", "T6-O2",
    "A1-T3", "T3-C3", "C3-CZ", "CZ-C4",
    "C4-T4", "T4-A2", "FP1-F3", "F3-C3",
    "C3-P3", "P3-O1", "FP2-F4", "F4-C4",
    "C4-P4", "P4-O2",
]

CHANNEL_GROUPS = {
    "temporal_izq": ["FP1-F7", "F7-T3", "T3-T5", "T5-O1"],
    "temporal_der": ["FP2-F8", "F8-T4", "T4-T6", "T6-O2"],
    "parasag_izq":  ["FP1-F3", "F3-C3", "C3-P3", "P3-O1"],
    "parasag_der":  ["FP2-F4", "F4-C4", "C4-P4", "P4-O2"],
    "central_aur":  ["A1-T3", "T3-C3", "C3-CZ", "CZ-C4", "C4-T4", "T4-A2"],
}
FEATURE_GROUPS = {
    "amplitud":    ["std_eeg", "rms_eeg", "hjorth_activity"],
    "energia":     ["line_length", "tkeo_mean"],
    "pot_relativa": ["bp_rel_delta", "bp_rel_theta", "bp_rel_alpha",
                     "bp_rel_beta", "bp_rel_gamma"],
    "ratios":      ["beta_alpha_ratio", "theta_alpha_ratio"],
    "forma_espec": ["hjorth_mobility", "hjorth_complexity",
                    "spectral_entropy", "sef95"],
}
 
if IG_STEPS < 1 or OCC_WINDOW_SEC <= 0:
    raise ValueError("IG_STEPS y OCC_WINDOW_SEC deben ser positivos.")
 
base_dir = Path(__file__).resolve().parent
DATA_PATH = base_dir / "_data"
 
if XAI_METHOD == "ig":
    settings_tag += f"_joint_steps_{IG_STEPS}_baseline_0"
else:
    settings_tag += f"_window_{OCC_WINDOW_SEC:g}s_baseline_{BASELINE_VALUE:g}"
 
RESULTS_DIR = base_dir / "_results" / RUN_ID / XAI_METHOD / settings_tag
RESULTS_DIR.mkdir(parents=True, exist_ok=True)
 
FEATURES_PATH = RESULTS_DIR / "features.parquet"
CHANNELS_PATH = RESULTS_DIR / "channels.parquet"
SIGNAL_PATH = RESULTS_DIR / "signal.npz"
COMPLETE_PATH = RESULTS_DIR / "completed.json"   # se crea al final
 
PLOTS_DIR = RESULTS_DIR / "plots"
PLOTS_DIR.mkdir(parents=True, exist_ok=True)
 
GROUP_ORDER = ("TP", "FP", "TN", "FN")
 
 
def patient_of(path):
    """ID de paciente a partir de la ruta. AJUSTA a tu convención.
    Por defecto: stem antes del primer '_' (p. ej. 'chb01_03.edf' -> 'chb01')."""
    return re.split(r"_", Path(str(path)).stem)[0]
 
 
def seizure_metrics(ds, gidx, ig_time, fs):
    """Por ventana: fracción dentro de crisis anotada (seiz_frac) y fracción de la
    importancia temporal de IG dentro de ella (seiz_mass). Si seiz_mass >> seiz_frac,
    IG se concentra en la crisis. Claves como en tu bloque original."""
    meta = ds.get("window_metadata")
    frac, mass = [], []
    for g, imp in zip(gidx, ig_time):
        try:
            info = meta[int(g)]
            t = info["start_sec"] + (np.arange(len(imp)) + 0.5) / fs
            m = np.zeros(len(imp), dtype=bool)
            for a in info["seizure_overlaps"]:
                m |= (t >= a["start"]) & (t <= a["stop"])
            tot = imp.sum()
            frac.append(m.mean())
            mass.append(imp[m].sum() / tot if tot > 0 else np.nan)
        except Exception:
            frac.append(np.nan)
            mass.append(np.nan)
    return np.array(frac), np.array(mass)
 
 
def unique_file(directory, pattern):
    matches = sorted(directory.glob(pattern))
    if len(matches) != 1:
        raise ValueError(
            f"Se esperaba un archivo {pattern} en {directory}; "
            f"se encontraron {len(matches)}. Define la ruta explícitamente."
        )
    return matches[0]
 
 
results_exist = all(p.is_file() for p in
                    (FEATURES_PATH, CHANNELS_PATH, SIGNAL_PATH, COMPLETE_PATH))
recalculated = False
attn_all = None          # (N, T) o None
ds = None
 
# ----------------------------------------------------------------------------
# Carga de resultados existentes
# ----------------------------------------------------------------------------
if results_exist and not FORCE_RECALCULATE:
    print(f"Cargando resultados existentes de {XAI_METHOD}...")
    df_features = pd.read_parquet(FEATURES_PATH)
    df_channels = pd.read_parquet(CHANNELS_PATH)
    with np.load(SIGNAL_PATH, allow_pickle=False) as data:
        signal_all = data["values"]
        saved_orig_idxs = data["orig_idx"]
        CHANNEL_NAMES = data["channel_names"].tolist()
        FS = int(data["fs"].item())
        time_edges_sec = data["time_edges_sec"]
        if "attn_time" in data.files:
            attn_all = data["attn_time"]
 
# ----------------------------------------------------------------------------
# Cálculo por lotes
# ----------------------------------------------------------------------------
else:
    COMPLETE_PATH.unlink(missing_ok=True)
 
    CONFIG_PATH = unique_file(base_dir, "*.json")
    MODEL_PATH = unique_file(base_dir, "*.pt")
 
    with open(CONFIG_PATH, encoding="utf-8") as f:
        config = json.load(f)
 
    config_obj = validate_config(load_config(CONFIG_PATH))
    transformer_params = _transformer_params_from_config(config_obj)
 
    FS = int(config["target_fs"])
    N_SAMPLES = int(FS * float(config["window_sec"]))
    FEATURE_NAMES = list(config["selected_features"])
    N_CHANNELS = config.get("n_channels", 22)
 
    DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")
 
    model = make_model(
        model_type=config_obj.model,
        input_shape=(N_SAMPLES, N_CHANNELS),
        feat_dim=len(FEATURE_NAMES),
        num_filters=config_obj.num_filters,
        kernel_size=config_obj.kernel_size,
        dropout_rate=config_obj.dropout,
        rnn_units=config_obj.rnn_units,
        time_step=config_obj.time_step_labels,
        transformer_params=transformer_params,
    ).to(DEVICE)
 
    checkpoint = torch.load(MODEL_PATH, map_location=DEVICE)
    model.load_state_dict(checkpoint.get("state_dict", checkpoint))
    model.eval()
 
    # Atención×gradiente exige el TransformerClassifier parcheado
    HAS_ATTN = (
        XAI_METHOD == "ig" and COMPUTE_ATTN
        and hasattr(model, "blocks") and hasattr(model, "time_step")
    )
    if XAI_METHOD == "ig" and COMPUTE_ATTN and not HAS_ATTN:
        print("⚠ El modelo no expone .blocks/.time_step: se omite atención×gradiente.")
 
    ds = load_dataset(DATA_PATH)
    X_sig_all = torch.as_tensor(ds["windows"], dtype=torch.float32)
    X_feat_all = torch.as_tensor(ds["features"], dtype=torch.float32)
    y_all = np.asarray(ds["labels"]).reshape(-1).astype(int)
 
    n_windows, n_times, n_channels = X_sig_all.shape
    n_features = X_feat_all.shape[1]
 
    assert n_windows > 0
    assert len(X_feat_all) == len(y_all) == n_windows
    assert len(FEATURE_NAMES) == n_features
    assert len(CHANNEL_NAMES) == n_channels
    assert np.isin(y_all, [0, 1]).all()
 
    print("Device:", DEVICE)
    if DEVICE.type == "cuda":
        print("GPU:", torch.cuda.get_device_name(DEVICE))
 
    with torch.no_grad():
        raw = model(X_sig_all[:1].to(DEVICE), X_feat_all[:1].to(DEVICE)).probabilities
    if raw.shape[0] != 1:
        raise ValueError(f"Salida inesperada: {tuple(raw.shape)}.")
 
    random.seed(13)
    torch.manual_seed(13)
 
    # w_z: valor que se EXPLICA (logit de la prob. media). w_p: probabilidad.
    w_z = ModelWrapper(model, output_fn=lambda o: o.logits,
                       activation=None, reduce=reduce_logit_of_mean_prob)
    w_p = ModelWrapper(model, output_fn=lambda o: o.probabilities,
                       activation=None, reduce="mean")
 
    z_all = predict_proba(w_z, (X_sig_all, X_feat_all), batch_size=BATCH_SIZE).reshape(-1)
    p_all = predict_proba(w_p, (X_sig_all, X_feat_all), batch_size=BATCH_SIZE).reshape(-1)
 
    groups = confusion_groups(y_all, p_all, threshold=THRESHOLD)
 
    lengths = []
    print("Evaluación del modelo:")
    for name in GROUP_ORDER:
        print(f"{name}: {len(groups[name])}")
        lengths.append(len(groups[name]))
 
 
    group_all = np.empty(n_windows, dtype="<U2")
    for name, idx in groups.items():
        group_all[idx] = name
 
    paths = np.array(ds["paths"])
    selected_indices = []
    for group_name, idx_list in groups.items():
        if len(idx_list) == 0:
            continue
        idx_by_patient = defaultdict(list)
        for idx in idx_list:
            idx_by_patient[patient_of(paths[idx])].append(idx)
        n_target = min(MAX_PER_GROUP, len(idx_list))
        per_patient = max(1, n_target // len(idx_by_patient))
        print(f"{group_name}: {len(idx_by_patient)} pacientes, "
              f"<= {per_patient} ventanas/paciente")
        for p_indices in idx_by_patient.values():
            selected_indices.extend(
                random.sample(p_indices, min(per_patient, len(p_indices))))
 
    sel = np.sort(np.unique(selected_indices))
    X_sig, X_feat = X_sig_all[sel], X_feat_all[sel]
    y_true, probs, logits = y_all[sel], p_all[sel], z_all[sel]
    group_all_sel = group_all[sel]
    orig_idx = sel
    n_windows = len(sel)
    print(f"Dataset reducido por muestreo estratificado (por paciente) a {n_windows} ventanas.")
 
    f = ds["features"]
    print("Media features:", np.round(f.mean(0), 2))
    print("Std features:  ", np.round(f.std(0), 2))   # ~0 y ~1 si están en z-score

    DO_ABL = XAI_METHOD == "occlusion" and COMPUTE_ABLATION
    if DO_ABL:
        ch_idx = {n: i for i, n in enumerate(CHANNEL_NAMES)}
        ch_groups = {k: [ch_idx[n] for n in v] for k, v in CHANNEL_GROUPS.items()}
        ft_groups = {k: [FEATURE_NAMES.index(n) for n in v] for k, v in FEATURE_GROUPS.items()}
        all_ch, all_ft = list(range(n_channels)), list(range(n_features))

        # media interictal por paciente (features); si no hay ventanas interictales, cae a 0
        pat_all = np.array([patient_of(p) for p in paths])
        F_np = X_feat_all.numpy()
        inter = {}
        for p in np.unique(pat_all):
            m = (pat_all == p) & (y_all == 0)
            inter[p] = F_np[m].mean(0) if m.any() else np.zeros(F_np.shape[1])
        feat_inter_sel = torch.as_tensor(
            np.stack([inter[p] for p in pat_all[sel]]), dtype=torch.float32)

        def run_ablation(xs, xf, fi, base):
            """Caída del logit = f(x) - f(x ablacionado). Positivo: lo ablacionado empujaba hacia crisis."""
            def drop(ch=None, ft=None, use_inter=False):
                s, f_ = xs.clone(), xf.clone()
                if ch is not None:
                    s[:, :, ch] = BASELINE_VALUE
                if ft is not None:
                    f_[:, ft] = fi[:, ft] if use_inter else BASELINE_VALUE
                out = predict_proba(w_z, (s, f_), batch_size=BATCH_SIZE)
                return base - np.asarray(out).reshape(-1)

            r = {
                "abl_branch_signal":         drop(ch=all_ch),
                "abl_branch_features":       drop(ft=all_ft),
                "abl_branch_features_inter": drop(ft=all_ft, use_inter=True),
                "abl_both":                  drop(ch=all_ch, ft=all_ft),
            }
            for k, v in ch_groups.items():
                r[f"abl_ch__{k}"] = drop(ch=v)
            for k, v in ft_groups.items():
                r[f"abl_ft__{k}"] = drop(ft=v)
                r[f"abl_ft_inter__{k}"] = drop(ft=v, use_inter=True)
            return r
 
    if XAI_METHOD == "occlusion":
        occ_window = max(1, round(OCC_WINDOW_SEC * FS))
        time_edges_sec = np.append(np.arange(0, n_times, occ_window), n_times) / FS
        signal_all = np.empty((n_windows, len(time_edges_sec) - 1), dtype=np.float32)
    else:
        time_edges_sec = np.arange(n_times + 1) / FS
        signal_all = np.empty((n_windows, n_times, n_channels), dtype=np.float32)
        if HAS_ATTN:
            attn_all = np.empty((n_windows, n_times), dtype=np.float32)
 
    feature_cols = [f"{XAI_METHOD}_feature__{n}" for n in FEATURE_NAMES]
    channel_cols = [f"{XAI_METHOD}_channel__{n}" for n in CHANNEL_NAMES]
    feature_batches, channel_batches = [], []
 
    for start in range(0, n_windows, BATCH_SIZE):
        end = min(start + BATCH_SIZE, n_windows)
        inputs = (X_sig[start:end], X_feat[start:end])
        batch_probs = probs[start:end]
        batch_groups = group_all_sel[start:end]
        extra = {}                         # columnas extra por ventana

        if DO_ABL:
            extra.update(run_ablation(X_sig[start:end], X_feat[start:end],
                                      feat_inter_sel[start:end], logits[start:end]))

        if XAI_METHOD == "ig":
            x_b = X_sig[start:end].to(DEVICE)
            f_b = X_feat[start:end].to(DEVICE)
 
            # --- IG conjunto: (señal, features) en una sola integral ---
            res = explain_ig(w_z, x_b, f_b, n_steps=IG_STEPS,
                             internal_bs=IG_INTERNAL_BS)
            batch_signal = res["attr_x"].cpu().numpy()          # (B,T,C)
            batch_features = res["attr_feat"].cpu().numpy()     # (B,F)
            batch_channels = batch_signal.sum(axis=1)           # suma temporal con signo
 
            delta = res["delta"].cpu().numpy()
            gap = res["gap"].cpu().numpy()
            rel_delta = np.abs(delta) / np.maximum(np.abs(gap), 1e-3)
            extra["ig_delta"] = delta
            extra["ig_gap"] = gap
            extra["ig_rel_delta"] = rel_delta
            if rel_delta.max() > DELTA_REL_TOL:
                print(f"⚠ IG no converge en el lote {start}:{end} "
                      f"(delta rel. máx={rel_delta.max():.3f}): sube IG_STEPS")
 
            # --- Atención×gradiente + fidelidad ---
            ig_time = np.abs(batch_signal).sum(axis=2)          # (B,T)
            sf, sm = seizure_metrics(ds, orig_idx[start:end], ig_time, FS)
            extra['seiz_frac'] = sf
            extra['seiz_mass'] = sm
            if HAS_ATTN:
                am = explain_attn_grad(model, w_z, x_b, f_b)    # (B,T)
                attn_all[start:end] = am.cpu().numpy()
 
            fid = defaultdict(list)
            for j in range(end - start):
                xj, fj = x_b[j:j + 1], f_b[j:j + 1]
                d_ig, d_rnd = deletion_scores(
                    w_z, xj, fj, torch.as_tensor(ig_time[j]), FID_FRACS)
                fid["del_ig"].append(d_ig)
                fid["del_rand"].append(d_rnd)
                if HAS_ATTN:
                    d_at, _ = deletion_scores(w_z, xj, fj, am[j], FID_FRACS)
                    fid["del_attn"].append(d_at)
                    fid["rho_attn_ig"].append(
                        spearmanr(ig_time[j], am[j].cpu().numpy()).correlation)
            extra.update({k: np.asarray(v) for k, v in fid.items()})
 
            check = [batch_probs, batch_signal, batch_features, batch_channels, delta]
 
        elif XAI_METHOD == "occlusion":  # oclusión (referencia agnóstica al modelo)
            batch_features, _ = occlusion(
                w_z, inputs, explain_idx=1, axis=1, window=1,
                baseline_value=BASELINE_VALUE)
            batch_channels, _ = occlusion(
                w_z, inputs, explain_idx=0, axis=2, window=1,
                baseline_value=BASELINE_VALUE)
            batch_signal, _ = occlusion(
                w_z, inputs, explain_idx=0, axis=1, window=occ_window,
                baseline_value=BASELINE_VALUE)
            check = [batch_probs, batch_signal, batch_features, batch_channels]
 
        if not all(np.isfinite(a).all() for a in check):
            raise ValueError(f"NaN o infinitos en el lote {start}:{end}.")
 
        signal_all[start:end] = batch_signal
 
        idx = orig_idx[start:end]
        metadata = pd.DataFrame({
            "orig_idx": idx,
            "y_true": y_true[start:end],
            "y_pred": (batch_probs >= THRESHOLD).astype(int),
            "prob_crisis": batch_probs,
            "group": batch_groups,
            "threshold": THRESHOLD,
            "logit": logits[start:end],
            "source_file": paths[idx],
            "patient": [patient_of(q) for q in paths[idx]],
        })
        times = np.asarray(ds["times"])[idx]
        metadata["start_sec"] = times[:, 0]
        metadata["end_sec"] = times[:, 1]
        for k, v in extra.items():
            metadata[k] = v
 
        feature_batches.append(pd.concat(
            [metadata, pd.DataFrame(batch_features, columns=feature_cols)], axis=1))
        channel_batches.append(pd.concat(
            [metadata, pd.DataFrame(batch_channels, columns=channel_cols)], axis=1))
 
        if start == 0 or end % 100 == 0 or end == n_windows:
            print(f"{XAI_METHOD}: {end}/{n_windows} ventanas")
 
    df_features = pd.concat(feature_batches, ignore_index=True)
    df_channels = pd.concat(channel_batches, ignore_index=True)
    # Los IDs guardados son los ÍNDICES ORIGINALES (coinciden con df['orig_idx'])
    saved_orig_idxs = orig_idx.copy()
 
    df_features.to_parquet(FEATURES_PATH, index=False)
    df_channels.to_parquet(CHANNELS_PATH, index=False)
 
    save_kwargs = dict(
        values=signal_all,
        orig_idx=saved_orig_idxs,
        channel_names=np.asarray(CHANNEL_NAMES, dtype=str),
        feature_names=np.asarray(FEATURE_NAMES, dtype=str),
        fs=np.asarray(FS),
        time_edges_sec=time_edges_sec,
        method=np.asarray(XAI_METHOD),
    )
    if attn_all is not None:
        save_kwargs["attn_time"] = attn_all
    np.savez_compressed(SIGNAL_PATH, **save_kwargs)
 
    COMPLETE_PATH.write_text(json.dumps({
        "run_id": RUN_ID,
        "method": XAI_METHOD,
        "threshold": THRESHOLD,
        "ig_steps": IG_STEPS if XAI_METHOD == "ig" else None,
        "ig_joint": XAI_METHOD == "ig",
        "baseline": 0.0 if XAI_METHOD == "ig" else BASELINE_VALUE,
        "occlusion_window_sec": OCC_WINDOW_SEC if XAI_METHOD == "occlusion" else None,
        "attn_grad": attn_all is not None,
        "model_path": str(MODEL_PATH),
        "config_path": str(CONFIG_PATH),
        "dataset_path": str(DATA_PATH),
        "output": "logits; reduce=logit of mean prob",
    }, indent=2), encoding="utf-8")
 
    recalculated = True
    print("Resultados guardados:", RESULTS_DIR)
                                          
# ----------------------------------------------------------------------------
# Tablas y validación
# ----------------------------------------------------------------------------
feature_prefix = f"{XAI_METHOD}_feature__"
channel_prefix = f"{XAI_METHOD}_channel__"
feature_cols = [c for c in df_features.columns if c.startswith(feature_prefix)]
channel_cols = [c for c in df_channels.columns if c.startswith(channel_prefix)]
feature_names = [c.removeprefix(feature_prefix) for c in feature_cols]
channel_names_table = [c.removeprefix(channel_prefix) for c in channel_cols]
 
if not feature_cols or not channel_cols:
    raise ValueError("Faltan columnas de resultados.")
if (not df_features["orig_idx"].is_unique or not df_channels["orig_idx"].is_unique
        or len(np.unique(saved_orig_idxs)) != len(saved_orig_idxs)):
    raise ValueError("Se encontraron IDs de ventana duplicados.")
if not (set(df_features["orig_idx"]) == set(df_channels["orig_idx"])
        == set(saved_orig_idxs)):
    raise ValueError("Los archivos no contienen las mismas ventanas.")
 
for _df in (df_features, df_channels):
    if "patient" not in _df.columns:
        _df["patient"] = _df["source_file"].map(patient_of)
 
features_by_id = df_features.set_index("orig_idx")
channels_by_id = df_channels.set_index("orig_idx")
map_positions = {int(o): pos for pos, o in enumerate(saved_orig_idxs)}
 
# Fidelidad: ¿IG es mejor que el azar? ¿entra atención×gradiente?
fid_cols = [c for c in ("rho_attn_ig", "del_ig", "del_attn", "del_rand")
            if c in df_features.columns]
if XAI_METHOD == "ig" and fid_cols:
    print("\nFidelidad por grupo (caída media del logit al anular lo 'importante'):")
    print(df_features.groupby("group")[fid_cols].mean().round(3))
    tp = df_features[df_features["group"] == "TP"]
    ref = tp if len(tp) else df_features
    m = ref[fid_cols].mean()
    print(f"\nVentanas de referencia: {'TP' if len(tp) else 'todas'} ({len(ref)})")
    print(f"IG supera al azar: {m['del_ig'] > m['del_rand']}  "
          f"({m['del_ig']:.3f} vs {m['del_rand']:.3f})")
    if "del_attn" in m:
        ok = (m["rho_attn_ig"] > 0.5) and (m["del_attn"] >= 0.8 * m["del_ig"])
        print(f"Atención×grad vs IG: rho={m['rho_attn_ig']:.2f}, "
              f"deleción {m['del_attn']:.3f} vs {m['del_ig']:.3f} -> "
              f"{'candidato válido' if ok else 'NO usar'} (umbrales orientativos)")
    print(f"IG delta relativo máx: {df_features['ig_rel_delta'].max():.3f}\n")
 
if "seiz_mass" in df_features.columns:
    if df_features["seiz_mass"].isna().all():
        print("⚠ seiz_mass vacío: revisa las claves de window_metadata en seizure_metrics.")
    else:
        print("Solapamiento con crisis anotada (seiz_mass: fracción de la importancia de "
              "IG dentro de la crisis; seiz_frac: lo esperable al azar):")
        print(df_features.groupby("group")[["seiz_frac", "seiz_mass"]].mean().round(3))
        pos = df_features[(df_features["group"] == "TP") & (df_features["seiz_frac"] > 0)]
        if len(pos):
            lift = (pos["seiz_mass"] / pos["seiz_frac"]).groupby(pos["patient"]).median()
            print(f"TP: lift mediano por paciente = {lift.median():.2f} "
                  f"(>1: IG se concentra en la crisis; n={len(lift)} pacientes)\n")
 
if XAI_METHOD == "ig":
    channel_label = "Suma temporal de IG con signo"
    feature_label = "Atribución IG con signo"
else:
    channel_label = "Δ logit (original − canal ocluido)"
    feature_label = "Δ logit (original − feature ocluida)"
    
abl_cols = [c for c in df_features.columns if c.startswith("abl_")]
if abl_cols:
    per_patient = df_features.groupby(["group", "patient"])[abl_cols].median()
    summ = per_patient.groupby("group").median().round(3).T
    print("\nAblación (caída del logit, mediana por paciente y luego entre pacientes):")
    print(summ)
    per_patient.to_csv(RESULTS_DIR / "ablation_by_patient.csv")
    summ.to_csv(RESULTS_DIR / "ablation_summary.csv")

    if XAI_METHOD == "occlusion":
        red = pd.DataFrame({
            "ablacion_rama_features": df_features["abl_branch_features"],
            "suma_oclusiones": df_features[feature_cols].sum(axis=1),
        }).groupby(df_features["group"]).median().round(3)
        print("\nRedundancia (ablación completa vs suma de oclusiones individuales):")
        print(red)
 
# ----------------------------------------------------------------------------
# Figuras
# ----------------------------------------------------------------------------
def plot_bars(ax, values, names, title, xlabel, ci=None):
    values = np.asarray(values, dtype=float)
    order = np.argsort(np.abs(values))[::-1]
    colors = [COLOR_POSITIVE if v >= 0 else COLOR_NEGATIVE for v in values[order]]
    xerr = None
    if ci is not None:
        lo, hi = np.asarray(ci[0])[order], np.asarray(ci[1])[order]
        xerr = [np.clip(values[order] - lo, 0, None), np.clip(hi - values[order], 0, None)]
    ax.barh(np.arange(len(values)), values[order], color=colors, xerr=xerr,
            ecolor="0.3", capsize=2)
    ax.set_yticks(np.arange(len(values)))
    ax.set_yticklabels([names[j] for j in order], fontsize=8)
    ax.invert_yaxis()
    ax.axvline(0, color="0.4", linewidth=0.7)
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.ticklabel_format(axis="x", style="sci", scilimits=(0, 0))
 
 
def make_window_figure(orig_idx):
    row = features_by_id.loc[orig_idx]
    channel_row = channels_by_id.loc[orig_idx]
    pos = map_positions[orig_idx]
    values = signal_all[pos]
    show_attn = XAI_METHOD == "ig" and attn_all is not None
 
    fig = plt.figure(figsize=(16, 13 if show_attn else 11), constrained_layout=True)
    if show_attn:
        grid = fig.add_gridspec(3, 2, height_ratios=[2.2, 1.2, 2])
        ax_signal = fig.add_subplot(grid[0, :])
        ax_time = fig.add_subplot(grid[1, :], sharex=ax_signal)
        ax_channels = fig.add_subplot(grid[2, 0])
        ax_features = fig.add_subplot(grid[2, 1])
    else:
        grid = fig.add_gridspec(2, 2)
        ax_signal = fig.add_subplot(grid[0, :])
        ax_channels = fig.add_subplot(grid[1, 0])
        ax_features = fig.add_subplot(grid[1, 1])
 
    if XAI_METHOD == "occlusion":
        ax_signal.bar(
            time_edges_sec[:-1], values, width=np.diff(time_edges_sec),
            align="edge",
            color=np.where(values >= 0, "firebrick", "steelblue"),
            edgecolor="white")
        ax_signal.axhline(0, color="0.4", linewidth=0.7)
        ax_signal.set_ylabel("z(original) − z(bloque ocultado)")
        ax_signal.set_title(L["occ_title"])
    else:
        limit = float(np.abs(values).max()) or 1.0
        image = ax_signal.imshow(
            values.T, origin="lower", aspect="auto", interpolation="nearest",
            extent=[0, values.shape[0] / FS, -0.5, values.shape[1] - 0.5],
            cmap="RdBu_r", vmin=-limit, vmax=limit, rasterized=True)
        ax_signal.set_yticks(np.arange(len(CHANNEL_NAMES)))
        ax_signal.set_yticklabels(CHANNEL_NAMES, fontsize=8)
        ax_signal.set_title(L["map_title"])
        fig.colorbar(image, ax=ax_signal, label=L["ig_cbar"], pad=0.01)
 
    if show_attn:
        t = np.arange(values.shape[0]) / FS
        ig_t = np.abs(values).sum(axis=1)
        ig_t = ig_t / max(ig_t.max(), 1e-8)
        ax_time.plot(t, ig_t, color=COLOR_POSITIVE, label="IG |atribución|")
        ax_time.plot(t, attn_all[pos], color="firebrick", alpha=0.8,
                     label="Atención×gradiente")
        rho = row.get("rho_attn_ig", np.nan)
        ax_time.set_title(f"{L['time_title']}  (ρ Spearman = {rho:.2f})")
        ax_time.set_ylabel("importancia (norm.)")
        ax_time.legend(loc="upper right")
        ax_time.set_xlabel("Tiempo dentro de la ventana (s)")
    else:
        ax_signal.set_xlabel("Tiempo dentro de la ventana (s)")
 
    plot_bars(ax_channels, channel_row[channel_cols].to_numpy(dtype=float),
              channel_names_table, L["channels"], channel_label)
    plot_bars(ax_features, row[feature_cols].to_numpy(dtype=float),
              feature_names, L["features"], feature_label)
 
    title = (
        f"{METHOD_LABEL[XAI_METHOD]} | Ventana {orig_idx} | "
        f"{GROUP_LABEL[row['group']]} | "
        f"Real={int(row['y_true'])} | Predicción={int(row['y_pred'])}\n"
        f"P(crisis)={row['prob_crisis']:.6g} | Umbral={row['threshold']:g}"
    )
    if XAI_METHOD == "ig":
        title += (f"\nDelta IG={row['ig_delta']:.2e} "
                  f"(relativo={row['ig_rel_delta']:.3f})")
    fig.suptitle(title, fontsize=12)
    return fig
 
 
def boot_ci(mat, n=BOOT_N, seed=0):
    """mat: (pacientes, variables). Mediana entre pacientes e IC95% bootstrap."""
    rng = np.random.default_rng(seed)
    k = mat.shape[0]
    meds = np.stack([np.median(mat[rng.integers(0, k, k)], axis=0) for _ in range(n)])
    return (np.median(mat, axis=0), np.percentile(meds, 2.5, axis=0),
            np.percentile(meds, 97.5, axis=0))
 
 
def top3_freq(d, cols):
    """Frecuencia con que cada variable está entre las 3 de mayor |atribución|
    (por paciente y luego media entre pacientes). No depende del signo."""
    vals = d[cols].abs().to_numpy()
    hit = np.zeros_like(vals)
    np.put_along_axis(hit, np.argsort(-vals, axis=1)[:, :3], 1, axis=1)
    return pd.DataFrame(hit, index=d.index).groupby(d["patient"]).mean().mean(0).to_numpy()
 
 
def group_summary(df, group_name, cols, names):
    d = df[df["group"] == group_name]
    mat = d.groupby("patient")[cols].median().to_numpy()      # un valor por paciente
    med, lo, hi = boot_ci(mat)
    table = pd.DataFrame({"median": med, "ci_lo": lo, "ci_hi": hi,
                          "top3_freq": top3_freq(d, cols)}, index=names)
    return table, mat.shape[0], len(d)
 
 
def make_group_figure(group_name):
    ch_t, n_pat, n_win = group_summary(df_channels, group_name, channel_cols,
                                       channel_names_table)
    ft_t, _, _ = group_summary(df_features, group_name, feature_cols, feature_names)
    ch_t.to_csv(RESULTS_DIR / f"summary_channels_{group_name}.csv")
    ft_t.to_csv(RESULTS_DIR / f"summary_features_{group_name}.csv")
 
    fig, axes = plt.subplots(1, 2, figsize=(16, 9), constrained_layout=True)
    plot_bars(axes[0], ch_t["median"], channel_names_table, L["channels"],
              channel_label, ci=(ch_t["ci_lo"], ch_t["ci_hi"]))
    plot_bars(axes[1], ft_t["median"], feature_names, L["features"],
              feature_label, ci=(ft_t["ci_lo"], ft_t["ci_hi"]))
    fig.suptitle(
        f"{METHOD_LABEL[XAI_METHOD]} | {GROUP_LABEL[group_name]} | "
        f"{n_win} ventanas, {n_pat} pacientes\n{L['note_signed']}", fontsize=12)
    return fig
 
 
if PLOT_RESULTS:
    if PLOT_ORIG_IDXS is None:
        selected_ids = []
        for group in GROUP_ORDER:
            cand = df_features.loc[df_features["group"] == group, "orig_idx"]
            if not cand.empty:
                selected_ids.append(int(cand.iloc[0]))
        selection_tag = "first_per_group"
    else:
        selected_ids = list(dict.fromkeys(int(i) for i in PLOT_ORIG_IDXS))
        selection_tag = "windows_" + "_".join(map(str, selected_ids))
 
    for o in selected_ids:
        if o not in map_positions:
            raise ValueError(f"No existe la ventana {o}.")
 
    jobs = [("window", o, PLOTS_DIR / f"{XAI_METHOD}_window_{o}.pdf")
            for o in selected_ids]
    for group in GROUP_ORDER:
        if (df_features["group"] == group).any():
            jobs.append(("group", group, PLOTS_DIR / f"{XAI_METHOD}_group_{group}.pdf"))
 
    report_path = PLOTS_DIR / f"{XAI_METHOD}_report_{selection_tag}.pdf"
    regenerate = FORCE_REPLOT or recalculated
    create_report = regenerate or not report_path.is_file()
 
    def render_job(kind, value):
        return make_window_figure(value) if kind == "window" else make_group_figure(value)
 
    if create_report:
        with PdfPages(report_path) as pdf:
            pdf.infodict()["Title"] = f"{L['pdf_title']} {METHOD_LABEL[XAI_METHOD]}"
            for kind, value, individual_path in jobs:
                fig = render_job(kind, value)
                if regenerate or not individual_path.is_file():
                    fig.savefig(individual_path, dpi=180)
                pdf.savefig(fig, dpi=180)
                plt.close(fig)
        print("Informe PDF guardado:", report_path)
    else:
        for kind, value, individual_path in jobs:
            if not individual_path.is_file():
                fig = render_job(kind, value)
                fig.savefig(individual_path, dpi=180)
                plt.close(fig)
        print("PDFs existentes.")
    print("Figuras individuales:", PLOTS_DIR.resolve())
 
# ----------------------------------------------------------------------------
# Solapamiento con crisis anotadas (solo tras un cálculo nuevo; claves por ajustar)
# ----------------------------------------------------------------------------
CORRELATION = False
if CORRELATION and ds is not None:
    meta = ds["window_metadata"]
    rows = []
    for _, r in df_features[["orig_idx", "group", "logit"]].iterrows():
        info = meta[int(r.orig_idx)]
        w0, w1 = info["start_sec"], info["end_sec"]
        ov = sum(max(0.0, min(w1, a["stop"]) - max(w0, a["start"]))   # AJUSTA claves
                 for a in info["seizure_overlaps"])
        rows.append({**r.to_dict(), "overlap_frac": ov / (w1 - w0),
                     "file": info["source_file"]})
    df_ov = pd.DataFrame(rows)
    print(df_ov.groupby("group")["overlap_frac"].describe())
    print(df_ov.groupby("group")["file"].nunique())

# ----------------------------------------------------------------------------
# Z Score
# ----------------------------------------------------------------------------
if ds is None:                                   # resultados cargados de disco
    ds = load_dataset(DATA_PATH)
Z = np.asarray(ds["features"])[df_features["orig_idx"].to_numpy()]   # (N, F), mismo orden que df_features
A = df_features[feature_cols].to_numpy()                             # (N, F)

def direction_table(df, A, Z, names):
    """Spearman(z, atribución) por feature, mediana entre pacientes.
    >0: más valor de la feature empuja hacia crisis; <0: al revés; ~0: no monótono."""
    rows = {}
    for p, ix in df.groupby("patient").indices.items():
        if len(ix) < 10:
            continue
        rows[p] = [spearmanr(Z[ix, j], A[ix, j]).correlation for j in range(A.shape[1])]
    t = pd.DataFrame(rows, index=names).T
    return pd.DataFrame({"rho_median": t.median(), "n_patients": t.notna().sum(),
                         "mean_abs_attr": np.abs(A).mean(0)}, index=names)

def plot_beeswarm(A, Z, names, title, top=15, path=None):
    order = np.argsort(np.abs(A).mean(0))[-top:]
    fig, ax = plt.subplots(figsize=(8, 0.4 * top + 2))
    rng = np.random.default_rng(0)
    for row, j in enumerate(order):
        sc = ax.scatter(A[:, j], row + rng.uniform(-.25, .25, len(A)),
                        c=np.clip(Z[:, j], -3, 3), cmap="coolwarm", vmin=-3, vmax=3, s=6, alpha=.6)
    ax.set_yticks(range(top)); ax.set_yticklabels([names[j] for j in order], fontsize=8)
    ax.axvline(0, color="0.4", lw=.7)
    ax.set_xlabel(feature_label); ax.set_title(title)
    fig.colorbar(sc, ax=ax, label="z de la feature")
    if path: fig.savefig(path, dpi=180)
    plt.close(fig)

for g in GROUP_ORDER:
    m = (df_features["group"] == g).to_numpy()
    if m.sum() < 10:
        continue
    plot_beeswarm(A[m], Z[m], feature_names,
                  f"{METHOD_LABEL[XAI_METHOD]} | {GROUP_LABEL[g]} | {m.sum()} ventanas",
                  path=PLOTS_DIR / f"{XAI_METHOD}_beeswarm_{g}.pdf")
    direction_table(df_features[m].reset_index(drop=True), A[m], Z[m], feature_names)\
        .to_csv(RESULTS_DIR / f"direction_features_{g}.csv")




"""General purpose models (under verification) ------------------------------------------------------------------------
import json
import random
from pathlib import Path
from collections import defaultdict

import numpy as np
import pandas as pd
import torch
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

from src.xai.xai_common import confusion_groups
from src.xai.xai_deep_core import (
    ModelWrapper,
    reduce_logit_of_mean_prob,
    predict_proba,
    saliency,
    integrated_gradients,
    occlusion,
)

from src.xai.models.temporal_transformer.sanchez_transformer_utils import (
    load_config,
    validate_config,
)
from src.xai.models.temporal_transformer.sanchez_transformer_pipeline import (
    make_model,
    _transformer_params_from_config,
)
from src.xai.models.temporal_transformer._data.data_extractor import (
    load_dataset,
)

# Settings
XAI_OPTIONS = ["occlusion", "ig"] # Saliency discarted for transformers
XAI_METHOD = XAI_OPTIONS[0]

BATCH_SIZE = 4
THRESHOLD = 0.5

IG_STEPS = 100      # IG implementations with zero baseline

# Temporal data and sustitution value
SAMPLE_FRACTION = 0.20
OCC_WINDOW_SEC = 0.5
BASELINE_VALUE = 0.0

FORCE_RECALCULATE = False
PLOT_RESULTS = True
FORCE_REPLOT = False

# Visualization settings
COLOR_POSITIVE = "#0D232F"
COLOR_NEGATIVE = "#6A8BA2"
COLOR_SALIENCY = "#193F61"

# Labels
L = {
    "occ_title":   "Oclusión temporal: todos los canales, por bloque de tiempo",
    "ig_cbar":     "IG con signo (línea base = 0)",
    "map_title":   "Tiempo × canal (escala de color propia de esta ventana)",
    "channels":    "Canales",
    "features":    "Características (features)",
    "delta_sig":   "Delta señal",
    "delta_feat":  "Delta características",
    "note_sal":    "Sensibilidad absoluta; los canales y features tienen escalas distintas.",
    "note_signed": "Mediana con signo sobre las ventanas seleccionadas; "
                    "no muestra la dispersión ni todos los efectos individuales.",
    "pdf_title":   "Resultados",
}
METHOD_LABEL = {"saliency": "Saliencia", "ig": "Gradientes integrados (IG)", "occlusion": "Oclusión"}
GROUP_LABEL  = {"TP": "VP", "FP": "FP", "TN": "VN", "FN": "FN"} 

PLOT_ORIG_IDXS = None
# None: First found, it can be selecte as [415, 165, 0, 127]

RUN_ID = "sanchez_v1"
settings_tag = f"threshold_{THRESHOLD:g}"

CHANNEL_NAMES = [
    "FP1-F7", "F7-T3", "T3-T5", "T5-O1",
    "FP2-F8", "F8-T4", "T4-T6", "T6-O2",
    "A1-T3", "T3-C3", "C3-CZ", "CZ-C4",
    "C4-T4", "T4-A2", "FP1-F3", "F3-C3",
    "C3-P3", "P3-O1", "FP2-F4", "F4-C4",
    "C4-P4", "P4-O2",
]

if IG_STEPS < 1 or OCC_WINDOW_SEC <= 0:
    raise ValueError("IG_STEPS y OCC_WINDOW_SEC must be positive.")

base_dir = Path(__file__).resolve().parent
DATA_PATH = base_dir / "_data"

if XAI_METHOD == "ig":
    settings_tag += f"_steps_{IG_STEPS}_baseline_0"
elif XAI_METHOD == "occlusion":
    settings_tag += (
        f"_window_{OCC_WINDOW_SEC:g}s"
        f"_baseline_{BASELINE_VALUE:g}"
    )

RESULTS_DIR = (
    base_dir / "_results" / RUN_ID / XAI_METHOD / settings_tag
)
RESULTS_DIR.mkdir(parents=True, exist_ok=True)

FEATURES_PATH = RESULTS_DIR / "features.parquet"
CHANNELS_PATH = RESULTS_DIR / "channels.parquet"
SIGNAL_PATH = RESULTS_DIR / "signal.npz"

# Created at the end
COMPLETE_PATH = RESULTS_DIR / "completed.json"

PLOTS_DIR = RESULTS_DIR / "plots"
PLOTS_DIR.mkdir(parents=True, exist_ok=True)

GROUP_ORDER = ("TP", "FP", "TN", "FN")

def unique_file(directory, pattern):
    matches = sorted(directory.glob(pattern))
    if len(matches) != 1:
        raise ValueError(
            f"Se esperaba un archivo {pattern} en {directory}; "
            f"se encontraron {len(matches)}. Define la ruta explícitamente."
        )
    return matches[0]


results_exist = all(
    path.is_file()
    for path in (
        FEATURES_PATH,
        CHANNELS_PATH,
        SIGNAL_PATH,
        COMPLETE_PATH,
    )
)

recalculated = False


# Loading results
if results_exist and not FORCE_RECALCULATE:
    print(f"Cargando resultados existentes de {XAI_METHOD}...")

    df_features = pd.read_parquet(FEATURES_PATH)
    df_channels = pd.read_parquet(CHANNELS_PATH)

    with np.load(SIGNAL_PATH, allow_pickle=False) as data:
        signal_all = data["values"]
        saved_orig_idxs = data["orig_idx"]
        CHANNEL_NAMES = data["channel_names"].tolist()
        FS = int(data["fs"].item())
        time_edges_sec = data["time_edges_sec"]


# Application by batches
else:
    COMPLETE_PATH.unlink(missing_ok=True)

    CONFIG_PATH = unique_file(base_dir, "*.json")
    MODEL_PATH = unique_file(base_dir, "*.pt")

    with open(CONFIG_PATH, encoding="utf-8") as f:
        config = json.load(f)

    config_obj = validate_config(load_config(CONFIG_PATH))
    transformer_params = _transformer_params_from_config(config_obj)

    FS = int(config["target_fs"])
    N_SAMPLES = int(FS * float(config["window_sec"]))
    FEATURE_NAMES = list(config["selected_features"])
    N_CHANNELS = config.get("n_channels", 22)

    DEVICE = torch.device(
        "cuda" if torch.cuda.is_available() else "cpu"
    )

    model = make_model(
        model_type=config_obj.model,
        input_shape=(N_SAMPLES, N_CHANNELS),
        feat_dim=len(FEATURE_NAMES),
        num_filters=config_obj.num_filters,
        kernel_size=config_obj.kernel_size,
        dropout_rate=config_obj.dropout,
        rnn_units=config_obj.rnn_units,
        time_step=config_obj.time_step_labels,
        transformer_params=transformer_params,
    ).to(DEVICE)

    checkpoint = torch.load(MODEL_PATH, map_location=DEVICE)
    state_dict = checkpoint.get("state_dict", checkpoint)
    model.load_state_dict(state_dict)
    model.eval()

    ds = load_dataset(DATA_PATH)
    X_sig_all  = torch.as_tensor(ds["windows"],  dtype=torch.float32)
    X_feat_all = torch.as_tensor(ds["features"], dtype=torch.float32)
    y_all      = np.asarray(ds["labels"]).reshape(-1).astype(int)

    n_windows, n_times, n_channels = X_sig_all.shape
    n_features = X_feat_all.shape[1]

    assert n_windows > 0
    assert len(X_feat_all) == len(y_all) == n_windows
    assert len(FEATURE_NAMES) == n_features
    assert len(CHANNEL_NAMES) == n_channels
    assert np.isin(y_all, [0, 1]).all()

    print("Device:", DEVICE)
    if DEVICE.type == "cuda":
        print("GPU:", torch.cuda.get_device_name(DEVICE))

    with torch.no_grad():
        raw = model(
            X_sig_all[:1].to(DEVICE),
            X_feat_all[:1].to(DEVICE),
        ).probabilities

    if raw.shape[0] != 1 or raw.numel() != 1:
        raise ValueError(
            f"Prob per window; output {raw.shape}."
        )

    random.seed(13)  

    w_z = ModelWrapper(model, output_fn=lambda o: o.logits,
                    activation=None, reduce=reduce_logit_of_mean_prob)
    w_p = ModelWrapper(model, output_fn=lambda o: o.probabilities,
                    activation=None, reduce="mean")

    z_all = predict_proba(w_z, (X_sig_all, X_feat_all), batch_size=BATCH_SIZE).reshape(-1)
    p_all = predict_proba(w_p, (X_sig_all, X_feat_all), batch_size=BATCH_SIZE).reshape(-1)

    groups = confusion_groups(y_all, p_all, threshold=THRESHOLD)

    lengths = []
    print("Evaluación del modelo:")
    for name in ("TP", "FP", "TN", "FN"):
        print(f"{name}: {len(groups[name])}")
        lengths.append(len(groups[name]))

    # 1. Definimos el tope dinámico global (convertido a entero)
    max_group_len = max(lengths)
    DYNAMIC_CAP = max(1, int(max_group_len * SAMPLE_FRACTION))
    print(f"Tope dinámico calculado (XAI): {DYNAMIC_CAP} ventanas.")

    group_all = np.empty(n_windows, dtype="<U2")
    for name, idx in groups.items():
        group_all[idx] = name

    paths = np.array(ds["paths"])
    selected_indices = []

    for group_name, idx_list in groups.items():
        if len(idx_list) == 0:
            continue
            
        # Index groups by confusion results
        idx_by_file = defaultdict(list)
        for idx in idx_list:
            idx_by_file[paths[idx]].append(idx)
        
        n_target = min(DYNAMIC_CAP, len(idx_list))
        n_files = len(idx_by_file)
        
        if n_files > 0:
            samples_per_file = max(1, n_target // n_files)
            
            # Fair extraction per patient
            for file_path, file_indices in idx_by_file.items():
                n_to_sample = min(samples_per_file, len(file_indices))
                sampled = random.sample(file_indices, n_to_sample)
                selected_indices.extend(sampled)
        
    selected_indices = np.sort(list(set(selected_indices)))

    # Tensors and subset
    sel = np.sort(np.unique(selected_indices))
    X_sig,  X_feat = X_sig_all[sel], X_feat_all[sel]
    y_true, probs, logits = y_all[sel], p_all[sel], z_all[sel]
    group_all_sel = group_all[sel]
    orig_idx = sel
    n_windows = len(sel)
    print(f"Dataset reducido por muestreo estratificado (balanceado por EDF) a {n_windows} ventanas para XAI.")

    # Z features
    f = ds["features"]
    print(np.round(f.mean(0), 2)); print(np.round(f.std(0), 2)) 

    # Saliency e IG: Complete map based on  (N, T, C).
    # Occlusion: Temporal batch (N, batch).
    if XAI_METHOD == "occlusion":
        occ_window = max(1, round(OCC_WINDOW_SEC * FS))

        time_edges_sec = np.append(
            np.arange(0, n_times, occ_window),
            n_times,
        ) / FS

        signal_all = np.empty(
            (n_windows, len(time_edges_sec) - 1),
            dtype=np.float32,
        )
    else:
        time_edges_sec = np.arange(n_times + 1) / FS
        signal_all = np.empty(
            (n_windows, n_times, n_channels),
            dtype=np.float32,
        )

    feature_cols = [
        f"{XAI_METHOD}_feature__{name}" for name in FEATURE_NAMES
    ]

    channel_cols = [
        f"{XAI_METHOD}_channel__{name}" for name in CHANNEL_NAMES
    ]

    feature_batches = []
    channel_batches = []

    for start in range(0, n_windows, BATCH_SIZE):
        end = min(start + BATCH_SIZE, n_windows)
        inputs = (X_sig[start:end], X_feat[start:end])

        # CAMBIO 4: probabilidades y grupos ya calculados; no se repite el forward
        batch_probs = probs[start:end]
        batch_groups = group_all_sel[start:end]

        delta_signal = None
        delta_features = None

        if XAI_METHOD == "saliency":
            batch_signal = saliency(
                w_z, inputs, explain_idx=0, absolute=True
            )
            batch_features = saliency(
                w_z, inputs, explain_idx=1, absolute=True
            )

            batch_channels = batch_signal.mean(axis=1)  # Mean of temporal gradient per channel

        elif XAI_METHOD == "ig":
            batch_signal, delta_signal = integrated_gradients(
                w_z,
                inputs,
                explain_idx=0,
                baseline=None,                          # Zero baseline
                n_steps=IG_STEPS,
                return_delta=True,
            )

            batch_features, delta_features = integrated_gradients(
                w_z,
                inputs,
                explain_idx=1,
                baseline=None,
                n_steps=IG_STEPS,
                return_delta=True,
            )

            batch_channels = batch_signal.sum(axis=1)   # Sum @ IG, mean @ Saliency

            # Si IG no converge (tolerancia en unidades de probabilidad)
            if max(np.abs(delta_signal).max(), np.abs(delta_features).max()) > 0.01:
                print(f"⚠ IG no converge en el lote {start}:{end}: sube IG_STEPS")

        else:
            # Hidding one feature at a time
            batch_features, _ = occlusion(
                w_z,
                inputs,
                explain_idx=1,
                axis=1,
                window=1,
                baseline_value=BASELINE_VALUE,
            )

            # Hidding one channel at a time
            batch_channels, _ = occlusion(
                w_z,
                inputs,
                explain_idx=0,
                axis=2,
                window=1,
                baseline_value=BASELINE_VALUE,
            )

            # Hidding one temporal batch at a time
            batch_signal, _ = occlusion(
                w_z,
                inputs,
                explain_idx=0,
                axis=1,
                window=occ_window,
                baseline_value=BASELINE_VALUE,
            )

        arrays = [
            batch_probs, batch_signal, batch_features, batch_channels
        ]
        if delta_signal is not None:
            arrays.extend([delta_signal, delta_features])

        if not all(np.isfinite(a).all() for a in arrays):
            raise ValueError(f"NaN o infinitos en el lote {start}:{end}.")

        signal_all[start:end] = batch_signal

        batch_true = y_true[start:end]
        batch_pred = (batch_probs >= THRESHOLD).astype(int)

        metadata = pd.DataFrame({
            "orig_idx": np.arange(start, end),
            "y_true": batch_true,
            "y_pred": batch_pred,
            "prob_crisis": batch_probs,
            "group": batch_groups,
            "threshold": THRESHOLD,
            "logit": logits[start:end],
            "orig_idx": orig_idx[start:end],
        })

        idx = orig_idx[start:end]

        metadata["source_file"] = paths[idx]

        times = np.asarray(ds["times"])[idx]
        metadata["start_sec"] = times[:, 0]
        metadata["end_sec"] = times[:, 1]

        if XAI_METHOD == "ig":
            metadata["ig_delta_signal"] = delta_signal
            metadata["ig_delta_features"] = delta_features

        feature_batches.append(
            pd.concat(
                [
                    metadata,
                    pd.DataFrame(batch_features, columns=feature_cols),
                ],
                axis=1,
            )
        )

        channel_batches.append(
            pd.concat(
                [
                    metadata,
                    pd.DataFrame(batch_channels, columns=channel_cols),
                ],
                axis=1,
            )
        )

        if start == 0 or end % 100 == 0 or end == n_windows:
            print(f"{XAI_METHOD}: {end}/{n_windows} ventanas")

    df_features = pd.concat(feature_batches, ignore_index=True)
    df_channels = pd.concat(channel_batches, ignore_index=True)
    saved_orig_idxs = np.arange(n_windows)

    df_features.to_parquet(FEATURES_PATH, index=False)
    df_channels.to_parquet(CHANNELS_PATH, index=False)

    np.savez_compressed(
        SIGNAL_PATH,
        values=signal_all,
        orig_idx=saved_orig_idxs,
        channel_names=np.asarray(CHANNEL_NAMES, dtype=str),
        feature_names=np.asarray(FEATURE_NAMES, dtype=str),
        fs=np.asarray(FS),
        time_edges_sec=time_edges_sec,
        method=np.asarray(XAI_METHOD),
    )

    COMPLETE_PATH.write_text(
        json.dumps(
            {
                "run_id": RUN_ID,
                "method": XAI_METHOD,
                "threshold": THRESHOLD,
                "ig_steps": IG_STEPS if XAI_METHOD == "ig" else None,
                "baseline": (
                    0.0 if XAI_METHOD == "ig"
                    else BASELINE_VALUE if XAI_METHOD == "occlusion"
                    else None
                ),
                "occlusion_window_sec": (
                    OCC_WINDOW_SEC if XAI_METHOD == "occlusion" else None
                ),
                "model_path": str(MODEL_PATH),
                "config_path": str(CONFIG_PATH),
                "dataset_path": str(DATA_PATH),
                "output": "logits; reduce=logit of mean prob",
            },
            indent=2,
        ),
        encoding="utf-8",
    )

    recalculated = True
    print("Resultados guardados:", RESULTS_DIR)


# Dataframe and graphics
feature_prefix = f"{XAI_METHOD}_feature__"
channel_prefix = f"{XAI_METHOD}_channel__"

feature_cols = [
    c for c in df_features.columns if c.startswith(feature_prefix)
]
channel_cols = [
    c for c in df_channels.columns if c.startswith(channel_prefix)
]

feature_names = [c.removeprefix(feature_prefix) for c in feature_cols]
channel_names_table = [
    c.removeprefix(channel_prefix) for c in channel_cols
]

if not feature_cols or not channel_cols:
    raise ValueError("Faltan columnas de resultados.")

if (
    not df_features["orig_idx"].is_unique
    or not df_channels["orig_idx"].is_unique
    or len(np.unique(saved_orig_idxs)) != len(saved_orig_idxs)
):
    raise ValueError("Se encontraron IDs de ventana duplicados.")

if not (
    set(df_features["orig_idx"])
    == set(df_channels["orig_idx"])
    == set(saved_orig_idxs)
):
    raise ValueError("Los archivos no contienen las mismas ventanas.")

features_by_id = df_features.set_index("orig_idx")
channels_by_id = df_channels.set_index("orig_idx")
map_positions = {
    int(orig_idx): pos
    for pos, orig_idx in enumerate(saved_orig_idxs)
}

if XAI_METHOD == "saliency":
    channel_label = "Media temporal de |gradiente|"
    feature_label = "|Gradiente respecto a feature escalada|"
elif XAI_METHOD == "ig":
    channel_label = "Suma temporal de IG con signo"
    feature_label = "Atribución IG con signo"
else:
    channel_label = "z(original) − z(canal ocultado)"
    feature_label = "z(original) − z(feature ocultada)"


def plot_bars(ax, values, names, title, xlabel):
    values = np.asarray(values, dtype=float)

    order = np.argsort(np.abs(values))[::-1]

    colors = (
    [COLOR_SALIENCY] * len(values)
    if XAI_METHOD == "saliency"
    else [
        COLOR_POSITIVE if v >= 0 else COLOR_NEGATIVE
        for v in values[order]
    ]
)

    ax.barh(np.arange(len(values)), values[order], color=colors)
    ax.set_yticks(np.arange(len(values)))
    ax.set_yticklabels([names[j] for j in order], fontsize=8)
    ax.invert_yaxis()
    ax.axvline(0, color="0.4", linewidth=0.7)
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.ticklabel_format(axis="x", style="sci", scilimits=(0, 0))


def make_window_figure(orig_idx):
    row = features_by_id.loc[orig_idx]
    channel_row = channels_by_id.loc[orig_idx]
    values = signal_all[map_positions[orig_idx]]

    fig = plt.figure(figsize=(16, 11), constrained_layout=True)
    grid = fig.add_gridspec(2, 2)

    ax_signal = fig.add_subplot(grid[0, :])
    ax_channels = fig.add_subplot(grid[1, 0])
    ax_features = fig.add_subplot(grid[1, 1])

    if XAI_METHOD == "occlusion":
        # Each bar represents the interal hidden
        ax_signal.bar(
            time_edges_sec[:-1],
            values,
            width=np.diff(time_edges_sec),
            align="edge",
            color=np.where(values >= 0, "firebrick", "steelblue"),
            edgecolor="white",
        )
        ax_signal.axhline(0, color="0.4", linewidth=0.7)
        ax_signal.set_ylabel("z(original) − z(bloque ocultado)")
        ax_signal.set_title(L["occ_title"])                       # CAMBIO 6 (idioma)
    else:
        if XAI_METHOD == "saliency":
            limit = float(values.max()) or 1.0
            cmap, vmin, vmax = "magma", 0, limit
            color_label = "|∂z/∂señal|"
        else:
            limit = float(np.abs(values).max()) or 1.0
            cmap, vmin, vmax = "RdBu_r", -limit, limit
            color_label = L["ig_cbar"]                            # CAMBIO 6

        image = ax_signal.imshow(
            values.T,
            origin="lower",
            aspect="auto",
            interpolation="nearest",
            extent=[0, values.shape[0] / FS, -0.5, values.shape[1] - 0.5],
            cmap=cmap,
            vmin=vmin,
            vmax=vmax,
            rasterized=True,
        )
        ax_signal.set_yticks(np.arange(len(CHANNEL_NAMES)))
        ax_signal.set_yticklabels(CHANNEL_NAMES, fontsize=8)
        ax_signal.set_title(L["map_title"])                       # CAMBIO 6
        fig.colorbar(image, ax=ax_signal, label=color_label, pad=0.01)

    ax_signal.set_xlabel("Tiempo dentro de la ventana (s)")

    plot_bars(
        ax_channels,
        channel_row[channel_cols].to_numpy(dtype=float),
        channel_names_table,
        L["channels"],                                            # CAMBIO 6
        channel_label,
    )
    plot_bars(
        ax_features,
        row[feature_cols].to_numpy(dtype=float),
        feature_names,
        L["features"],                                            # CAMBIO 6
        feature_label,
    )

    title = (
        f"{METHOD_LABEL[XAI_METHOD]} | Ventana {orig_idx} | "    # CAMBIO 6
        f"{GROUP_LABEL[row['group']]} | "
        f"Real={int(row['y_true'])} | Predicción={int(row['y_pred'])}\n"
        f"P(crisis)={row['prob_crisis']:.6g} | "
        f"Umbral={row['threshold']:g}"
    )

    if XAI_METHOD == "ig":
        title += (
            f"\n{L['delta_sig']}={row['ig_delta_signal']:.2e}; "  # CAMBIO 6
            f"{L['delta_feat']}={row['ig_delta_features']:.2e}"
        )

    fig.suptitle(title, fontsize=12)
    return fig


def make_group_figure(group_name):
    features = df_features.loc[df_features["group"] == group_name]
    channels = df_channels.loc[df_channels["group"] == group_name]

    fig, axes = plt.subplots(
        1, 2, figsize=(16, 9), constrained_layout=True
    )

    plot_bars(
        axes[0],
        channels[channel_cols].mean().to_numpy(),
        channel_names_table,
        f"{L['channels']}: promedio entre ventanas",              # CAMBIO 6
        channel_label,
    )
    plot_bars(
        axes[1],
        features[feature_cols].mean().to_numpy(),
        feature_names,
        f"{L['features']}: promedio entre ventanas",              # CAMBIO 6
        feature_label,
    )

    note = (
        L["note_sal"]                                             # CAMBIO 6
        if XAI_METHOD == "saliency"
        else L["note_signed"]
    )

    fig.suptitle(
        f"{METHOD_LABEL[XAI_METHOD]} | {GROUP_LABEL[group_name]} | "  # CAMBIO 6
        f"{len(features)} ventanas\n{note}",
        fontsize=12,
    )
    return fig


# Generation of results to use in documentation 
if PLOT_RESULTS:
    if PLOT_ORIG_IDXS is None:
        selected_ids = []

        for group in GROUP_ORDER:
            candidates = df_features.loc[
                df_features["group"] == group, "orig_idx"
            ]
            if not candidates.empty:
                selected_ids.append(int(candidates.iloc[0]))

        selection_tag = "first_per_group"
    else:
        selected_ids = list(dict.fromkeys(int(i) for i in PLOT_ORIG_IDXS))
        selection_tag = "windows_" + "_".join(map(str, selected_ids))

    for orig_idx in selected_ids:
        if orig_idx not in map_positions:
            raise ValueError(f"No existe la ventana {orig_idx}.")

    jobs = []

    for orig_idx in selected_ids:
        jobs.append((
            "window",
            orig_idx,
            PLOTS_DIR / f"{XAI_METHOD}_window_{orig_idx}.pdf",
        ))

    for group in GROUP_ORDER:
        if (df_features["group"] == group).any():
            jobs.append((
                "group",
                group,
                PLOTS_DIR / f"{XAI_METHOD}_group_{group}.pdf",
            ))

    report_path = PLOTS_DIR / f"{XAI_METHOD}_report_{selection_tag}.pdf"

    regenerate = FORCE_REPLOT or recalculated
    create_report = regenerate or not report_path.is_file()

    def render_job(kind, value):
        if kind == "window":
            return make_window_figure(value)
        return make_group_figure(value)

    if create_report:
        with PdfPages(report_path) as pdf:
            pdf.infodict()["Title"] = f"{L['pdf_title']} {METHOD_LABEL[XAI_METHOD]}"  # CAMBIO 6

            for kind, value, individual_path in jobs:
                fig = render_job(kind, value)

                if regenerate or not individual_path.is_file():
                    fig.savefig(individual_path, dpi=180)

                pdf.savefig(fig, dpi=180)
                plt.close(fig)

        print("Informe PDF guardado:", report_path)

    else:
        for kind, value, individual_path in jobs:
            if not individual_path.is_file():
                fig = render_job(kind, value)
                fig.savefig(individual_path, dpi=180)
                plt.close(fig)

        print("Existent PDFs are saved.")

    print("Individual figures:", PLOTS_DIR.resolve())


# Correlation:
base_dir = Path(__file__).resolve().parent
DATA_PATH = base_dir / "_data"
CORRELATION = True
if CORRELATION:
    meta = ds["window_metadata"]
    rows = []
    for _, r in df_features[["window_id", "orig_idx", "group", "logit"]].iterrows():
        info = meta[int(r.orig_idx)]
        w0, w1 = info["start_sec"], info["end_sec"]
        ov = sum(max(0.0, min(w1, a["stop"]) - max(w0, a["start"]))   # AJUSTA las claves
                for a in info["seizure_overlaps"])
        rows.append({**r.to_dict(), "overlap_frac": ov / (w1 - w0),
                    "file": info["source_file"]})
    df_ov = pd.DataFrame(rows)

    print(df_ov.groupby("group")["overlap_frac"].describe())
    print(df_ov.groupby("group")["file"].nunique())     # cuántos archivos por grupo

"""