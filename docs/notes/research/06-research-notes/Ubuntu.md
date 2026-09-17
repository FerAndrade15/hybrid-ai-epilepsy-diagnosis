# Ubuntu

## Uso
name: mariaandrade
password: tesis1102

## Comandos / Código
```bash
# comando aquí
```


Download the files using your terminal:

wget -r -N -c -np https://physionet.org/files/chbmit/1.0.0/

### `wget -r -N -c -np`

| Opción | Nombre        | ¿Qué hace?                                                                |
| ------ | ------------- | ------------------------------------------------------------------------- |
| `-r`   | **Recursive** | Descarga no solo un archivo, sino toda la carpeta y subcarpetas           |
| `-N`   | **Newer**     | Solo descarga si el archivo es más nuevo que el que ya tienes             |
| `-c`   | **Continue**  | Si la descarga se interrumpe, la **continúa** desde donde quedó           |
| `-np`  | **No Parent** | No sube a carpetas superiores, solo descarga lo que está dentro de la URL |

### `wget` vs `rsync`

||`wget`|`rsync`|
|---|---|---|
|**Para qué**|Descargar de internet|Sincronizar/copiar archivos|
|**Desde dónde**|URLs (HTTP, HTTPS, FTP)|Servidores SSH, discos locales|
|**Reanuda descargas**|✅ Con `-c`|✅ Automático|
|**Solo descarga cambios**|⚠️ Con `-N`|✅ Siempre, es su especialidad|
|**Velocidad**|Normal|Más eficiente en archivos grandes|
|**Uso típico**|Datasets públicos en la web|Backups, servidores cloud|


---

## Errores comunes 
- Error: descripción → Solución: cómo lo resolví

## Referencias
- Fuente, link, paper, o conversación de donde salió esto o para el que es base para usar después

## Fecha
**Creación**: YYYY-MM-DD
**Última actualización**: YYYY-MM-DD