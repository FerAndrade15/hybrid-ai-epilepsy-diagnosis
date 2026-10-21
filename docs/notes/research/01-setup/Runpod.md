# Runpod

## ¿Qué es?


## Uso
- Control de versiones de mi código
- Clonar repositorios existentes
- Subir cambios al repositorio remoto
- Navegar carpetas y ejecutar comandos Linux en Windows

---

## Comandos

### Network
```bash
rsync -avP -e "ssh -p <PORT> -i ~/.ssh/id_ed25519" /path/to/local/dataset/ root@<RUNPOD_IP>:/workspace/dataset/

rsync -avP --info=progress2 -e "ssh -p 10020 -i ~/.ssh/id_ed25519" /mnt/d/tuh_eeg/tuh_eeg_seizure/ root@203.57.40.93:/workspace/dataset/

```


### Manejo del repositorio
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
git rm .                            # Eliminar archivos ya rastreados en el Git
git rm -r .                         # Eliminar carpetas (borrar recursivamente)
```

### Actualización y revisión del Git
```bash
#Contenido en el repositorio
git ls-tree -r --name-only origin/margin  #--name-only para no ver la estructura

# Identificar archivos sin rastreo/nuevos
git ls-files --others --exclude-standard
```

### Mantener la estructura del repositorio
```bash
find . -type d -empty -not -path "./.git/*" -exec touch {}/.gitkeep \;
git add .
git commit -m "Add .gitkeep to preserve empty directories"
git push 
```

### Crear versiones o hitos
```bash
 git tag -a vx.x.x -m "Comment to describe the version x.x.x"
 git push origin --tagas # For all tags
 git push origin vx.x.x  # Just the selected tag
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
**Última actualización**: 2026-08-21
