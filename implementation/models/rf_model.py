"""
# File: rf_model.py
# Project: Trabajo de graduación
# Author: Maria Fernanda Andrade Recinos

Reusable RF (Random Forest) modules for the AI pipeline.
"""
import numpy as np
import pandas as pd
import joblib
import random
from pathlib import Path
from scipy.stats import randint

from sklearn.ensemble import RandomForestClassifier
from sklearn.multioutput import MultiOutputClassifier
from imblearn.ensemble import BalancedRandomForestClassifier
from sklearn.model_selection import (
    ParameterGrid, 
    GridSearchCV, 
    GroupKFold, 
    cross_val_score,
)
from sklearn.metrics import (
    f1_score, 
    classification_report, 
    confusion_matrix, 
    recall_score, 
    precision_score, 
    accuracy_score, 
    roc_auc_score, 
    precision_recall_curve, 
    fbeta_score,
)
from sklearn.metrics import make_scorer, fbeta_score

# Functions from modules
from implementation.core.data_splitter import split_features_target

# Binary RF
def build_rf_model(balanced_bootstrap=False, **overrides):
    """
    RF cofiguration with overrides for hiperparameters testing.
    """
    params = {
        "n_estimators": 200,
        "class_weight": "balanced",
        "max_depth": None,
        "min_samples_split": 2,
        "max_features": "sqrt",
        "random_state": 42,
        "n_jobs": -1,
    }

    if balanced_bootstrap:
        params["sampling_strategy"] = "all"
        params.update(overrides)
        return BalancedRandomForestClassifier(
            replacement=True, bootstrap=True, **params
        )
    else:
        params["class_weight"] = "balanced"
        params.update(overrides)
        return RandomForestClassifier(**params)

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


def binary_rf(df, model_name, window_size_sec, search_data=None, models_dir="models", 
              verbose=True, leakage_cols=[], search_method="grid", search_kwargs=None,
              force_retrain = False, balanced_bootstrap=False, max_fp_per_day=100
             ):
    """
    Generic function to train a binary Random Forest classifier.
    y: DataFrame with a binary column (0/1) / Series with binary labels.
    """
    # Saving the model
    model_dir = Path(models_dir)
    model_dir.mkdir(parents=True, exist_ok=True)
    model_path = model_dir / f"rf_{model_name}_{search_method}.joblib"
    analysis_path = model_dir / f"rf_{model_name}_and_analysis_{search_method}.joblib"

    if model_path.exists() and analysis_path.exists() and not force_retrain:
        print(f"[INFO] Pretrained model found, loading: {analysis_path}")
        return joblib.load(analysis_path)
    else:
        X_train, y_train = split_features_target(df, "train", leakage_cols)
        X_val, y_val = split_features_target(df, "val", leakage_cols)
        X_test, y_test = split_features_target(df, "test", leakage_cols)

        if verbose:
            print(f"\n{'='*60}\nModelo: {model_name}")
            print(f"Train: {len(X_train)} (pos={y_train.sum()}) | "
                f"Val: {len(X_val)} (pos = {y_val.sum()}) | "
                f"Test: {len(X_test)} (pos={y_test.sum()})")

        if len(X_val) == 0 or len(X_test) == 0:
            raise ValueError(f"[{model_name}] Val o Test are emtpy. Check the split to verify if n_patients is enough.")

        if verbose:
            print(f"[DEBUG] y_val dist ({model_name}):", y_val.value_counts().to_dict())
            print(f"[DEBUG] y_val hash ({model_name}):", pd.util.hash_pandas_object(y_val).sum())
            print(f"[DEBUG] X_val hash ({model_name}):", pd.util.hash_pandas_object(X_val).sum())            

        search_kwargs = search_kwargs or {}

        if search_method == "grid":
            best_model, best_params, best_score = _search_grid(X_train, y_train, X_val, y_val, search_data, verbose, balanced_bootstrap)
        elif search_method == "random":
            best_model, best_params, best_score = _search_random(X_train, y_train, X_val, y_val, search_kwargs, search_data, verbose, balanced_bootstrap)
        elif search_method == "optuna":
            best_model, best_params, best_score = _search_optuna(X_train, y_train, X_val, y_val, search_kwargs, verbose, balanced_bootstrap)
        elif search_method == "hba":
            best_model, best_params, best_score = _search_hba_binary(X_train, y_train, X_val, y_val, search_kwargs, verbose, balanced_bootstrap)
        else:
            raise ValueError(f"search_method desconocido: {search_method}")

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

## Optimization functions
def _search_grid(X_train, y_train, X_val, y_val, param_grid, verbose, balanced_bootstrap=False):
    param_grid = param_grid or [{}]
    best_score, best_params, best_model = -1, None, None
    for params in ParameterGrid(param_grid):
        rf = build_rf_model(balanced_bootstrap, **params)
        rf.fit(X_train, y_train)
        score = f1_score(y_val, rf.predict(X_val), pos_label=1, zero_division=0)
        if verbose:
            print(f"\tparams:{params}\n\tf1 score:{score}")
        if score > best_score:
            best_score, best_params, best_model = score, params, rf
    return best_model, best_params, best_score


