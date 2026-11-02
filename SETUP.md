# Configuración del entorno

Esta guía describe cómo preparar el entorno local del proyecto **Hybrid AI for Epilepsy Diagnosis**, configurar las rutas de datos y mantener las dependencias necesarias para reproducir los experimentos.

> Los datasets y los pesos de gran tamaño no se distribuyen directamente en este repositorio.

---

## 1. Requisitos

El proyecto utiliza:

- **Python 3.11**, definido en `.python-version`;
- **uv** para crear el entorno virtual e instalar dependencias;
- Git para clonar y actualizar el repositorio.

No es necesario instalar Python 3.11 manualmente si se utiliza `uv`: cuando la versión solicitada no está disponible localmente, `uv` puede descargarla automáticamente.

---

## 2. Instalación rápida

Clona el repositorio:

```bash
git clone https://github.com/FerAndrade15/hybrid-ai-epilepsy-diagnosis.git
cd hybrid-ai-epilepsy-diagnosis
```

Ejecuta:

```bash
./setup.sh
```

El script:

1. verifica si `uv` está disponible;
2. intenta instalar `uv` si no se encuentra;
3. crea `.venv` utilizando la versión indicada en `.python-version`;
4. instala las dependencias definidas en `requirements.txt`.

Si `uv` acaba de instalarse pero la terminal todavía no lo reconoce, cierra la terminal, abre una nueva sesión y vuelve a ejecutar:

```bash
./setup.sh
```

---

## 3. Ejecución del código

### Opción recomendada: usar `uv run`

No es necesario activar manualmente el entorno virtual:

```bash
uv run python ruta/al/script.py
```

Para módulos del proyecto:

```bash
uv run python -m pipelines.seizures.aitrics_cnn_lstm --smoke
```

### Opción alternativa: activar `.venv`

**Windows / Git Bash**

```bash
source .venv/Scripts/activate
```

**Linux / macOS / WSL**

```bash
source .venv/bin/activate
```

Después:

```bash
python ruta/al/script.py
```

---

## 4. Dependencias

El proyecto mantiene dos archivos:

### `requirements.in`

Contiene las **dependencias directas** utilizadas por el proyecto.

Ejemplos:

- PyTorch y TensorFlow;
- scikit-learn y XGBoost;
- MNE y PyEDFlib;
- Captum y SHAP;
- FastAPI;
- herramientas de interfaz y notebooks.

Si el proyecto empieza a utilizar una dependencia nueva de forma permanente, debe agregarse aquí.

### `requirements.txt`

Contiene las dependencias **resueltas y versionadas** utilizadas para reproducir el entorno.

Este archivo fue generado a partir de `requirements.in` con:

```bash
uv pip compile requirements.in -o requirements.txt
```

### Agregar o actualizar una dependencia

1. Agrega la dependencia a `requirements.in`.
2. Regenera `requirements.txt`:

```bash
uv pip compile requirements.in -o requirements.txt
```

Para actualizar las versiones disponibles de todas las dependencias:

```bash
uv pip compile requirements.in -o requirements.txt --upgrade
```

3. Instala el entorno actualizado:

```bash
uv pip install -r requirements.txt
```

> Evita usar `uv pip freeze > requirements.txt` como método principal de mantenimiento, ya que `requirements.in` es la fuente de dependencias directas del proyecto.

---

## 5. Datos

Los datasets utilizados por el proyecto **no se incluyen en GitHub**.

El código trabaja principalmente con:

- TUH EEG Artifact Corpus (TUAR);
- TUH EEG Seizure Corpus (TUSZ);
- Siena Scalp EEG Database, cuando corresponde.

Las rutas principales se resuelven actualmente en:

```text
src/core/data_config.py
```

El código busca automáticamente ubicaciones conocidas para los datos, incluyendo:

```text
/workspace/data
```

para ejecución en RunPod, además de rutas configuradas para almacenamiento externo y equipos del laboratorio.

Si ninguna ruta válida existe, el código genera:

```text
FileNotFoundError: No valid data path found
```

Antes de ejecutar pipelines en una computadora nueva, revisa en `src/core/data_config.py`:

```python
ALL_DATA_POSSIBLE_PATHS
ALL_OUTPUTS_POSSIBLE_PATHS
```

y agrega o adapta una ruta local si es necesario.

### Estructura de corpus esperada

La configuración actual contempla, entre otros:

```text
tuh_eeg_artifact/
└── v3.0.1/

tuh_eeg_seizure/
└── v2.0.6/
```

Las versiones utilizadas por un experimento deben verificarse en su configuración o documentación correspondiente antes de reproducir resultados.

---

## 6. Directorio de resultados

Los resultados y cachés de procesamiento no deben escribirse dentro de los datasets originales.

`src/core/data_config.py` busca una carpeta de salida independiente mediante:

```python
ALL_OUTPUTS_POSSIBLE_PATHS
```

Entre las ubicaciones contempladas actualmente se encuentran:

```text
/workspace/ml-outputs
```

y rutas equivalentes en almacenamiento externo o equipos del laboratorio.

Si ninguna carpeta de salida válida existe, se genera:

```text
FileNotFoundError: No valid outputs path found
```

---

## 7. Pesos de modelos

Los checkpoints grandes no se almacenan directamente en GitHub.

El `.gitignore` excluye, entre otros:

```text
*.pt
*.pth
epileptic_eeg_analysis_toolbox/models_weights/
```

Por lo tanto, clonar el repositorio **no garantiza que los modelos preentrenados estén disponibles localmente**.

Las instrucciones de descarga o recuperación de pesos finales deben consultarse en la documentación de modelos correspondiente.

Por ejemplo, el código de SeizureTransformer espera el peso en una ubicación equivalente a:

```text
epileptic_eeg_analysis_toolbox/
└── models_weights/
    └── seizure_transformer.pth
```

cuando se utiliza esa integración.

---

## 8. Docker y RunPod

El repositorio contiene:

```text
__docker__/
__runpod__/
```

Estas carpetas contienen recursos específicos para ejecución reproducible o remota.

Su uso **no es obligatorio para instalar el entorno local básico** descrito en este documento.

Docker también puede utilizarse como medio de distribución para checkpoints de gran tamaño cuando así se indique en la documentación del modelo correspondiente.

---

## 9. Archivos que sí deben conservarse con el código

Para poder reconstruir el entorno, deben mantenerse versionados:

```text
.python-version
requirements.in
requirements.txt
setup.sh
SETUP.md
```

El entorno virtual local no debe subirse:

```text
.venv/
```

Los datasets, outputs y pesos pesados también se mantienen fuera del repositorio según las reglas de `.gitignore`.

---

## 10. Solución de problemas

### `uv: command not found`

Si `setup.sh` acaba de instalar `uv`, cierra la terminal y vuelve a abrirla.

También puedes comprobar:

```bash
uv --version
```

### Verificar Python

```bash
uv run python --version
```

Debe utilizar Python 3.11 según `.python-version`.

Si activaste manualmente el entorno:

```bash
python --version
```

### El entorno instala correctamente pero el pipeline falla al importar `src`

Ejecuta los comandos desde la raíz del repositorio y, cuando el pipeline esté organizado como módulo, prefiere:

```bash
uv run python -m pipelines.<subcarpeta>.<script>
```

### `No valid data path found`

Configura una ruta válida en:

```python
src/core/data_config.py
```

dentro de:

```python
ALL_DATA_POSSIBLE_PATHS
```

### `No valid outputs path found`

Configura o crea una ruta válida incluida en:

```python
ALL_OUTPUTS_POSSIBLE_PATHS
```

### No se encuentra un archivo `.pt` o `.pth`

Los pesos grandes están excluidos de GitHub. Consulta la documentación del modelo para obtener el checkpoint requerido.

---

## 11. Verificación mínima

Después de preparar el entorno:

```bash
uv run python --version
uv pip list
```

Para verificar una parte concreta del proyecto, utiliza los tests o el modo `--smoke` de los pipelines que lo soporten.

Ejemplo:

```bash
uv run python -m pipelines.seizures.aitrics_cnn_lstm --smoke
```

---

## Resumen rápido

En una máquina nueva:

```bash
git clone https://github.com/FerAndrade15/hybrid-ai-epilepsy-diagnosis.git
cd hybrid-ai-epilepsy-diagnosis
./setup.sh
uv run python --version
```

Después:

1. configura o conecta los datasets;
2. configura una ubicación de outputs;
3. descarga los pesos requeridos por el modelo que quieras utilizar;
4. ejecuta el pipeline correspondiente.

Para una descripción general del proyecto, consulta [`README.md`](README.md).
