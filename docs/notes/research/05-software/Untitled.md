Aquí tienes el **Plan Maestro de Construcción en Orden Estricto de Dependencias**, estructurado para que el flujo sea lógico: desde las bases de datos y la configuración del backend, pasando por el procesamiento y la inteligencia artificial, hasta llegar a la interfaz de usuario en PySide6.

Cada archivo incluye su función técnica exacta y su estado actual:

### FASE 1: Configuración Global y Entorno (La Base del Proyecto)

Antes de procesar datos o conectar módulos, el sistema necesita conocer rutas y estándares clínicos.

- **[1.1] `config/app_config.py`**
    
    - **Función:** Define rutas relativas y absolutas dinámicas usando `sys._MEIPASS` para asegurar que el software funcione tanto en desarrollo como una vez compilado a ejecutable `.exe` independiente.
        
    - **Estado:** **¡Completado!**
        
- **[1.2] `config/data_config.py`**
    
    - **Función:** Almacena los diccionarios del sistema 10-20 (19–21 canales clínicos estándar), las fórmulas de montajes bipolares/longitudinales (doble banana) y las equivalencias taxonómicas de anotaciones (TUSZ/TUAR: crisis, artefactos, fondo).
        
    - **Estado:** **¡Completado!**
        

### FASE 2: Capa de Persistencia y Metadatos Clínicos (`backend/database/`)
f
Gestiona la base de datos relacional (expedientes clínicos, auditoría y rutas en disco de los registros EDF).

- **[2.1] `backend/database/models.py`**
    
    - **Función:** Modela el esquema relacional en SQLAlchemy con las tablas `User` (autenticación), `Patient` (expediente clínico, demografía, notas) y `EEGStudy` (duración, frecuencia de muestreo y la columna `edf_file_path` apuntando al disco duro).
        
    - **Estado:** **¡Completado!**
        
- **[2.2] `backend/database/db_manager.py`**
    
    - **Función:** Desencripta las credenciales hospitalarias con `Fernet`, genera el motor de conexión (`create_engine`) y corre `metadata.create_all()` para instanciar físicamente las tablas.
        
    - **Estado:** **¡Completado y verificado en terminal!**
        
- **[2.3] `backend/database/repositories.py`**
    
    - **Función:** Capa de abstracción CRUD (Create, Read, Update, Delete). Expone funciones en Python (`PatientRepository.get_by_code()`, `StudyRepository.create()`, etc.) para que el resto de la app consulte y guarde registros sin escribir SQL manual ni gestionar sesiones directamente.
        
    - **Estado:** **¡Completado!**
        

### FASE 3: Ingesta, Filtrado y Segmentación de Señales (`backend/pipelines/`)

Manejo de archivos biomédicos pesados y acondicionamiento de señales con MNE y NumPy.

- **[3.1] `backend/pipelines/data_loader.py`**
    
    - **Función:** Carga perezosa de señales desde archivos `.edf` (`mne.io.read_raw_edf(..., preload=False)`) para no desbordar la memoria RAM, extracción de metadatos clínicos y lectura de eventos en `.csv`.
        
    - **Estado:** **¡Completado!**
        
- **[3.2] `backend/pipelines/preprocessing.py`**
    
    - **Función:** Acondicionamiento de señal con filtros pasa-banda (0.5 – 70 Hz), filtro notch para interferencia de red eléctrica (50/60 Hz), normalización Z-score y derivación matemática de montajes clínicos bipolares o referenciales.
        
    - **Estado:** **¡Completado!**
        
- **[3.3] `backend/pipelines/windowing.py`**
    
    - **Función:** Segmentación de los trazados continuos en ventanas deslizantes con o sin solapamiento (ej. ventanas de 1s a 4s), preparándolas para los algoritmos analíticos.
        
    - **Estado:** _**¡Completado!**_
        

### FASE 4: Módulos de Diagnóstico e Inteligencia Artificial (`backend/ml_service/`)

Procesamiento analítico e inferencia desacoplada de la interfaz gráfica.

- **[4.1] `backend/ml_service/ica_module.py`**
    
    - **Función:** Descomposición de la señal en Componentes Independientes (ICA) y clasificación automática de componentes de ruido (parpadeos oculares, artefactos cardíacos y musculares).
        
    - **Estado:** **¡Completado!**
        
