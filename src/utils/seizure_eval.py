# File: src/utils/seizure_eval.py

import numpy as np
import pandas as pd
from sklearn.metrics import (confusion_matrix, recall_score, precision_score,
                             accuracy_score, f1_score, roc_auc_score)

def get_intervals_from_binary_mask(mask):
    """
    Convierte un vector booleano 1D en una lista de intervalos (start_idx, end_idx).
    Usamos índices en lugar de segundos para igualar el código original del paper.
    """
    if len(mask) == 0:
        return []
        
    mask = np.concatenate(([0], mask, [0]))
    diff = np.diff(mask)
    starts = np.where(diff == 1)[0]
    ends = np.where(diff == -1)[0]
    
    if len(starts) == 0:
        return []
        
    return [(starts[i], ends[i]) for i in range(len(starts))]


def calc_hf(ref_start, ref_end, hyp_start, hyp_end):
    """Calcula hit y false alarm para un solapamiento individual (según Ziyabari et al.)"""
    ref_dur = ref_end - ref_start
    if ref_dur == 0: ref_dur = 1e-9 # Prevención div/0
        
    hyp_dur = hyp_end - hyp_start
    hit = 0.0
    fa = 0.0

    if hyp_start <= ref_start and hyp_end <= ref_end:
        hit = (hyp_end - ref_start) / ref_dur
        fa = (ref_start - hyp_start) / ref_dur if (ref_start - hyp_start) / ref_dur < 1.0 else 1.0
    elif hyp_start >= ref_start and hyp_end >= ref_end:
        hit = (ref_end - hyp_start) / ref_dur
        fa = (hyp_end - ref_end) / ref_dur if (hyp_end - ref_end) / ref_dur < 1.0 else 1.0
    elif hyp_start < ref_start and hyp_end > ref_end:
        hit = 1.0
        fa = ((hyp_end - ref_end) + (ref_start - hyp_start)) / ref_dur
        if fa > 1.0: fa = 1.0
    else:
        hit = (hyp_end - hyp_start) / ref_dur

    return hit, max(0.0, fa)


def evaluate_taes(ref_intervals, hyp_intervals):
    """Calcula el Time-Aligned Event Score para toda la sesión."""
    hit_t, mis_t, fal_t = 0.0, 0.0, 0.0
    
    # Esta es una aproximación directa y eficiente de la métrica TAES
    for r_s, r_e in ref_intervals:
        r_dur = r_e - r_s
        overlap = 0.0
        for h_s, h_e in hyp_intervals:
            o_s = max(r_s, h_s)
            o_e = min(r_e, h_e)
            if o_e > o_s:
                overlap += (o_e - o_s)
        
        hit_t += (overlap / r_dur) if r_dur > 0 else 0
        mis_t += (1.0 - (overlap / r_dur)) if r_dur > 0 else 1.0

    for h_s, h_e in hyp_intervals:
        overlap = 0.0
        for r_s, r_e in ref_intervals:
            o_s = max(r_s, h_s)
            o_e = min(r_e, h_e)
            if o_e > o_s:
                overlap += (o_e - o_s)
        if overlap == 0:
            fal_t += 1.0
            
    return hit_t, mis_t, fal_t


def evaluate_ovlp(ref_intervals, hyp_intervals):
    """Calcula Any-Overlap (OVLP)."""
    hit, mis, fal = 0, 0, 0
    
    for r_s, r_e in ref_intervals:
        overlapped = False
        for h_s, h_e in hyp_intervals:
            if h_e > r_s and h_s < r_e:
                overlapped = True
                break
        if overlapped: hit += 1
        else: mis += 1
        
    for h_s, h_e in hyp_intervals:
        overlapped = False
        for r_s, r_e in ref_intervals:
            if h_e > r_s and h_s < r_e:
                overlapped = True
                break
        if not overlapped: fal += 1
        
    return hit, mis, fal


