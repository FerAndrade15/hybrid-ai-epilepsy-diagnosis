"""
# File: rf_model.py
# Project: Trabajo de graduación
# Author: Maria Fernanda Andrade Recinos

Reusable RF (Random Forest) modules for the AI pipeline.
"""

import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.multioutput import MultiOutputClassifier
from sklearn.model_selection import GridSearchCV, GroupKFold, cross_val_score
from sklearn.metrics import make_scorer, f1_score

# Binary RF
def train_binary_rf(X, y, model_name="model", test_size=0.2, random_state=42,
                    rf_params=None, verbose=True):
    """
    Generic function to train a binary Random Forest classifier.
    y: DataFrame with a binary column (0/1) / Series with binary labels.
    """
    rf_params = rf_params or {}
    rf_params.setdefault("n_estimators", 200)
    rf_params.setdefault("max_depth", None)
    rf_params.setdefault("min_samples_split", 2)
    rf_params.setdefault("min_samples_leaf", 1)
    rf_params.setdefault("max_features", "sqrt")
    rf_params.setdefault("class_weight", "balanced_subsample")
    rf_params.setdefault("random_state", random_state)
    rf_params.setdefault("n_jobs", -1)
    
    model = RandomForestClassifier(
        class_weight="balanced_subsample",
        n_jobs=-1,
        random_state=42,
        **rf_params,
    )
    if sample_weight is not None:
        model.fit(X, y, sample_weight=sample_weight)
    else:
        model.fit(X, y)
    return model
# Multilabel training
def train_rf(X, y, sample_weight=None, targets=DEFAULT_TARGETS, **rf_params):
    """
    y: DataFrame con una columna binaria por categoría (multi-label).
    Entrena un RF binario por categoría vía MultiOutputClassifier.
    """
    base = RandomForestClassifier(
        class_weight="balanced_subsample",
        n_jobs=-1,
        random_state=42,
        **rf_params,
    )
    model = MultiOutputClassifier(base)
    fit_params = {}
    if sample_weight is not None:
        model.fit(X, y[targets], sample_weight=sample_weight)
    else:
        model.fit(X, y[targets])
    return model


def macro_f1_multilabel(y_true, y_pred):
    return np.mean([
        f1_score(y_true.iloc[:, i], y_pred[:, i], zero_division=0)
        for i in range(y_true.shape[1])
    ])

# Grid search optimization 
def optimize_rf_gridsearch(X, y, groups, targets=DEFAULT_TARGETS,
                            param_grid=None, cv_splits=5, n_jobs=1, m_jobs=1):
    if param_grid is None:
        param_grid = {
            "estimator__n_estimators": [200, 400, 600],
            "estimator__max_depth": [None, 10, 20, 30],
            "estimator__min_samples_split": [2, 5, 10],
            "estimator__min_samples_leaf": [1, 2, 4],
            "estimator__max_features": ["sqrt", "log2"],
        }

    base = MultiOutputClassifier(
        RandomForestClassifier(class_weight="balanced_subsample", random_state=42, n_jobs=m_jobs)
    )
    gkf = GroupKFold(n_splits=cv_splits)
    scorer = make_scorer(macro_f1_multilabel)

    cv_splits_list = list(gkf.split(X, y[targets], groups))

    search = GridSearchCV(
        base, 
        param_grid, 
        scoring=scorer, 
        cv=cv_splits_list,
        n_jobs=n_jobs, 
        verbose=3,
        error_score='raise'
    )
    search.fit(X, y[targets])
    return search.best_estimator_, search.best_params_, search.best_score_


# Honey Badger Algorithm (Hashim et al., 2022) — metaheurístico
def _decode_position(pos, bounds):
    """pos: vector en [0,1]^d -> valores reales dentro de bounds."""
    decoded = []
    for p, (lo, hi) in zip(pos, bounds):
        decoded.append(lo + p * (hi - lo))
    return decoded

def _params_from_vector(vec):
    n_estimators = int(round(vec[0]))
    max_depth = int(round(vec[1])) if vec[1] > 2 else None
    min_samples_split = int(round(vec[2]))
    min_samples_leaf = int(round(vec[3]))
    max_features_frac = float(np.clip(vec[4], 0.1, 1.0))
    return dict(
        n_estimators=max(n_estimators, 50),
        max_depth=max_depth,
        min_samples_split=max(min_samples_split, 2),
        min_samples_leaf=max(min_samples_leaf, 1),
        max_features=max_features_frac,
    )

