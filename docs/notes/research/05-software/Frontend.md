
# Development of Software FrontEnd

## ¿Qué es?
Capa de visualización y manipulación de datos, es decir, interfaz gráfica del entorno para la aplicación del análisis de datos realizado mediante los algoritmos de Inteligencia artificial obtenidos.
## Requerimientos - GUI
Los requirimientos funcionales identificados mediante un mapeo y análisis de las opciones comerciales y considerando las observaciones y consideraciones de los modelos previos presentados al Centro HUMANA, se enumeran a continuación.
1. Ingreso y manejo de datos
	- Lectura de metadatos y señales: .edf y matriz de datos crudos
	- Gestión del caché local: 


2. Lector de metadatos
3. Lector de señales 
4. Gestión de caché local
5. Renderización de múltiples canales (Escala de amplitud y desplazamiento temporal interactivo)
6. Control de offset vertical dinámico
7. Panel retráctil con selector de canales activos y ajuste de filtros digitales interactivos
8. Capas de anotación manual (ingreso de labels por el neurologo o especialista, capaz activable igual por un panel retractil para ver losmismos canales pero se note que cambia de herramientas y anotar)
9. Regiones sombreadas de lo que aprendió el modeo (con una ventana movible algo transparaente o dato que me permitan saber qué certeza tiene el modelo de algo / como el confidence de mi modelo traían todos 1, en este caso se reduciría)
10. Permitir encender y apagar las marcas manuales y las generadas
11. Permitir la extracción de los labels con canales monopolares, bipolares y tiempos, como los csv que yo recibo para mi modelo
12. Permitir activar y desactivar la aparición de artefactos (en este caso sería solo marcarlos como regiones no releventes o con mejor importancia porque están contaminadas)
13. Motor de montaje clínico (bipolar, referencial y promedio auricular/común)
14. Control de velocidad de barrido (Desplazamiento horizontal sobre la data)


## Comandos / Código
```bash
uv run pyside6-designer app/interface.ui
```

## Errores comunes 
- Error: descripción → Solución: cómo lo resolví

## Referencias
- Fuente, link, paper, o conversación de donde salió esto o para el que es base para usar después

## Fecha
**Creación**: YYYY-MM-DD
**Última actualización**: YYYY-MM-DD