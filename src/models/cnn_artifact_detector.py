"""
# File: cnn_artifact_detector.py
# Project: Trabajo de graduación
# Author: Maria Fernanda Andrade Recinos

Reusable CNN (1D Convolutional networks) modules for the AI pipeline.
"""

# General imports
import json
import time
import logging
from pathlib import Path
from typing import Optional, Dict, Any, Tuple, Literal

# Data libraries
import numpy as np
import pandas as pd

# Model imports
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.utils.data import Dataset, DataLoader
from sklearn.metrics import (
    classification_report, confusion_matrix, roc_curve,
    precision_recall_curve, accuracy_score, precision_score,
    recall_score, f1_score, auc,
)

from implementation.core.session_cache import get_or_compute_session

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
print(f"[INFO] Using device: {device}")

# Loss

class FocalLossWithClassWeights(nn.Module):
    """Binary focal loss with class weights."""

    def __init__(self, alpha: float = 0.25, gamma: float = 2.0,
                 class_weights: Optional[Dict[int, float]] = None):
        super().__init__()
        self.alpha = alpha
        self.gamma = gamma
        self.class_weights = class_weights or {0: 1.0, 1: 1.0}

    def forward(self, logits: torch.Tensor, targets: torch.Tensor) -> torch.Tensor:
        probs = torch.sigmoid(logits)
        bce = F.binary_cross_entropy_with_logits(logits, targets, reduction="none")
        p_t = probs * targets + (1 - probs) * (1 - targets)
        focal_weight = (1 - p_t) ** self.gamma
        alpha_t = self.alpha * targets + (1 - self.alpha) * (1 - targets)
        class_w = self.class_weights[1] * targets + self.class_weights[0] * (1 - targets)
        loss = alpha_t * focal_weight * class_w * bce
        return loss.mean()


# Early stopping
class F1EarlyStopping:
    """Stops training according to F1 validation improvement by epocsh `patience`."""

    def __init__(self, patience: int = 10, restore_best_weights: bool = True, verbose: bool = True):
        self.patience = patience
        self.restore_best_weights = restore_best_weights
        self.verbose = verbose
        self.best_f1 = -float("inf")
        self.wait = 0
        self.best_state: Optional[dict] = None
        self.should_stop = False

    def step(self, current_f1: float, model, epoch: int) -> None:
        import copy
        if current_f1 > self.best_f1:
            self.best_f1 = current_f1
            self.wait = 0
            if self.restore_best_weights:
                self.best_state = copy.deepcopy(model.state_dict())
        else:
            self.wait += 1
            if self.wait >= self.patience:
                if self.verbose:
                    print(f"\nEpoch {epoch + 1}: early stopping (F1 without improvement in {self.patience} epochs)")
                self.should_stop = True
                if self.restore_best_weights and self.best_state is not None:
                    model.load_state_dict(self.best_state)


# Model
class ArtifactCNN(nn.Module):
    """
    Reusable generic binary CNN for artefact detection.
    """

    def __init__(self, input_shape: Tuple[int, int], model_type: Literal["lightweight", "standard"] = "lightweight"):
        super().__init__()
        n_channels, n_timesteps = input_shape
        self.model_type = model_type

        if model_type == "lightweight":
            self.conv = nn.Sequential(
                nn.Conv1d(n_channels, 16, kernel_size=5, padding=2),
                nn.ReLU(),
                nn.MaxPool1d(2),
            )
            out_ch = 16
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

        self.pool = nn.AdaptiveAvgPool1d(1)

        if model_type == "lightweight":
            self.classifier = nn.Sequential(nn.Flatten(), nn.Linear(out_ch, 16), nn.ReLU(), nn.Linear(16, 1))
        else:
            self.classifier = nn.Sequential(
                nn.Flatten(),
                nn.Linear(out_ch, 128), nn.ReLU(), nn.BatchNorm1d(128), nn.Dropout(0.3),
                nn.Linear(128, 64), nn.ReLU(), nn.BatchNorm1d(64), nn.Dropout(0.3),
                nn.Linear(64, 1),
            )

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        x = self.conv(x)
        x = self.pool(x)
        return self.classifier(x).squeeze(-1)


