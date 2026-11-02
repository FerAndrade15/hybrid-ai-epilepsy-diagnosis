# Notebooks (`notebooks/`)

Esta carpeta contiene notebooks utilizados para exploración, análisis y validación durante el desarrollo de **Hybrid AI for Epilepsy Diagnosis**.

Los notebooks complementan el código principal del proyecto y se utilizan principalmente para:

- análisis exploratorio de los datasets;
- inspección y validación de etapas de procesamiento;
- pruebas interactivas;
- visualización de señales y resultados;
- desarrollo y análisis de métodos de explicabilidad (XAI);
- experimentos previos a su integración en pipelines reproducibles.

## Organización

El contenido se agrupa por propósito, incluyendo áreas como:

```text
notebooks/
├── eda/
├── core_tests/
└── xai/
```

- `eda/` contiene análisis exploratorios de los corpus EEG.
- `core_tests/` contiene pruebas interactivas de componentes del procesamiento.
- `xai/` contiene experimentación y análisis relacionados con inteligencia artificial explicable.

## Relación con el resto del proyecto

Los notebooks se utilizan principalmente para trabajo interactivo.

El código consolidado y reutilizable se mantiene en:

[`src/`](../src/)

Los experimentos reproducibles se ejecutan desde:

[`pipelines/`](../pipelines/)

Los resultados finales seleccionados para preservación se almacenan en:

[`results/`](../results/)

De forma general:

```text
notebooks/
    ↓
exploración y validación
    ↓
src/ y pipelines/
    ↓
results/
```

## Ejecución

El entorno del proyecto incluye Jupyter y JupyterLab.

Desde la raíz del repositorio:

```bash
uv run jupyter lab
```

o:

```bash
uv run jupyter notebook
```

La configuración general del entorno se encuentra en [`SETUP.md`](../SETUP.md).

## Convenciones

- Los datasets originales no se almacenan dentro de esta carpeta.
- Los notebooks se utilizan para análisis y experimentación interactiva.
- El código estable y reutilizable se conserva en `src/`.
- Los resultados finales se preservan en `results/`.
- Los notebooks mantienen suficiente contexto para comprender el objetivo del análisis realizado.