def _search_random(X_train, y_train, X_val, y_val, kwargs, space, verbose, balanced_bootstrap=False):
    n_iter = kwargs.get("n_iter", 40)
    rng = np.random.default_rng(kwargs.get("seed", 42))
    py_rng = random.Random(kwargs.get("seed", 42))

    space = space or [{}]

    best_score, best_params, best_model = -1, None, None
    for _ in range(n_iter):
        params = {
            "n_estimators": int(space["n_estimators"].rvs(random_state=rng)),
            "max_depth": int(space["max_depth"].rvs(random_state=rng)),
            "min_samples_split": int(space["min_samples_split"].rvs(random_state=rng)),
            "min_samples_leaf": int(space["min_samples_leaf"].rvs(random_state=rng)),
            "max_features": py_rng.choice(space["max_features"]),
        }
        extra = {}
        if balanced_bootstrap:
            extra["sampling_strategy"] = rng.choice(space["sampling_strategy"])
        
        rf = build_rf_model(balanced_bootstrap, **params, **extra)
        rf.fit(X_train, y_train)
        score = f2_scorer(y_val, rf.predict(X_val))
        if verbose:
            print(f"\tparams:{params}\n\tf2 score:{score}")
        if score > best_score:
            best_score, best_params, best_model = score, params, rf
    return best_model, best_params, best_score


def _search_optuna(X_train, y_train, X_val, y_val, kwargs, verbose, balanced_bootstrap=False):
    import optuna
    n_trials = kwargs.get("n_trials", 60)

    def objective(trial):
        params = dict(
            n_estimators=trial.suggest_int("n_estimators", 100, 800),
            max_depth=trial.suggest_categorical("max_depth", [None, 10, 15, 20, 30]),
            min_samples_split=trial.suggest_int("min_samples_split", 2, 20),
            min_samples_leaf=trial.suggest_int("min_samples_leaf", 1, 10),
            max_features=trial.suggest_categorical("max_features", ["sqrt", "log2", 0.3, 0.5]),
        )
        rf = build_rf_model(balanced_bootstrap, **params)
        rf.fit(X_train, y_train)
        return f1_score(y_val, rf.predict(X_val), pos_label=1, zero_division=0)

    optuna.logging.set_verbosity(optuna.logging.WARNING if not verbose else optuna.logging.INFO)
    study = optuna.create_study(direction="maximize")
    study.optimize(objective, n_trials=n_trials)

    best_params = study.best_params
    best_model = build_rf_model(balanced_bootstrap, **best_params)
    best_model.fit(X_train, y_train)
    return best_model, best_params, study.best_value

def _search_hba_binary(X_train, y_train, X_val, y_val, kwargs, verbose, balanced_bootstrap=False):
    bounds = [(50, 800), (3, 40), (2, 20), (1, 10), (0.1, 1.0)]

    def fitness_fn(vec):
        params = _params_from_vector(vec)
        rf = build_rf_model(balanced_bootstrap, **params)
        rf.fit(X_train, y_train)
        return f1_score(y_val, rf.predict(X_val), pos_label=1, zero_division=0)

    best_vec, best_score, _ = honey_badger_optimizer(
        fitness_fn, bounds,
        n_agents=kwargs.get("n_agents", 15),
        max_iter=kwargs.get("max_iter", 25),
        seed=kwargs.get("seed", 42),
        verbose=verbose,
    )
    best_params = _params_from_vector(best_vec)
    best_model = build_rf_model(balanced_bootstrap, **best_params)
    best_model.fit(X_train, y_train)
    return best_model, best_params, best_score

