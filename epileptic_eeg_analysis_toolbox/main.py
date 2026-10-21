"""
# File: main.py
# Project: Trabajo de graduación
# Author: Maria Fernanda Andrade Recinos
"""
import os, sys
if getattr(sys, "frozen", False) and sys.stdout is None:
    sys.stdout = sys.stderr = open(os.devnull, "w")

from PySide6.QtWidgets import QApplication
from config.app_config import get_resource_path
from frontend.main_window import MainWindow

def main():
    app = QApplication(sys.argv)
    qss = get_resource_path("assets/styles.qss")
    if qss.exists():
        app.setStyleSheet(qss.read_text(encoding="utf-8"))
    win = MainWindow()
    win.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()