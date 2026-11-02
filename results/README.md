# Resultados (`results/`)

Esta carpeta contiene los resultados experimentales preservados del proyecto **Hybrid AI for Epilepsy Diagnosis**.

Su función es centralizar las salidas relevantes de los experimentos, manteniéndolas separadas del código fuente, los datasets originales y los archivos temporales de ejecución.

## Estructura

```text
results/
├── figures/
├── metrics/
└── xai/
```

## `figures/`

Contiene figuras finales o relevantes utilizadas para interpretar y comunicar los resultados del proyecto.

Incluye visualizaciones de desempeño, comparaciones entre modelos y material gráfico utilizado en documentación académica o presentaciones.

## `metrics/`

Contiene métricas y resúmenes cuantitativos derivados de los experimentos de detección de artefactos y crisis epilépticas.

Las métricas preservadas permiten comparar modelos, configuraciones y conjuntos de evaluación.

## `xai/`

Contiene resultados de **Explainable Artificial Intelligence (XAI)** aplicados a los modelos analizados.

Incluye resultados derivados de métodos de atribución, importancia de características, análisis por canal y técnicas de ablación.

La implementación de estos métodos se mantiene principalmente en:

[`src/xai/`](../src/xai/)

## Trazabilidad

Los resultados preservados mantienen, cuando corresponde, información suficiente para relacionarlos con:

- modelo utilizado;
- configuración experimental;
- dataset y partición;
- hiperparámetros;
- método de evaluación;
- versión del código;
- checkpoint utilizado.

## Resultados preservados

Durante el desarrollo se generan archivos temporales, cachés y resultados exploratorios.

La carpeta `results/` conserva principalmente resultados que:

- respaldan las conclusiones del trabajo;
- permiten comparar modelos;
- forman parte del análisis XAI;
- se utilizan en documentación académica;
- contribuyen a la reproducibilidad;
- resultan útiles para futuras fases del proyecto.

## Pesos de modelos

Los checkpoints de gran tamaño no se almacenan directamente en esta carpeta ni se versionan en GitHub.

Los pesos asociados con modelos finales se distribuyen mediante el medio definido para cada modelo, incluyendo Docker cuando corresponde.

## Relación con otras carpetas

```text
src/
   ↓
pipelines/
   ↓
results/
```

- [`src/`](../src/) contiene las implementaciones reutilizables.
- [`pipelines/`](../pipelines/) ejecuta los experimentos.
- `results/` conserva las salidas relevantes.

## Convenciones

- Los datasets originales no se almacenan en `results/`.
- La carpeta no se utiliza como caché general.
- Se evitan resultados duplicados.
- Los resultados preservados mantienen suficiente contexto para ser interpretados posteriormente.