def full_report(val_preds, test_preds, margin_sec=5, window_size_sec=4, shift_sec=1):
    """
    Busca el mejor umbral en Validación (maximizando TPR + TNR) y lo aplica al Test set, 
    idéntico a la metodología de Lee et al.
    """
    # Excluimos las columnas base, nos quedamos con las probabilidades de clase (ej. "p_seiz", "p_focal")
    prob_cols = [c for c in val_preds.columns if c.startswith("p_")]
    
    reports = []
    
    for p_col in prob_cols:
        cat = p_col.replace("p_", "")
        y_col = f"y_{cat}"
        
        # --- BÚSQUEDA DE UMBRAL EN VALIDACIÓN ---
        best_threshold = 0.5
        best_score = -1
        
        # Iterar en 100 pasos (optimizado vs 500 del paper para velocidad)
        for i in range(1, 100):
            thr = i / 100.0
            hit_t, fal_t, refo_t, hypo_t = 0, 0, 0, 0
            
            for keys, group in val_preds.groupby("key"):
                y_true = group[y_col].values
                y_pred = (group[p_col].values > thr).astype(int)
                
                ref_events = get_intervals_from_binary_mask(y_true)
                hyp_events = get_intervals_from_binary_mask(y_pred)
                
                refo_t += len(ref_events)
                hypo_t += len(hyp_events)
                
                h, m, f = evaluate_ovlp(ref_events, hyp_events)
                hit_t += h
                fal_t += f
                
            tpr = hit_t / refo_t if refo_t > 0 else 1.0
            tnr = 1.0 - (fal_t / hypo_t) if hypo_t > 0 else 0.0
            
            if (tpr + tnr) > best_score:
                best_score = tpr + tnr
                best_threshold = thr
                
        # --- EVALUACIÓN FINAL EN TEST ---
        hit_t, mis_t, fal_t, refo_t, hypo_t = 0, 0, 0, 0, 0
        taes_hit_t, taes_mis_t, taes_fal_t = 0.0, 0.0, 0.0
        onset_hits, offset_hits = 0, 0
        
        total_duration_windows = 0
        
        for keys, group in test_preds.groupby("key"):
            y_true = group[y_col].values
            y_pred = (group[p_col].values > best_threshold).astype(int)
            total_duration_windows += len(y_true)
            
            ref_events = get_intervals_from_binary_mask(y_true)
            hyp_events = get_intervals_from_binary_mask(y_pred)
            
            refo_t += len(ref_events)
            hypo_t += len(hyp_events)
            
            # OVLP
            h, m, f = evaluate_ovlp(ref_events, hyp_events)
            hit_t += h; mis_t += m; fal_t += f
            
            # TAES
            t_h, t_m, t_f = evaluate_taes(ref_events, hyp_events)
            taes_hit_t += t_h; taes_mis_t += t_m; taes_fal_t += t_f
            
            # MARGIN (Convertir margen en segundos a número de ventanas)
            margin_windows = int(margin_sec / shift_sec)
            for r_s, r_e in ref_events:
                o_matched, e_matched = False, False
                for h_s, h_e in hyp_events:
                    if abs(h_s - r_s) <= margin_windows: o_matched = True
                    if abs(h_e - r_e) <= margin_windows: e_matched = True
                if o_matched: onset_hits += 1
                if e_matched: offset_hits += 1

        # Cálculos Finales OVLP
        ovlp_tpr = hit_t / refo_t if refo_t > 0 else 1.0
        ovlp_tnr = 1.0 - (fal_t / hypo_t) if hypo_t > 0 else 0.0
        ovlp_fa24 = (fal_t / (total_duration_windows * shift_sec)) * (60 * 60 * 24) if total_duration_windows > 0 else 0.0
        
        # Cálculos Finales TAES
        taes_tpr = taes_hit_t / refo_t if refo_t > 0 else 1.0
        taes_tnr = 1.0 - (taes_fal_t / hypo_t) if hypo_t > 0 else 0.0
        taes_fa24 = (taes_fal_t / (total_duration_windows * shift_sec)) * (60 * 60 * 24) if total_duration_windows > 0 else 0.0
        
        reports.append({
            "Class": cat,
            "Best_Threshold": best_threshold,
            "OVLP_Sens": round(ovlp_tpr, 4),
            "OVLP_Spec": round(ovlp_tnr, 4),
            "OVLP_FA/24h": round(ovlp_fa24, 2),
            "TAES_Sens": round(taes_tpr, 4),
            "MARGIN_Onset": round(onset_hits / refo_t if refo_t > 0 else 0, 4),
            "MARGIN_Offset": round(offset_hits / refo_t if refo_t > 0 else 0, 4)
        })
        
    return pd.DataFrame(reports)

def compute_window_metrics(y_true, y_pred, y_prob, stride_sec, model_name="model"):
    """Mismas métricas por ventana que compute_full_metrics de ml_models, sin depender de ese módulo."""
    tn, fp, fn, tp = confusion_matrix(y_true, y_pred, labels=[0, 1]).ravel()
    try:
        auc_roc = roc_auc_score(y_true, y_prob)
    except ValueError:
        auc_roc = np.nan
    total_time_sec = len(y_true) * stride_sec
    total_days = total_time_sec / 86400
    return {
        "model": model_name,
        "sensitivity": round(recall_score(y_true, y_pred, zero_division=0), 4),
        "specificity": round(tn / (tn + fp), 4) if (tn + fp) > 0 else np.nan,
        "precision": round(precision_score(y_true, y_pred, zero_division=0), 4),
        "accuracy": round(accuracy_score(y_true, y_pred), 4),
        "f1_score": round(f1_score(y_true, y_pred, zero_division=0), 4),
        "auc_roc": round(auc_roc, 4) if not np.isnan(auc_roc) else np.nan,
        "false_alarm_rate": round(fp / (fp + tn), 4) if (fp + tn) > 0 else np.nan,
        "fp_per_day": round(fp / total_days, 2) if total_days > 0 else np.nan,
        "covered_test_days": round(total_days, 4),
        "TP": int(tp), "FP": int(fp), "TN": int(tn), "FN": int(fn),
        "n_test_windows": len(y_true),
        "covered_test_hours": round(total_time_sec / 3600, 2),
    }


def window_metrics(test_preds, thresholds, shift_sec=1):
    """Métricas por ventana y por clase, con el umbral elegido en validación."""
    rows = []
    for cat, thr in thresholds.items():
        y_true = test_preds[f"y_{cat}"].astype(int).values
        y_prob = test_preds[f"p_{cat}"].values
        y_pred = (y_prob > thr).astype(int)
        rows.append(compute_window_metrics(y_true, y_pred, y_prob, shift_sec, model_name=cat))
    return pd.DataFrame(rows)