"""
# File: cnn_artifact_detector.py
# Project: Trabajo de graduación
# Author: Maria Fernanda Andrade Recinos

Reusable CNN (1D Convolutional networks) modules for the AI pipeline.
"""
# cnn_artifact_detector.py

# General imports
import json
import psutil
import random
import logging
import argparse
import hashlib, shutil
from pathlib import Path
from typing import Optional, Dict, Any, Tuple, Literal
from collections import OrderedDict

# Data libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Model imports
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.utils.data import Dataset, DataLoader
from sklearn.metrics import (
    classification_report, confusion_matrix, roc_curve,
    precision_recall_curve, accuracy_score, precision_score,
    recall_score, f1_score, average_precision_score, balanced_accuracy_score, roc_auc_score, auc,
)
from tqdm import tqdm

from src.utils.session_cache import get_or_compute_session
from src.utils.artifacts_eval import artifact_channel_masks, MedicalEval
from src.models.ml_models import (
    find_best_threshold, compute_full_metrics
)
from src.core.data_config import NORMALIZE, NORMALIZE_CLIP

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
print(f"[INFO] Using device: {device}")

KEY = ["Patient", "Session", "Section", "Start"]
REQUIRED_COLS = KEY + ["end", "EDF_path", "split"]
DEBUG = True

## DEBUGGING Secondary Functions
def _check_columns(df, target_col):
    missing = [c for c in REQUIRED_COLS + [target_col] if c not in df.columns]
    assert not missing, (
        f"windowed_df no tiene las columnas {missing}. "
        f"Columnas disponibles: {sorted(df.columns)}. "
        "Si vienen del dataset de features, haz merge con las ventanas originales."
    )
    assert df["split"].isin(["train", "val", "test"]).all(), \
        f"Valores de split inesperados: {df['split'].unique()}"


class TrainingInterrupted(RuntimeError):
    """Checkpoint saved, training stopped"""

def set_seed(seed: int) -> None:
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)

def covered_days(n_windows: int, stride_sec: float) -> float:
    return n_windows * stride_sec / 86400

def cap_threshold_for_fp(y_val, p_val, thr, max_fp_per_day, stride_sec):
    days = covered_days(len(y_val), stride_sec)
    k = int(np.floor(max_fp_per_day * days))          # FP permitidos
    neg = np.sort(p_val[y_val == 0].astype(np.float64))
    if k >= len(neg):
        return thr, False
    t = float(np.nextafter(neg[len(neg) - k - 1], np.inf))  # deja <= k negativos con p >= t
    return (t, True) if t > thr else (thr, False)


# Thresholding
def select_f1_optimal_threshold(y_true: np.ndarray, y_proba: np.ndarray) -> Tuple[float, int]:
    precision, recall, thresholds = precision_recall_curve(y_true, y_proba)
    f1_scores = 2 * (precision[:-1] * recall[:-1]) / (precision[:-1] + recall[:-1] + 1e-8)
    best_idx = int(np.nanargmax(f1_scores))
    return float(thresholds[best_idx]), best_idx


def select_operating_threshold(
    y_val: np.ndarray, y_proba_val: np.ndarray,
    mode: Literal["youden", "fixed_spec", "max_tpr_at_fpr"] = "youden",
    fixed_spec: float = 0.95, max_fpr: float = 0.10,
) -> Tuple[float, str]:
    fpr, tpr, thr_roc = roc_curve(y_val, y_proba_val)
    chosen_thr = thr_roc[np.argmax(tpr - fpr)]
    chosen_mode = "youden"

    if mode == "fixed_spec":
        spec = 1 - fpr
        mask = spec >= fixed_spec
        if np.any(mask):
            idx = np.argmax(tpr[mask])
            chosen_thr = thr_roc[mask][idx]
            chosen_mode = f"fixed_spec@{fixed_spec:.2f}"
        else:
            chosen_mode = "youden(fallback)"
    elif mode == "max_tpr_at_fpr":
        mask = fpr <= max_fpr
        if np.any(mask):
            idx = np.argmax(tpr[mask])
            chosen_thr = thr_roc[mask][idx]
            chosen_mode = f"max_tpr_at_fpr<={max_fpr:.2f}"
        else:
            chosen_mode = "youden(fallback)"

    if not np.isfinite(chosen_thr):
        chosen_thr, chosen_mode = 0.5, f"thr05({chosen_mode}_inf)"

    return float(chosen_thr), chosen_mode


