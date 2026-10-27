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
    average_precision_score,
    roc_auc_score,
)

# Functions from modules
from src.core.data_config import SCORER, KEYS
from src.core.data_splitter import split_features_target

from src.utils.seizure_eval import (
    get_intervals_from_binary_mask, 
    calculate_ovlp, 
    calculate_taes, 
    calculate_margin
)

KEY = ["Patient", "Session", "Section", "Start"]
POS_THR, IGN_THR, FEATURE_VERSION = 0.5, 0.2, 2
LABEL_TAG = f"pt{POS_THR}_it{IGN_THR}_f{FEATURE_VERSION}"
_VAL_SCORE = None
FORBIDDEN_IN_X = {
    "Patient", "Session", "Section", "Start", "split",
    "is_positive", "y_med", "ic_index",
    "ic_raw_label", "ic_target_label", "ic_iclabel_prob",
}
SUSPECT_PREFIXES = ("tuar_", "bipolar_channels", "monopolar_channels")

def audit_features(df, X, target_col, tag="train", strict=True):
    """Muestra qué columnas entran al modelo y cuáles no, y falla si hay fuga."""
    df_cols = set(re.sub('[^A-Za-z0-9_]+', '', c) for c in df.columns)
    x_cols = set(X.columns)

    dropped = sorted(df_cols - x_cols)
    leaked = sorted(c for c in x_cols if c in FORBIDDEN_IN_X or c.startswith(SUSPECT_PREFIXES))
    non_numeric = sorted(c for c in X.columns if not np.issubdtype(X[c].dtype, np.number))
    const = sorted(c for c in X.columns if X[c].nunique(dropna=False) <= 1)

    print(f"\n[AUDIT:{tag}] df={len(df_cols)} cols | X={len(x_cols)} features | target={target_col}")
    print(f"[AUDIT:{tag}] EXCLUIDAS ({len(dropped)}): {dropped}")
    print(f"[AUDIT:{tag}] FEATURES ({len(x_cols)}): {sorted(x_cols)}")
    if non_numeric:
        print(f"[AUDIT:{tag}] [WARN] no numéricas: {non_numeric}")
    if const:
        print(f"[AUDIT:{tag}] [WARN] constantes: {const}")
    if leaked:
        msg = f"[AUDIT:{tag}] FUGA: estas columnas están entrando al modelo: {leaked}"
        if strict:
            raise AssertionError(msg)
        print(msg)

def to_window_level(df_split, prob, target_col, return_df=False):
    t = df_split[KEY].copy()
    t["p"] = np.asarray(prob)
    t["y"] = df_split[target_col].values
    w = t.groupby(KEY, sort=False).agg(y=("y", "max"), p=("p", "max")).reset_index()
    if return_df:
        return w
    return w["y"].astype(int).values, w["p"].values

def fp_per_day_by_group(w, thr, stride_sec, group="Patient"):
    d = w.copy()
    d["fp"] = ((d["p"] >= thr) & (d["y"] == 0)).astype(int)
    g = d.groupby(group).agg(fp=("fp", "sum"), n=("fp", "size"))
    g["dias_cubiertos"] = g["n"] * stride_sec / 86400
    g["fp_por_dia"] = g["fp"] / g["dias_cubiertos"]
    return g.sort_values("fp_por_dia", ascending=False)

"""
def make_val_score(X_val, df_val, target_col):
    def val_score(model):
        p = model.predict_proba(X_val)[:, 1]
        yv_, sv_ = to_window_level(df_val, p, target_col)
        
        thr, score = find_best_threshold(yv_, sv_, beta=SCORER)
        return score, thr
    return val_score
"""
def extreme_thresholds(y, p, min_recall=0.9, min_precision=0.5):
    prec, rec, thr = precision_recall_curve(y, p)
    prec, rec = prec[:-1], rec[:-1]
    ok_lo = rec >= min_recall
    t_bajo = thr[ok_lo].max() if ok_lo.any() else thr.min()
    ok_hi = prec >= min_precision
    t_alto = thr[ok_hi].min() if ok_hi.any() else thr.max()
    return float(t_bajo), float(t_alto)

