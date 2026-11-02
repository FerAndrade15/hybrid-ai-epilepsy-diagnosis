# Docker (`__docker__/`)

Esta carpeta contiene recursos relacionados con Docker utilizados por **Hybrid AI for Epilepsy Diagnosis**.

Docker se utiliza como apoyo para crear entornos reproducibles y para distribuir componentes del proyecto que no se almacenan directamente en GitHub, como determinados checkpoints de modelos.

## Contenido

La carpeta incluye scripts y recursos auxiliares para preparar o utilizar Docker en los entornos donde se ejecuta el proyecto.

Estos recursos complementan la instalación local documentada en:

[`SETUP.md`](../SETUP.md)

## Uso dentro del proyecto

Docker cumple principalmente funciones de:

- reproducibilidad del entorno;
- ejecución aislada;
- transferencia de modelos o dependencias pesadas;
- soporte para despliegue y ejecución remota.

Su uso no es obligatorio para ejecutar todas las partes del proyecto localmente.

## Pesos de modelos

Los checkpoints de gran tamaño no se versionan directamente en GitHub.

Cuando un modelo se distribuye mediante Docker, la imagen correspondiente contiene o permite recuperar los recursos necesarios para su ejecución.

## Convenciones

- Los recursos Docker se mantienen separados del código científico principal.
- La lógica de modelos permanece en [`src/`](../src/) o en la herramienta correspondiente.
- Las instrucciones generales de instalación se mantienen en [`SETUP.md`](../SETUP.md).