"""Puente al repositorio de Sánchez; basado en las firmas del XAI.ipynb recibido."""
from pathlib import Path
import importlib
import sys
import json
import csv
import numpy as np
from xai_core import TorchAdapter


def import_repo(repo_root):
    root = Path(repo_root).expanduser().resolve()
    if not root.is_dir():
        raise FileNotFoundError(root)
    # La disposición esperada es la del notebook original: pt/pipeline.py.
    if not (root / 'pt' / 'pipeline.py').is_file():
        raise FileNotFoundError(f'Se esperaba {root}/pt/pipeline.py; ajuste el adaptador a su copia.')
    # Evitar reutilizar accidentalmente otro módulo utils ya importado.
    for name in ('utils', 'pt', 'api'):
        old = sys.modules.get(name)
        file = getattr(old, '__file__', None)
        if file and not Path(file).resolve().is_relative_to(root):
            raise RuntimeError(f'{name} ya proviene de {file}. Reinicie el kernel.')
    sys.path.insert(0, str(root))
    sys.path.insert(0, str(root / 'pt'))
    return (importlib.import_module('utils'),
            importlib.import_module('pt.pipeline'))


def binary_probability(output):
    """Solo salidas binarias (B,), (B,1), (B,1,1); no logits ni multiclase."""
    import torch
    if hasattr(output, 'probabilities'):
        y = output.probabilities
    elif isinstance(output, dict):
        y = output['probabilities']
    elif isinstance(output, tuple):
        y = output[0]
    else:
        y = output
    if not torch.is_tensor(y) or y.ndim < 1:
        raise ValueError('La salida no contiene un tensor de probabilidades.')
    if any(dim != 1 for dim in y.shape[1:]):
        raise ValueError('Salida temporal/multiclase: defina un selector explícito.')
    return y.reshape(y.shape[0])


def load_sanchez(repo_root, config_path, model_path, signal_shape, feature_count,
                 device='cpu', state_key=None):
    import torch
    utils, pipeline = import_repo(repo_root)
    cfg = utils.load_config(str(config_path))
    validated = utils.validate_config(cfg)
    if validated is not None:
        cfg = validated
    raw = json.loads(Path(config_path).read_text(encoding='utf-8'))
    if cfg.time_step_labels:
        raise ValueError('Este adaptador requiere clasificación binaria por ventana.')
    expected_t = int(float(raw['target_fs']) * float(raw['window_sec']))
    if signal_shape[0] != expected_t or feature_count != len(raw['selected_features']):
        raise ValueError('Las dimensiones de los arrays no coinciden con config_used.json.')
    model = pipeline.make_model(
        model_type=cfg.model, input_shape=tuple(signal_shape), feat_dim=feature_count,
        num_filters=cfg.num_filters, kernel_size=cfg.kernel_size,
        dropout_rate=cfg.dropout, rnn_units=cfg.rnn_units,
        time_step=cfg.time_step_labels,
        transformer_params=pipeline._transformer_params_from_config(cfg))
    checkpoint = torch.load(model_path, map_location='cpu', weights_only=True)
    if state_key is not None:
        state = checkpoint[state_key]
    elif isinstance(checkpoint, dict) and 'state_dict' in checkpoint:
        state = checkpoint['state_dict']
    elif isinstance(checkpoint, dict) and 'model_state_dict' in checkpoint:
        state = checkpoint['model_state_dict']
    else:
        state = checkpoint
    model.load_state_dict(state, strict=True)
    return TorchAdapter(model, binary_probability, device), raw


def load_cached(directory):
    """Carga entradas ya preparadas por el notebook original. No reescala."""
    d = Path(directory)
    x = np.load(d / 'windows_np.npy', mmap_mode='r', allow_pickle=False)
    f = np.load(d / 'features_scaled.npy', mmap_mode='r', allow_pickle=False)
    y = np.load(d / 'labels_np.npy', allow_pickle=False)
    if x.ndim != 3 or f.ndim != 2 or y.shape != (len(x),) or len(f) != len(x):
        raise ValueError('Cache incompatible: esperado (N,T,C), (N,F), (N,).')
    if not np.isin(y, [0, 1]).all():
        raise ValueError('Etiquetas no binarias.')
    state_path = d / 'xai_state.json'
    metadata = json.loads(state_path.read_text()) if state_path.exists() else {}
    return x, f, y, metadata


def parse_intervals(path):
    with Path(path).open(encoding='utf-8-sig') as handle:
        lines = [line for line in handle if line.strip() and not line.lstrip().startswith('#')]
    for i, line in enumerate(lines):
        if line.strip().startswith('channel,'):
            return [(float(r['start_time']), float(r['stop_time']))
                    for r in csv.DictReader(lines[i:]) if r['label'].strip().lower() == 'seiz']
    raise ValueError(f'No se encontró encabezado csv_bi en {path}')


def prepare_edf(repo_root, edf_paths, config, scaler, preprocess,
                min_overlap_sec=1.0):
    """Opcional: reutiliza lectura/extracción del repositorio.

    preprocess(signals, fs, config) debe reproducir EXACTAMENTE entrenamiento.
    No se inventan filtros ni normalización. Verifique también la etapa de
    extracción de features; si difiere de este flujo, adapte esta función.
    """
    import_repo(repo_root)
    mod = importlib.import_module('api.processing.network_eval')
    windows, features, labels, records = [], [], [], []
    for path in map(Path, edf_paths):
        intervals = parse_intervals(path.with_suffix('.csv_bi'))
        signal, fs = mod._load_bipolar_signals(
            path, montage=config['montage'], target_fs=float(config['target_fs']))
        signal = preprocess(signal, fs, config)
        for window, start, end in mod._iter_windows(
            signal, fs=fs, window_sec=float(config['window_sec']),
            hop_sec=float(config['hop_sec']),
            window_samples=int(fs * float(config['window_sec'])),
            hop_samples=int(fs * float(config['hop_sec']))):
            feature_dict = mod._compute_feature_vector(window, fs=fs)
            # Un nombre ausente falla explícitamente; nunca se sustituye por cero.
            features.append([float(feature_dict[name]) for name in config['selected_features']])
            windows.append(window)
            labels.append(int(any(min(end, b) - max(start, a) >= min_overlap_sec
                                  for a, b in intervals)))
            records.append({'path': str(path), 'start': start, 'end': end})
    if not windows:
        raise ValueError('No se generaron ventanas.')
    return (np.asarray(windows, dtype=np.float32),
            np.asarray(scaler.transform(features), dtype=np.float32),
            np.asarray(labels, dtype=np.int8), records)
