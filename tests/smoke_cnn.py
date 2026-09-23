# smoke_test_cnn.py
import pandas as pd
from pathlib import Path
from src.models.cnn_artifact_detector import binary_cnn  

split_dir = Path(r"D:\Users\disenoeinnovacion\ml-outputs\artifact\splits")
base_name = "split_train70.0_val15.0_test15.0_p10_v1_eye_w5_s2_sw0.7_ua0.1"

df_full = pd.read_parquet(split_dir / f"{base_name}.parquet")

# Recorta a 1 paciente por split para que corra rápido en CPU
sample_patients = {
    split: df_full[df_full["split"] == split]["Patient"].unique()[:1]
    for split in ["train", "val", "test"]
}
df_small = pd.concat([
    df_full[(df_full["split"] == split) & (df_full["Patient"].isin(pats))].head(200)
    for split, pats in sample_patients.items()
])
print(df_small["split"].value_counts())

results = binary_cnn(
    windowed_df=df_small,
    target_col="eye",
    model_name="smoke_test_eye",
    window_size_sec=5.0,
    sfreq=256,
    n_channels=18,
    session_cache_dir="cache/sessions",
    ica_cache_dir="cache/ica",
    models_dir="models_cnn_smoke_test",
    model_type="lightweight",
    epochs=1,
    batch_size=8,
    checkpoints_dir="./checkpoints_smoke_test",
    force_retrain=True,
)

print("\n[SMOKE TEST OK]")
print(results["metrics_results"])