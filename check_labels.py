import pandas as pd
from glob import glob

artifact = "eye"
window_tag = "w2_s1"  # Cambiado a w2_s1 según tus archivos disponibles

# Ruta del Random Forest para w2_s1 y uao.15
rf_path = f"/workspace/ml-outputs/artifact/dataset/_comparison/rf_dataset_{artifact}_{window_tag}_ua0.15_p15_v6_pt0.5_it0.2_norm0.parquet"

# Búsqueda automática del archivo de la CNN para w2_s1
cnn_matches = glob(f"/workspace/ml-outputs/artifact/models_v2/cnn_cnn_{artifact}*_{window_tag}*/preds_test.parquet")
if not cnn_matches:
    # Búsqueda genérica por si acaso
    cnn_matches = glob(f"/workspace/ml-outputs/artifact/models_v2/cnn_cnn_{artifact}*/preds_test.parquet")

if not cnn_matches:
    raise FileNotFoundError(f"No se encontró preds_test.parquet para {artifact}")

cnn_path = cnn_matches[0]

print(f"[INFO] Usando RF: {rf_path}")
print(f"[INFO] Usando CNN: {cnn_path}")

KEY = ["Patient", "Session", "Section", "Start"]

rf = pd.read_parquet(rf_path).drop_duplicates(KEY)
cnn = pd.read_parquet(cnn_path).drop_duplicates(KEY)

m = rf[KEY + [f"tuar_{artifact}"]].merge(cnn, on=KEY)

print("\n" + "=" * 50)
print(f"MATRIZ DE EQUIVALENCIA DE ETIQUETAS ({artifact.upper()})")
print("=" * 50)
print(pd.crosstab(m[f"tuar_{artifact}"] > 0, m["y"], margins=True))
print("=" * 50)
