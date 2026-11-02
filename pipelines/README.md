# Pipelines experimentales (`pipelines/`)

Esta carpeta contiene los flujos experimentales de extremo a extremo utilizados en **Hybrid AI for Epilepsy Diagnosis**.

Mientras [`src/`](../src/) contiene componentes reutilizables, `pipelines/` combina esos componentes para ejecutar experimentos completos de entrenamiento, validación y evaluación.

## Estructura

```text
pipelines/
├── artifacts/
└── seizures/
```

---

## `artifacts/`

Contiene los experimentos relacionados con la **detección de artefactos en EEG** utilizando TUAR.

Los pipelines combinan etapas como:

```text
carga de datos
    ↓
segmentación en ventanas
    ↓
partición de pacientes
    ↓
preprocesamiento
    ↓
extracción de características
    ↓
entrenamiento del modelo
    ↓
evaluación
    ↓
resultados
```

Entre los enfoques implementados se encuentran:

- ICA e ICLabel;
- Random Forest;
- XGBoost;
- SVM en experimentos exploratorios;
- CNN 1D para detección de artefactos;
- combinaciones de características derivadas de ICA con modelos de aprendizaje automático.

Archivos representativos:

| Archivo              | Propósito                                                          |
| -------------------- | ------------------------------------------------------------------ |
| `cnn_detectors.py`   | Entrenamiento de CNN para las categorías de artefactos             |
| `ica_rf.py`          | Pipeline basado en características de ICA/ICLabel + Random Forest  |
| `ica_cnn_rf.py`      | Pipeline experimental que combina representaciones y Random Forest |
| `ica_cnn_xgboost.py` | Pipeline experimental con XGBoost                                  |
| `ica_cnn_svm.py`     | Variante experimental con SVM                                      |

Algunos archivos corresponden a comparaciones o experimentos intermedios y no necesariamente representan el modelo final seleccionado.

Los detalles específicos de ejecución están documentados en [`artifacts/README.md`](artifacts/).

---

## `seizures/`

Contiene los experimentos relacionados con la **detección de crisis epilépticas**.

El conjunto principal utilizado es TUSZ, con Siena Scalp EEG como conjunto adicional de evaluación cuando la comparación es metodológicamente válida.

Los experimentos del proyecto se organizan conceptualmente en los siguientes brazos:

| Brazo   | Enfoque                                                              |
| ------- | -------------------------------------------------------------------- |
| **S1**  | Large EEG-U-Transformer / SeizureTransformer con pesos oficiales     |
| **S2**  | CNN2D + LSTM basada en Lee et al. (CHIL 2022)                        |
| **S3**  | Características diseñadas manualmente + XGBoost                      |
| **S4a** | Características de S3 combinadas con representación aprendida por S2 |
| **S4b** | Características de S3 combinadas con salida o representación de S1   |

Entre los pipelines presentes se encuentran:

| Archivo                      | Propósito                                                          |
| ---------------------------- | ------------------------------------------------------------------ |
| `aitrics_cnn_lstm.py`        | Entrenamiento y evaluación de la adaptación CNN2D + LSTM           |
| `aitrics_cnn_lstm_optuna.py` | Variante para búsqueda y ajuste de hiperparámetros mediante Optuna |

Ejemplo de prueba rápida:

```bash
uv run python -m pipelines.seizures.aitrics_cnn_lstm --smoke
```

También se utilizan configuraciones específicas de representación, por ejemplo:

```bash
uv run python -m pipelines.seizures.aitrics_cnn_lstm --enc psd
```

Los detalles de cada experimento están documentados en [`seizures/README.md`](seizures/).

---

## Relación con `src/`

Los pipelines reutilizan principalmente:

```text
src/core/     → carga, preprocessing, ventanas y features
src/models/   → arquitecturas y modelos
src/utils/    → datasets, caché y evaluación
src/xai/      → explicabilidad
```

De forma general:

```text
datasets
   ↓
src/core/
   ↓
pipelines/
   ↓
src/models/
   ↓
src/utils/
   ↓
results/
```

---

## Entradas

Dependiendo del pipeline, las entradas incluyen:

- archivos EEG en formato EDF;
- anotaciones asociadas;
- datasets preprocesados;
- cachés de sesiones;
- configuraciones de modelos;
- checkpoints preentrenados.

Las rutas de datasets y outputs se configuran principalmente mediante:

```text
src/core/data_config.py
```

Consulta [`SETUP.md`](../SETUP.md) para información sobre rutas y configuración del entorno.

---

## Salidas

Los pipelines generan, según el experimento:

- datasets intermedios;
- métricas;
- predicciones;
- checkpoints;
- logs de entrenamiento;
- figuras;
- archivos de evaluación.

Los resultados finales preservados se organizan bajo:

[`results/`](../results/)

Los checkpoints pesados no se almacenan directamente en GitHub.

---

## Ejecución

Los pipelines se ejecutan desde la raíz del repositorio.

Se utiliza la forma:

```bash
uv run python -m pipelines.<subcarpeta>.<script>
```

Ejemplo:

```bash
uv run python -m pipelines.seizures.aitrics_cnn_lstm --smoke
```

Esto mantiene correctamente las importaciones desde `src/`.

---

## Convenciones

- `pipelines/` contiene lógica experimental completa.
- El código reutilizable se mantiene en [`src/`](../src/).
- Los datos originales no se almacenan en esta carpeta.
- Los resultados finales se dirigen a [`results/`](../results/).
- Los checkpoints grandes se almacenan o distribuyen por el medio definido para modelos.
- Los experimentos antiguos o duplicados se identifican claramente para evitar confundirlos con pipelines activos.