def make_val_score(X_val, df_val, target_col):
    def val_score(model):
        p = model.predict_proba(X_val)[:, 1]
        yv_, sv_ = to_window_level(df_val, p, target_col)
        return average_precision_score(yv_, sv_), float("nan")
    return val_score

## Metric analysis functions
def compute_full_metrics(y_true, y_pred, y_prob, win_sec, stride_sec, margin_sec=5.0, model_name="model"):
    """
    Calculation of SzCore metrics set + Clinical Event metrics (OVLP, TAES, MARGIN).
    """
    tn, fp, fn, tp = confusion_matrix(y_true, y_pred, labels=[0, 1]).ravel()

    sensitivity = recall_score(y_true, y_pred, pos_label=1, zero_division=0)
    specificity = tn / (tn + fp) if (tn + fp) > 0 else np.nan
    precision = precision_score(y_true, y_pred, pos_label=1, zero_division=0)
    accuracy = accuracy_score(y_true, y_pred)
    f1 = f1_score(y_true, y_pred, pos_label=1, zero_division=0)
    false_alarm_rate = fp / (fp + tn) if (fp + tn) > 0 else np.nan

    try:
        auc_roc = roc_auc_score(y_true, y_prob)
    except ValueError:
        auc_roc = np.nan

    total_time_sec = len(y_true) * stride_sec
    total_time_days = total_time_sec / 86400
    fp_per_day = fp / total_time_days if total_time_days > 0 else np.nan

    # EVENT-BASED
    true_intervals = get_intervals_from_binary_mask(y_true, win_sec, stride_sec)
    pred_intervals = get_intervals_from_binary_mask(y_pred, win_sec, stride_sec)
    
    ovlp_sens, ovlp_fa = calculate_ovlp(true_intervals, pred_intervals)
    taes_score = calculate_taes(true_intervals, pred_intervals)
    margin_onset, margin_offset = calculate_margin(true_intervals, pred_intervals, margin_sec)

    return {
        "model": model_name,
        "sensitivity": round(sensitivity, 4),
        "specificity": round(specificity, 4),
        "precision": round(precision, 4),
        "accuracy": round(accuracy, 4),
        "f1_score": round(f1, 4),
        "auc_roc": round(auc_roc, 4) if not np.isnan(auc_roc) else np.nan,
        "false_alarm_rate": round(false_alarm_rate, 4),
        "fp_per_day": round(fp_per_day, 2),
        "covered_test_days": round(total_time_days, 4),
        "TP": int(tp),
        "FP": int(fp),
        "TN": int(tn),
        "FN": int(fn),
        "n_test_windows": len(y_true),
        "covered_test_hours": round(total_time_sec / 3600, 2),
        
        "OVLP_Sensitivity": round(ovlp_sens, 4),
        "OVLP_False_Alarms": ovlp_fa,
        "TAES_Score": round(taes_score, 4),
        f"MARGIN_{int(margin_sec)}s_Onset": round(margin_onset, 4),
        f"MARGIN_{int(margin_sec)}s_Offset": round(margin_offset, 4)
    }

def find_best_threshold(y_val, y_prob_val, beta=SCORER, smooth_window=0.02):
    precisions, recalls, thresholds = precision_recall_curve(y_val, y_prob_val)
    fbeta = (1 + beta**2) * (precisions *  recalls)/(beta**2 * precisions + recalls + 1e-12)
    fbeta = fbeta[:-1]
    smoothed = np.array([
        fbeta[(np.abs(thresholds - t)<= smooth_window)].mean()
        for t in thresholds
    ])
    best_idx = np.argmax(smoothed)
    return thresholds[best_idx], fbeta[best_idx]

# Scorers
def fbeta_scorer(y_true, y_pred, beta=SCORER):
    return fbeta_score(y_true, y_pred, beta=beta, pos_label=1, zero_division=0)