def build_model_for_artifact(input_shape: Tuple[int, int], model_type: str = "lightweight") -> ArtifactCNN:
    return ArtifactCNN(input_shape=input_shape, model_type=model_type)


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

    return float(chosen_thr), chosen_mode


def compute_full_metrics(y_true, y_pred, y_prob, window_size_sec, model_name="model"):
    """SzCore metrics set for general comparison between models."""
    tn, fp, fn, tp = confusion_matrix(y_true, y_pred, labels=[0, 1]).ravel()
    sensitivity = recall_score(y_true, y_pred, pos_label=1, zero_division=0)
    specificity = tn / (tn + fp) if (tn + fp) > 0 else np.nan
    precision = precision_score(y_true, y_pred, pos_label=1, zero_division=0)
    accuracy = accuracy_score(y_true, y_pred)
    f1 = f1_score(y_true, y_pred, pos_label=1, zero_division=0)
    false_alarm_rate = fp / (fp + tn) if (fp + tn) > 0 else np.nan

    try:
        from sklearn.metrics import roc_auc_score
        auc_roc = roc_auc_score(y_true, y_prob)
    except ValueError:
        auc_roc = np.nan

    total_time_sec = len(y_true) * window_size_sec
    total_time_days = total_time_sec / 86400
    fp_per_day = fp / total_time_days if total_time_days > 0 else np.nan

    return {
        "model": model_name, "sensitivity": round(sensitivity, 4), "specificity": round(specificity, 4),
        "precision": round(precision, 4), "accuracy": round(accuracy, 4), "f1_score": round(f1, 4),
        "auc_roc": round(auc_roc, 4) if not np.isnan(auc_roc) else np.nan,
        "false_alarm_rate": round(false_alarm_rate, 4), "fp_per_day": round(fp_per_day, 2),
        "TP": int(tp), "FP": int(fp), "TN": int(tn), "FN": int(fn),
        "n_test_windows": len(y_true), "covered_test_hours": round(total_time_sec / 3600, 2),
    }


