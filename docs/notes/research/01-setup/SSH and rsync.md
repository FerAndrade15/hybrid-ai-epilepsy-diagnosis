# SSH & rsync

## ¿Qué es?
**SSH**: Protocolo para conectarse de forma segura a servidores remotos.
Usa un par de llaves: una privada (solo tú) y una pública (la das al servidor).
**rsync**: Herramienta para transferir y sincronizar archivos entre computadoras.
Usa SSH como transporte seguro. Solo transfiere lo que ha cambiado.

---

## Configuración de SSH Keys

### Ubicación de mis keys
- Llave funcional (registrada en el servidor): `C:\Users\ferch\.ssh\id_ed25519`
- En MobaXterm se accede como: `/mnt/c/Users/ferch/.ssh/id_ed25519`

### Verificar key fingerprint 
```bash
ssh-keygen -lf /mnt/c/Users/ferch/.ssh/id_ed25519.pub
```

### Probar conexión al servidor
```bash
ssh -i /mnt/c/Users/ferch/.ssh/id_ed25519 -v nedc-tuh-eeg@www.isip.piconepress.com
```

---

## Comandos rsync

### Descarga sin descargar (dry run)
```bash
rsync -auvxLn --stats -e "ssh -i /mnt/c/Users/ferch/.ssh/id_ed25519" nedc-tuh-eeg@www.isip.piconepress.com:data/tuh_eeg /ruta/destino/
```

### Descarga del dataset completo
```bash
rsync -auvxL -e "ssh -i /mnt/c/Users/ferch/.ssh/id_ed25519" nedc-tuh-eeg@www.isip.piconepress.com:data/tuh_eeg /ruta/destino/
```

### Test de acceso
```bash
rsync -auvxL -e "ssh -i /mnt/c/Users/ferch/.ssh/id_ed25519" nedc-tuh-eeg@www.isip.piconepress.com:data/tuh_eeg/TEST .
```

### Flags explicadas
| Flag | Significado |
|------|-------------|
| `-a` | Archive: preserva permisos y fechas |
| `-u` | Update: no sobreescribe archivos más nuevos |
| `-v` | Verbose: muestra lo que transfiere |
| `-x` | No sale del sistema de archivos actual |
| `-L` | Sigue links simbólicos |
| `-n` | Dry run: simula sin descargar |
| `--stats` | Muestra resumen de tamaño total |

---

## Errores comunes

- **Permission denied (publickey)** → verificar que la llave correcta es `/mnt/c/Users/ferch/.ssh/` y no `/home/mobaxterm/.ssh/`. MobaXterm tiene dos homes distintos.
- **no identity pubkey loaded** → el `.pub` no estaba junto a la privada o eran llaves diferentes.
- **receiver change_dir failed** → el comando rsync estaba en múltiples líneas con `\`. Escribirlo en una sola línea.

---

## Referencias
- Dataset TUH EEG: https://isip.piconepress.com/projects/nedc/html/tuh_eeg/

## Fecha
**Creación**: 2026-05-09
**Última actualización**: 2026-05-09