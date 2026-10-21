# XAI reutilizable con adaptador para Sánchez

Extraído y reorganizado a partir del XAI.ipynb adjunto. No incluye datos, pesos,
scaler ni código del repositorio de Sánchez. No modifica el notebook original.

## Uso en WSL / VS Code

1. Descomprima esta carpeta en su proyecto. Mantenga los .py junto al notebook.
2. Seleccione el kernel de su entorno WSL. Integre requirements.in en sus
   dependencias existentes; no reemplace las del proyecto ni sincronice un
   entorno de entrenamiento solo con esta lista. Captum requiere PyTorch.
3. Abra XAI_general_sanchez.ipynb. Edite REPO_ROOT, CONFIG_PATH, MODEL_PATH,
   CACHE_DIR y OUTPUT_DIR. El adaptador espera pt/pipeline.py dentro de REPO_ROOT,
   como en el notebook recibido. Si su copia usa network/pt, ajuste los imports
   en sanchez_adapter.py; no es posible comprobar esa estructura sin el repo.
4. Reutilice windows_np.npy, features_scaled.npy y labels_np.npy del notebook
   original. No vuelva a aplicar el scaler a features_scaled.npy.
5. Confirme que cache, checkpoint, configuración, scaler y orden de canales
   corresponden a la misma ejecución. Establezca CACHE_PREPROCESS_CONFIRMED=True
   solo tras verificarlo. La bandera documenta una comprobación del usuario;
   no demuestra automáticamente la equivalencia con entrenamiento.
6. Ejecute en orden. Los arrays se guardan al terminar cada grupo. Las atribuciones
   del grupo interrumpido deberán recalcularse. La última celda regenera PDF
   desde disco sin modelo, EDF ni recálculo de XAI.
7. Sustituya Canal 1, Canal 2... por nombres verificados en el orden del loader.

## Si no existen los arrays

Use prepare_edf en sanchez_adapter.py. Recibe una lista explícita de EDF,
configuración, scaler original y una función preprocess(signals, fs, config).
Esta función debe reproducir el pipeline de entrenamiento. No se copió como
verdad el filtro fijo del notebook original ni se inventó normalización.

Ejemplo dentro de su entorno (cargue pickle solo de sus archivos de confianza):

```python
import json, pickle
from pathlib import Path
import numpy as np
from sanchez_adapter import prepare_edf

config = json.loads(CONFIG_PATH.read_text())
with (REPO_ROOT / 'api/networks/pt/feature_scaler.pkl').open('rb') as f:
    scaler = pickle.load(f)
# Defina/importе preprocess_exact como la preparación usada al entrenar.
# Debe aceptar (signals, fs, config) y devolver la señal preparada.
x, features, labels, records = prepare_edf(
    REPO_ROOT, sorted(Path('/ruta/eval').rglob('*.edf')),
    config, scaler, preprocess=preprocess_exact)
CACHE_DIR.mkdir(parents=True, exist_ok=True)
np.save(CACHE_DIR / 'windows_np.npy', x)
np.save(CACHE_DIR / 'features_scaled.npy', features)
np.save(CACHE_DIR / 'labels_np.npy', labels)
(CACHE_DIR / 'records.json').write_text(json.dumps(records, indent=2))
```

Este lector asume anotaciones csv_bi con etiqueta exacta seiz y solapamiento
mínimo de un segundo, siguiendo el criterio del notebook. Confirme este criterio
y la etapa de cálculo de características contra el entrenamiento. Si los datos
requieren normalización por ventana, adapte prepare_edf en esa etapa.

## Qué significa agnóstico aquí

| Función | Contrato |
|---|---|
| predict / occlusion / kernel_shap | score(*arrays NumPy) devuelve (B,), un escalar por muestra; cualquier framework mediante wrapper |
| saliency / integrated_gradients | TorchAdapter diferenciable; no limitado a Transformer ni Sánchez |
| load_sanchez / prepare_edf | Únicos componentes ligados al repositorio y formato EDF |
| plot_importance / plot_signal_map | Arrays NumPy, nombres y frecuencia explícitos; exportan PDF |

Para sklearn: score = lambda x: classifier.predict_proba(x)[:, 1].
Para TensorFlow: score = lambda x: model(x, training=False).numpy()[:, 0].
La tupla (X,) es una entrada; (signal, features) son dos. Los modelos con
diccionarios, otras formas de llamada o salidas temporales requieren wrapper.
Para multiclase elija un índice de clase explícito en score/selector. La selección
TP/FP/TN/FN del ejemplo es exclusivamente binaria; no pertenece al núcleo XAI.

## Correcciones y límites de interpretación

- Definiciones antes de llamadas; sin dependencias de variables del kernel antiguo.
- IG usa additional_forward_args para expandir correctamente las otras entradas.
  Conserva delta por muestra; revise su magnitud y convergencia aumentando pasos.
- SHAP explica cada ventana fijando SU señal, con background explícito. Se guarda
  valor esperado y residual de aditividad. Puede ser lento; inicia desactivado.
- Oclusión retorna diferencias firmadas. Saliency usa magnitud por defecto.
- Las atribuciones de señal y features son PARCIALES: se mantiene fija la otra
  rama. Si las features derivan de la señal, no se recalculan tras perturbarla.
  Esto no representa una intervención fisiológica ni efectos causales.
- Cero es una referencia configurable, no necesariamente ausencia de EEG. Para
  features estandarizadas puede representar la media; verifique su scaler.
- No se extrae atención automáticamente: capturar activaciones por nombre no
  garantiza pesos. Añada un extractor específico solo conociendo la arquitectura.
- No se entrenan modelos ni se infiere que el checkpoint esté bien entrenado.
- Ventanas extremas por grupo sirven para casos ilustrativos, no para estimar
  rendimiento ni generalización. La selección de pacientes y particiones va fuera.
- La carga de pesos usa weights_only=True y strict=True; no fuerza compatibilidad
  ni desactiva restricciones si encuentra un checkpoint distinto.
- Los PDF mantienen líneas/texto vectoriales; mapas imshow contienen un raster.

## Verificación

Ejecute en su entorno:

```bash
python -m unittest -v test_xai.py
```

La entrega fue comprobada con cuatro pruebas NumPy y compilación de módulos y
celdas. Dos pruebas analíticas adicionales de SHAP y PyTorch/Captum se incluyen,
pero se omitieron aquí porque esas bibliotecas no están instaladas. No se ejecutó
Sánchez: faltan repositorio, checkpoint y datos. Al instalar dependencias, dichas
pruebas dejan de omitirse. No equivale a validar resultados científicos reales.

Documentación consultada:
- https://captum.ai/api/integrated_gradients.html
- https://shap.readthedocs.io/en/latest/generated/shap.KernelExplainer.html
