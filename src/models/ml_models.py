"""
# File: ml_models.py
# Project: Trabajo de graduación
# Author: Maria Fernanda Andrade Recinos

Reusable metrics, best threshold search, train and validation functions.
"""
# File: ml_models.py

# Data management libraries
import re
import random
import joblib
import numpy as np
import pandas as pd
from pathlib import Path
from scipy.stats import randint

# AI required functions
import optuna
from sklearn.model_selection import ParameterGrid
from sklearn.metrics import (
    f1_score, 
    confusion_matrix, 
    recall_score, 
    precision_score, 
    accuracy_score, 
    roc_auc_score, 
    precision_recall_curve, 
    fbeta_score,
    classification_report, 
)

# Functions from modules
from src.core.data_splitter import split_features_target

## Metric analysis functions
def compute_full_metrics(y_true, y_pred, y_prob, window_size_sec, model_name="model"):
    """
    Calculation of SzCore metrics set.
    """
    tn, fp, fn, tp = confusion_matrix(y_true, y_pred, labels=[0, 1]).ravel()

    sensitivity = recall_score(y_true, y_pred, pos_label=1, zero_division=0)
    specificity = tn / (tn + fp) if (tn + fp) > 0 else np.nan
    precision = precision_score(y_true, y_pred, pos_label=1, zero_division=0)
    accuracy = accuracy_score(y_true, y_pred)
    f1 = f1_score(y_true, y_pred, pos_label=1, zero_division=0)
    false_alarm_rate = fp / (fp + tn) if (fp + tn) > 0 else np.nan  # = 1 - especificidad

    try:
        auc_roc = roc_auc_score(y_true, y_prob)
    except ValueError:
        auc_roc = np.nan

    total_time_sec = len(y_true) * window_size_sec
    total_time_days = total_time_sec / 86400

    fp_per_day = fp / total_time_days if total_time_days > 0 else np.nan

    return{
        "model": model_name,
        "sensitivity": round(sensitivity, 4),
        "specificity": round(specificity, 4),
        "precision": round(precision, 4),
        "accuracy": round(accuracy, 4),
        "f1_score": round(f1, 4),
        "auc_roc": round(auc_roc, 4) if not np.isnan(auc_roc) else np.nan,
        "false_alar_rate": round(false_alarm_rate, 4),
        "fp_per_day": round(fp_per_day, 2),
        "TP": int(tp),
        "FP": int(fp),
        "TN": int(tn),
        "FN": int(fn),
        "n_test_windows": len(y_true),
        "covered_test_hours": round(total_time_sec / 3600, 2),
    }

def find_best_threshold(y_val, y_prob_val, beta=2, smooth_window=0.02):
    precisions, recalls, thresholds = precision_recall_curve(y_val, y_prob_val)
    fbeta = (1 + beta**2) * (precisions *  recalls)/(beta**2 * precisions + recalls + 1e-12)
    fbeta = fbeta[:-1]
    smoothed = np.array([
        fbeta[(np.abs(thresholds - t)<= smooth_window)].mean()
        for t in thresholds
    ])
    best_idx = np.argmax(smoothed)
    return thresholds[best_idx], fbeta[best_idx]

def f2_scorer(y_true, y_pred):
    return fbeta_score(y_true, y_pred, beta=2, pos_label=1, zero_division=0)

def select_threshold(y_val, y_prob_val,window_size_sec, beta=2, max_fp_per_day=100):
    adjusted_threshold, _ = find_best_threshold(y_val, y_prob_val, beta=beta)
    candidates = {"thr05":0.5, "adjusted":adjusted_threshold}
    scores, details = {}, {}

    total_time_days = len(y_val)*window_size_sec / 86400

    for name, thr in candidates.items():
        y_pred = (y_prob_val >= thr).astype(int)
        fbeta = f2_scorer(y_val, y_pred)
        fp = ((y_pred==1) & (y_val==0)).sum()
        fp_per_day_val = fp / total_time_days if total_time_days > 0 else np.inf
        details[name] = {"threshold": thr, "fbeta":fbeta, "fp_per_day_val": fp_per_day_val}
        scores[name]= fbeta if fp_per_day_val <= max_fp_per_day else -1
    best_name = max(scores, key=scores.get)

    if scores[best_name]==-1:
        best_name = "thr05"
    return candidates[best_name], best_name, details


## Optimization functions
def _search_grid(X_train, y_train, X_val, y_val, param_grid, verbose, build_model_fn, balanced=False):
    param_grid = param_grid or [{}]
    best_score, best_params, best_model = -1, None, None
    
    for params in ParameterGrid(param_grid):
        model = build_model_fn(balanced=balanced, **params)
        model.fit(X_train, y_train)
        
        # Asumiendo que prefieres f1_score aquí, como en tu código original
        score = f1_score(y_val, model.predict(X_val), pos_label=1, zero_division=0)
        
        if verbose:
            print(f"\tparams:{params}\n\tf1 score:{score}")
            
        if score > best_score:
            best_score, best_params, best_model = score, params, model
            
    return best_model, best_params, best_score


