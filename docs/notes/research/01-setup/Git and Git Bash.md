# Git & Git Bash

## ¿Qué es?
**Github**: Plataforma de desarrollo colaboratorio para ealmacenar, compartir y gestionar proyectos de software. 
**Git Bash**: Aplicación de emulación de una terminal Unix para Windows. Permite controlar repositorios, carpetas, crear entornos virtuales, correr programas, etc.

## Uso
- Control de versiones de mi código
- Clonar repositorios existentes
- Subir cambios al repositorio remoto
- Navegar carpetas y ejecutar comandos Linux en Windows

---

## Comandos

### Navegación
```bash
cd /ruta/del/repositorio        # Navegar a una carpeta
pwd                             # Ver dirección actual
ls                              # Ver contenido de la carpeta
ls -R                           # Ver contenido recursivo
```

### Repositorio
```bash
git clone https://github.com/User/repo         # Clonar repositorio
git config --global credential.helper store    # Guardar credenciales
```

### Commits
```bash
git status                          # Ver estado actual
git add .                           # Agregar todos los cambios
git commit -m "Update: descripción" # Guardar cambios con mensaje
git push                            # Subir al repositorio remoto
```

### Actualización y revisión de Commits
```bash
#Contenido en el repositorio
git ls-tree -r --name-only origin/margin  #--name-only para no ver la estructura

# Identificar archivos sin rastreo/nuevos
git ls-files --others --exclude-standard
```


### Tipos de commits
| Prefijo  | Cuándo usarlo                 |
| -------- | ----------------------------- |
| `Add`    | Agregar contenido nuevo       |
| `Fix`    | Corregir un error             |
| `Update` | Modificar contenido existente |
| `Remove` | Eliminar contenido            |
| `Init`   | Inicializar algo nuevo        |

---

## Errores comunes 
*(Not found yet)*

## Referencias
- Esencial para la configuración inicial del proyecto (levantamiento de los entornos)

## Fecha
**Creación**: 2026-04-25
**Última actualización**: 2026-05-09
