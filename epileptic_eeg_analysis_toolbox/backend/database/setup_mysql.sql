CREATE DATABASE IF NOT EXISTS HospitalHumana;
CREATE USER IF NOT EXISTS 'hospital_humana'@'%' IDENTIFIED BY 'cambiar_esta_clave';
GRANT ALL PRIVILEGES ON HospitalHumana.* TO 'hospital_humana'@'%';
FLUSH PRIVILEGES;