def select_threshold(y_val, y_prob_val, stride_sec, beta=SCORER, max_fp_per_day=100):
    adjusted_threshold, _ = find_best_threshold(y_val, y_prob_val, beta=beta)
    candidates = {"thr05":0.5, "adjusted":adjusted_threshold}
    
    total_time_days = len(y_val) * stride_sec / 86400
    scores, details = {}, {}
    valid_candidates = {}

    for name, thr in candidates.items():
        y_pred = (y_prob_val >= thr).astype(int)
        fbeta = fbeta_scorer(y_val, y_pred, beta=beta)
        fp = ((y_pred == 1) & (y_val == 0)).sum()
        fp_per_day_val = fp / total_time_days if total_time_days > 0 else np.inf
        
        details[name] = {"threshold": thr, "fbeta": fbeta, "fp_per_day_val": fp_per_day_val}
        
        if fp_per_day_val <= max_fp_per_day:
            valid_candidates[name] = fbeta

    if valid_candidates:
        best_name = max(valid_candidates, key=valid_candidates.get)
    else:
        print(f"\n[WARNING] Ningún umbral cumplió el límite de {max_fp_per_day} FP/día. Aplicando fallback de menor daño.")
        best_name = min(details, key=lambda k: details[k]["fp_per_day_val"])

    return candidates[best_name], best_name, details

def redirect_threshold(y_val, p_val, beta=SCORER):
    thr, f = find_best_threshold(y_val, p_val, beta=beta)
    return float(thr), {"threshold": float(thr), "fbeta_val": float(f)}