def _search_random(X_train, y_train, X_val, y_val, kwargs, space, verbose, build_model_fn, balanced=False):
    n_iter = kwargs.get("n_iter", 40)
    rng = np.random.default_rng(kwargs.get("seed", 42))
    py_rng = random.Random(kwargs.get("seed", 42))

    space = space or {}
    best_score, best_params, best_model = -1, None, None
    
    for _ in range(n_iter):
        params = {}
        for param_name, param_space in space.items():
            if hasattr(param_space, "rvs"):
                val = param_space.rvs(random_state=rng)
                params[param_name] = int(val) if isinstance(val, np.integer) else float(val)
            else:
                params[param_name] = py_rng.choice(param_space)
        
        model = build_model_fn(balanced=balanced, **params)
        model.fit(X_train, y_train)
        
        # Aquí usabas f2_scorer en tu código original
        score = f2_scorer(y_val, model.predict(X_val))
        
        if verbose:
            print(f"\tparams:{params}\n\tf2 score:{score}")
            
        if score > best_score:
            best_score, best_params, best_model = score, params, model
            
    return best_model, best_params, best_score


def _search_optuna(X_train, y_train, X_val, y_val, kwargs, space, verbose, build_model_fn, balanced=False):
    """
    'space' is a dict with type and range:
    space = {
        "n_estimators": ("int", 100, 800),
        "max_depth": ("categorical", [None, 10, 15, 20]),
        "learning_rate": ("float", 0.01, 0.3)
    }
    """
    n_trials = kwargs.get("n_trials", 60)

    def objective(trial):
        params = {}
        # Mapeo dinámico del espacio de búsqueda para Optuna
        for param_name, config in space.items():
            p_type = config[0]
            if p_type == "int":
                params[param_name] = trial.suggest_int(param_name, config[1], config[2])
            elif p_type == "float":
                params[param_name] = trial.suggest_float(param_name, config[1], config[2])
            elif p_type == "categorical":
                params[param_name] = trial.suggest_categorical(param_name, config[1])

        model = build_model_fn(balanced=balanced, **params)
        model.fit(X_train, y_train)
        
        return f1_score(y_val, model.predict(X_val), pos_label=1, zero_division=0)

    optuna.logging.set_verbosity(optuna.logging.WARNING if not verbose else optuna.logging.INFO)
    study = optuna.create_study(direction="maximize")
    study.optimize(objective, n_trials=n_trials)

    best_params = study.best_params
    best_model = build_model_fn(balanced=balanced, **best_params)
    best_model.fit(X_train, y_train)
    
    return best_model, best_params, study.best_value


def _search_hba_binary(X_train, y_train, X_val, y_val, kwargs, space, verbose, build_model_fn, balanced=False):
    """
    HBA 'space' must have 'bounds' and a 'parser':
    space = {
        "bounds": [(50, 800), (3, 40)],
        "parser": lambda vec: {"n_estimators": int(vec[0]), "max_depth": int(vec[1])}
    }
    """
    bounds = space["bounds"]
    parser_fn = space["parser"]

    def fitness_fn(vec):
        params = parser_fn(vec)
        model = build_model_fn(balanced=balanced, **params)
        model.fit(X_train, y_train)
        
        return f1_score(y_val, model.predict(X_val), pos_label=1, zero_division=0)

    best_vec, best_score, _ = honey_badger_optimizer(
        fitness_fn, bounds,
        n_agents=kwargs.get("n_agents", 15),
        max_iter=kwargs.get("max_iter", 25),
        seed=kwargs.get("seed", 42),
        verbose=verbose,
    )
    
    best_params = parser_fn(best_vec)
    best_model = build_model_fn(balanced=balanced, **best_params)
    best_model.fit(X_train, y_train)
    
    return best_model, best_params, best_score


