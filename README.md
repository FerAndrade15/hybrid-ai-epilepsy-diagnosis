<p align="center">
  <img src="docs/img/logo-uvg.png"
       alt="Logo Universidad del Valle de Guatemala"
       height="58"/>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
  <img src="docs/img/logo-ingenieria.png"
       alt="Logo Facultad de Ingeniería"
       height="58"/>
</p>

<h1 align="center">Hybrid AI for Epilepsy Diagnosis</h1>

<h3 align="center">Detección de artefactos y crisis epilépticas en EEG mediante técnicas de inteligencia artificial con un enfoque híbrido</h3>

<p align="center"><strong>Fase VII · Trabajo de graduación · 2026</strong></p>

<p align="center">
  <strong>Autora:</strong> <a href="https://github.com/FerAndrade15">Fernanda Andrade</a><br/>
  <strong>Asesor:</strong> Dr. Luis Alberto Rivera<br/>
  <strong>Departamento de Ingeniería Electrónica, Mecatrónica y Biomédica · Universidad del Valle de Guatemala</strong>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/status-en%20desarrollo-yellow" alt="Estado: En desarrollo"/>
  <img src="https://img.shields.io/github/languages/top/FerAndrade15/hybrid-ai-epilepsy-diagnosis" alt="Lenguaje principal"/>
  <img src="https://img.shields.io/github/last-commit/FerAndrade15/hybrid-ai-epilepsy-diagnosis" alt="Último commit"/>
</p>

> [!WARNING]
> **Proyecto de investigación.** Los modelos y herramientas incluidos en este repositorio no constituyen un dispositivo médico, no han sido validados para uso clínico y no deben utilizarse para diagnosticar pacientes ni para tomar decisiones médicas.

---

## Descripción

Este repositorio contiene el desarrollo correspondiente a la **Fase VII** de una línea de investigación de la Universidad del Valle de Guatemala enfocada en el análisis computacional de señales electroencefalográficas (EEG) y epilepsia.

El trabajo estudia dos problemas relacionados:

1. **Detección de artefactos en EEG**, utilizando el TUH EEG Artifact Corpus (TUAR).
2. **Detección de crisis epilépticas**, utilizando el TUH EEG Seizure Corpus (TUSZ) y Siena Scalp EEG como conjunto de evaluación externa cuando la comparación es metodológicamente válida.

El enfoque experimental compara métodos clásicos, aprendizaje automático, redes neuronales, modelos preentrenados y combinaciones híbridas. Además, el repositorio incorpora **inteligencia artificial explicable (XAI)** para estudiar e interpretar las decisiones de los modelos.

---

## Objetivos del repositorio

El repositorio busca conservar de forma reproducible:

- pipelines de preprocesamiento y preparación de EEG;
- generación de ventanas y características;
- implementaciones de modelos;
- configuraciones de entrenamiento y evaluación;
- resultados, métricas y figuras;
- métodos de explicabilidad;
- checkpoints y artefactos relevantes para futuras fases, cuando su distribución sea posible;
- antecedentes técnicos de la línea de investigación.

---

## Líneas de trabajo

### 1. Detección de artefactos

La detección de artefactos se desarrolla sobre **TUAR** y considera tres categorías principales:

| Artefacto | Ventana | Paso |
|---|---:|---:|
| Ocular | 5 s | 2 s |
| Muscular | 5 s | 2 s |
| No fisiológico | 2 s | 1 s |

Los enfoques comparados incluyen:

- reglas y umbrales como línea base;
- Random Forest;
- XGBoost;
- redes neuronales convolucionales (CNN).

Los pipelines correspondientes se encuentran en [`pipelines/artifacts/`](pipelines/artifacts/).

### 2. Detección de crisis epilépticas

La detección de crisis utiliza **TUSZ** como corpus principal y **Siena Scalp EEG** como conjunto de evaluación externa cuando la comparación es metodológicamente válida.