# Dataset
class EEGWindowDataset(Dataset):
    """
    Dataset to extract raw signal windows with splitted windowed_df.
    """

    def __init__(self, windowed_df: pd.DataFrame, target_col: str,
                 session_cache_dir: str = "cache/sessions", ica_cache_dir: str = "cache/ica"):
        self.df = windowed_df.reset_index(drop=True)
        self.target_col = target_col
        self.session_cache_dir = session_cache_dir
        self.ica_cache_dir = ica_cache_dir
        self._cached_key = None
        self._cache = None

    def __len__(self) -> int:
        return len(self.df)

    def _get_session(self, patient, session, path_edf):
        key = (patient, session)
        if self._cached_key != key:
            self._cache = get_or_compute_session(
                patient, session, path_edf,
                cache_dir=self.session_cache_dir, ica_cache_dir=self.ica_cache_dir, use_ica=False,
            )
            self._cached_key = key
        return self._cache

    def __getitem__(self, idx):
        row = self.df.iloc[idx]
        s = self._get_session(row.Patient, row.Session, row.EDF_path)
        start = int(round(row.Start * s["sfreq"]))
        end = int(round(row.end * s["sfreq"]))
        window = s["data"][:, start:end]
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

    def build_model(self, n_channels: int, n_timesteps: int) -> nn.Module:
        self.model = build_model_for_artifact((n_channels, n_timesteps), self.model_type).to(self.device)
        n_params = sum(p.numel() for p in self.model.parameters())
        self.logger.info(f"Model({self.model_type}). Parameters: {n_params:,}")
        return self.model

    def train(self, train_loader: DataLoader, val_loader: DataLoader,
              epochs: int = 100, lr: float = 1e-3, patience_f1: int = 10, patience_lr: int = 3,
              class_weights: Optional[Dict[int, float]] = None,
              focal_params: Optional[Dict[str, float]] = None) -> Dict[str, list]:

        focal_params = focal_params or {"alpha": 0.25, "gamma": 2.0}
        class_weights = class_weights or {0: 1.0, 1: 1.0}

        criterion = FocalLossWithClassWeights(**focal_params, class_weights=class_weights)
        optimizer = torch.optim.Adam(self.model.parameters(), lr=lr)
        scheduler = torch.optim.lr_scheduler.ReduceLROnPlateau(
            optimizer, mode="min", factor=0.7, patience=patience_lr, min_lr=1e-7
        )
        early_stopper = F1EarlyStopping(patience=patience_f1, verbose=self.verbose)

        run_id = int(time.time())
        ckpt_dir = Path("checkpoints") / self.artifact_name
        ckpt_dir.mkdir(parents=True, exist_ok=True)
        ckpt_path = ckpt_dir / f"cnn_{self.artifact_name}_best_{run_id}.pt"
        best_val_loss = float("inf")

        self.logger.info(f"Iniciando entrenamiento: epochs={epochs}")

        for epoch in range(epochs):
            self.model.train()
            train_loss = 0.0
            for X_batch, y_batch in train_loader:
                X_batch, y_batch = X_batch.to(self.device), y_batch.to(self.device)
                optimizer.zero_grad()
                logits = self.model(X_batch)
                loss = criterion(logits, y_batch)
                loss.backward()
                optimizer.step()
                train_loss += loss.item()
            train_loss /= len(train_loader)

            self.model.eval()
            val_loss, all_probs, all_true = 0.0, [], []
            with torch.no_grad():
                for X_batch, y_batch in val_loader:
                    X_batch, y_batch = X_batch.to(self.device), y_batch.to(self.device)
                    logits = self.model(X_batch)
                    val_loss += criterion(logits, y_batch).item()
                    all_probs.append(torch.sigmoid(logits).cpu().numpy())
                    all_true.append(y_batch.cpu().numpy())
            val_loss /= len(val_loader)

            y_proba_val = np.concatenate(all_probs)
            y_true_val = np.concatenate(all_true)
            val_f1 = f1_score(y_true_val, (y_proba_val >= 0.5).astype(int), zero_division=0)

            self.history["loss"].append(train_loss)
            self.history["val_loss"].append(val_loss)
            self.history["val_f1"].append(val_f1)

            if self.verbose:
                print(f"[{self.artifact_name}] Epoch {epoch+1}/{epochs} "
                      f"- loss={train_loss:.4f} val_loss={val_loss:.4f} val_f1={val_f1:.4f}")

            scheduler.step(val_loss)
            if val_loss < best_val_loss:
                best_val_loss = val_loss
                torch.save(self.model.state_dict(), ckpt_path)

            early_stopper.step(val_f1, self.model, epoch)
            if early_stopper.should_stop:
                break

        self.model.load_state_dict(torch.load(ckpt_path, map_location=self.device))
        self.logger.info("Entrenamiento completado.")
        return self.history

    def _predict_proba(self, loader: DataLoader) -> Tuple[np.ndarray, np.ndarray]:
        self.model.eval()
        probs, trues = [], []
        with torch.no_grad():
            for X_batch, y_batch in loader:
                logits = self.model(X_batch.to(self.device))
                probs.append(torch.sigmoid(logits).cpu().numpy())
                trues.append(y_batch.numpy())
        return np.concatenate(probs), np.concatenate(trues)

    def evaluate(self, val_loader: DataLoader, test_loader: DataLoader,
                 window_size_sec: float, max_fp_per_day: float = 100,
                 threshold_mode: str = "youden") -> Dict[str, Any]:

        y_proba_val, y_val = self._predict_proba(val_loader)
        y_proba_test, y_test = self._predict_proba(test_loader)

        best_threshold, _ = select_f1_optimal_threshold(y_val, y_proba_val)
        chosen_thr, chosen_mode = select_operating_threshold(y_val, y_proba_val, mode=threshold_mode)

        total_time_days = len(y_val) * window_size_sec / 86400
        fp_at_thr = ((y_proba_val >= chosen_thr).astype(int) == 1) & (y_val == 0)
        fp_per_day_val = fp_at_thr.sum() / total_time_days if total_time_days > 0 else np.inf
        if fp_per_day_val > max_fp_per_day:
            chosen_thr, chosen_mode = 0.5, "thr05(fp_per_day_exceeded)"

        y_pred_test = (y_proba_test >= chosen_thr).astype(int)

        full_metrics = compute_full_metrics(y_test, y_pred_test, y_proba_test,
                                             window_size_sec=window_size_sec, model_name=self.artifact_name)
        class_report = classification_report(y_test, y_pred_test, target_names=["no_" + self.artifact_name, self.artifact_name])
        conf_matrix = confusion_matrix(y_test, y_pred_test)

        if self.verbose:
            print(f"\n{'='*60}\nEVALUATION(TEST) — {self.artifact_name}")
            print(f"Threshold optim-F1 (val): {best_threshold:.3f} | Operativo ({chosen_mode}): {chosen_thr:.3f}")
            print(class_report)
            print(conf_matrix)
            print(pd.Series(full_metrics).to_string())

        return {
            "chosen_threshold": chosen_thr, "chosen_mode": chosen_mode,
            "test_report": class_report, "confusion_matrix": conf_matrix,
            "metrics_results": full_metrics,
        }

    def save(self, filepath: Optional[str] = None) -> None:
        filepath = Path(filepath) if filepath else self.results_dir / f"cnn_{self.artifact_name}.pt"
        torch.save({"state_dict": self.model.state_dict(), "model_type": self.model_type}, filepath)
        hist_path = self.results_dir / f"cnn_{self.artifact_name}_history.json"
        with open(hist_path, "w", encoding="utf-8") as f:
            json.dump(self.history, f, indent=2)
        self.logger.info(f"Model saved in {self.results_dir}")


