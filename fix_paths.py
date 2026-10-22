import pandas as pd
from pathlib import Path

# Buscamos en toda la carpeta de outputs
base_dir = Path("/workspace/ml-outputs/artifact")
parquet_files = list(base_dir.rglob("*.parquet"))

print(f"Encontrados {len(parquet_files)} archivos Parquet para revisar...")

for file_path in parquet_files:
    try:
        df = pd.read_parquet(file_path)
        changed = False
        
        # Buscamos en todas las columnas de texto (donde viven EDF_path y CSV)
        for col in df.select_dtypes(include=['object', 'string']).columns:
            # Si detectamos diagonales invertidas de Windows
            if df[col].astype(str).str.contains(r"\\").any():
                # 1. Volteamos las diagonales a formato Linux
                df[col] = df[col].astype(str).str.replace(r"\\", "/", regex=True)
                
                # 2. Cortamos la ruta de tu PC (D:/Users/.../) y ponemos la de Runpod
                # Buscamos cualquier cosa que termine en /edf/ y lo reemplazamos por el root de Linux
                df[col] = df[col].str.replace(
                    r"^.*/edf/", 
                    "/workspace/data/tuh_eeg_artifact/v3.0.1/edf/", 
                    regex=True
                )
                changed = True
                
        if changed:
            df.to_parquet(file_path)
            print(f"[CORREGIDO] {file_path.name}")
        else:
            print(f"[OK] {file_path.name} (Sin rutas de Windows)")
            
    except Exception as e:
        print(f"[ERROR] No se pudo procesar {file_path.name}: {e}")

print("\n¡Listo! Todas las rutas en los Parquets ahora apuntan a Linux.")