## Binary model (Classifier)
def train_binary_model( df, model_name, window_size_sec, build_model_fn,
                       search_data=None, models_dir="models", verbose=True, 
                       leakage_cols=[], search_method="grid", search_kwargs=None,
                       force_retrain=False, balanced=False, max_fp_per_day=100
                    ):
    """
    Generic function to train a binary classifier.
    y: DataFrame with a binary column (0/1) / Series with binary labels.
    """
    if leakage_cols is None:
        leakage_cols = []

    # Saving the model
    model_dir = Path(models_dir)
    model_dir.mkdir(parents=True, exist_ok=True)
    model_path = model_dir / f"{model_name}_{search_method}.joblib"
    analysis_path = model_dir / f"{model_name}_and_analysis_{search_method}.joblib"

    if model_path.exists() and analysis_path.exists() and not force_retrain:
        print(f"[INFO] Pretrained model found, loading: {analysis_path}")
        return joblib.load(analysis_path)
    else:
        X_train, y_train = split_features_target(df, "train", leakage_cols)
        X_val, y_val = split_features_target(df, "val", leakage_cols)
        X_test, y_test = split_features_target(df, "test", leakage_cols)

        X_train = X_train.rename(columns=lambda x:re.sub('[^A-Za-z0-9_]+', '', x))
        X_val = X_val.rename(columns=lambda x:re.sub('[^A-Za-z0-9_]+', '', x))
        X_test = X_test.rename(columns=lambda x:re.sub('[^A-Za-z0-9_]+', '', x))

        if verbose:
            print(f"\n{'='*60}\nModelo: {model_name}")
            print(f"Train: {len(X_train)} (pos={y_train.sum()}) | "
                f"Val: {len(X_val)} (pos = {y_val.sum()}) | "
                f"Test: {len(X_test)} (pos={y_test.sum()})")

        if len(X_val) == 0 or len(X_test) == 0:
            raise ValueError(f"[{model_name}] Val o Test are emtpy. Check the split to verify if n_patients is enough.")

        search_kwargs = search_kwargs or {}

        if search_method == "grid":
            best_model, best_params, best_score = _search_grid(X_train, y_train, X_val, y_val, search_data, verbose, build_model_fn, balanced)
        elif search_method == "random":
            best_model, best_params, best_score = _search_random(X_train, y_train, X_val, y_val, search_kwargs, search_data, verbose, build_model_fn, balanced)
        elif search_method == "optuna":
            best_model, best_params, best_score = _search_optuna(X_train, y_train, X_val, y_val, search_kwargs, verbose, build_model_fn, balanced)
        elif search_method == "hba":
            best_model, best_params, best_score = _search_hba_binary(X_train, y_train, X_val, y_val, search_kwargs, verbose,build_model_fn, balanced)
        else:
            raise ValueError(f"Unknown search_method: {search_method}")

        # Best threshold results
        y_prob_val = best_model.predict_proba(X_val)[:,1]
        chosen_threshold, chosen_name, threshold_details = select_threshold(y_val, y_prob_val, window_size_sec['window_size_sec'], max_fp_per_day=max_fp_per_day)

        y_prob_test =  best_model.predict_proba(X_test)[:,1]
        y_test_predict = (y_prob_test >= chosen_threshold).astype(int)

        class_report = classification_report(y_test, y_test_predict, target_names=["no_"+model_name, model_name])
        conf_matrix = confusion_matrix(y_test, y_test_predict)
        full_metrics = compute_full_metrics(y_test.values, y_test_predict, y_prob_test,
                                            window_size_sec=window_size_sec['window_size_sec'], model_name=model_name)

        if verbose:
            print(f"[INFO] Threshold decision based on validation:")
            for name, d in threshold_details.items():
                flag = " <- choosen" if name==chosen_name else ""
                print(f"\t{name}: threshold={d['threshold']:.4f} | F2(val)={d['fbeta']:.4f} | fp_per_day_val(val)={d['fp_per_day_val']:.4f}{flag}")
            print(f"[INFO] Best configuration found with validation: {best_params} | F1(val)={best_score:.4f}")
            print("Final report", "-"*25)
            print(class_report)
            print("Confusion matrix", "-"*25)
            print(conf_matrix)
            print("General metrics", "-"*25)
            print(pd.Series(full_metrics).to_string())

        importances = pd.DataFrame({
            "features": X_train.columns,
            "importance": best_model.feature_importances_
        }).sort_values("importance", ascending=False).reset_index(drop=True)

        # Saving data
        joblib.dump({
            "model":best_model, "params":best_params, 
            "feature_col": list(X_train.columns), "val_f1": best_score,
        }, model_path)
        print(f"Model saved in {model_path}")

        joblib.dump({
            "model":best_model, "params":best_params, 
            "feature_col": list(X_train.columns), "val_f1": best_score,
            "chosen_threshold": chosen_threshold,
            "chosen_thresold_name": chosen_name,
            "test_report": class_report,
            "confusion_matrix": conf_matrix,
            "metrics_results": full_metrics,
            "importances": importances,
        }, analysis_path)
        print(f"Model with metrics saved in {analysis_path}")

        return{
            "model":best_model, "params":best_params, 
            "feature_col": list(X_train.columns), "val_f1": best_score,
            "test_report": class_report,
            "confusion_matrix": conf_matrix,
            "metrics_results": full_metrics,
            "importances": importances,
        }