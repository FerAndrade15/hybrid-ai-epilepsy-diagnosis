"""
# File: db_manager.py
# Project: Trabajo de graduación
# Author: María Fernanda Andrade Recinos
#
# Creates permanent bridge of the database and app while open.
# Connects the database with the tables templates:
#       Running and defined @ models.py
"""
# Import libraries
import os
import sys
import json
from pathlib import Path
from sqlalchemy import create_engine
from cryptography.fernet import Fernet
from backend.database.models import base

# Engine flag
_engine = None

# Searching paths
MAX_LEVELS_UP = 4
MAX_DEPTH_DOWN = 4
IGNORE_DIRS = {".venv", "venv", ".git", "node_modules", "__pycache__", "build"}

def has_config(folder):
    return (folder / "secret.key").exists() and (folder / "config.enc").exists()

def search_down(root, max_depth):
    """Busca secret.key + config.enc dentro de root, bajando hasta max_depth niveles."""
    if has_config(root):
        return root
    if max_depth == 0:
        return None
    try:
        for child in root.iterdir():
            if child.is_dir() and child.name not in IGNORE_DIRS:
                found = search_down(child, max_depth - 1)
                if found:
                    return found
    except PermissionError:
        pass
    return None


def find_config_dir():
    if getattr(sys, "frozen", False):
        return Path(sys.executable).parent

    here = Path(__file__).resolve()
    for level, parent in enumerate(here.parents[:MAX_LEVELS_UP], start=1):
        found = search_down(parent, MAX_DEPTH_DOWN)
        if found:
            print(f">> Encontrado en {found}")
            return found

    raise FileNotFoundError(
        f"No se encontró secret.key y config.enc en {MAX_LEVELS_UP} niveles "
        f"hacia arriba de {here}"
    )
    
def load_safe_config(base_dir):
    # Read engine structure  
    with open(os.path.join(base_dir, "secret.key"), "rb") as key_file:
        key = key_file.read()
    cipher_suite = Fernet(key)

    with open(os.path.join(base_dir, "config.enc"), "rb") as file:
        cipher_text = file.read()
    json_bytes = cipher_suite.decrypt(cipher_text)
    cfg = json.loads(json_bytes.decode('utf-8'))

    return cfg

def get_connection():
    # Search for dist
    dist_path = find_config_dir()
    # Engine settings
    global _engine
    if _engine is None:
        # Saved configuration
        cfg = load_safe_config(dist_path)
        # URL
        connection_string = f"mysql+pymysql://{cfg['user']}:{cfg['password']}@{cfg['host']}:{cfg['port']}/{cfg['database']}"
        # Engine
        _engine = create_engine(connection_string)
        # Variables templates
        base.metadata.create_all(_engine)
    return _engine

if __name__ == "__main__":
    try:
        engine = get_connection()
        print("¡Conexión establecida con éxito usando configuración cifrada!")
        
        with engine.connect() as conn:
            print("El motor de base de datos está activo y respondiendo.")
            
    except Exception as ex:
        print(f"Error crítico al conectar con la base de datos: {ex}")