def partial_roc_auc(y_true, y_score, max_fpr=0.1):
    """Calcula el área bajo la curva ROC truncada a un FPR máximo sin normalizar."""
    fpr, tpr, _ = roc_curve(y_true, y_score)
    
    # Filtrar hasta el max_fpr
    stop_index = np.searchsorted(fpr, max_fpr, side='right')
    fpr_partial = fpr[:stop_index]
    tpr_partial = tpr[:stop_index]
    
    # Interpolar el punto exacto en max_fpr para mayor precisión
    if len(fpr_partial) > 0 and fpr_partial[-1] < max_fpr:
        tpr_interp = np.interp(max_fpr, fpr, tpr)
        fpr_partial = np.append(fpr_partial, max_fpr)
        tpr_partial = np.append(tpr_partial, tpr_interp)
        
    return auc(fpr_partial, tpr_partial)

def prevalence_adjusted_pr_auc(y_true, y_score):
    """Calcula el PR-AUC estandarizado a una prevalencia del 50% (1:1)."""
    fpr, tpr, _ = roc_curve(y_true, y_score)
    # Al estandarizar a prevalencia 1:1, TP = TPR y FP = FPR
    # Por lo tanto, Precision_adj = TPR / (TPR + FPR)
    with np.errstate(divide='ignore', invalid='ignore'):
        precision_adj = np.divide(tpr, tpr + fpr)
    
    # Corregir los casos donde TPR+FPR == 0 (inicio de la curva)
    precision_adj[np.isnan(precision_adj)] = 1.0 
    
    # El área se calcula bajo la curva Recall (TPR) vs Precision ajustada
    return auc(tpr, precision_adj)

def extra_metrics(y_true, y_pred, y_prob):
    return {
        "AP": round(float(average_precision_score(y_true, y_prob)), 4),
        "balanced_accuracy": round(float(balanced_accuracy_score(y_true, y_pred)), 4),
        "pROC_0.1": round(float(partial_roc_auc(y_true, y_prob, 0.1)), 4),
        "adj_PR_AUC": round(float(prevalence_adjusted_pr_auc(y_true, y_prob)), 4),
    }


# Loss
class FocalLossWithClassWeights(nn.Module):
    """Binary focal loss with class weights."""

    def __init__(self, alpha: float = 0.25, gamma: float = 2.0,
                 class_weights: Optional[Dict[int, float]] = None):
        super().__init__()
        self.alpha = alpha
        self.gamma = gamma
        self.class_weights = class_weights or {0: 1.0, 1: 1.0}

    def forward(self, logits: torch.Tensor, targets: torch.Tensor, valid: Optional[torch.Tensor] = None) -> torch.Tensor:
        probs = torch.sigmoid(logits)
        bce = F.binary_cross_entropy_with_logits(logits, targets, reduction="none")
        p_t = probs * targets + (1 - probs) * (1 - targets)
        focal_weight = (1 - p_t) ** self.gamma
        alpha_t = self.alpha * targets + (1 - self.alpha) * (1 - targets)
        class_w = self.class_weights[1] * targets + self.class_weights[0] * (1 - targets)
        loss = alpha_t * focal_weight * class_w * bce
        if valid is None:
            return loss.mean()
        m = valid.view(-1, *([1] * (loss.dim() - 1))).expand_as(loss)
        return (loss * m).sum() / m.sum().clamp(min=1)


# Early stopping
class EarlyStopping:
    """Stops training according to F1 validation improvement by epochs `patience`."""

    def __init__(self, patience: int = 10, restore_best_weights: bool = True, verbose: bool = True, metric: str = "AP"):
        self.patience = patience
        self.restore_best_weights = restore_best_weights
        self.verbose = verbose
        self.metric = metric
        self.best_score = -float("inf")
        self.wait = 0
        self.best_state: Optional[dict] = None
        self.should_stop = False

    def step(self, current_score: float, model, epoch: int) -> None:
        import copy
        if current_score > self.best_score:
            self.best_score = current_score
            self.wait = 0
            if self.restore_best_weights:
                self.best_state = copy.deepcopy(model.state_dict())
        else:
            self.wait += 1
            if self.wait >= self.patience:
                if self.verbose:
                    print(f"\nEpoch {epoch + 1}: early stopping (metric {self.metric.upper()} without improvement in {self.patience} epochs)")
                self.should_stop = True
                if self.restore_best_weights and self.best_state is not None:
                    model.load_state_dict(self.best_state)