## Optimization functions
def _search_grid(X_train, y_train, X_val, y_val, param_grid, verbose, build_model_fn, balanced=False):
    param_grid = param_grid or [{}]
    best_score, best_params, best_model = -1, None, None
    
    for params in ParameterGrid(param_grid):
        model = build_model_fn(balanced=balanced, **params)
        model.fit(X_train, y_train)
        
        #score = fbeta_scorer(y_val, model.predict(X_val))
        score, _thr = _VAL_SCORE(model)
        
        if verbose:
            print(f"\tparams:{params}\n\tF{SCORER}(val, ventana)={score:.4f} | thr={_thr:.3f}")
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
                if isinstance(val, (int, np.integer)):
                    params[param_name] = int(val)
                elif isinstance(val, (float, np.floating)):
                    params[param_name] = float(val)
                else: 
                    params[param_name] = val
            else:
                params[param_name] = py_rng.choice(param_space)
        
        model = build_model_fn(balanced=balanced, **params)
        model.fit(X_train, y_train)
        
        #score = fbeta_scorer(y_val, model.predict(X_val))
        score, _thr = _VAL_SCORE(model)

        if verbose:
            print(f"\tparams:{params}\n\tF{SCORER}(val, ventana)={score:.4f} | thr={_thr:.3f}")            
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
                use_log = config[3] if len(config) > 3 else False
                params[param_name] = trial.suggest_float(param_name, config[1], config[2], log=use_log)
            elif p_type == "categorical":
                params[param_name] = trial.suggest_categorical(param_name, config[1])

        model = build_model_fn(balanced=balanced, **params)
        model.fit(X_train, y_train)

        #score = fbeta_scorer(y_val, model.predict(X_val))
        score, _thr = _VAL_SCORE(model)

        return score

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

        #score = fbeta_scorer(y_val, model.predict(X_val))
        score, _thr = _VAL_SCORE(model)
  
        return score

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
                       force_retrain=False, balanced=False, max_fp_per_day=100, 
                       target_col = "is_positive", medical=None,
                    ):
    """
    Generic function to train a binary classifier.
    y: DataFrame with a binary column (0/1) / Series with binary labels.
    """
    if leakage_cols is None:
        leakage_cols = []

    # Medical Ground Truth
    eval_col = target_col
    if medical is not None:
        medical.fit_meta(df)                              # guarda tuar_*, bipolar_/monopolar_channels_*
        df = medical.add_truth(df)                        # crea la columna y_med
        eval_col = medical.eval_col                       # validación y umbral usan y_med
        leakage_cols = list(leakage_cols) + [eval_col]    # y_med no puede ser feature
    
    cols_to_drop = [c for c in df.columns if c.startswith("tuar_") or "channels" in c]
    df = df.drop(columns=cols_to_drop, errors="ignore")

    # Gray Zone
    df = df[~((df["split"] != "test") & (df[target_col] == -1))].copy()
    df.loc[df[target_col] == -1, target_col] = 0

    # Saving the model
    model_dir = Path(models_dir)
    model_dir.mkdir(parents=True, exist_ok=True)
    model_path = model_dir / f"{model_name}_{search_method}.joblib"
    analysis_path = model_dir / f"{model_name}_and_analysis_{search_method}.joblib"

    reuse = model_path.exists() and analysis_path.exists() and not force_retrain
    cached = None
    if reuse:
        cached = joblib.load(analysis_path)
        if medical is not None and "med_ch_f1_micro" not in cached["metrics_results"]:
            print("[INFO] Modelo guardado sin métricas de canales: se recalculan con el modelo cargado (sin reentrenar).")
            reuse = False                     # entra a la rama de cálculo, reutilizando el modelo

    if reuse:
        print(f"[INFO] Pretrained model found, loading: {analysis_path}")
        print("Final report", "-"*25)
        print(cached["test_report"])
        print("Confusion matrix", "-"*25)
        print(cached["confusion_matrix"])
        print("General metrics", "-"*25)
        print(pd.Series(cached["metrics_results"]).to_string())

        return{
            "model":            cached["model"],
            "params":           cached["params"],
            "feature_col":      cached["feature_col"],
            "val_f1":           cached["val_f1"],
            "test_report":      cached["test_report"],
            "confusion_matrix": cached["confusion_matrix"],
            "metrics_results":  cached["metrics_results"],
            "importances":      cached["importances"]
        }

    else:
        X_train, y_train = split_features_target(df, "train", leakage_cols)
        X_val, y_val = split_features_target(df, "val", leakage_cols)
        X_test, y_test = split_features_target(df, "test", leakage_cols)

        X_train = X_train.rename(columns=lambda x:re.sub('[^A-Za-z0-9_]+', '', x))
        X_val = X_val.rename(columns=lambda x:re.sub('[^A-Za-z0-9_]+', '', x))
        X_test = X_test.rename(columns=lambda x:re.sub('[^A-Za-z0-9_]+', '', x))

        audit_features(df, X_train, eval_col, tag="train")
        assert list(X_train.columns) == list(X_val.columns) == list(X_test.columns), "train/val/test tienen columnas distintas"

        if verbose:
            print(f"\n{'='*60}\nModelo: {model_name}")
            print(f"Train: {len(X_train)} (pos={y_train.sum()}) | "
                f"Val: {len(X_val)} (pos = {y_val.sum()}) | "
                f"Test: {len(X_test)} (pos={y_test.sum()})")

        if len(X_val) == 0 or len(X_test) == 0:
            raise ValueError(f"[{model_name}] Val o Test are emtpy. Check the split to verify if n_patients is enough.")

        search_kwargs = search_kwargs or {}

        global _VAL_SCORE
        df_val = df[df["split"] == "val"]
        assert len(df_val) == len(X_val)
        _VAL_SCORE = make_val_score(X_val, df_val, eval_col)

        if cached is not None:
            assert list(X_val.columns) == cached["feature_col"], "las columnas cambiaron: reentrena (force_retrain=True)"
            best_model, best_params, best_score = cached["model"], cached["params"], cached["val_f1"]
        elif search_method == "grid":
            best_model, best_params, best_score = _search_grid(X_train, y_train, X_val, y_val, search_data, verbose, build_model_fn, balanced)
        elif search_method == "random":
            best_model, best_params, best_score = _search_random(X_train, y_train, X_val, y_val, search_kwargs, search_data, verbose, build_model_fn, balanced)
        elif search_method == "optuna":
            best_model, best_params, best_score = _search_optuna(X_train, y_train, X_val, y_val, search_kwargs, search_data, verbose, build_model_fn, balanced)
        elif search_method == "hba":
            best_model, best_params, best_score = _search_hba_binary(X_train, y_train, X_val, y_val, search_kwargs, search_data, verbose, build_model_fn, balanced)
        else:
            raise ValueError(f"Unknown search_method: {search_method}")

        # Best threshold results
        stride = window_size_sec["stride_sec"]
        df_test = df[df["split"]=="test"]
        assert len(df_val) == len(X_val) and len(df_test) == len(X_test)

        y_prob_val = best_model.predict_proba(X_val)[:,1]
        y_prob_test =  best_model.predict_proba(X_test)[:,1]

        wv = to_window_level(df_val,  y_prob_val,  eval_col, return_df=True); wv["split"] = "val"
        wt = to_window_level(df_test, y_prob_test, eval_col, return_df=True); wt["split"] = "test"
        yv, sv = wv["y"].astype(int).values, wv["p"].values
        yt, st = wt["y"].astype(int).values, wt["p"].values
        pred_path = model_dir / f"{model_name}_{search_method}_preds.parquet"
        pd.concat([wv, wt], ignore_index=True).to_parquet(pred_path, index=False)

        # chosen_threshold, chosen_name, threshold_details = select_threshold(yv, sv, stride, max_fp_per_day=max_fp_per_day)
        chosen_threshold, thr_info = redirect_threshold(yv, sv)
        chosen_name = "fbeta_val"

        t_bajo, t_alto = extreme_thresholds(yv, sv, min_recall=0.9, min_precision=0.5)

    # Comprobación: Si la restricción realmente se cumplió
            # Comprobación: la restricción de recall/precisión se cumple en val
    for name, t in [("t_bajo", t_bajo), ("t_alto", t_alto)]:
        pred = (sv >= t).astype(int)
        print(f"[INFO] {name}={t:.4f} | recall(val)={recall_score(yv, pred):.3f} "
                f"| precision(val)={precision_score(yv, pred, zero_division=0):.3f}")

    y_test_predict = (st >= chosen_threshold).astype(int)
    class_report = classification_report(yt, y_test_predict, target_names=["no_"+model_name, model_name])
    conf_matrix = confusion_matrix(yt, y_test_predict)

    win = window_size_sec["window_size_sec"]
    stride = window_size_sec["stride_sec"]

    full_metrics = compute_full_metrics(yt, y_test_predict, st, win, stride, model_name=model_name)
    full_metrics["threshold"] = round(float(chosen_threshold), 4)
    full_metrics["AP"] = round(average_precision_score(yt, st), 4)

    if medical is not None:
        med = medical.report(df_test, y_prob_test, chosen_threshold)

        # localización por canal: umbral elegido en val, reporte en test
        keys_v, P_val = medical.channel_scores(df_val, y_prob_val)
        G_val, ok_val = medical.channel_truth(keys_v)
        tau = medical.pick_tau(P_val[ok_val], G_val[ok_val])
        med.update(medical.report_channels(df_test, y_prob_test, tau))
        med["ch_tau"] = round(float(tau), 3)

        full_metrics.update({f"med_{k}": v for k, v in med.items()})

    fp_by_patient = fp_per_day_by_group(wt, chosen_threshold, stride)

    if verbose:
        print(fp_by_patient.round(3).to_string())
        print(f"[INFO] Umbral (F{SCORER}, validación, ventana): {chosen_threshold:.4f} | F{SCORER}(val)={thr_info['fbeta_val']:.4f}")
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
        "model": best_model, "params": best_params,
        "feature_col": list(X_train.columns), "val_f1": best_score,
    }, model_path)
    print(f"Model saved in {model_path}")

    joblib.dump({
        "model": best_model, "params": best_params,
        "feature_col": list(X_train.columns), "val_f1": best_score,
        "chosen_threshold": chosen_threshold,
        "chosen_thresold_name": chosen_name,
        "test_report": class_report,
        "confusion_matrix": conf_matrix,
        "metrics_results": full_metrics,
        "importances": importances,
        "t_bajo": t_bajo,
        "t_alto": t_alto,
    }, analysis_path)
    print(f"Model with metrics saved in {analysis_path}")

    return{
        "model": best_model, "params": best_params,
        "feature_col": list(X_train.columns), "val_f1": best_score,
        "test_report": class_report,
        "confusion_matrix": conf_matrix,
        "metrics_results": full_metrics,
        "importances": importances,
    }