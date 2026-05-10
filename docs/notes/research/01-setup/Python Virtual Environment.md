# Entornos virtuales - Python

## ¿Qué es?
Es un directorio autocontenido para mantener aislados los recursos necesarios para correr un programa de las versiones en el sistema operativo y de otros entornos virtuales. Permite el uso de dependencias específicas por proyecto y su correcta separación.

## Uso y requerimientos
Los entornos virtuales se utilizaron principalmente debido a que en la Fase VII se necesita un aislamiento de entornos de trabajo con pytorch y tensorflow.
### Versión de Python
Python 3.11.9

## Comandos

### Manejo del entorno
```bash
# Navegación hacia el repositorio
cd /ruta/del/repositori

# Creación del entorno
py -3.11 -m venv .venv

# Activación del entorno
source .venv/Scripts/activate 

# Eliminación del entorno
rm -rf .venv                                # .venv es el nombre genérico     

# Desactivación del entorno
deactivate
```

### Manejo de librerías
```bash
# Instalación de las dependencias
python -m pip install -r requirements.txt
  
# Para instalar cualquier librería
pip install nombre-libreria                

#  Actualización de los requirements del venv al agregar librerías
pip freeze --local > requirements.txt      

# Desinstalación de librerías 
pip unistall nombre-librería                
pip install -r requirenemts.txt
```
## Errores comunes 
- Error: descripción → Solución: cómo lo resolví

## Referencias
- Fuente, link, paper, o conversación de donde salió esto o para el que es base para usar después

## Fecha
**Creación**: YYYY-MM-DD
**Última actualización**: YYYY-MM-DD