# Model: By window and channel
class ArtifactCNN(nn.Module):
    """
    Reusable generic binary CNN for artefact detection.
    (B, 18, T) -> logits (B, 18).
    """

    def __init__(self, input_shape: Tuple[int, int], model_type = "lightweight", per_channel=False):
        super().__init__()
        n_channels, n_timesteps = input_shape
        self.model_type = model_type
        self.per_channel = per_channel

        # Backbone
        if model_type == "lightweight":
            self.conv = nn.Sequential(
                nn.Conv1d(n_channels, 16, kernel_size=5, padding=2),
                nn.ReLU(),
                nn.MaxPool1d(2),
            )
            out_ch = 16
        elif model_type == "paper":
            blocks, in_ch = [], n_channels
            for out_c in (16, 32, 64, 128):
                blocks += [
                    nn.Conv1d(in_ch, out_c, kernel_size=5, padding=2),
                    nn.ReLU(),
                    nn.MaxPool1d(2),
                ]
                in_ch = out_c
            self.conv = nn.Sequential(*blocks)
            out_ch = out_c
        elif model_type == "standard":
            blocks, in_ch = [], n_channels
            for out_c in (32, 64, 128):
                blocks += [
                    nn.Conv1d(in_ch, out_c, kernel_size=3, padding=1),
                    nn.BatchNorm1d(out_c),
                    nn.ReLU(),
                    nn.MaxPool1d(3),
                    nn.Dropout(0.3),
                ]
                in_ch = out_c
            self.conv = nn.Sequential(*blocks)
            out_ch = in_ch
        else:
            raise ValueError(f"Unknown model_type: {model_type}")

        # Channels analysis
        if per_channel:
            self.head = nn.Conv1d(out_ch, n_channels, kernel_size=1)
        else:
            self.pool = nn.AdaptiveAvgPool1d(1)

        # Classifier by type
        if model_type == "lightweight":
            self.classifier = nn.Sequential(nn.Flatten(), nn.Linear(out_ch, 16), nn.ReLU(), nn.Linear(16, 1))
        elif model_type == "paper":
            self.classifier = nn.Sequential(nn.Flatten(), nn.Linear(out_ch, 16), nn.ReLU(), nn.Linear(16,1))
        else:
            self.classifier = nn.Sequential(
                nn.Flatten(),
                nn.Linear(out_ch, 128), nn.ReLU(), nn.BatchNorm1d(128), nn.Dropout(0.3),
                nn.Linear(128, 64), nn.ReLU(), nn.BatchNorm1d(64), nn.Dropout(0.3),
                nn.Linear(64, 1),
            )
       


    def forward(self, x: torch.Tensor) -> torch.Tensor:
        x = self.conv(x)
        if self.per_channel:
            return self.head(x).amax(dim=-1)                    # (B, 18)
        return self.classifier(self.pool(x)).squeeze(-1)        # (B,)


