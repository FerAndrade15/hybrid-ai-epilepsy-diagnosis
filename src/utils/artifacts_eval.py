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


def artifact_channel_masks(session_group, keywords, n_samples, sfreq, bip_names):
    """
    Verdad por canal y tiempo para UNA sesión y UNA categoría:
    Y[c, t] = True si TUAR marca ese par bipolar con una etiqueta de `keywords`.
    n_samples: longitud REAL del caché (data.shape[1]), no la del header.
    """
    from src.core.preprocessing import channel_standard_nomenclature   # import perezoso (evita ciclos)
    from src.core.windowing import split_compound_label

    idx = {frozenset(n.upper().split("-")): i for i, n in enumerate(bip_names)}
    Y = np.zeros((len(bip_names), n_samples), bool)
    for r in session_group.itertuples():
        pair = [channel_standard_nomenclature(x) for x in str(r.channel).split("-")]
        if len(pair) != 2 or None in pair:
            continue                                   # par no mapeable: queda fuera, no como 0
        i = idx.get(frozenset(p.upper() for p in pair))
        if i is None:
            continue
        if split_compound_label(str(r.label)) & set(keywords):
            a = int(r.start_time * sfreq)
            b = min(int(r.stop_time * sfreq), n_samples)
            Y[i, a:b] = True
    return Y


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

    # --- reporte ORIGINAL (solo test, con el umbral elegido en val) -------------
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

    # ===================== NUEVO: localización por canal (etapa 1) ================
    def channel_scores(self, df_split, prob):
        """P[c] por ventana (noisy-OR sobre TODOS los componentes). Devuelve (keys, P[n_win, 18])."""
        t = df_split[KEY + ["ic_index"]].reset_index(drop=True).assign(p=np.asarray(prob))
        keys, rows = [], []
        for key, g in t.groupby(KEY, sort=False):
            A = self._mixing(key[0], key[1], key[2])               # (19, n_ic)
            ks = g["ic_index"].to_numpy(int)
            m = np.abs(self.W @ A[:, ks])                          # (18, K)  |W a_k|
            w = m / (m.max(axis=0, keepdims=True) + 1e-12)         # en [0, 1]
            p = g["p"].to_numpy()[None, :]                         # (1, K)
            rows.append(1.0 - np.prod(1.0 - p * w, axis=1))        # (18,)
            keys.append(key)
        return keys, np.vstack(rows)

    def channel_truth(self, keys):
        """G[n_win, 18] con los pares anotados; ok=False si es positiva sin canales mapeables."""
        pos = {frozenset(n.upper().split("-")): i for i, n in enumerate(self.bip_names)}
        meta = self.meta.to_dict("index")
        G = np.zeros((len(keys), len(self.bip_names)), bool)
        ok = np.ones(len(keys), bool)
        for r, key in enumerate(keys):
            for pr in self._pairs(meta[key][self.bip_col]):
                if pr in pos:
                    G[r, pos[pr]] = True
            if meta[key][self.truth_col] > 0 and not G[r].any():
                ok[r] = False
        return G, ok

    @staticmethod
    def pick_tau(P, G, grid=np.linspace(0.05, 0.95, 19)):
        """Umbral por canal elegido en VALIDACIÓN (maximiza F1 micro)."""
        def f1(tau):
            Ph = P >= tau
            tp = (Ph & G).sum()
            return 2 * tp / max(2 * tp + (Ph & ~G).sum() + (~Ph & G).sum(), 1)
        return float(max(grid, key=f1))

    def report_channels(self, df_split, prob, tau):
        keys, P = self.channel_scores(df_split, prob)
        G, ok = self.channel_truth(keys)
        P, G = P[ok], G[ok]
        Ph = P >= tau
        tp = (Ph & G).sum(0); fp = (Ph & ~G).sum(0); fn = (~Ph & G).sum(0)
        inter, union = (Ph & G).sum(1), (Ph | G).sum(1)
        act = union > 0
        has = (tp + fn) > 0
        out = {
            "ch_f1_micro": 2 * tp.sum() / max(2 * tp.sum() + fp.sum() + fn.sum(), 1),
            "ch_f1_macro": float((2 * tp / np.maximum(2 * tp + fp + fn, 1))[has].mean()) if has.any() else float("nan"),
            "ch_jaccard": float((inter[act] / union[act]).mean()) if act.any() else float("nan"),
            "n_win_scored": int(ok.sum()),
        }
        return {k: round(float(v), 4) for k, v in out.items()}

    # ===================== NUEVO: localización temporal (etapa 3) =================
    def window_activity(self, S, A, X, ks, p, start, end, sfreq, tau_k, bin_s=0.25):
        """R[c, bin]: fracción de la energía bipolar explicada por los componentes marcados (p >= tau_k)."""
        a, b = int(round(start * sfreq)), int(round(end * sfreq))
        L = int(bin_s * sfreq)
        nb = (b - a) // L
        sel = ks[p >= tau_k]
        if len(sel) == 0 or nb == 0:
            return np.zeros((len(self.bip_names), max(nb, 0)))
        art = (self.W @ A[:, sel]) @ S[sel, a:b]            # (18, T) artefacto proyectado
        sig = self.W @ X[:, a:b]                            # (18, T) señal total bipolar
        e = lambda M: (M[:, :nb * L] ** 2).reshape(len(self.bip_names), nb, L).mean(2)
        return e(art) / (e(sig) + 1e-12)

    def time_arrays(self, df_split, prob, tau_k, ann_by_session, keywords, win_sec, bin_s=0.25):
        """
        Recorre las ventanas y devuelve (R, Yb) aplanados a (n_bins_total, 18):
        actividad reconstruida y verdad binada. ann_by_session = {(Patient, Session, Section): anotaciones}.
        """
        t = df_split[KEY + ["ic_index"]].reset_index(drop=True).assign(p=np.asarray(prob))
        meta = self.meta.to_dict("index")
        Rs, Ys = [], []
        for sess, gs in t.groupby(["Patient", "Session", "Section"], sort=False):
            f = self.session_cache_dir / f"{sess[0]}_{sess[1]}_{sess[2]}_mono.npz"
            with np.load(f) as z:
                S, A, X, sf = z["sources_full"], z["mixing"], z["data"], float(z["sfreq"])
            Y = artifact_channel_masks(ann_by_session[sess], keywords, X.shape[1], sf, self.bip_names)
            L = int(bin_s * sf)
            for key, g in gs.groupby("Start", sort=False):
                start = float(key)
                a, b = int(round(start * sf)), int(round((start + win_sec) * sf))
                nb = (b - a) // L
                if nb == 0 or b > X.shape[1]:
                    continue
                Yb = Y[:, a:b][:, :nb * L].reshape(len(self.bip_names), nb, L).any(2)
                m = meta[(sess[0], sess[1], sess[2], start)]
                if m[self.truth_col] > 0 and not Yb.any():
                    continue                                # positiva sin canales mapeables: fuera
                R = self.window_activity(S, A, X, g["ic_index"].to_numpy(int), g["p"].to_numpy(),
                                         start, start + win_sec, sf, tau_k, bin_s)
                Rs.append(R.T); Ys.append(Yb.T)             # (nb, 18)
        return np.vstack(Rs), np.vstack(Ys)

    @staticmethod
    def pick_rho(R, Yb, grid=np.linspace(0.05, 0.95, 19)):
        def f1(rho):
            Ph = R >= rho
            tp = (Ph & Yb).sum()
            return 2 * tp / max(2 * tp + (Ph & ~Yb).sum() + (~Ph & Yb).sum(), 1)
        return float(max(grid, key=f1))

    @staticmethod
    def report_time(R, Yb, rho):
        Ph = R >= rho
        tp = (Ph & Yb).sum(); fp = (Ph & ~Yb).sum(); fn = (~Ph & Yb).sum()
        out = {
            "t_precision": tp / max(tp + fp, 1),
            "t_recall": tp / max(tp + fn, 1),
            "t_f1": 2 * tp / max(2 * tp + fp + fn, 1),
            "n_bins": int(len(R)),
        }
        return {k: round(float(v), 4) for k, v in out.items()}


