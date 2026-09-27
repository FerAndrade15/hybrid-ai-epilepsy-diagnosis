
# Development of Software FrontEnd

## ¿Qué es?
Capa de visualización y manipulación de datos, es decir, interfaz gráfica del entorno para la aplicación del análisis de datos realizado mediante los algoritmos de Inteligencia artificial obtenidos.
## Requerimientos - GUI
Los requirimientos funcionales identificados mediante un mapeo y análisis de las opciones comerciales y considerando las observaciones y consideraciones de los modelos previos presentados al Centro HUMANA, se enumeran a continuación.
### Ingreso y manejo de datos
- Lectura de metadatos y señales: .edf y matriz de datos crudos
- Gestión del caché local: Capacidad para analizar los resúmenes en caché (.npz, .parquet, entre otros)
### Visualización y procesamiento:
- Motor de renderizado gráfico: Visualización multicanal de alta velocidad con control de velocidad de barrido.
- Control visual clínico: Ajuste dinámico de la escala de amplitud y offset vertical independiente por canal para evitar solapamientos.
- Motor de montajes clínicos: Conversión matricial en tiempo real para alternar entre montajes bipolares, referenciales y promedio (auricular/común).
- Filtros y panel de control: Aplicación de filtros interactivos y panel retráctil de canales activos
### Anotación, visualización de asistente y control de calidad
- Anotación manual: Ingreso de etiquetas clínicas con persistencia incremental para evitar pérdida de datos
- Asistencia con IA: Renderizado de regiones sombreadas por módulo de especialidad con opacidad dependiente del nivel de confianza del modelo.
	- Gestión de artefactos: Segmentos no relevantes o contaminados
- Control de capas visuales.
### Exportación de datos
Exportacíon estructurada de las etiquetas formateadas en csv o compatibles con los modelos.

## Comandos / Código
```bash
# Creación o apertura de PySide Designer sobre el proyecto
uv run pyside6-designer app/interface.ui
```

## Errores comunes 
- Error: descripción → Solución: cómo lo resolví

## Referencias
- Fuente, link, paper, o conversación de donde salió esto o para el que es base para usar después

## Fecha
**Creación**: YYYY-MM-DD
**Última actualización**: YYYY-MM-DD