| Brazo | Descripción |
|---|---|
| **S1** | [SeizureTransformer](https://github.com/keruiwu/SeizureTransformer) con pesos oficiales, sin reentrenamiento dentro de este proyecto |
| **S2** | Replicación/adaptación de la arquitectura **CNN2D + LSTM** descrita por Lee et al. (CHIL 2022), implementada en `src/models/aitrics_cnn_lstm.py` |
| **S3** | Características diseñadas manualmente + XGBoost |
| **S4a** | S3 combinado con una representación aprendida por S2 |
| **S4b** | S3 combinado con salida o representación de S1, según la configuración experimental |

**Referencias de los modelos externos:**
- **S1 — SeizureTransformer:** K. Wu, Z. Zhao y B. Yener, *Large EEG-U-Transformer for Time-Step Level Detection Without Pre-Training*, arXiv:2504.00336, 2025.
- **S2 — CNN2D + LSTM:** K. Lee et al., *Real-Time Seizure Detection using EEG: A Comprehensive Comparison of Recent Approaches under a Realistic Setting*, CHIL 2022.

Los pipelines correspondientes se encuentran en [`pipelines/seizures/`](pipelines/seizures/).

---

## Inteligencia artificial explicable

El repositorio incluye una línea de **Explainable Artificial Intelligence (XAI)** orientada a estudiar las decisiones de los modelos y la relevancia de señales, características o representaciones durante la clasificación.

El código asociado se encuentra en [`src/xai/`](src/xai/) y los resultados generados se organizan en [`results/xai/`](results/xai/).

---

## Datos

Los datasets **no se distribuyen en este repositorio**. Deben obtenerse directamente de sus proveedores y utilizarse de acuerdo con sus respectivos términos de acceso.

| Dataset | Uso en el proyecto | Acceso |
|---|---|---|
| TUH EEG Artifact Corpus (TUAR) | Detección de artefactos | [Temple University / NEDC](https://isip.piconepress.com/projects/nedc/html/tuh_eeg/) |
| TUH EEG Seizure Corpus (TUSZ) | Detección de crisis | [Temple University / NEDC](https://isip.piconepress.com/projects/nedc/html/tuh_eeg/) |
| Siena Scalp EEG Database | Evaluación externa de crisis | [PhysioNet](https://physionet.org/content/siena-scalp-eeg/) |

La configuración local se describe en [`SETUP.md`](SETUP.md).

---

## Evaluación

### Artefactos

Se consideran métricas de clasificación por ventana:

- sensibilidad;
- especificidad;
- F1-score;
- PR-AUC;
- ROC-AUC;
- intervalos de confianza al 95 % mediante bootstrap por paciente.

### Crisis epilépticas

La evaluación prioriza métricas por evento:

- sensibilidad;
- precisión;
- F1;
- falsas alarmas por 24 horas;
- coincidencia temporal de eventos.

Los umbrales y parámetros de posprocesamiento deben seleccionarse utilizando datos de validación y no el conjunto de evaluación final.

---

## Trabajo previo

Este trabajo forma parte de una línea de investigación desarrollada durante varios años en la Universidad del Valle de Guatemala.

| Año | Autor(es) | Contribución principal | Repositorio |
|---|---|---|---|
| 2023 | Katherine Caceros | Organización de datos y recursos biomédicos relacionados con epilepsia, sueño y actividad muscular. | [Repositorio-Biomedico-2023](https://github.com/cac1837/Repositorio-Biomedico-2023) |
| 2023 | Cristhofer Isaac Patzán | Aplicación de aprendizaje automático a señales bioeléctricas y extracción de características temporales, frecuenciales y basadas en wavelets. | [Tesis_2023](https://github.com/pat19218/Tesis_2023) |
| 2023 | Diego Méndez | Desarrollo y continuidad de la herramienta de análisis EEG en MATLAB App Designer, con integración de MySQL mediante ODBC. | [Herramienta](https://github.com/Men19673/Herramienta) |
| 2024 | Javier Alejandro Pérez Marín y Dylan Antonio Ixcayau Morán | Extensión mediante aprendizaje supervisado y no supervisado, incluyendo LSTM, TCN y técnicas de clustering sobre datos de TUH. | [Herramienta](https://github.com/JAPM8/Herramienta) |
| 2025 | Santiago Sánchez | Modelos TCN, Transformer e híbridos sobre TUSZ, con implementaciones en TensorFlow y PyTorch, API de inferencia e interfaz para EDF. | [TesisFinal](https://github.com/sansancas/TesisFinal) |
| 2026 | Fernanda Andrade | Comparación de métodos para artefactos y crisis, combinaciones híbridas, evaluación externa y XAI. | [Este repositorio](https://github.com/FerAndrade15/hybrid-ai-epilepsy-diagnosis) |

El código y material técnico preservado de fases anteriores se encuentra en [`prior_work/`](prior_work/). La documentación histórica más detallada se consolida dentro de `docs/`.

---

## Estructura principal del repositorio

```text
.
├── __docker__/                       # Configuración y artefactos Docker
├── __runpod__/                       # Scripts/configuración para RunPod
├── docs/                             # Notas, referencias y documentación técnica (incluyendo documentación de los modelos entrenados)
├── epileptic_eeg_analysis_toolbox/   # Herramienta EEG heredada/integrada
├── notebooks/                        # Exploración y análisis experimental
├── pipelines/
│   ├── artifacts/                    # Pipelines de detección de artefactos
│   └── seizures/                     # Pipelines de detección de crisis
├── prior_work/                       # Material técnico de fases anteriores
├── results/
│   ├── figures/                      # Figuras
│   ├── metrics/                      # Métricas
│   └── xai/                          # Resultados de explicabilidad
├── src/
│   ├── core/                         # Componentes principales
│   ├── models/                       # Modelos
│   ├── utils/                        # Utilidades
│   └── xai/                          # Implementaciones XAI
├── tests/                            # Pruebas y verificaciones
├── .python-version                   # Python 3.11
├── CITATION.cff                      # Metadatos de citación
├── README.md                         # Documento principal
├── SETUP.md                          # Instalación y entorno
├── requirements.in                   # Dependencias directas
├── requirements.txt                  # Dependencias resueltas
└── setup.sh                          # Preparación rápida del entorno
```

Este árbol muestra la **estructura principal** y no pretende listar logs, salidas temporales o archivos de depuración.

---

## Instalación

El proyecto utiliza **Python 3.11** y `uv` para la preparación del entorno.

Consulta [`SETUP.md`](SETUP.md) para las instrucciones completas.

```bash
git clone https://github.com/FerAndrade15/hybrid-ai-epilepsy-diagnosis.git
cd hybrid-ai-epilepsy-diagnosis
./setup.sh
```

El proyecto mantiene:

- `requirements.in`: dependencias principales declaradas;
- `requirements.txt`: conjunto de dependencias resueltas utilizado para reproducibilidad.

---

## Resultados y preservación de modelos

Los resultados experimentales se almacenan bajo [`results/`](results/).

Para cada modelo considerado final o relevante para futuras fases se conservan:
- checkpoint o pesos;
- configuración del experimento;
- versión o commit del código;
- dataset y partición utilizados;
- semilla e hiperparámetros;
- métricas obtenidas;
- instrucciones de inferencia,
según corresponda. 

Los pesos de gran tamaño no se almacenan directamente en GitHub. Los modelos disponibles, el medio de distribución utilizado y las instrucciones para descargarlos se documentan en docs/models/.

---

## Limitaciones

- Los resultados corresponden a investigación y no equivalen a validación clínica.
- TUAR y TUSZ pertenecen a la familia de corpus TUH/TUEG; se deben controlar posibles solapamientos de pacientes cuando la comparación lo requiera.
- La prevalencia de las clases puede variar entre particiones y afectar especialmente PR-AUC.
- Siena contiene un número limitado de pacientes, por lo que la incertidumbre de sus métricas debe interpretarse con cautela.
- SeizureTransformer fue desarrollado utilizando TUSZ y Siena; por ello, S1 y las configuraciones dependientes de S1 no deben presentarse sobre Siena como una prueba externa completamente independiente.

---

## Reproducibilidad

Los experimentos deben registrar, cuando corresponda:

- configuración;
- versión del dataset;
- partición de pacientes;
- semilla;
- hiperparámetros;
- checkpoint o versión del modelo;
- commit o versión del código;
- predicciones;
- métricas finales.

Los pesos de gran tamaño no se almacenan directamente en GitHub. Los modelos disponibles, el medio de distribución utilizado y las instrucciones para descargarlos se documentan en [`docs/models/`](docs/models/).

---

## Citación

El repositorio utiliza [`CITATION.cff`](CITATION.cff) para registrar los metadatos básicos del software y de autoría.
