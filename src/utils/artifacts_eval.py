"""
# File: artifacts_eval.py
# Project: Trabajo de graduación
# 
# Several functions required to understand the validation applied 
# for the data structure and artifacts pipeline.
#
"""
from pathlib import Path
import numpy as np
from sklearn.metrics import average_precision_score, precision_score, recall_score

from src.core.data_config import BIPOLAR_MONTAGE, MONOPOLAR_CHANNELS
from src.core.preprocessing import bipolar_matrix

KEY = ["Patient", "Session", "Section", "Start"]


def _mean(x):
    return float(np.mean(x)) if len(x) else float("nan")


class MedicalEval:
    eval_col = "y_med"

    def __init__(self, artifact, session_cache_dir, k=3, universe=None):
        """
        session_cache_dir: el mismo que pasas a get_or_build_features (cache/sessions).
        universe: opcional, ventanas del split ANTES de la ICA (Patient, Session,
                  Section, Start, split, <artifact>) para medir recall de extremo a extremo.
        """
        self.artifact, self.k, self.universe = artifact, k, universe
        self.session_cache_dir = Path(session_cache_dir)
        self.truth_col = f"tuar_{artifact}"
        self.bip_col = f"bipolar_channels_{artifact}"
        self.mono_col = f"monopolar_channels_{artifact}"
        self.W = bipolar_matrix()                       # 18x19
        self.bip_names = list(BIPOLAR_MONTAGE["names"])
        self.meta = None
        self._mix = {}

    # --- antes de que train_binary_model borre tuar_* y *channels* -------------
    def fit_meta(self, df):
        cols = [self.truth_col, self.bip_col, self.mono_col]
        self.meta = df.drop_duplicates(KEY).set_index(KEY)[cols]
        return self

    def add_truth(self, df):
        truth = self.meta[self.truth_col].reset_index()
        y = df[KEY].merge(truth, on=KEY, how="left")[self.truth_col]
        assert y.notna().all(), "hay ventanas sin verdad médica"
        return df.assign(**{self.eval_col: (y.values > 0).astype(int)})

    # --- utilidades -------------------------------------------------------------
    def _mixing(self, patient, session, section):
        key = (patient, session, section)
        if key not in self._mix:
            f = self.session_cache_dir / f"{patient}_{session}_{section}_mono.npz"
            with np.load(f) as z:
                self._mix[key] = z["mixing"]            # (19, n_ic), con signo
        return self._mix[key]

    @staticmethod
    def _pairs(names):
        return {frozenset(str(n).upper().split("-")) for n in names}

    def _topk_bipolar(self, mix_col):
        topo = np.abs(self.W @ mix_col)                 # primero W con signo, luego abs
        return self._pairs(self.bip_names[i] for i in np.argsort(-topo)[: self.k])

    def _topk_mono(self, mix_col):
        return {MONOPOLAR_CHANNELS[i].upper() for i in np.argsort(-np.abs(mix_col))[: self.k]}

    # --- reporte (solo test, con el umbral elegido en val) ----------------------
    def report(self, df_split, prob, threshold):
        t = df_split[KEY + ["ic_index"]].copy().reset_index(drop=True)
        t["p"] = np.asarray(prob)
        t["y"] = df_split[self.eval_col].values
        w = t.loc[t.groupby(KEY, sort=False)["p"].idxmax()].reset_index(drop=True)  # IC ganador

        y, pred = w["y"].astype(int).values, (w["p"] >= threshold).values
        out = {
            "win_precision": precision_score(y, pred, zero_division=0),
            "win_recall": recall_score(y, pred, zero_division=0),
            "win_AP": average_precision_score(y, w["p"]),
        }
        tp = w[pred & (y == 1)]
        out["n_tp_windows"] = len(tp)

        if self.universe is not None:                   # ventanas que la ICA descartó también cuentan
            u = self.universe[self.universe["split"] == "test"]
            out["n_pos_universe"] = int(u[self.artifact].sum())
            out["n_pos_scored"] = int(y.sum())
            out["recall_end2end"] = len(tp) / max(out["n_pos_universe"], 1)

        meta = self.meta.to_dict("index")
        bip_hit, bip_iou, mono_hit = [], [], []
        for r in tp.itertuples(index=False):
            m = meta[(r.Patient, r.Session, r.Section, r.Start)]
            col = self._mixing(r.Patient, r.Session, r.Section)[:, int(r.ic_index)]
            gt_b = self._pairs(m[self.bip_col])
            if gt_b:
                top = self._topk_bipolar(col)
                inter = len(top & gt_b)
                bip_hit.append(inter > 0)
                bip_iou.append(inter / len(top | gt_b))
            gt_m = {str(c).upper() for c in m[self.mono_col]}
            if gt_m:
                mono_hit.append(len(self._topk_mono(col) & gt_m) > 0)

        out.update({
            f"ch_bip_hit@{self.k}": _mean(bip_hit), "ch_bip_iou": _mean(bip_iou),
            "n_tp_with_bip_gt": len(bip_hit),
            f"ch_mono_hit@{self.k}": _mean(mono_hit), "n_tp_with_mono_gt": len(mono_hit),
        })
        return {k: round(float(v), 4) for k, v in out.items()}