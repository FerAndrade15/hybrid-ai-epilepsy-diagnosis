
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
Exportación estructurada de las etiquetas formateadas en csv o compatibles con los modelos.

## Estructura propuesta
```bash
+---------------------------------------------------------------------------------------------------------+
| [Menú]: Archivo (EDF)  |  Ver (Paneles)  |  Montajes  |  Filtros Clínicos  |  Asistente IA (ON/OFF)     |
+--------------------------+------------------------------------------------------+-----------------------+
| DOCK IZQUIERDO           | ÁREA CENTRAL: QSplitter (Vertical)                   | DOCK DERECHO          |
| (Exploración & Montajes) | +--------------------------------------------------+ | (Diagnóstico Asistido)|
|                          | | [EEGCanvas] - Trazado Multicanal Continuo        | |                       |
| • ID Paciente            | |  - Exploración 19–21 canales en cascada (µV)     | | • EventPanel:         |
| • Selector de Montaje    | |  - Anotaciones manuales del médico (Drag & Drop) | |   Tabla estructurada  |
|   (Bipolar / Ref)        | |  - Cursor rojo de sincronización temporal        | |   (inicio, fin,       |
| • Filtros en caliente    | +=================== Splitter =====================+ |    canal, tipo, conf) |
|   (Notch 60Hz, PasaBanda)| | [AnnotationViewer] - Auditoría (QTabWidget)      | |                       |
| • Canales (QScrollArea)  | |  (VISIBLE SOLO SI ASISTENTE IA ESTÁ ACTIVO)      | | • Foco Clínico:       |
|   [x] FP1-F7             | |  - Tab 1: Canal Foco & Overlays (tipo MATLAB)    | |   Electrodo con       |
|   [x] F7-T3              | |  - Tab 2: ICA & Descomposición Espacial          | |   mayor peso espacial |
|                          | |  - Tab 3: Espectro & XAI                         | |                       |
+--------------------------+------------------------------------------------------+-----------------------+
| Barra de Estado: [Listo] | [Estudio: 256 Hz | 19 canales] | [Asistente IA: Activado / Inactivo]         |
+---------------------------------------------------------------------------------------------------------+
```


## Recursos 
#### QThread
Recurso para optimizar y paralelizar operaciones, se realizaron pruebas de actividades y permitir una interacción constante desde la UI.
#### PyQtGraph
Se implementó como motor de gráfico nativo y optimizado para la aceleración por hardware de la tarjeta gráfica.
#### Downsampling estratégico
Aplicación de submuestreo de acuerdo a la capacidad de visualización del equipo.
#### Carga por bloques: Lazy loading
Se evita mandar toda la información de forma simultánea a la gráfica o espacio de visualización.
La idea es cargar la información en la memoria RAM y enviar el segmento predeterminado (configuración posterior a la carga del edf).
#### Separación de la lectura de archivos (I/O) en la GUI
Desviar la lectura de EEG a un hilo secundario, para que se siga visualizando y utilizando la interfaz durante la carga de información.
#### Canvas viewport
Medio para guardar una matriz con la informacio´n extraido y que permita mostrarla sin releerla constantemente.


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