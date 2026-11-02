# Código fuente (`src/`)

Esta carpeta contiene los componentes reutilizables del proyecto **Hybrid AI for Epilepsy Diagnosis**.

A diferencia de [`pipelines/`](../pipelines/), que contiene flujos experimentales completos, `src/` agrupa las funciones, configuraciones, modelos y utilidades que pueden reutilizarse entre diferentes experimentos.

## Estructura

```text
src/
├── core/
├── models/
├── utils/
├── xai/
├── all.py
└── main.py
```

## `core/`

Contiene la lógica principal para carga, preparación y transformación de los datos EEG.

Entre sus responsabilidades se encuentran:

- configuración de corpus y rutas de datos;
- carga de archivos EDF y anotaciones;
- preprocesamiento de señales;
- creación de montajes;
- segmentación en ventanas;
- extracción de características;
- partición de pacientes y datos.

Archivos principales:

| Archivo | Propósito |
|---|---|
| `data_config.py` | Configuración compartida de datasets, rutas, canales, etiquetas y parámetros de procesamiento |
| `data_loader.py` | Carga de señales EEG y anotaciones |
| `preprocessing.py` | Preprocesamiento y transformación de señales |
| `windowing.py` | Segmentación de registros y anotaciones en ventanas |
| `feature_extractor.py` | Extracción de características temporales, espectrales y otras representaciones |
| `data_splitter.py` | Creación y manejo de particiones de datos |

> **Nota sobre rutas:** `data_config.py` contiene varias ubicaciones conocidas para datasets y outputs, incluyendo RunPod, almacenamiento externo y equipos del laboratorio. En una computadora nueva puede ser necesario adaptar `ALL_DATA_POSSIBLE_PATHS` y `ALL_OUTPUTS_POSSIBLE_PATHS`. Consulta [`SETUP.md`](../SETUP.md).

---

## `models/`

Contiene implementaciones reutilizables de los modelos utilizados en los experimentos.

Actualmente incluye, entre otros:

- Random Forest;
- XGBoost;
- SVM;
- CNN para detección de artefactos;
- CNN2D + LSTM para detección de crisis;
- Large EEG-U-Transformer / SeizureTransformer;
- componentes compartidos para entrenamiento, validación y selección de umbrales.

Archivos relevantes:

| Archivo | Propósito |
|---|---|
| `rf_model.py` | Implementación y utilidades para Random Forest |
| `xgboost_model.py` | Implementación y utilidades para XGBoost |
| `svm_model.py` | Implementación y utilidades para SVM |
| `cnn_artifact_detector.py` | CNN utilizada en detección de artefactos |
| `aitrics_cnn_lstm.py` | Adaptación de CNN2D + LSTM para detección de crisis |
| `large_eeg_u_transformer.py` | Adaptación/integración del modelo SeizureTransformer |
| `ica_model.py` | Componentes asociados con ICA e ICLabel |
| `ml_models.py` | Funciones compartidas para entrenamiento, evaluación y selección de modelos |

La carpeta `__old__/`, cuando esté presente, contiene implementaciones anteriores conservadas únicamente como referencia y no debe asumirse como la versión activa de los modelos.

---

## `utils/`

Contiene funciones auxiliares compartidas por los pipelines y módulos principales.

Incluye utilidades relacionadas con:

- caché de sesiones y particiones;
- evaluación de artefactos;
- evaluación de crisis epilépticas;
- construcción de datasets para modelos de crisis;
- inventario de corpus;
- registro y control de pacientes;
- análisis de resultados de corridas;
- optimización de parámetros de ventanas.

Algunos archivos relevantes son:

| Archivo | Propósito |
|---|---|
| `session_cache.py` | Almacenamiento y recuperación de sesiones preprocesadas |
| `split_cache.py` | Persistencia de particiones o datos procesados |
| `artifacts_eval.py` | Funciones de evaluación para detección de artefactos |
| `seizure_eval.py` | Métricas y evaluación para detección de crisis |
| `seizure_dataset.py` | Dataset y muestreo utilizados en modelos de crisis |
| `corpus_inventory.py` | Inspección y distribución de corpus |
| `patient_registry.py` | Manejo de pacientes y particiones |
| `window_parameters_optimization.py` | Análisis y optimización de parámetros de segmentación |

---

## `xai/`

Contiene la implementación de técnicas de **Explainable Artificial Intelligence (XAI)** utilizadas para analizar el comportamiento de los modelos.

Incluye componentes para:

- análisis de atribuciones;
- selección y comparación de variables relevantes;
- análisis por tipo de predicción;
- interpretación de señales y características;
- análisis de modelos profundos;
- integración con modelos de crisis utilizados en fases actuales y anteriores.

Entre los archivos compartidos se encuentran:

| Archivo | Propósito |
|---|---|
| `xai_common.py` | Funciones comunes para análisis XAI y agrupación de resultados |
| `xai_deep_core.py` | Funciones compartidas para explicabilidad de modelos profundos |

Las implementaciones y recursos específicos de cada arquitectura pueden encontrarse bajo:

```text
src/xai/models/
```

Los resultados finales de explicabilidad que deban conservarse como resultados del proyecto se organizan bajo:

```text
results/xai/
```

---

## Relación con `pipelines/`

`src/` contiene componentes reutilizables.

`pipelines/` utiliza esos componentes para construir experimentos completos.

De forma simplificada:

```text
datasets
   ↓
src/core/
   ↓
src/models/
   ↓
pipelines/
   ↓
src/utils/
   ↓
results/
   ↓
src/xai/
```

Por ejemplo, un pipeline puede:

1. cargar y preprocesar EEG mediante `src/core/`;
2. utilizar un modelo definido en `src/models/`;
3. evaluar las predicciones mediante `src/utils/`;
4. guardar resultados en `results/`;
5. aplicar técnicas de explicabilidad desde `src/xai/`.

---

## Ejecución

Los módulos de `src/` están diseñados principalmente para ser utilizados desde los pipelines y no necesariamente como scripts independientes.

Para ejecutar experimentos completos, consulta:

- [`pipelines/artifacts/`](../pipelines/artifacts/)
- [`pipelines/seizures/`](../pipelines/seizures/)

La instalación y configuración del entorno se documentan en:

[`SETUP.md`](../SETUP.md)

---

## Convenciones

- Los datasets originales no deben almacenarse dentro de `src/`.
- Los pesos grandes de modelos no deben versionarse directamente en GitHub.
- Los resultados finales deben dirigirse a `results/`.
- El código reutilizable debe permanecer en `src/`; la lógica específica de una corrida o experimento debe mantenerse en `pipelines/`.
- Las implementaciones antiguas conservadas por trazabilidad deben identificarse claramente y no confundirse con las versiones activas.