if __name__ == "__main__":
    import tempfile
    import pandas as pd

    rng = np.random.default_rng(0)
    sf, T = 256, 256 * 8
    mono = [c.upper() for c in MONOPOLAR_CHANNELS]
    pairs = list(BIPOLAR_MONTAGE["names"])
    j = pairs.index("FP1-F7")

    A = np.zeros((19, 2))
    A[mono.index("FP1"), 0] = 1.0                       # comp 0: frontal
    A[mono.index("O1"), 1] = 1.0                        # comp 1: occipital
    A[mono.index("O2"), 1] = 1.0
    S = rng.normal(size=(2, T))
    X = A @ S

    with tempfile.TemporaryDirectory() as tmp:
        np.savez(Path(tmp) / "P1_s1_t1_mono.npz", data=X, sfreq=sf, mixing=A, sources_full=S)
        ev = MedicalEval("eye", tmp, k=3)

        meta = pd.DataFrame({
            "Patient": ["P1", "P1"], "Session": ["s1", "s1"], "Section": ["t1", "t1"],
            "Start": [0.0, 2.0], "tuar_eye": [1, 0],
            "bipolar_channels_eye": [["FP1-F7"], []],
            "monopolar_channels_eye": [["FP1", "F7"], []],
        })
        ev.fit_meta(meta)
        df = pd.DataFrame({"Patient": "P1", "Session": "s1", "Section": "t1",
                           "Start": [0.0, 0.0, 2.0, 2.0], "ic_index": [0, 1, 0, 1]})
        prob = np.array([0.9, 0.05, 0.1, 0.05])

        keys, P = ev.channel_scores(df, prob)
        far = [pairs.index(n) for n in ("P8-O2", "P4-O2", "P3-O1", "P7-O1")]
        assert P.shape == (2, 18)
        assert abs(P[0, j] - 0.9) < 1e-9 and np.allclose(P[0, far], 0.05) and abs(P[1, j] - 0.1) < 1e-9
        print("[OK] channel_scores")

        G, ok = ev.channel_truth(keys)
        assert G[0].sum() == 1 and G[0, j] and G[1].sum() == 0 and ok.all()
        print("[OK] channel_truth")

        rep = ev.report_channels(df, prob, tau=0.5)
        assert abs(rep["ch_f1_micro"] - 2 / 3) < 1e-3 and abs(rep["ch_jaccard"] - 0.5) < 1e-3
        print("[OK] report_channels", rep)

        ks = np.array([0, 1])
        act = np.abs(ev.W @ A).sum(1) > 0
        R_all = ev.window_activity(S, A, X, ks, np.array([0.9, 0.05]), 0.0, 8.0, sf, tau_k=0.0)
        assert R_all.shape == (18, 32) and np.allclose(R_all[act], 1.0, atol=1e-6)
        print("[OK] window_activity (identidad A@S = X)")

        R_one = ev.window_activity(S, A, X, ks, np.array([0.9, 0.05]), 0.0, 8.0, sf, tau_k=0.5)
        assert R_one[j].min() > 0.99 and R_one[far].max() < 1e-6
        print("[OK] window_activity (selección por componente)")

    print("[OK] artifacts_eval")