- **[4.2] `backend/ml_service/feature_extractor.py`**
    
    - **Función:** Cálculo de descriptores matemáticos por ventana: coeficientes de Transformada Wavelet (DWT), parámetros de movilidad y complejidad de Hjorth, densidades espectrales de potencia (PSD en bandas delta, theta, alfa, beta, gamma) y métricas estadísticas.
        
    - **Estado:** _Pendiente_
        
- **[4.3] `backend/ml_service/inference_engine.py`**
    
    - **Función:** Carga de modelos preentrenados almacenados en `checkpoints/` e inferencia multiclase o binaria (detección de crisis epileptiformes vs. actividad de fondo basal).
        
    - **Estado:** _Pendiente_
        

### FASE 5: Hilos de Ejecución en Segundo Plano (`frontend/workers/`)

El puente de comunicación entre el backend y la UI para evitar congelamientos.

- **[5.1] `frontend/workers/db_worker.py`**
    
    - **Función:** Clase `QThread` que delega las consultas y escrituras a `repositories.py` en un hilo secundario con señales Qt (`pyqtSignal`) de éxito o fallo.
        
    - **Estado:** _Pendiente_
        
- **[5.2] `frontend/workers/analysis_worker.py`**
    
    - **Función:** `QThread` que ejecuta los pipelines de filtrado y el motor de inferencia mientras emite el progreso en tiempo real a la barra de estado de la interfaz.
        
    - **Estado:** _Pendiente_
        

### FASE 6: Componentes Visuales Desacoplados (`frontend/components/`)

Widgets individuales construidos en PySide6 y PyQtGraph.

- **[6.1] `frontend/components/patient_view.py`**
    
    - **Función:** Panel con formulario y tabla para dar de alta nuevos expedientes, consultar el historial clínico y seleccionar pacientes de la base de datos.
        
    - **Estado:** _Pendiente_
        
- **[6.2] `frontend/components/eeg_canvas.py`**
    
    - **Función:** Visor multicanal apilado de alto rendimiento con `pyqtgraph`, soporte de zoom, paneo temporal continuo, reglas de amplitud en $\mu\text{V}$ y sombreado visual de detecciones clínicas.
        
    - **Estado:** _Pendiente_
        
- **[6.3] `frontend/components/event_panel.py`**
    
    - **Función:** Lista de eventos epileptiformes con marcas de tiempo (inicio, fin, canal de origen y confianza del modelo), permitiendo al médico hacer clic para saltar directamente a ese segundo en el trazado.
        
    - **Estado:** _Pendiente_
        
- **[6.4] `frontend/components/settings_sidebar.py`**
    
    - **Función:** Panel lateral de configuración técnica (parámetros de filtros, selección de montaje y credenciales de red/base de datos).
        
    - **Estado:** _Pendiente_
        

### FASE 7: Ensamblaje y Despliegue (Cierre de la Aplicación)

Integración final del entorno de escritorio.

- **[7.1] `assets/styles.qss`**
    
    - **Función:** Hoja de estilos Qt con paleta de colores médicos de alto contraste y tipografía adecuada para entornos de diagnóstico.
        
    - **Estado:** _Pendiente_
        
- **[7.2] `frontend/main_window.py`**
    
    - **Función:** Ventana central (`QMainWindow`) que ensambla los componentes en docks movibles, barras de herramientas, menú de archivos y barra de estado.
        
    - **Estado:** _Pendiente_
        
- **[7.3] `main.py`**
    
    - **Función:** Archivo raíz ejecutable: inicializa `QApplication`, aplica los estilos, verifica la integridad del sistema y lanza la ventana principal.
        
    - **Estado:** _Pendiente_
        

### ¿En dónde estamos posicionados hoy?

Habiendo terminado **[2.1]** y **[2.2]**, el siguiente paso indispensable para cerrar completamente la base de datos y poder pasar a la carga de señales es **[2.3] `backend/database/repositories.py`**.

¿Comenzamos a estructurar `repositories.py`?


IMPORTANTE:
Para alimentar un clasificador clínico (Random Forest) a nivel de ventana, las propiedades de los componentes independientes deben consolidarse de forma fija mediante agregación estadística o proyección espacial. De lo contrario, una ventana con 15 componentes generaría 15 predicciones discrepantes en lugar de un único veredicto temporal.