# ---------------------------------------------------------------------------------------------
if __name__ == "__main__":
    
    # Data integration libraries / project modules
    from implementation.core.data_config import ARTIFACT_KEYWORDS, WINDOW_REQUESTS_ARTIFACTS, RATIOS, VERSION, LEAKAGE_COLS
    from implementation.core.data_loader import build_annotations_index, find_project_root
    from implementation.core.windowing import label_windowing
    from implementation.core.data_splitter import get_or_compute_split, split_features_target
    from implementation.core.feature_extractor import build_feature_dataset, build_rf_dataset

    # Data visualization and search libraries
    from IPython.display import display

    BASE_DIR = find_project_root()
    CORPUS_OUTPUTS_DIR = BASE_DIR / Path("outputs/artifact")
    ICA_CACHE_DIR = CORPUS_OUTPUTS_DIR / Path("individual_tests/cache/ica")
    SESSION_CACHE_DIR = CORPUS_OUTPUTS_DIR / Path("individual_tests/cache/sessions")
    FEATURES_DIR = CORPUS_OUTPUTS_DIR / Path("individual_tests/features")
    SPLIT_CACHE_DIR = CORPUS_OUTPUTS_DIR / Path("individual_tests/splits")
    MODELS_DIR = CORPUS_OUTPUTS_DIR / Path("individual_tests/models")

    for d in (FEATURES_DIR, ICA_CACHE_DIR, SPLIT_CACHE_DIR):
        d.mkdir(parents=True, exist_ok=True)

    PARAM_GRID = {
        "n_estimators": [200, 400],
        "max_depth": [None, 20]
    }
    RANDOM_SPACE = {
        "eye": {
            "space":{
                "n_estimators": randint(150, 600),
                "max_depth": randint(5, 30),
                "min_samples_split": randint(5, 30),
                "min_samples_leaf": randint(2, 15),
                "max_features": ["sqrt", "log2", 0.3, 0.5],
                "sampling_strategy": [0.3, 0.5, 0.7, 1.0],
            },
            "max_fp_per_day": 50,
            "n_iter": 60,
        },
        "muscle": {
            "space":{
                "n_estimators": randint(150, 600),
                "max_depth": randint(5, 30),
                "min_samples_split": randint(2, 15),
                "min_samples_leaf": randint(1, 8),
                "max_features": ["sqrt", "log2", 0.3, 0.5],
                "sampling_strategy": [0.3, 0.5, 0.7, 1.0],
            },
            "max_fp_per_day": 300,
            "n_iter": 60,
        },
        "non_physiological": {
            "space":{
                "n_estimators": randint(150, 600),
                "max_depth": randint(5, 35),
                "min_samples_split": randint(2, 15),
                "min_samples_leaf": randint(1, 8),
                "max_features": ["sqrt", "log2", 0.3, 0.5],
                "sampling_strategy": [0.3, 0.5, 0.7, 1.0],
            },
            "max_fp_per_day": 1000,
            "n_iter": 60,
        },
    }

    print("\nLoading 25 artifact patients, 1 sessions per patient for testing...")
    database_corpus_patient = build_annotations_index("artifact", n_patients=25, max_sessions=1, paths=True)
    display(database_corpus_patient.head(5))

    results = {}

    for artifact, window in WINDOW_REQUESTS_ARTIFACTS.items():
        print("\n" + "-"*50)
        print(f"ARTIFACT: {artifact} | windows: {window ['window_size_sec']}s")
        print("\n" + "-"*50)

        rf_dataset_path = FEATURES_DIR/f"rf_dataset_{artifact}.parquet"
        if rf_dataset_path.exists():
            print(f"[INFO] Existing dataset, loading: {rf_dataset_path}")
            rf_dataset = pd.read_parquet(rf_dataset_path)
        else:
            print("\nGenerating windows...")
            windowed_annotations_corpus_patient = label_windowing(
                            database_corpus_patient, WINDOW_REQUESTS_ARTIFACTS[artifact],
                            ARTIFACT_KEYWORDS, unreviewd_tokens=True,
                        )
            display(windowed_annotations_corpus_patient.head(5))

            windowed_annotated_splited, assignment, report = get_or_compute_split(windowed_annotations_corpus_patient, 
                                                                                  target_taxonomy=ARTIFACT_KEYWORDS, 
                                                                                  dataset_division_dir=str(SPLIT_CACHE_DIR), 
                                                                                  ratios=RATIOS, 
                                                                                  version=VERSION,
                                                                                  target=artifact)
            print("[INFO] Split report")
            print(report)

            print("\nStarting features extraction from channels and ICA components...")
            featured_windows = build_feature_dataset(windowed_annotated_splited, use_ica=True, ica_cache_dir=str(ICA_CACHE_DIR), session_cache_dir=str(SESSION_CACHE_DIR))
            display(featured_windows.head(5))

            if not featured_windows.empty:
                print("[INFO] Successful features extraction")
                rf_features_dataset = build_rf_dataset(featured_windows, target_artifact=artifact, features_dir=str(FEATURES_DIR))
                print(rf_features_dataset.head(5))
                print("[INFO] Positive count:")
                print(rf_features_dataset["is_positive"].value_counts())
            else:
                raise ValueError(f"Error: Resulting empty dataset")

            rf_dataset = build_rf_dataset(featured_windows, target_artifact=artifact, features_dir=str(FEATURES_DIR))

        split_counts = rf_dataset["split"].value_counts(dropna=False)
        print("[INFO] Split distribution: ", split_counts)

        print(f"\nStarting training of Random Forest ({artifact})")

        config = RANDOM_SPACE[artifact]
        results[artifact] = binary_rf(rf_dataset, window_size_sec=WINDOW_REQUESTS_ARTIFACTS[artifact], model_name=f"rf_{artifact}", 
                                      models_dir=str(MODELS_DIR), leakage_cols= LEAKAGE_COLS,
                                      search_method="random",
                                      search_data=config["space"],
                                      search_kwargs={"n_iter": config["n_iter"]},
                                      force_retrain=True, balanced_bootstrap=True,
                                      max_fp_per_day=config["max_fp_per_day"]
                                     )

    print("\n"+"*-" * 25)
    print("Final report")
    for artifact, res in results.items():
        print(('-'*10),artifact,('-'*10))
        print(f"\t\t F1(val)={res['val_f1']:.4f}")
        print(f"\t\t best_params={res['params']}")
        print("\t\t Confusion matrix:", res['confusion_matrix'])
        print("\t\t Metrics results:", res['metrics_results'])