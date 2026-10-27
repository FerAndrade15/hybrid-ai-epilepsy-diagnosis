# File: src/utils/seizure_dataset.py
import numpy as np
import torch
import random
from torch.utils.data import Dataset, WeightedRandomSampler

# Configuraciones de tu proyecto
from src.core.data_config import SFREQ, WINDOWS_REQUESTS_SEIZURES

# Utilities
from src.utils.session_cache import get_or_compute_session, get_bip_slice
from src.core.windowing import taxonomy_intervals, mask_from_intervals, window_labels

class HybridSeizureDataset(Dataset):
    """
    Dataset Agnóstico: Agrupa ventanas consecutivas en 'chunks' para alimentar el LSTM.
    Soporta tareas Binarias y Multilabel basado en el `target_taxonomy`.
    """
    def __init__(self, index_df, split_name, target_taxonomy, 
                 bipolar_montage=True, use_ica=False,
                 ica_cache_dir="cache/ica", session_cache_dir="cache/sessions"):
        
        self.win_sec = WINDOWS_REQUESTS_SEIZURES["win_sec"]
        self.shift_sec = WINDOWS_REQUESTS_SEIZURES["shift_sec"]
        self.min_pos_sec = WINDOWS_REQUESTS_SEIZURES["min_pos_sec"]
        self.cw = WINDOWS_REQUESTS_SEIZURES["chunk_windows"]
        
        self.win = int(self.win_sec * SFREQ)
        self.shift = int(self.shift_sec * SFREQ)
        
        self.bipolar_montage = bipolar_montage
        self.use_ica = use_ica
        self.ica_cache_dir = ica_cache_dir
        self.session_cache_dir = session_cache_dir
        
        self.classes = list(target_taxonomy.keys())
        
        # Filtrar el dataframe por el split (train, val, test)
        df = index_df[index_df["split"] == split_name].reset_index(drop=True)
        group_cols = ["Patient", "Session", "Section", "EDF_path"]
        
        self.wlabels = []
        self.chunks = []
        self.sessions_info = []
        
        si = 0
        for keys, group in df.groupby(group_cols, dropna=False):
            patient, session, section, edf_path = keys
            
            duration_s = float(group["Duration"].iloc[0])
            total_samples = int(duration_s * SFREQ)
            
            # Usar la extracción agnóstica de windowing.py
            intervals_dict = taxonomy_intervals(group, target_taxonomy)
            
            session_labels = []
            for cat in self.classes:
                iv = intervals_dict[cat]
                y_mask = mask_from_intervals(iv, total_samples, SFREQ)
                wl = window_labels(y_mask, SFREQ, self.win_sec, self.shift_sec, self.min_pos_sec)
                session_labels.append(wl)
                
            wl_stacked = np.column_stack(session_labels)
            
            if len(wl_stacked) >= self.cw:
                self.wlabels.append(wl_stacked)
                self.sessions_info.append({
                    "Patient": patient,
                    "Session": session,
                    "Section": section,
                    "EDF_path": edf_path
                })
                
                # Cortar la sesión en bloques de 60 (chunk_windows)
                for w0 in range(0, len(wl_stacked) - self.cw + 1, self.cw):
                    self.chunks.append((si, w0))
                
                si += 1
                
        self.chunk_pos = np.array([bool(self.wlabels[idx][w0:w0 + self.cw].any()) for idx, w0 in self.chunks])
        print(f"[INFO] HybridSeizureDataset[{split_name}]: {len(self.chunks)} chunks, {int(self.chunk_pos.sum())} con eventos objetivos.")

    def __len__(self):
        return len(self.chunks)

    def __getitem__(self, i):
        try:
            si, w0 = self.chunks[i]
            sess_meta = self.sessions_info[si]

            a = w0 * self.shift
            b = (w0 + self.cw - 1) * self.shift + self.win

            x = get_bip_slice(sess_meta["Patient"], sess_meta["Session"], sess_meta["Section"],
                              sess_meta["EDF_path"], a, b, self.session_cache_dir)
            if x.shape[1] != b - a:
                raise RuntimeError(f"chunk {i} {sess_meta['Patient']}_{sess_meta['Session']}: "
                                   f"señal {x.shape[1]} != {b - a}")

            xs = torch.from_numpy(np.array(x, dtype=np.float32))
            ys = torch.from_numpy(self.wlabels[si][w0:w0 + self.cw].astype(np.float32))
            return xs, ys
        except ValueError as e:
            if "Missing channels" not in str(e):
                raise
            return self.__getitem__(random.randint(0, len(self) - 1))

    def make_sampler(self, num_samples, pos_frac=0.5):
        n_pos = int(self.chunk_pos.sum())
        n_neg = len(self.chunk_pos) - n_pos
        if n_pos == 0 or n_neg == 0:
            raise ValueError(f"Se necesitan tanto bloques positivos como negativos (pos={n_pos}, neg={n_neg}).")
        w = np.where(self.chunk_pos, pos_frac / n_pos, (1 - pos_frac) / n_neg)
        return WeightedRandomSampler(torch.as_tensor(w, dtype=torch.double), num_samples, replacement=True)