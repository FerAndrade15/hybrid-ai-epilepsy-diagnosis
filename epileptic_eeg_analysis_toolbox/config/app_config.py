"""
# File: app_config.py
# Project: Trabajo de graduación
# Author: María Fernanda Andrade Recinos

System global paths configuration and 
execution compatibility for .exe files
"""
# Required libraries
import sys
from pathlib import Path

# Absolute project root
PROJECT_ROOT = Path(__file__).resolve().parent.parent

if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

def get_resource_path(relative_path: str) -> Path:
    """
    Resolves problems with relative roots and static resources.
    Compatible with python and PyInstaller execution (sys._MEIPASS)
    """
    if hasattr(sys, "_MEIPASS"):
        return Path(sys._MEIPASS) / relative_path
    return PROJECT_ROOT / relative_path

# Standard directory of the app
ASSETS_DIR = PROJECT_ROOT / "assets"
STYLESHEET_PATH = ASSETS_DIR / "styles.qss"
CHECKPOINTS_DIR = PROJECT_ROOT / "backend" / "ml_service" / "checkpoints"
CACHE_DIR = PROJECT_ROOT / "cache"

DB_DEFAULT_PATH = PROJECT_ROOT / "local_hospital.db"