def honey_badger_optimizer(fitness_fn, bounds, n_agents=15, max_iter=25,
                            beta=6.0, C=2.0, seed=42, verbose=True):
    """
    Implementación del Honey Badger Algorithm para maximizar fitness_fn(vec) -> float.
    bounds: lista de (min, max) por dimensión.
    Devuelve (mejor_vector, mejor_score, historial_scores).
    """
    rng = np.random.default_rng(seed)
    dim = len(bounds)
    lo = np.array([b[0] for b in bounds])
    hi = np.array([b[1] for b in bounds])

    positions = rng.uniform(lo, hi, size=(n_agents, dim))
    fitness = np.array([fitness_fn(p) for p in positions])

    best_idx = np.argmax(fitness)
    prey_pos = positions[best_idx].copy()
    prey_fit = fitness[best_idx]
    history = [prey_fit]

    for t in range(1, max_iter + 1):
        alpha = C * np.exp(-t / max_iter) 
        for i in range(n_agents):
            r = rng.random(9)
            d_i = np.linalg.norm(prey_pos - positions[i]) + 1e-12
            S_i = (positions[i] - (positions[i - 1] if i > 0 else positions[-1])) ** 2
            intensity = r[0] ** 2 * np.mean(S_i) / (4 * np.pi * d_i ** 2 + 1e-12)

            F = 1.0 if r[1] <= 0.5 else -1.0

            if r[2] < 0.5:
                # fase de excavación (digging)
                new_pos = prey_pos + F * beta * intensity * prey_pos + \
                          F * r[3] * alpha * d_i * np.abs(
                              np.cos(2 * np.pi * r[4]) * (1 - np.cos(2 * np.pi * r[5]))
                          )
            else:
                # fase de la miel (honey)
                new_pos = prey_pos + F * r[6] * alpha * d_i

            new_pos = np.clip(new_pos, lo, hi)
            new_fit = fitness_fn(new_pos)

            if new_fit > fitness[i]:  # selección voraz
                positions[i] = new_pos
                fitness[i] = new_fit

        gen_best = np.argmax(fitness)
        if fitness[gen_best] > prey_fit:
            prey_fit = fitness[gen_best]
            prey_pos = positions[gen_best].copy()

        history.append(prey_fit)
        if verbose:
            print(f"[HBA] iter {t}/{max_iter} - mejor score: {prey_fit:.4f}")

    return prey_pos, prey_fit, history

def optimize_rf_hba(X, y, groups, targets=DEFAULT_TARGETS, cv_splits=5,
                     n_agents=15, max_iter=25, seed=42):
    """
    bounds: [n_estimators, max_depth, min_samples_split, min_samples_leaf, max_features_frac]
    """
    bounds = [(50, 800), (3, 40), (2, 20), (1, 10), (0.1, 1.0)]
    gkf = GroupKFold(n_splits=cv_splits)
    scorer = make_scorer(macro_f1_multilabel)

    def fitness_fn(vec):
        params = _params_from_vector(vec)
        base = MultiOutputClassifier(
            RandomForestClassifier(class_weight="balanced_subsample", random_state=42,
                                    n_jobs=-1, **params)
        )
        scores = cross_val_score(
            base, X, y[targets], groups=groups, cv=gkf, scoring=scorer, n_jobs=1,
        )
        return scores.mean()

    best_vec, best_score, history = honey_badger_optimizer(
        fitness_fn, bounds, n_agents=n_agents, max_iter=max_iter, seed=seed,
    )
    best_params = _params_from_vector(best_vec)
    return best_params, best_score, history

if __name__ == "__main__":
    train = pd.read_parquet("features/features_train.parquet")
    feature_cols = [c for c in train.columns if c not in
                    ["Patient", "Session", "Start", "is_clean_window", "is_ambiguous",
                     "is_excluded", "eye", "muscle", "non_physiological", "sample_weight"]
                    and not c.startswith("coverage_")]

    X = train[feature_cols]
    y = train[DEFAULT_TARGETS]
    groups = train["Patient"]

    best_params_hba, best_score_hba, hist = optimize_rf_hba(X, y, groups, max_iter=20, n_agents=12)
    print("HBA best params:", best_params_hba, "score:", best_score_hba)

    best_model_gs, best_params_gs, best_score_gs = optimize_rf_gridsearch(X, y, groups)
    print("GridSearch best params:", best_params_gs, "score:", best_score_gs)