def build_cnn_dataloaders(rf_dataset: pd.DataFrame, target_col: str,
                           session_cache_dir: str, ica_cache_dir: str,
                           batch_size: int = 64) -> Tuple[DataLoader, DataLoader, DataLoader]:
    """
    Structures the 3 DataLoaders (train/val/test) with windowed dataframes.
    """
    def _loader_for(split_name, shuffle):
        subset = rf_dataset[rf_dataset["split"] == split_name]
        ds = EEGWindowDataset(subset, target_col=target_col,
                              session_cache_dir=session_cache_dir, ica_cache_dir=ica_cache_dir)
        return DataLoader(ds, batch_size=batch_size, shuffle=shuffle, num_workers=0)

    return _loader_for("train", True), _loader_for("val", False), _loader_for("test", False)


def binary_cnn(windowed_df: pd.DataFrame, target_col: str, model_name: str,
               window_size_sec: float, sfreq: float, n_channels: int,
               session_cache_dir: str, ica_cache_dir: str, models_dir: str = "models_cnn",
               model_type: str = "lightweight", epochs: int = 100, batch_size: int = 64,
               max_fp_per_day: float = 100, force_retrain: bool = False) -> Dict[str, Any]:
    """
    Evaluation of each artefact.
    """
    model_dir = Path(models_dir)
    model_dir.mkdir(parents=True, exist_ok=True)
    analysis_path = model_dir / f"cnn_{model_name}_analysis.joblib"

    if analysis_path.exists() and not force_retrain:
        import joblib
        print(f"[INFO] Pretrained model found: {analysis_path}")
        return joblib.load(analysis_path)

    train_loader, val_loader, test_loader = build_cnn_dataloaders(
        windowed_df, target_col, session_cache_dir, ica_cache_dir, batch_size=batch_size
    )

    n_timesteps = int(window_size_sec * sfreq)
    detector = ArtifactDetector(artifact_name=model_name, model_type=model_type)
    detector.build_model(n_channels=n_channels, n_timesteps=n_timesteps)
    detector.train(train_loader, val_loader, epochs=epochs)

    results = detector.evaluate(val_loader, test_loader, window_size_sec=window_size_sec,
                                 max_fp_per_day=max_fp_per_day)
    detector.save()

    import joblib
    joblib.dump(results, analysis_path)
    return results