# Pruebas (`tests/`)

Esta carpeta contiene pruebas y scripts de validación utilizados durante el desarrollo de **Hybrid AI for Epilepsy Diagnosis**.

Su función es comprobar el funcionamiento de componentes individuales, flujos de procesamiento e integraciones entre módulos antes de incorporarlos en experimentos completos.

Las pruebas abarcan, entre otros aspectos:

- partición de datos;
- procesamiento de señales;
- integración de pipelines;
- carga de modelos;
- ejecución de pruebas rápidas o *smoke tests*;
- inspección de estructuras de datos;
- visualización y verificación de resultados intermedios.

## Relación con el proyecto

Las pruebas utilizan principalmente componentes definidos en:

```text
src/
pipelines/
epileptic_eeg_analysis_toolbox/
```

Los notebooks utilizados para validación interactiva se mantienen por separado en:

[`notebooks/`](../notebooks/)

## Ejecución

Las pruebas se ejecutan desde la raíz del repositorio utilizando el entorno configurado en [`SETUP.md`](../SETUP.md).

Cuando el archivo está organizado como módulo se utiliza, según corresponda:

```bash
uv run python -m tests.<script>
```

También existen scripts que se ejecutan directamente.

## Convenciones

- Los tests no almacenan datasets originales.
- Los archivos de esta carpeta se utilizan para validación técnica y no representan resultados finales.
- Los resultados finales se conservan en [`results/`](../results/).
- Las pruebas experimentales permanecen separadas del código reutilizable de [`src/`](../src/).