# Dataset
class EEGWindowDataset(Dataset):
    """
    Dataset to extract raw signal windows with splitted windowed_df.
    """

    def __init__(self, windowed_df: pd.DataFrame, target_col: str,
                 session_cache_dir: str = "cache/sessions", 
                 ica_cache_dir: str = "cache/ica",
                 max_cached_sessions: Optional[int] = 320,
                 cache_memory_fraction: float = 0.3,
                 expected_n_timesteps: Optional[int] = None,
                 ann_by_session = None,
                 keywords = None,
                 bip_names = None,
                 ):
        self.df = windowed_df.reset_index(drop=True)
        missing = [c for c in KEY + ["end", "EDF_path", target_col] if c not in self.df.columns]
        assert not missing, f"EEGWindowDataset: faltan columnas {missing}"
        self.target_col = target_col
        self.session_cache_dir = session_cache_dir
        self.ica_cache_dir = ica_cache_dir
        self.cache_memory_fraction = cache_memory_fraction
        self.max_cached_sessions = max_cached_sessions
        self.expected_n_timesteps = expected_n_timesteps
        self._session_cache: "OrderedDict[tuple, dict]" = OrderedDict()
        self._estimated_session_bytes: Optional[int] = None
        self._truncated_count = 0
        self.ann = ann_by_session
        self.keywords = keywords
        self.bip_names = bip_names

    def __len__(self) -> int:
        return len(self.df)

    def _get_session(self, patient, session, section, path_edf):
        key = (patient, session, section)
        if key in self._session_cache:
            self._session_cache.move_to_end(key)
            self._cache_hits = getattr(self, "_cache_hits", 0) + 1
            return self._session_cache[key]

        self._cache_misses = getattr(self, "_cache_misses", 0) + 1
        data = get_or_compute_session(
            patient, session, section, path_edf,
            cache_dir=self.session_cache_dir,
            ica_cache_dir = self.ica_cache_dir,
            use_ica=False,
            bipolar_montage=True,
        )

        if self._estimated_session_bytes is None:
            if self.max_cached_sessions is None:
                available_bytes = psutil.virtual_memory().available
                budget = available_bytes * self.cache_memory_fraction
                self.max_cached_sessions = max(1, int(budget // data["data"].nbytes))
                self.logger_max_cached_sessions_msg = (
                    f"[INFO] Calculated max_cached_sessions:"
                    f"{self.max_cached_sessions} (session={data['data'].nbytes/1e6:.1f}MB,)"
                    f"budget: {budget/1e9:.2f}GB"
                )
                print(self.logger_max_cached_sessions_msg)

        self._session_cache[key] = data
        if self.max_cached_sessions != None and len(self._session_cache) > self.max_cached_sessions:
            self._session_cache.popitem(last=False)

        return data

    def _normalize_stats(self, s):
        if "_norm" not in s:
            x = s["data"][:, ::10]
            med = np.median(x, axis=1, keepdims=True)
            q75, q25 = np.percentile(x, [75,25], axis=1)
            scale = np.maximum((q75 - q25)[:, None]/1.349, 1e-12)
            s["_norm"] = (med.astype(np.float32), scale.astype(np.float32))
        return s["_norm"]
    
    def __getitem__(self, idx):
        row = self.df.iloc[idx]
        s = self._get_session(row.Patient, row.Session, row.Section, row.EDF_path)
        start = int(round(row.Start * s["sfreq"]))
        end = int(round(row.end * s["sfreq"]))
        window = s["data"][:, start:end]

        if NORMALIZE: 
            med, scale = self._normalize_stats(s)
            window = (window - med) / scale
            window = np.clip(window, -NORMALIZE_CLIP, NORMALIZE_CLIP)

        if self.expected_n_timesteps is not None and window.shape[1] != self.expected_n_timesteps:
            self._truncated_count += 1
            n_channels = window.shape[0] 
            padded = np.zeros((n_channels, self.expected_n_timesteps), dtype=window.dtype)
            n_copy = min(window.shape[1], self.expected_n_timesteps)
            padded[:, :n_copy] = window[:, :n_copy]
            window = padded

        y_win = float(getattr(row, self.target_col)) 
        if self.ann is not None:
            if "_Y" not in s:  
                s["_Y"] = artifact_channel_masks(
                        self.ann[(row.Patient, row.Session, row.Section)],
                        self.keywords, s["data"].shape[1], s["sfreq"], self.bip_names
                    )
            y_ch = s["_Y"][:, start:end].any(axis=1)                   # (18,)
            valid = not (y_win > 0 and not y_ch.any())                 # positiva sin canal mapeable -> fuera
            return (torch.tensor(window, dtype=torch.float32),
                    torch.tensor(y_ch, dtype=torch.float32),
                    torch.tensor(float(valid)),
                    torch.tensor(y_win, dtype=torch.float32))

        label = float(getattr(row, self.target_col))
        return torch.tensor(window, dtype=torch.float32), torch.tensor(label, dtype=torch.float32)


# Main detector
class ArtifactDetector:
    """
    Generic binary CNN detector (eye / muscle / non_physiological).
    """

    def __init__(self, artifact_name: str, model_type: str = "lightweight",
                 device: Optional[str] = None, verbose: bool = True, results_dir: str = "models_cnn"):
        self.artifact_name = artifact_name
        self.model_type = model_type
        self.device = device or ("cuda" if torch.cuda.is_available() else "cpu")
        self.verbose = verbose
        self.model: Optional[nn.Module] = None
        self.history: Dict[str, list] = {"loss": [], "val_loss": [], "val_f1": []}
        self.logger = logging.getLogger(f"ArtifactDetector[{artifact_name}]")
        if not verbose:
            self.logger.setLevel(logging.WARNING)
        self.results_dir = Path(results_dir) / f"cnn_{artifact_name}"
        self.results_dir.mkdir(parents=True, exist_ok=True)

    def build_model(self, n_channels: int, n_timesteps: int, per_channel=False) -> nn.Module:
        self.input_shape = (n_channels, n_timesteps)
        self.model = build_model_for_artifact((n_channels, n_timesteps), self.model_type, per_channel=per_channel).to(self.device)
        n_params = sum(p.numel() for p in self.model.parameters())
        self.logger.info(f"Model({self.model_type}). Parameters: {n_params:,}")
        return self.model

    def train(self, train_loader: DataLoader, 
              val_loader: DataLoader,
              epochs: int = 100, 
              lr: float = 1e-3, 
              patience: int = 10, 
              patience_lr: int = 3,
              class_weights: Optional[Dict[int, float]] = None,
              focal_params: Optional[Dict[str, float]] = None,
              checkpoints_dir: str = "/workspace/checkpoints",
              use_class_weights = True,
              early_stop_metric: str = "ap"         # "ap" | "f1"
        ) -> Dict[str, list]:

        assert early_stop_metric in ("ap", "f1")

        ds = train_loader.dataset
        all_train_labels = ds.df[ds.target_col].to_numpy().astype(int)

        hits = getattr(train_loader.dataset, "_cache_hits", 0)
        misses = getattr(train_loader.dataset, "_cache_misses", 0)
        total = hits + misses
        if total > 0:
            print(f"[CACHE] hits={hits} | misses={misses} | hit_rate={hits/total:.2%}")

        neg_count = (all_train_labels == 0).sum()
        pos_count = (all_train_labels == 1).sum()
        total = neg_count + pos_count

        calculated_class_weights = {
            0: total / (2.0 * neg_count) if neg_count > 0 else 1.0,
            1: total / (2.0 * pos_count) if pos_count > 0 else 1.0
        }
        self.logger.info(f"Pesos de clase calculados para el entrenamiento: {calculated_class_weights}")

        focal_params = focal_params or {"alpha": 0.25, "gamma": 2.0}

        if use_class_weights:
            pos = tot = 0.0
            for _, y_ch, valid, _ in train_loader:
                m = valid[:, None].expand_as(y_ch)
                pos += (y_ch * m).sum().item(); tot += m.sum().item()
            class_weights = {0: tot / (2 * max(tot - pos, 1)), 1: tot / (2 * max(pos, 1))}
            # class_weights = class_weights or calculated_class_weights
        else:
            class_weights = None 

        criterion = FocalLossWithClassWeights(**focal_params, class_weights=class_weights)
        optimizer = torch.optim.Adam(self.model.parameters(), lr=lr)
        scheduler = torch.optim.lr_scheduler.ReduceLROnPlateau(
            optimizer, mode="min", factor=0.7, patience=patience_lr, min_lr=1e-7
        )
        early_stopper = EarlyStopping(patience=patience, verbose=self.verbose, metric=early_stop_metric)
        self.history.setdefault("val_ap", [])

        ckpt_dir = Path(checkpoints_dir) / f"cnn_{self.artifact_name}"
        ckpt_dir.mkdir(parents=True, exist_ok=True)
        latest_path = ckpt_dir / "latest.pt"
        best_path = ckpt_dir / "best_score.pt"

        start_epoch = 0
        if latest_path.exists():
            ckpt = torch.load(latest_path, map_location=self.device, weights_only=False)
            if ckpt.get("early_stop_metric") != early_stop_metric:
                self.logger.warning("Checkpoint con otra métrica de selección: Se debe ignorar y reentrenar el modelo.")
            else:
                self.model.load_state_dict(ckpt["model_state"])
                optimizer.load_state_dict(ckpt["optimizer_state"])
                scheduler.load_state_dict(ckpt["scheduler_state"])
                early_stopper.best_score = ckpt["early_stopper_best_score"]
                early_stopper.wait = ckpt["early_stopper_wait"]
                early_stopper.best_state = ckpt["early_stopper_best_state"]
                self.history = ckpt["history"]
                start_epoch = ckpt["epoch"] + 1
                self.logger.info(f"Resuming from {start_epoch} epoch (best_score={early_stopper.best_score:.4f})")
                self.history = ckpt["history"]
                self.history.setdefault("val_ap", [])

        self.logger.info(f"Starting training: epochs={epochs}")

        import signal
        _interrupted = {"flag": False}
        def _handle_sigterm(signum, frame):
            _interrupted["flag"] = True
        signal.signal(signal.SIGTERM, _handle_sigterm)

        for epoch in range(start_epoch, epochs):
            if _interrupted["flag"]:
                self.logger.warning(f"SIGTERM received, stopping at {epoch} epoch")
                break

            self.model.train()
            train_loss = 0.0
            train_bar = tqdm(train_loader, desc=f"[{self.artifact_name}] Epoch {epoch+1}/{epochs} [train]", leave=False)
            
            for X_batch, y_batch, valid, _ in train_bar:
                X_batch, y_batch, valid = X_batch.to(self.device), y_batch.to(self.device), valid.to(self.device)
                optimizer.zero_grad()
                logits = self.model(X_batch)
                loss = criterion(logits, y_batch, valid)
                loss.backward()
                optimizer.step()
                train_loss += loss.item()
                train_bar.set_postfix(loss=f"{loss.item():.4f}")


            train_loss /= len(train_loader)

            self.model.eval()
            val_loss, all_probs, all_true = 0.0, [], []
            val_bar = tqdm(val_loader, desc=f"[{self.artifact_name}] Epoch {epoch+1}/{epochs} [val]", leave=False)

            with torch.no_grad():
                for X_batch, y_ch, valid, y_win in val_bar:
                    X_batch, y_ch, valid = X_batch.to(self.device), y_ch.to(self.device), valid.to(self.device)
                    logits = self.model(X_batch)
                    batch_val_loss = criterion(logits, y_ch, valid).item()
                    val_bar.set_postfix(loss=f"{batch_val_loss:.4f}")
                    all_probs.append(torch.sigmoid(logits).cpu().numpy())   # (B, 18)
                    all_true.append(y_win.numpy()) 
                    val_loss += batch_val_loss
            val_loss /= len(val_loader)

            y_proba_val = np.concatenate(all_probs).max(1)
            y_true_val = np.concatenate(all_true).astype(int)
            if y_true_val.sum() > 0:
                val_ap = average_precision_score(y_true_val, y_proba_val)
                best_thr, _ = select_f1_optimal_threshold(y_true_val, y_proba_val)
                val_f1 = f1_score(y_true_val, (y_proba_val >= best_thr).astype(int), zero_division=0)
            else:
                val_ap = val_f1 = 0.0

            self.history["loss"].append(train_loss)
            self.history["val_loss"].append(val_loss)
            self.history["val_f1"].append(val_f1)
            self.history["val_ap"].append(val_ap)

            if self.verbose:
                print(f"[{self.artifact_name}] Epoch {epoch+1}/{epochs} - loss={train_loss:.4f} "
                    f"val_loss={val_loss:.4f} val_ap={val_ap:.4f} val_f1={val_f1:.4f} (selección: {early_stop_metric})")

            n_trunc_train = getattr(train_loader.dataset, "_truncated_count", 0)
            n_trunc_val = getattr(val_loader.dataset, "_truncated_count", 0)
            if n_trunc_train or n_trunc_val:
                self.logger.warning(f"Small windows (padding): train={n_trunc_train}, val={n_trunc_val}")
            train_loader.dataset._truncated_count = 0
            val_loader.dataset._truncated_count = 0

            scheduler.step(val_loss)

            val_score = val_ap if early_stop_metric == "ap" else val_f1
            was_best = val_score > early_stopper.best_score
            early_stopper.step(val_score, self.model, epoch)

            if was_best:
                torch.save(self.model.state_dict(), best_path)

            torch.save({
                "epoch": epoch,
                "model_state": self.model.state_dict(),
                "optimizer_state": optimizer.state_dict(),
                "scheduler_state": scheduler.state_dict(),
                "early_stop_metric": early_stop_metric,
                "early_stopper_best_score": early_stopper.best_score,
                "early_stopper_wait": early_stopper.wait,
                "early_stopper_best_state": early_stopper.best_state,
                "history": self.history,
            }, latest_path)

            if early_stopper.should_stop:
                break

        if early_stopper.best_state is not None:
            self.model.load_state_dict(early_stopper.best_state)
        elif best_path.exists():
            self.model.load_state_dict(torch.load(best_path, map_location=self.device, weights_only=True))

        if _interrupted["flag"]:
            self.logger.warning("Interrumpido por SIGTERM: checkpoint guardado, sin evaluar.")
            raise TrainingInterrupted(self.artifact_name)

        self.logger.info("Training completed.")
        return self.history

    def _predict_proba(self, loader: DataLoader) -> Tuple[np.ndarray, np.ndarray]:
        self.model.eval()
        probs, trues = [], []
        with torch.no_grad():
            for X_batch, y_batch in loader:
                logits = self.model(X_batch.to(self.device))
                probs.append(torch.sigmoid(logits).cpu().numpy().astype(np.float64))
                trues.append(y_batch.numpy())
        return np.concatenate(probs), np.concatenate(trues)

    def _predict(self, loader):
        self.model.eval()
        P, G, V, Y = [], [], [], []
        with torch.no_grad():
            for X, y_ch, valid, y_win in loader:
                P.append(torch.sigmoid(self.model(X.to(self.device))).cpu().numpy().astype(np.float64))
                G.append(y_ch.numpy().astype(bool)); V.append(valid.numpy().astype(bool)); Y.append(y_win.numpy())
        return np.vstack(P), np.vstack(G), np.concatenate(V), np.concatenate(Y)

    def evaluate(self, val_loader: DataLoader,
                test_loader: DataLoader,
                window_size_sec: float,
                stride_sec: float,
                max_fp_per_day: Optional[float] = None,
                medical=None,
        ) -> Dict[str, Any]:

        P_val, G_val, ok_val, y_val = self._predict(val_loader)
        P_test, G_test, ok_test, y_test = self._predict(test_loader)
        y_val, y_test = y_val.astype(int), y_test.astype(int)
        y_proba_val, y_proba_test = P_val.max(1), P_test.max(1)

        # Ventana + 18 canales
        pred_paths = {}
        for name, loader, y, P in (("val", val_loader, y_val, P_val),
                                ("test", test_loader, y_test, P_test)):
            tbl = loader.dataset.df[KEY].copy()
            tbl["y"], tbl["p"] = y, P.max(1)
            for c in range(P.shape[1]):
                tbl[f"p_ch{c}"] = P[:, c]
            path = self.results_dir / f"preds_{name}.parquet"
            tbl.to_parquet(path, index=False)
            pred_paths[name] = str(path)

        chosen_thr, _ = find_best_threshold(y_val, y_proba_val)
        chosen_mode = "fbeta_val"

        # Dataframe
        wt = test_loader.dataset.df[KEY].copy()
        wt["y"], wt["p"] = y_test, y_proba_test

        def _metrics_at(thr: float):
            y_pred = (y_proba_test >= thr).astype(int)
            m = compute_full_metrics(y_test, y_pred, y_proba_test,
                                    window_size_sec, stride_sec,
                                    model_name=self.artifact_name, w=wt)
            m.update(extra_metrics(y_test, y_pred, y_proba_test))
            m["threshold"] = round(float(thr), 4)
            fp_val = ((y_proba_val >= thr) & (y_val == 0)).sum()
            m["val_fp_per_day"] = round(float(fp_val / covered_days(len(y_val), stride_sec)), 2)
            return y_pred, m

        y_pred_test, full_metrics = _metrics_at(chosen_thr)

        # Localización por canal
        if medical is not None:
            tau = medical.pick_tau(P_val[ok_val], G_val[ok_val])
            chan = medical.report_channels_PG(P_test, G_test, ok_test, tau)
            full_metrics.update({f"med_{k}": v for k, v in chan.items()})
            full_metrics["med_ch_tau"] = round(float(tau), 3)

        # Punto secundario con tope de FP/día
        capped_result = None
        if max_fp_per_day is not None and max_fp_per_day < 1000:
            thr_cap, capped = cap_threshold_for_fp(y_val, y_proba_val, chosen_thr, max_fp_per_day, stride_sec)
            _, m_cap = _metrics_at(thr_cap)
            capped_result = {
                "threshold": thr_cap,
                "mode": chosen_mode + ("+fp_cap" if capped else "(cap_not_binding)"),
                "max_fp_per_day": max_fp_per_day,
                "metrics_results": m_cap,
            }

        class_report = classification_report(y_test, y_pred_test,
                                            target_names=["no_" + self.artifact_name, self.artifact_name])
        conf_matrix = confusion_matrix(y_test, y_pred_test)

        if self.verbose:
            print(f"\n{'='*60}\nEVALUATION(TEST) — {self.artifact_name}")
            print(f"Umbral ({chosen_mode}, val): {chosen_thr:.3f}")
            print(class_report)
            print(conf_matrix)
            print(pd.Series(full_metrics).to_string())
            if capped_result is not None:
                print(f"\n-- Con tope {max_fp_per_day} FP/día: thr={capped_result['threshold']:.3f} "
                    f"({capped_result['mode']})")
                print(pd.Series(capped_result["metrics_results"]).to_string())

        return {
            "chosen_threshold": chosen_thr, "chosen_mode": chosen_mode,
            "test_report": class_report, "confusion_matrix": conf_matrix,
            "metrics_results": full_metrics,
            "capped": capped_result,
            "pred_paths": pred_paths,
        }


    def plot_and_save_history(self):
        plt.figure(figsize=(10, 4))

        # Loss (Train vs Val)
        plt.subplot(1, 2, 1)
        plt.plot(self.history["loss"], label="Train Loss")
        plt.plot(self.history["val_loss"], label="Val Loss")
        plt.title(f"Loss - {self.artifact_name}")
        plt.xlabel("Épocas")
        plt.ylabel("Loss")
        plt.legend()

        plt.subplot(1, 2, 2)
        plt.plot(self.history["val_f1"], label="Val F1", color="green")
        if self.history.get("val_ap"):
            plt.plot(self.history["val_ap"], label="Val AP", color="orange")
        plt.title(f"Validación - {self.artifact_name}")
        plt.xlabel("Épocas"); plt.ylabel("Score")
        plt.legend()  

        plt.tight_layout()
        plot_path = self.results_dir / f"cnn_{self.artifact_name}_learning_curves.png"
        plt.savefig(plot_path)
        plt.close()
        self.logger.info(f"Gráfica de evolución guardada en: {plot_path}")

    def save(self, filepath: Optional[str] = None) -> None:
        save_path = Path(filepath) if filepath else self.results_dir / f"cnn_{self.artifact_name}.pt"
        torch.save({
            "state_dict": self.model.state_dict(), 
            "model_type": self.model_type, 
            "input_shape": self.input_shape,
            }, save_path)
        hist_path = self.results_dir / f"cnn_{self.artifact_name}_history.json"
        with open(hist_path, "w", encoding="utf-8") as f:
            json.dump(self.history, f, indent=2)
        self.logger.info(f"Model saved in {self.results_dir}")
        self.plot_and_save_history()

def build_model_for_artifact(input_shape: Tuple[int, int], model_type: str = "lightweight", per_channel=False) -> ArtifactCNN:
    return ArtifactCNN(input_shape=input_shape, model_type=model_type, per_channel=per_channel)

def build_cnn_dataloaders(rf_dataset: pd.DataFrame, target_col: str,
                           session_cache_dir: str, ica_cache_dir: str,
                           batch_size: int = 64, seed: int = 0,
                           expected_n_timesteps: Optional[int] = None,
                           session_ann=None, keywords=None, bip_names=None,
                           ) -> Tuple[DataLoader, DataLoader, DataLoader]:
    """
    Structures the 3 DataLoaders (train/val/test) with windowed dataframes.
    """
    def _loader_for(split_name, shuffle):
        subset = rf_dataset[rf_dataset["split"] == split_name]
        ds = EEGWindowDataset(subset, target_col=target_col,
                              session_cache_dir=session_cache_dir, ica_cache_dir=ica_cache_dir,
                              expected_n_timesteps=expected_n_timesteps, 
                              ann_by_session=session_ann, keywords=keywords, bip_names=bip_names)
        
        gen = torch.Generator().manual_seed(seed) if shuffle else None
        return DataLoader(ds, batch_size=batch_size, shuffle=shuffle, num_workers=0, generator=gen)

    return _loader_for("train", True), _loader_for("val", False), _loader_for("test", False)


def binary_cnn(windowed_df: pd.DataFrame, 
               target_col: str, 
               model_name: str,
               window_size_sec: float, 
               stride_sec: float,
               sfreq: float, 
               n_channels: int,
               session_cache_dir: str, 
               ica_cache_dir: str, 
               models_dir: str = "models_cnn",
               model_type: str = "lightweight", 
               epochs: int = 100, 
               batch_size: int = 64,
               max_fp_per_day: Optional[float] = None,
               seed: int = 0,
               code_version: str = "v1",
               force_retrain: bool = False,
               use_class_weights: bool = True,
               checkpoints_dir: str="/workspace/checkpoints",
               lr: float = 1e-3,
               class_weigths: Optional[Dict[int, float]] = None,
               focal_params: Optional[Dict[str, float]] = None,
               medical = None,
               keywords=None, bip_names=None, session_ann=None,
               early_stop_metric = "ap"
               ) -> Dict[str, Any]:
    """
    Evaluation of each artefact.
    """
    if DEBUG:
        _check_columns(windowed_df, target_col)

    df = windowed_df.drop_duplicates(KEY).copy()
    assert df["EDF_path"].notna().all(), "Hay ventanas sin EDF_path"
    assert (df["end"] > df["Start"]).all(), "Hay ventanas con end <= Start"
    df = df[~((df["split"] != "test") & (df[target_col] == -1))]
    df.loc[df[target_col] == -1, target_col] = 0

    split_fp = hashlib.md5(
        df[["Patient", "split"]].drop_duplicates().sort_values(["Patient", "split"])
        .to_csv(index=False).encode()
        ).hexdigest()[:8]
    
    cfg = dict(model_type=model_type, 
               epochs=epochs, lr=lr, 
               batch_size=batch_size,
               focal_params=focal_params, 
               use_class_weights=use_class_weights,
               window=window_size_sec, 
               stride=stride_sec,
               seed=seed, 
               code_version=code_version, 
               split=split_fp,
               early_stop_metric=early_stop_metric, 
               target_col=target_col, 
               per_channel=True,
               normalize=NORMALIZE, 
               clip=NORMALIZE_CLIP
            )
    
    tag = hashlib.md5(json.dumps(cfg, sort_keys=True, default=str).encode()).hexdigest()[:8]
    model_name = f"{model_name}_{tag}"

    if force_retrain:
        shutil.rmtree(Path(checkpoints_dir) / f"cnn_{model_name}", ignore_errors=True)

    model_dir = Path(models_dir)
    model_dir.mkdir(parents=True, exist_ok=True)
    analysis_path = model_dir / f"cnn_{model_name}_analysis.joblib"

    if analysis_path.exists() and not force_retrain:
        import joblib
        print(f"[INFO] Pretrained model found: {analysis_path}")
        return joblib.load(analysis_path)

    n_timesteps = int(window_size_sec * sfreq)
    set_seed(seed)
    detector = ArtifactDetector(artifact_name=model_name, model_type=model_type, results_dir=models_dir)
    detector.build_model(n_channels=n_channels, n_timesteps=n_timesteps, per_channel = True)

    train_loader, val_loader, test_loader = build_cnn_dataloaders(  df, 
                                                                    target_col, 
                                                                    session_cache_dir, 
                                                                    ica_cache_dir,
                                                                    batch_size=batch_size, 
                                                                    seed=seed, 
                                                                    expected_n_timesteps=n_timesteps,
                                                                    session_ann=session_ann, 
                                                                    keywords=keywords, 
                                                                    bip_names=bip_names
                                                                )

    detector.train(train_loader, 
                   val_loader, 
                   epochs=epochs, 
                   lr=lr,
                   class_weights=class_weigths,
                   focal_params=focal_params,
                   checkpoints_dir=checkpoints_dir,
                   use_class_weights=use_class_weights,
                   early_stop_metric=early_stop_metric,
                   )

    results = detector.evaluate(val_loader, test_loader, window_size_sec=window_size_sec, stride_sec=stride_sec,
                                 max_fp_per_day=max_fp_per_day, medical=medical)
    detector.save()

    import joblib
    joblib.dump(results, analysis_path)
    return results