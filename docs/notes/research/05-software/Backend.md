# Backend

## MySQL
Configuración y activación de servidor local desde wsl
#### Encender y entrar
``` bash
sudo service mysql start 
sudo mysql
```
#### Creación
```bash
CREATE DATABASE IF NOT EXISTS HospitalHumana 
	CHARACTER SET utf8mb4 
	COLLATE utf8mb4_unicode_ci;

CREATE USER IF NOT EXISTS 'hospital_humana'@'localhost' 
	IDENTIFIED BY 'general_data';
	
GRANT ALL PRIVILEGES ON HospitalHumana.* TO 'hospital_humana'@'localhost'; 
FLUSH PRIVILEGES; 
SHOW GRANTS FOR 'hospital_humana'@'localhost';
```

#### Verificación y revisión
```bash
GRANT ALL PRIVILEGES ON HospitalHumana.* TO 'hospital_humana'@'localhost'; 
FLUSH PRIVILEGES; 
SHOW GRANTS FOR 'hospital_humana'@'localhost'; 
exit;
```

#### Apagar
```bash
sudo service mysql stop
```
#### Confirmación del estado
```bash
sudo service mysql status
```

### Resumen de comandos sudo para activar el servidor

| Acción              | Comando                     |
| ------------------- | --------------------------- |
| Encender            | `sudo service mysql start`  |
| Entrar como admin   | `sudo mysql`                |
| Salir de la consola | `exit;`                     |
| Ver estado          | `sudo service mysql status` |
| Apagar              | `sudo service mysql stop`   |

## Estructura general 
En qué situación necesito esto.

## Comandos / Código
```bash
# comando aquí
```

## Errores comunes 
- Error: descripción → Solución: cómo lo resolví

## Referencias
- Fuente, link, paper, o conversación de donde salió esto o para el que es base para usar después

## Fecha
**Creación**: YYYY-MM-DD
**Última actualización**: YYYY-MM-DD