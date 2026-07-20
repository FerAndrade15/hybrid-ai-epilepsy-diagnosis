# Setup del entorno con `uv`

Esta guía deja el proyecto **plug and play**: cualquier persona (o tú mismo en otra computadora del laboratorio) puede clonar el repo y tener el entorno listo con 3 comandos, sin preocuparse por qué versión de Python hay instalada en esa máquina.

---

## 1. Qué es `uv` y por qué lo usamos

`uv` es una herramienta (de Astral, los creadores de Ruff) que reemplaza `pip` + `venv` + gestión de versiones de Python en un solo binario. A diferencia de `python -m venv`, **si la versión de Python que pides no existe en la máquina, `uv` la descarga y la aísla automáticamente** — no depende del PATH del sistema, del `py` launcher, ni de permisos de administrador.

---

## 2. Instalar `uv` (una sola vez por computadora)

### Windows (Git Bash / PowerShell)
```bash
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

### Mac / Linux
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Después de instalar, **cierra y reabre la terminal** para que reconozca el comando `uv`. Verifica con:

```bash
uv --version
```

---

## 3. Configuración del proyecto (esto ya se deja listo en el repo)

### 3.1 Archivo `.python-version`
Fija la versión de Python que el proyecto necesita, para que `uv` la use automáticamente sin que nadie tenga que recordarla:

```
3.11
```

### 3.2 `requirements.txt`
Se mantiene igual que ahora — `uv` lo lee sin cambios.

### 3.3 Script `setup.sh`
Este es el corazón del "plug and play". Automatiza todo el proceso:

```bash
#!/bin/bash
set -e

echo "Verificando uv..."
if ! command -v uv &> /dev/null; then
    echo "uv no está instalado. Instálalo primero:"
    echo "  Windows: powershell -ExecutionPolicy ByPass -c \"irm https://astral.sh/uv/install.ps1 | iex\""
    echo "  Mac/Linux: curl -LsSf https://astral.sh/uv/install.sh | sh"
    exit 1
fi

echo "Creando entorno virtual con Python $(cat .python-version 2>/dev/null || echo '3.11')..."
uv venv --python "$(cat .python-version 2>/dev/null || echo '3.11')"

echo "Instalando dependencias..."
uv pip install -r requirements.txt

echo ""
echo "Listo. Activa el entorno con:"
echo "  source .venv/Scripts/activate   (Windows/Git Bash)"
echo "  source .venv/bin/activate       (Mac/Linux)"
```

Dale permisos de ejecución una vez (esto se guarda en git):

```bash
chmod +x setup.sh
```

---

## 4. Uso diario (para ti o cualquier colaborador)

### Primera vez en una máquina nueva
```bash
git clone <url-del-repo>
cd hybrid-ai-epilepsy-diagnosis
./setup.sh
source .venv/Scripts/activate   # Windows/Git Bash
```

### Días siguientes (el venv ya existe)
```bash
source .venv/Scripts/activate
```

### Agregar una dependencia nueva
```bash
uv pip install nombre-paquete
uv pip freeze > requirements.txt   # actualiza el archivo para que el equipo la reciba
```

---

## 5. Comandos equivalentes (referencia rápida)

| Antes (pip/venv)                          | Ahora (uv)                              |
|--------------------------------------------|------------------------------------------|
| `python -m venv .venv`                     | `uv venv --python 3.11`                   |
| `pip install -r requirements.txt`          | `uv pip install -r requirements.txt`      |
| `pip freeze > requirements.txt`            | `uv pip freeze > requirements.txt`        |
| `pip install paquete`                      | `uv pip install paquete`                  |

La activación del entorno (`source .venv/Scripts/activate`) **no cambia** — sigue siendo la misma en ambos casos.

---

## 6. Qué subir a git

Agrega esto a tu `.gitignore` (si no está ya):

```
.venv/
__pycache__/
*.pyc
```

Y **sí sube** estos archivos, son los que hacen el setup reproducible:
- `.python-version`
- `requirements.txt`
- `setup.sh`
- este archivo, `SETUP.md`

---

## 7. Troubleshooting rápido

**"uv: command not found" después de instalar**
Cierra la terminal por completo y ábrela de nuevo — el instalador modifica el PATH y solo se recarga en una sesión nueva.

**Git Bash en Windows no reconoce el `.venv/Scripts/activate`**
Revisa que estés parado en la carpeta del proyecto (`pwd`) antes de correr el comando; la ruta es relativa.

**Quiero verificar qué Python está usando el venv activado**
```bash
which python
python --version
```
