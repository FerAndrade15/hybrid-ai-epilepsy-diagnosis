"""
# File: setup_config.py
# Project: Trabajo de graduación
# Author: María Fernanda Andrade Recinos
#
# Creation of encrypted configuration for engine connection
"""
# Imports for data generation
import os
import json
from cryptography.fernet import Fernet

def generate_encrypted_config():
    print(">> Configuración de conexión de base de datos")
    print(">>\t Por favor, ingrese los datos proporcionados por el administrador de sistemas")

    # Input for user execution
    user = input("Usuario de la base de datos [default: root]: ").strip() or "root"
    password = input("Contraseña de la base de datos: ").strip()
    host = input("IP del servidor (Host) [default: 127.0.0.1]: ").strip() or "127.0.0.1"
    port_str = input("Puerto [default: 3306]: ").strip() or "3306"
    database = input("Nombre de la base de datos [default: HospitalHumana]: ").strip() or "HospitalHumana"

    connection_data = {
        "user": user,
        "password": password,
        "host": host,
        "port": int(port_str),
        "database": database
    }

    # Encrypted key
    key = Fernet.generate_key()
    cipher_suite = Fernet(key)

    # Encrypted data
    json_bytes = json.dumps(connection_data).encode('utf-8')
    cipher_text = cipher_suite.encrypt(json_bytes)

    with open("secret.key", "wb") as key_file:
        key_file.write(key)

    with open("config.enc", "wb") as file:
        file.write(cipher_text)

    print("\nConfiguración completada con éxito! Archivos 'secret.key' y 'config.enc' generados.")

if __name__ == "__main__":
    generate_encrypted_config()