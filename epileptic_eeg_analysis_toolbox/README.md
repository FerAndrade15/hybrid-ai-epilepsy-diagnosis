# Epileptic EEG Analysis Toolbox

Esta carpeta contiene la herramienta de análisis EEG integrada desarrollada y extendida como parte de **Hybrid AI for Epilepsy Diagnosis**.

La aplicación reúne procesamiento de señales, visualización EEG, gestión de información, ejecución de modelos de inteligencia artificial y presentación de resultados dentro de una interfaz gráfica.

## Estructura general

```text
epileptic_eeg_analysis_toolbox/
├── backend/
├── frontend/
├── config/
├── tests/
├── models_weights/
└── main.py
```

## `frontend/`

Contiene la interfaz gráfica de la aplicación.

Incluye componentes para:

- visualización interactiva de señales EEG;
- navegación por registros;
- presentación de eventos detectados;
- visualización de anotaciones;
- interacción con resultados de modelos;
- integración de análisis y herramientas de apoyo.

La interfaz está implementada principalmente con PySide6 y PyQtGraph.

## `backend/`

Contiene la lógica que conecta la interfaz con procesamiento de datos, modelos y almacenamiento.

Incluye componentes para:

- carga y procesamiento de señales;
- ejecución de modelos;
- inferencia clínica;
- postprocesamiento;
- acceso a base de datos;
- manejo de resultados y anotaciones.

Dentro del backend se encuentra el servicio de machine learning:

```text
backend/ml_service/
```

Este componente integra los modelos disponibles y coordina la inferencia desde la aplicación.

## `config/`

Contiene configuraciones globales relacionadas con:

- rutas de la aplicación;
- procesamiento EEG;
- compatibilidad de ejecución;
- parámetros compartidos.

## Modelos

La herramienta integra modelos desarrollados o utilizados durante las distintas fases del proyecto.

La carga de modelos se organiza mediante el registro e infraestructura contenidos en:

```text
backend/ml_service/
```

Los pesos grandes se mantienen fuera del control de versiones.

Cuando se utilizan localmente, se almacenan en:

```text
models_weights/
```

Esta carpeta está excluida del repositorio de GitHub.

## Base de datos

El backend incluye soporte para almacenamiento estructurado mediante SQL.

La capa de base de datos contiene:

- definición de modelos;
- manejo de conexiones;
- repositorios de acceso a información;
- configuración inicial.

Las credenciales y configuraciones locales no se almacenan directamente en el repositorio.

## Ejecución

El punto principal de entrada de la aplicación es:

```text
main.py
```

La aplicación utiliza el mismo entorno Python definido para el proyecto principal.

La instalación de dependencias se encuentra documentada en:

[`SETUP.md`](../SETUP.md)

## Relación con el código experimental

La herramienta representa la integración orientada al uso de los métodos desarrollados durante el proyecto.

De forma general:

```text
src/ y pipelines/
        ↓
modelos y métodos validados
        ↓
epileptic_eeg_analysis_toolbox/
        ↓
interfaz de análisis EEG
```

El desarrollo experimental permanece separado de la lógica de la aplicación para facilitar mantenimiento y reproducibilidad.

## Convenciones

- Los datasets originales no se almacenan dentro de la herramienta.
- Los checkpoints pesados se mantienen fuera de Git.
- Las credenciales de base de datos permanecen fuera del control de versiones.
- La herramienta utiliza modelos y componentes previamente desarrollados y validados dentro del proyecto.
- Los cambios experimentales se mantienen separados de la integración estable de la aplicación.