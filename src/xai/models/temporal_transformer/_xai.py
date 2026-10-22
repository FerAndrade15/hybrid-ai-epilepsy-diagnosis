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
# XAI sobre todas las ventanas, con lectura y escritura por lotes.
"""
import hashlib
import json
import math
import os
import random
import re
from contextlib import ExitStack
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import torch
from matplotlib.backends.backend_pdf import PdfPages
from scipy.stats import spearmanr

from src.xai.xai_common import confusion_groups
from src.xai.xai_deep_core import (
    ModelWrapper,
    reduce_logit_of_mean_prob,
    predict_proba,
    occlusion,
    explain_ig,
    explain_attn_grad,
    deletion_scores,
)
from src.xai.models.temporal_transformer.sanchez_transformer_utils import (
    load_config,
    validate_config,
)
from src.xai.models.temporal_transformer.sanchez_transformer_pipeline import (
    make_model,
    _transformer_params_from_config,
)


# Configuración: todas las ventanas, sin muestreo.
XAI_METHOD = "occlusion"  # "ig" u "occlusion"

BATCH_SIZE = 8      #4
THRESHOLD = 0.5

IG_STEPS = 100
IG_INTERNAL_BS = 64 #25
DELTA_REL_TOL = 0.05

COMPUTE_ATTN = True
COMPUTE_FIDELITY = True
COMPUTE_ABLATION = True

FID_FRACS = (0.1, 0.2, 0.3, 0.5)

OCC_WINDOW_SEC = 0.5
BASELINE_VALUE = 0.0

SEED = 13
BOOT_N = 2000

# Reutiliza una ejecución completa.
# Una ejecución XAI incompleta comienza de nuevo.
FORCE_RECALCULATE = False

PLOT_RESULTS = True
PLOT_ORIG_IDXS = None  # None: primera ventana de cada grupo.

RUN_ID = "sanchez_full_v3"

BASE_DIR = Path(__file__).resolve().parent

DATA_PATH = Path("/workspace/xai_results/data_extractor")
# DATA_PATH = Path("/mnt/d/xai_results/data_extractor")
RESULTS_ROOT = Path("/mnt/d/xai_results/temporal_transformer")

MODEL_PATH = BASE_DIR / "sanchez_transformer_final_model.pt"
CONFIG_PATH = BASE_DIR / "sanchez_transformer_config_used.json"

CHANNEL_NAMES = [
    "FP1-F7", "F7-T3", "T3-T5", "T5-O1",
    "FP2-F8", "F8-T4", "T4-T6", "T6-O2",
    "A1-T3", "T3-C3", "C3-CZ", "CZ-C4",
    "C4-T4", "T4-A2", "FP1-F3", "F3-C3",
    "C3-P3", "P3-O1", "FP2-F4", "F4-C4",
    "C4-P4", "P4-O2",
]

CHANNEL_GROUPS = {
    "temporal_izq": [
        "FP1-F7", "F7-T3", "T3-T5", "T5-O1",
    ],
    "temporal_der": [
        "FP2-F8", "F8-T4", "T4-T6", "T6-O2",
    ],
    "parasag_izq": [
        "FP1-F3", "F3-C3", "C3-P3", "P3-O1",
    ],
    "parasag_der": [
        "FP2-F4", "F4-C4", "C4-P4", "P4-O2",
    ],
    "central_aur": [
        "A1-T3", "T3-C3", "C3-CZ",
        "CZ-C4", "C4-T4", "T4-A2",
    ],
}

FEATURE_GROUPS = {
    "amplitud": [
        "std_eeg", "rms_eeg", "hjorth_activity",
    ],
    "energia": [
        "line_length", "tkeo_mean",
    ],
    "pot_relativa": [
        "bp_rel_delta", "bp_rel_theta", "bp_rel_alpha",
        "bp_rel_beta", "bp_rel_gamma",
    ],
    "ratios": [
        "beta_alpha_ratio", "theta_alpha_ratio",
    ],
    "forma_espec": [
        "hjorth_mobility", "hjorth_complexity",
        "spectral_entropy", "sef95",
    ],
}

GROUP_ORDER = ("TP", "FP", "TN", "FN")

GROUP_LABEL = {
    "TP": "VP",
    "FP": "FP",
    "TN": "VN",
    "FN": "FN",
}

METHOD_LABEL = {
    "ig": "Gradientes integrados",
    "occlusion": "Oclusión",
}

COLOR_POSITIVE = "#0D232F"
COLOR_NEGATIVE = "#6A8BA2"


def read_json(path):
    with Path(path).open(encoding="utf-8") as f:
        return json.load(f)


def write_json(path, data):
    path = Path(path)
    temporary = path.with_suffix(path.suffix + ".tmp")

    with temporary.open("w", encoding="utf-8") as f:
        json.dump(
            data,
            f,
            indent=2,
            ensure_ascii=False,
            allow_nan=False,
        )
        f.flush()
        os.fsync(f.fileno())

    temporary.replace(path)


def file_hash(path):
    digest = hashlib.sha256()

    with Path(path).open("rb") as f:
        for block in iter(
            lambda: f.read(1024 * 1024),
            b"",
        ):
            digest.update(block)

    return digest.hexdigest()


class NpyRows:
    """
    Lee filas contiguas de un NPY C-order.

    No carga ni mapea el arreglo completo.
    """

    def __init__(self, path):
        self.path = Path(path)

        with self.path.open("rb") as f:
            version = np.lib.format.read_magic(f)

            if version == (1, 0):
                header = np.lib.format.read_array_header_1_0(f)
            elif version == (2, 0):
                header = np.lib.format.read_array_header_2_0(f)
            else:
                raise ValueError(
                    f"Versión NPY no contemplada: {version}"
                )

            self.shape, fortran_order, self.dtype = header
            self.offset = f.tell()

        if fortran_order or self.dtype.hasobject or not self.shape:
            raise ValueError(
                f"Se requiere un NPY numérico C-order: {self.path}"
            )

        self.row_items = math.prod(self.shape[1:])
        self.row_bytes = self.row_items * self.dtype.itemsize

        expected_size = (
            self.offset
            + self.shape[0] * self.row_bytes
        )

        if self.path.stat().st_size != expected_size:
            raise ValueError(
                f"NPY incompleto o de tamaño inesperado: {self.path}"
            )

    def __len__(self):
        return self.shape[0]

    def __getitem__(self, key):
        scalar = isinstance(key, (int, np.integer))

        if scalar:
            index = int(key)

            if index < 0:
                index += len(self)

            if not 0 <= index < len(self):
                raise IndexError(index)

            start, stop = index, index + 1

        elif isinstance(key, slice):
            start, stop, step = key.indices(len(self))

            if step != 1:
                raise ValueError(
                    "Solo se permiten slices con paso 1."
                )

        else:
            raise TypeError(
                "Usa un índice entero o un slice contiguo."
            )

        n_rows = max(0, stop - start)

        with self.path.open("rb") as f:
            f.seek(self.offset + start * self.row_bytes)

            array = np.fromfile(
                f,
                dtype=self.dtype,
                count=n_rows * self.row_items,
            )

        if array.size != n_rows * self.row_items:
            raise OSError(
                f"Lectura incompleta: {self.path}"
            )

        array = array.reshape(
            (n_rows, *self.shape[1:])
        )

        return array[0] if scalar else array


class NpyWriter:
    """
    Escribe filas secuencialmente.

    No reserva RAM ni un mapa de memoria del resultado completo.
    """

    def __init__(self, path, shape):
        self.path = Path(path)
        self.shape = tuple(shape)
        self.rows = 0
        self.file = self.path.open("wb")

        np.lib.format.write_array_header_2_0(
            self.file,
            {
                "descr": np.lib.format.dtype_to_descr(
                    np.dtype("float32")
                ),
                "fortran_order": False,
                "shape": self.shape,
            },
        )

    def append(self, array):
        array = np.ascontiguousarray(
            array,
            dtype=np.float32,
        )

        if (
            array.shape[1:] != self.shape[1:]
            or self.rows + len(array) > self.shape[0]
        ):
            raise ValueError(
                f"Dimensiones inesperadas al escribir {self.path}"
            )

        raw = memoryview(array).cast("B")
        chunk_size = 16 * 1024 * 1024

        for start in range(0, len(raw), chunk_size):
            part = raw[start:start + chunk_size]

            if self.file.write(part) != len(part):
                raise OSError(
                    f"Escritura incompleta: {self.path}"
                )

        self.rows += len(array)
        self.file.flush()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        try:
            self.file.flush()
            os.fsync(self.file.fileno())
        finally:
            self.file.close()

        if exc_type is None and self.rows != self.shape[0]:
            raise ValueError(
                f"Resultado incompleto: "
                f"{self.rows}/{self.shape[0]} filas"
            )


def load_inputs(directory):
    directory = Path(directory)

    complete_path = directory / "dataset_complete.json"

    if not complete_path.is_file():
        raise RuntimeError(
            "Falta dataset_complete.json; "
            "verifica la consolidación."
        )

    ds = read_json(directory / "meta.json")

    ds["windows"] = NpyRows(
        directory / "windows_np.npy"
    )

    # Estos arreglos son pequeños respecto al EEG de 18 GiB.
    ds["features"] = np.load(
        directory / "features_scaled.npy",
        allow_pickle=False,
    )

    ds["labels"] = np.load(
        directory / "labels_np.npy",
        allow_pickle=False,
    )

    n_windows = len(ds["windows"])

    for key in (
        "features",
        "labels",
        "paths",
        "times",
        "window_metadata",
    ):
        if len(ds[key]) != n_windows:
            raise ValueError(
                f"Cantidad inconsistente para {key}"
            )

    if read_json(complete_path)["n_windows"] != n_windows:
        raise ValueError(
            "La marca final no coincide con "
            "la cantidad de ventanas."
        )

    return ds


def tensor_batch(array, device):
    return torch.from_numpy(
        np.array(
            array,
            dtype=np.float32,
            copy=True,
        )
    ).to(device)


def as_numpy(value):
    if torch.is_tensor(value):
        return value.detach().cpu().numpy()

    return np.asarray(value)


def predict_all(
    w_z,
    w_p,
    signals,
    features,
    device,
):
    n_windows = len(signals)

    logits = np.empty(n_windows, dtype=np.float32)
    probs = np.empty(n_windows, dtype=np.float32)

    for start in range(0, n_windows, BATCH_SIZE):
        end = min(start + BATCH_SIZE, n_windows)

        inputs = (
            tensor_batch(signals[start:end], device),
            tensor_batch(features[start:end], device),
        )

        with torch.no_grad():
            z = as_numpy(
                predict_proba(
                    w_z,
                    inputs,
                    batch_size=BATCH_SIZE,
                )
            ).reshape(-1)

            p = as_numpy(
                predict_proba(
                    w_p,
                    inputs,
                    batch_size=BATCH_SIZE,
                )
            ).reshape(-1)

        if len(z) != end - start or len(p) != end - start:
            raise ValueError(
                "La predicción no devuelve un valor por ventana."
            )

        if not np.isfinite(z).all() or not np.isfinite(p).all():
            raise ValueError(
                f"Predicciones no finitas: {start}:{end}"
            )

        logits[start:end] = z
        probs[start:end] = p

        if (
            start == 0
            or end % 1000 == 0
            or end == n_windows
        ):
            print(
                f"Predicción: {end}/{n_windows}",
                flush=True,
            )

    return logits, probs


def patient_of(path):
    return re.split(
        r"_",
        Path(str(path)).stem,
    )[0]


def seizure_metrics(ds, indices, importance, fs):
    fractions = []
    masses = []

    for index, imp in zip(indices, importance):
        info = ds["window_metadata"][int(index)]

        t = (
            float(info["start_sec"])
            + (np.arange(len(imp)) + 0.5) / fs
        )

        mask = np.zeros(len(imp), dtype=bool)

        for overlap in info["seizure_overlaps"]:
            mask |= (
                (t >= overlap["overlap_start_sec"])
                & (t < overlap["overlap_end_sec"])
            )

        total = float(imp.sum())

        fractions.append(float(mask.mean()))

        masses.append(
            float(imp[mask].sum() / total)
            if total > 0
            else np.nan
        )

    return (
        np.asarray(fractions),
        np.asarray(masses),
    )


def run_ablation(
    w_z,
    xs,
    xf,
    interictal,
    original_logits,
    ch_groups,
    ft_groups,
):
    def drop(ch=None, ft=None, use_inter=False):
        signal = xs.clone()
        features = xf.clone()

        if ch is not None:
            signal[:, :, ch] = BASELINE_VALUE

        if ft is not None:
            features[:, ft] = (
                interictal[:, ft]
                if use_inter
                else BASELINE_VALUE
            )

        with torch.no_grad():
            changed = as_numpy(
                predict_proba(
                    w_z,
                    (signal, features),
                    batch_size=BATCH_SIZE,
                )
            ).reshape(-1)

        return original_logits - changed

    all_ch = list(range(xs.shape[2]))
    all_ft = list(range(xf.shape[1]))

    results = {
        "abl_branch_signal": drop(ch=all_ch),
        "abl_branch_features": drop(ft=all_ft),
        "abl_branch_features_inter": drop(
            ft=all_ft,
            use_inter=True,
        ),
        "abl_both": drop(ch=all_ch, ft=all_ft),
    }

    for name, indices in ch_groups.items():
        results[f"abl_ch__{name}"] = drop(ch=indices)

    for name, indices in ft_groups.items():
        results[f"abl_ft__{name}"] = drop(ft=indices)

        results[f"abl_ft_inter__{name}"] = drop(
            ft=indices,
            use_inter=True,
        )

    return results


def calculate(ds, config, results_dir, signature):
    config_obj = validate_config(
        load_config(CONFIG_PATH)
    )

    fs = float(config["target_fs"])

    signals = ds["windows"]
    features = ds["features"]
    y = np.asarray(ds["labels"]).reshape(-1).astype(int)

    n_windows, n_times, n_channels = signals.shape
    feature_names = list(config["selected_features"])

    if (
        n_windows == 0
        or n_times != int(fs * float(config["window_sec"]))
        or n_channels != len(CHANNEL_NAMES)
    ):
        raise ValueError(
            "Las dimensiones de las ventanas "
            "no coinciden con el modelo."
        )

    if (
        features.shape != (n_windows, len(feature_names))
        or list(ds["feature_names"]) != feature_names
    ):
        raise ValueError(
            "Cantidad u orden de features incompatible "
            "con el modelo."
        )

    if not np.isin(y, [0, 1]).all():
        raise ValueError(
            "Se esperan etiquetas binarias."
        )

    device = torch.device(
        "cuda" if torch.cuda.is_available() else "cpu"
    )

    print("Device:", device, flush=True)

    if device.type == "cuda":
        print(
            "GPU:",
            torch.cuda.get_device_name(device),
            flush=True,
        )

    model = make_model(
        model_type=config_obj.model,
        input_shape=(n_times, n_channels),
        feat_dim=len(feature_names),
        num_filters=config_obj.num_filters,
        kernel_size=config_obj.kernel_size,
        dropout_rate=config_obj.dropout,
        rnn_units=config_obj.rnn_units,
        time_step=config_obj.time_step_labels,
        transformer_params=_transformer_params_from_config(
            config_obj
        ),
    ).to(device)

    checkpoint = torch.load(
        MODEL_PATH,
        map_location=device,
    )

    model.load_state_dict(
        checkpoint.get("state_dict", checkpoint)
    )
    model.eval()

    w_z = ModelWrapper(
        model,
        output_fn=lambda output: output.logits,
        activation=None,
        reduce=reduce_logit_of_mean_prob,
    )

    w_p = ModelWrapper(
        model,
        output_fn=lambda output: output.probabilities,
        activation=None,
        reduce="mean",
    )

    has_attention = (
        XAI_METHOD == "ig"
        and COMPUTE_ATTN
        and hasattr(model, "blocks")
        and hasattr(model, "time_step")
    )

    if (
        XAI_METHOD == "ig"
        and COMPUTE_ATTN
        and not has_attention
    ):
        print(
            "Modelo sin soporte de atención × gradiente: "
            "se omite.",
            flush=True,
        )

    logits, probs = predict_all(
        w_z,
        w_p,
        signals,
        features,
        device,
    )

    np.savez_compressed(
        results_dir / "predictions.npz",
        logits=logits,
        probs=probs,
        y=y,
    )

    groups = confusion_groups(
        y,
        probs,
        threshold=THRESHOLD,
    )

    group_all = np.full(
        n_windows,
        "",
        dtype="<U2",
    )

    for name in GROUP_ORDER:
        indices = groups[name]
        group_all[indices] = name

        print(
            f"{name}: {len(indices)} ventanas",
            flush=True,
        )

    if np.any(group_all == ""):
        raise ValueError(
            "Hay ventanas sin grupo de confusión."
        )

    paths = np.asarray(ds["paths"])
    patients = np.asarray([
        patient_of(path)
        for path in paths
    ])
    times = np.asarray(ds["times"])

    do_ablation = (
        XAI_METHOD == "occlusion"
        and COMPUTE_ABLATION
    )

    interictal = {}
    ch_groups = {}
    ft_groups = {}

    if do_ablation:
        ch_groups = {
            name: [
                CHANNEL_NAMES.index(channel)
                for channel in channels
            ]
            for name, channels in CHANNEL_GROUPS.items()
        }

        ft_groups = {
            name: [
                feature_names.index(feature)
                for feature in group_features
            ]
            for name, group_features in FEATURE_GROUPS.items()
        }

        for patient in np.unique(patients):
            mask = (
                (patients == patient)
                & (y == 0)
            )

            interictal[patient] = (
                features[mask].mean(axis=0)
                if mask.any()
                else np.zeros(len(feature_names))
            )

    occ_window = max(
        1,
        round(OCC_WINDOW_SEC * fs),
    )

    if XAI_METHOD == "occlusion":
        time_edges = np.append(
            np.arange(0, n_times, occ_window),
            n_times,
        ) / fs

        signal_shape = (
            n_windows,
            len(time_edges) - 1,
        )
    else:
        time_edges = np.arange(n_times + 1) / fs

        signal_shape = (
            n_windows,
            n_times,
            n_channels,
        )

    feature_cols = [
        f"{XAI_METHOD}_feature__{name}"
        for name in feature_names
    ]

    channel_cols = [
        f"{XAI_METHOD}_channel__{name}"
        for name in CHANNEL_NAMES
    ]

    feature_frames = []
    channel_frames = []

    print(
        f"XAI sobre TODAS las {n_windows} ventanas.",
        flush=True,
    )

    with ExitStack() as stack:
        signal_writer = stack.enter_context(
            NpyWriter(
                results_dir / "signal_values.npy",
                signal_shape,
            )
        )

        attention_writer = (
            stack.enter_context(
                NpyWriter(
                    results_dir / "attention_values.npy",
                    (n_windows, n_times),
                )
            )
            if has_attention
            else None
        )

        for start in range(0, n_windows, BATCH_SIZE):
            end = min(
                start + BATCH_SIZE,
                n_windows,
            )

            xs = tensor_batch(
                signals[start:end],
                device,
            )
            xf = tensor_batch(
                features[start:end],
                device,
            )

            extra = {}

            if do_ablation:
                fi = tensor_batch(
                    np.stack([
                        interictal[patient]
                        for patient in patients[start:end]
                    ]),
                    device,
                )

                extra.update(
                    run_ablation(
                        w_z,
                        xs,
                        xf,
                        fi,
                        logits[start:end],
                        ch_groups,
                        ft_groups,
                    )
                )

            if XAI_METHOD == "ig":
                result = explain_ig(
                    w_z,
                    xs,
                    xf,
                    n_steps=IG_STEPS,
                    internal_bs=IG_INTERNAL_BS,
                )

                attr_signal = as_numpy(result["attr_x"])
                attr_features = as_numpy(result["attr_feat"])
                attr_channels = attr_signal.sum(axis=1)

                delta = as_numpy(
                    result["delta"]
                ).reshape(-1)

                gap = as_numpy(
                    result["gap"]
                ).reshape(-1)

                if (
                    not np.isfinite(delta).all()
                    or not np.isfinite(gap).all()
                ):
                    raise ValueError(
                        f"Delta o gap IG no finito: {start}:{end}"
                    )

                relative_delta = (
                    np.abs(delta)
                    / np.maximum(np.abs(gap), 1e-3)
                )

                extra.update(
                    ig_delta=delta,
                    ig_gap=gap,
                    ig_rel_delta=relative_delta,
                )

                if relative_delta.max() > DELTA_REL_TOL:
                    print(
                        f"IG: delta relativo alto en {start}:{end}: "
                        f"{relative_delta.max():.3f}",
                        flush=True,
                    )

                importance = np.abs(attr_signal).sum(axis=2)

                (
                    extra["seiz_frac"],
                    extra["seiz_mass"],
                ) = seizure_metrics(
                    ds,
                    np.arange(start, end),
                    importance,
                    fs,
                )

                if has_attention:
                    attention = explain_attn_grad(
                        model,
                        w_z,
                        xs,
                        xf,
                    )

                    attention_np = as_numpy(attention)

                    if not np.isfinite(attention_np).all():
                        raise ValueError(
                            f"Atención no finita: {start}:{end}"
                        )

                    attention_writer.append(attention_np)

                if COMPUTE_FIDELITY:
                    deletion_ig = []
                    deletion_random = []
                    deletion_attention = []
                    attention_correlations = []

                    for j in range(end - start):
                        d_ig, d_random = deletion_scores(
                            w_z,
                            xs[j:j + 1],
                            xf[j:j + 1],
                            torch.as_tensor(importance[j]),
                            FID_FRACS,
                        )

                        deletion_ig.append(
                            float(as_numpy(d_ig))
                        )
                        deletion_random.append(
                            float(as_numpy(d_random))
                        )

                        if has_attention:
                            d_attention, _ = deletion_scores(
                                w_z,
                                xs[j:j + 1],
                                xf[j:j + 1],
                                attention[j],
                                FID_FRACS,
                            )

                            deletion_attention.append(
                                float(as_numpy(d_attention))
                            )

                            attention_correlations.append(
                                spearmanr(
                                    importance[j],
                                    attention_np[j],
                                ).correlation
                            )

                    extra.update(
                        del_ig=deletion_ig,
                        del_rand=deletion_random,
                    )

                    if has_attention:
                        extra.update(
                            del_attn=deletion_attention,
                            rho_attn_ig=attention_correlations,
                        )

                del result

            else:
                attr_features, _ = occlusion(
                    w_z,
                    (xs, xf),
                    explain_idx=1,
                    axis=1,
                    window=1,
                    baseline_value=BASELINE_VALUE,
                )

                attr_channels, _ = occlusion(
                    w_z,
                    (xs, xf),
                    explain_idx=0,
                    axis=2,
                    window=1,
                    baseline_value=BASELINE_VALUE,
                )

                attr_signal, _ = occlusion(
                    w_z,
                    (xs, xf),
                    explain_idx=0,
                    axis=1,
                    window=occ_window,
                    baseline_value=BASELINE_VALUE,
                )

                attr_signal = as_numpy(attr_signal)
                attr_features = as_numpy(attr_features)
                attr_channels = as_numpy(attr_channels)

            if not all(
                np.isfinite(array).all()
                for array in (
                    attr_signal,
                    attr_features,
                    attr_channels,
                )
            ):
                raise ValueError(
                    f"Atribuciones no finitas: {start}:{end}"
                )

            signal_writer.append(attr_signal)

            metadata = pd.DataFrame({
                "orig_idx": np.arange(start, end),
                "y_true": y[start:end],
                "y_pred": (
                    probs[start:end] >= THRESHOLD
                ).astype(int),
                "prob_crisis": probs[start:end],
                "group": group_all[start:end],
                "threshold": THRESHOLD,
                "logit": logits[start:end],
                "source_file": paths[start:end],
                "patient": patients[start:end],
                "start_sec": times[start:end, 0],
                "end_sec": times[start:end, 1],
            })

            for key, values in extra.items():
                metadata[key] = np.asarray(values).reshape(-1)

            feature_frames.append(
                pd.concat(
                    [
                        metadata,
                        pd.DataFrame(
                            attr_features,
                            columns=feature_cols,
                        ),
                    ],
                    axis=1,
                )
            )

            channel_frames.append(
                pd.concat(
                    [
                        metadata,
                        pd.DataFrame(
                            attr_channels,
                            columns=channel_cols,
                        ),
                    ],
                    axis=1,
                )
            )

            if (
                start == 0
                or end % 100 == 0
                or end == n_windows
            ):
                print(
                    f"{XAI_METHOD}: {end}/{n_windows}",
                    flush=True,
                )

    # Los mapas grandes ya están guardados en D:.
    # Solo se reúnen las tablas resumidas en RAM.
    df_features = pd.concat(
        feature_frames,
        ignore_index=True,
    )
    df_channels = pd.concat(
        channel_frames,
        ignore_index=True,
    )

    df_features.to_parquet(
        results_dir / "features.parquet",
        index=False,
    )

    df_channels.to_parquet(
        results_dir / "channels.parquet",
        index=False,
    )

    write_json(
        results_dir / "signal_meta.json",
        {
            "fs": fs,
            "channel_names": CHANNEL_NAMES,
            "feature_names": feature_names,
            "time_edges_sec": time_edges.tolist(),
            "method": XAI_METHOD,
            "attn_grad": has_attention,
            "n_windows": n_windows,
        },
    )

    # Se publica únicamente después de guardar todos los resultados.
    write_json(
        results_dir / "completed.json",
        signature,
    )

    return df_features, df_channels


def plot_bars(
    ax,
    values,
    names,
    title,
    xlabel,
    ci=None,
):
    values = np.asarray(values, dtype=float)
    order = np.argsort(np.abs(values))[::-1]

    colors = [
        COLOR_POSITIVE if value >= 0 else COLOR_NEGATIVE
        for value in values[order]
    ]

    xerr = None

    if ci is not None:
        lo = np.asarray(ci[0])[order]
        hi = np.asarray(ci[1])[order]

        xerr = np.vstack([
            np.maximum(values[order] - lo, 0),
            np.maximum(hi - values[order], 0),
        ])

    ax.barh(
        np.arange(len(values)),
        values[order],
        color=colors,
        xerr=xerr,
        capsize=2,
    )

    ax.set_yticks(np.arange(len(values)))
    ax.set_yticklabels(
        [names[j] for j in order],
        fontsize=8,
    )
    ax.invert_yaxis()
    ax.axvline(0, color="0.4", linewidth=0.7)
    ax.set(title=title, xlabel=xlabel)
    ax.ticklabel_format(
        axis="x",
        style="sci",
        scilimits=(0, 0),
    )


def group_summary(df, group, cols, names):
    data = df.loc[df["group"] == group]

    # Un valor por paciente antes de resumir entre pacientes.
    matrix = (
        data.groupby("patient")[cols]
        .median()
        .to_numpy()
    )

    rng = np.random.default_rng(SEED)

    bootstrap_medians = np.stack([
        np.median(
            matrix[
                rng.integers(
                    0,
                    len(matrix),
                    len(matrix),
                )
            ],
            axis=0,
        )
        for _ in range(BOOT_N)
    ])

    values = data[cols].abs().to_numpy()
    hits = np.zeros_like(values)

    np.put_along_axis(
        hits,
        np.argsort(-values, axis=1)[:, :min(3, len(cols))],
        1,
        axis=1,
    )

    top3 = (
        pd.DataFrame(hits, index=data.index)
        .groupby(data["patient"])
        .mean()
        .mean(axis=0)
        .to_numpy()
    )

    return pd.DataFrame(
        {
            "median": np.median(matrix, axis=0),
            "ci_lo": np.percentile(
                bootstrap_medians,
                2.5,
                axis=0,
            ),
            "ci_hi": np.percentile(
                bootstrap_medians,
                97.5,
                axis=0,
            ),
            "top3_freq": top3,
        },
        index=names,
    )


def reports(ds, df_features, df_channels, results_dir):
    info = read_json(
        results_dir / "signal_meta.json"
    )

    feature_names = info["feature_names"]
    channel_names = info["channel_names"]
    fs = info["fs"]
    time_edges = np.asarray(info["time_edges_sec"])

    signal = NpyRows(
        results_dir / "signal_values.npy"
    )

    attention = (
        NpyRows(results_dir / "attention_values.npy")
        if info["attn_grad"]
        else None
    )

    feature_cols = [
        f"{XAI_METHOD}_feature__{name}"
        for name in feature_names
    ]

    channel_cols = [
        f"{XAI_METHOD}_channel__{name}"
        for name in channel_names
    ]

    for df in (df_features, df_channels):
        if (
            not df["orig_idx"].is_unique
            or len(df) != len(signal)
        ):
            raise ValueError(
                "IDs duplicados o cantidad de "
                "resultados inconsistente."
            )

    if not np.array_equal(
        df_features["orig_idx"],
        df_channels["orig_idx"],
    ):
        raise ValueError(
            "Las tablas no contienen las mismas "
            "ventanas en el mismo orden."
        )

    if not np.array_equal(
        df_features["orig_idx"],
        np.arange(len(signal)),
    ):
        raise ValueError(
            "Se esperaban todas las ventanas "
            "en orden original."
        )

    feature_by_id = df_features.set_index("orig_idx")
    channel_by_id = df_channels.set_index("orig_idx")

    fidelity_cols = [
        name
        for name in (
            "del_ig",
            "del_rand",
            "del_attn",
            "rho_attn_ig",
        )
        if name in df_features
    ]

    if fidelity_cols:
        print("Fidelidad por grupo:")
        print(
            df_features.groupby("group")[fidelity_cols]
            .mean()
            .round(3)
        )

    if "seiz_mass" in df_features:
        print("Solapamiento temporal con anotaciones:")
        print(
            df_features.groupby("group")[
                ["seiz_frac", "seiz_mass"]
            ]
            .mean()
            .round(3)
        )

    ablation_cols = [
        name
        for name in df_features
        if name.startswith("abl_")
    ]

    if ablation_cols:
        per_patient = (
            df_features.groupby(["group", "patient"])[
                ablation_cols
            ]
            .median()
        )

        per_patient.to_csv(
            results_dir / "ablation_by_patient.csv"
        )

        (
            per_patient.groupby("group")
            .median()
            .T
            .to_csv(results_dir / "ablation_summary.csv")
        )

    summaries = {}

    for group in GROUP_ORDER:
        if not (df_features["group"] == group).any():
            continue

        summaries[group] = (
            group_summary(
                df_channels,
                group,
                channel_cols,
                channel_names,
            ),
            group_summary(
                df_features,
                group,
                feature_cols,
                feature_names,
            ),
        )

        for kind, table in zip(
            ("channels", "features"),
            summaries[group],
        ):
            table.to_csv(
                results_dir / f"summary_{kind}_{group}.csv"
            )

    plots_dir = results_dir / "plots"
    plots_dir.mkdir(exist_ok=True)

    channel_label = (
        "Suma temporal de IG con signo"
        if XAI_METHOD == "ig"
        else "Delta logit por canal"
    )

    feature_label = (
        "IG con signo"
        if XAI_METHOD == "ig"
        else "Delta logit por feature"
    )

    if PLOT_RESULTS:
        if PLOT_ORIG_IDXS is not None:
            selected = list(
                dict.fromkeys(
                    int(index)
                    for index in PLOT_ORIG_IDXS
                )
            )
        else:
            selected = [
                int(
                    df_features.loc[
                        df_features["group"] == group,
                        "orig_idx",
                    ].iloc[0]
                )
                for group in GROUP_ORDER
                if (df_features["group"] == group).any()
            ]

        with PdfPages(
            plots_dir / f"{XAI_METHOD}_report.pdf"
        ) as pdf:
            for index in selected:
                row = feature_by_id.loc[index]
                channel_row = channel_by_id.loc[index]
                values = signal[index]

                show_attention = attention is not None

                fig = plt.figure(
                    figsize=(
                        16,
                        13 if show_attention else 11,
                    ),
                    constrained_layout=True,
                )

                grid = fig.add_gridspec(
                    3 if show_attention else 2,
                    2,
                )

                ax_signal = fig.add_subplot(grid[0, :])

                if XAI_METHOD == "occlusion":
                    ax_signal.bar(
                        time_edges[:-1],
                        values,
                        width=np.diff(time_edges),
                        align="edge",
                        color=np.where(
                            values >= 0,
                            "firebrick",
                            "steelblue",
                        ),
                    )
                    ax_signal.axhline(
                        0,
                        color="0.4",
                        linewidth=0.7,
                    )
                    ax_signal.set_ylabel("Delta logit")

                else:
                    limit = max(
                        float(np.abs(values).max()),
                        1e-12,
                    )

                    image = ax_signal.imshow(
                        values.T,
                        origin="lower",
                        aspect="auto",
                        cmap="RdBu_r",
                        vmin=-limit,
                        vmax=limit,
                        rasterized=True,
                        extent=[
                            0,
                            values.shape[0] / fs,
                            -0.5,
                            len(channel_names) - 0.5,
                        ],
                    )

                    ax_signal.set_yticks(
                        range(len(channel_names))
                    )
                    ax_signal.set_yticklabels(
                        channel_names,
                        fontsize=8,
                    )

                    fig.colorbar(
                        image,
                        ax=ax_signal,
                        label="IG con signo",
                    )

                ax_signal.set_xlabel(
                    "Tiempo dentro de la ventana (s)"
                )

                if show_attention:
                    ax_time = fig.add_subplot(grid[1, :])

                    importance = np.abs(values).sum(axis=1)

                    ax_time.plot(
                        np.arange(len(importance)) / fs,
                        importance / max(
                            float(importance.max()),
                            1e-12,
                        ),
                        label="IG absoluto",
                    )

                    ax_time.plot(
                        np.arange(len(importance)) / fs,
                        attention[index],
                        label="Atención × gradiente",
                    )

                    ax_time.legend()

                plot_bars(
                    fig.add_subplot(grid[-1, 0]),
                    channel_row[channel_cols].to_numpy(float),
                    channel_names,
                    "Canales",
                    channel_label,
                )

                plot_bars(
                    fig.add_subplot(grid[-1, 1]),
                    row[feature_cols].to_numpy(float),
                    feature_names,
                    "Características",
                    feature_label,
                )

                fig.suptitle(
                    f"{METHOD_LABEL[XAI_METHOD]} | "
                    f"Ventana {index} | "
                    f"{GROUP_LABEL[row['group']]}\n"
                    f"Real={int(row['y_true'])}; "
                    f"pred={int(row['y_pred'])}; "
                    f"P={row['prob_crisis']:.4f}"
                )

                pdf.savefig(fig)

                fig.savefig(
                    plots_dir
                    / f"{XAI_METHOD}_window_{index}.pdf"
                )

                plt.close(fig)

            for group, (channel_table, feature_table) in (
                summaries.items()
            ):
                fig, axes = plt.subplots(
                    1,
                    2,
                    figsize=(16, 9),
                    constrained_layout=True,
                )

                plot_bars(
                    axes[0],
                    channel_table["median"],
                    channel_names,
                    "Canales",
                    channel_label,
                    (
                        channel_table["ci_lo"],
                        channel_table["ci_hi"],
                    ),
                )

                plot_bars(
                    axes[1],
                    feature_table["median"],
                    feature_names,
                    "Características",
                    feature_label,
                    (
                        feature_table["ci_lo"],
                        feature_table["ci_hi"],
                    ),
                )

                count = int(
                    (df_features["group"] == group).sum()
                )

                fig.suptitle(
                    f"{GROUP_LABEL[group]} | "
                    f"{count} ventanas | "
                    "Mediana por paciente e IC95% bootstrap"
                )

                pdf.savefig(fig)

                fig.savefig(
                    plots_dir
                    / f"{XAI_METHOD}_group_{group}.pdf"
                )

                plt.close(fig)

    # Relación entre valor de feature escalada y atribución.
    indices = df_features["orig_idx"].to_numpy(dtype=int)

    Z = ds["features"][indices]
    A = df_features[feature_cols].to_numpy()

    for group in GROUP_ORDER:
        mask = (
            df_features["group"] == group
        ).to_numpy()

        if mask.sum() < 10:
            continue

        data = df_features.loc[mask].reset_index(drop=True)
        zg = Z[mask]
        ag = A[mask]

        correlations = {}

        for patient, patient_indices in (
            data.groupby("patient").indices.items()
        ):
            if len(patient_indices) >= 10:
                correlations[patient] = [
                    spearmanr(
                        zg[patient_indices, j],
                        ag[patient_indices, j],
                    ).correlation
                    for j in range(len(feature_names))
                ]

        correlation_table = pd.DataFrame(
            correlations,
            index=feature_names,
        ).T

        pd.DataFrame(
            {
                "rho_median": correlation_table.median(),
                "n_patients": (
                    correlation_table.notna().sum()
                ),
                "mean_abs_attr": np.abs(ag).mean(axis=0),
            },
            index=feature_names,
        ).to_csv(
            results_dir
            / f"direction_features_{group}.csv"
        )

        if PLOT_RESULTS:
            top = min(15, len(feature_names))

            order = np.argsort(
                np.abs(ag).mean(axis=0)
            )[-top:]

            fig, ax = plt.subplots(
                figsize=(8, 0.4 * top + 2)
            )

            rng = np.random.default_rng(SEED)

            for line, j in enumerate(order):
                scatter = ax.scatter(
                    ag[:, j],
                    line + rng.uniform(
                        -0.25,
                        0.25,
                        len(ag),
                    ),
                    c=np.clip(zg[:, j], -3, 3),
                    cmap="coolwarm",
                    vmin=-3,
                    vmax=3,
                    s=6,
                    alpha=0.6,
                    rasterized=True,
                )

            ax.set_yticks(range(top))
            ax.set_yticklabels(
                [feature_names[j] for j in order],
                fontsize=8,
            )

            ax.axvline(
                0,
                color="0.4",
                linewidth=0.7,
            )

            ax.set(
                xlabel=feature_label,
                title=(
                    f"{GROUP_LABEL[group]} | "
                    f"{len(ag)} ventanas"
                ),
            )

            fig.colorbar(
                scatter,
                ax=ax,
                label="Valor de feature escalada",
            )

            fig.tight_layout()

            fig.savefig(
                plots_dir
                / f"{XAI_METHOD}_beeswarm_{group}.pdf"
            )

            plt.close(fig)


def main():
    if (
        XAI_METHOD not in METHOD_LABEL
        or BATCH_SIZE < 1
        or IG_STEPS < 1
        or OCC_WINDOW_SEC <= 0
    ):
        raise ValueError(
            "Revisa método, batch size, "
            "pasos IG y ventana de oclusión."
        )

    random.seed(SEED)
    np.random.seed(SEED)
    torch.manual_seed(SEED)

    if torch.cuda.is_available():
        torch.cuda.manual_seed_all(SEED)

    config = read_json(CONFIG_PATH)
    ds = load_inputs(DATA_PATH)

    if XAI_METHOD == "ig":
        settings_tag = (
            f"threshold_{THRESHOLD:g}"
            f"_joint_steps_{IG_STEPS}_baseline_0"
        )
    else:
        settings_tag = (
            f"threshold_{THRESHOLD:g}"
            f"_window_{OCC_WINDOW_SEC:g}s"
            f"_baseline_{BASELINE_VALUE:g}"
        )

    results_dir = (
        RESULTS_ROOT
        / RUN_ID
        / XAI_METHOD
        / settings_tag
    )

    results_dir.mkdir(
        parents=True,
        exist_ok=True,
    )

    # Detecta cambios sin calcular una huella
    # de los 18 GiB completos de EEG.
    input_stats = {
        name: {
            "size": (DATA_PATH / name).stat().st_size,
            "mtime_ns": (DATA_PATH / name).stat().st_mtime_ns,
        }
        for name in (
            "windows_np.npy",
            "features_scaled.npy",
            "labels_np.npy",
        )
    }

    signature = {
        "implementation": "streaming-xai-v1",
        "method": XAI_METHOD,
        "model_sha256": file_hash(MODEL_PATH),
        "config_sha256": file_hash(CONFIG_PATH),
        "dataset_meta_sha256": file_hash(
            DATA_PATH / "meta.json"
        ),
        "input_files": input_stats,
        "dataset_path": str(DATA_PATH),
        "threshold": THRESHOLD,
        "ig_steps": IG_STEPS,
        "ig_internal_bs": IG_INTERNAL_BS,
        "occlusion_window_sec": OCC_WINDOW_SEC,
        "baseline": BASELINE_VALUE,
        "compute_attention": COMPUTE_ATTN,
        "compute_fidelity": COMPUTE_FIDELITY,
        "compute_ablation": COMPUTE_ABLATION,
        "fid_fracs": list(FID_FRACS),
        "seed": SEED,
        "batch_size": BATCH_SIZE,
        "n_windows": len(ds["windows"]),
    }

    complete_path = results_dir / "completed.json"

    if complete_path.exists() and not FORCE_RECALCULATE:
        if read_json(complete_path) != signature:
            raise RuntimeError(
                "Los resultados pertenecen a otra configuración. "
                "Cambia RUN_ID."
            )

        print(
            "Cargando resultados completos existentes.",
            flush=True,
        )

        df_features = pd.read_parquet(
            results_dir / "features.parquet"
        )
        df_channels = pd.read_parquet(
            results_dir / "channels.parquet"
        )

    else:
        complete_path.unlink(missing_ok=True)

        df_features, df_channels = calculate(
            ds,
            config,
            results_dir,
            signature,
        )

    reports(
        ds,
        df_features,
        df_channels,
        results_dir,
    )

    print(
        "Resultados:",
        results_dir,
        flush=True,
    )


if __name__ == "__main__":
    main()