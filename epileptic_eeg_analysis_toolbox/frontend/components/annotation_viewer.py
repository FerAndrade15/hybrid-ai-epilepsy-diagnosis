"""
# File: annotation_viewer.py
# Project: Trabajo de graduación
# Author: Maria Fernanda Andrade Recinos

Panel for windows analysis by channel, ICA, XAI metrics, events panel and clinical register.
"""
from typing import Optional, List, Dict, Any
import numpy as np
import pyqtgraph as pg
from PySide6.QtCore import Qt, Signal
from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QTabWidget, 
    QComboBox, QLabel, QCheckBox
)

from frontend.components.event_panel import EventPanel

class AnnotationViewer(QWidget):
    # Annotations starter (cursor de auditoría)
    point_inspected = Signal(float, float)                  # time (s), amplitud (µV)

    def __init__(self, parent: Optional[QWidget] = None):
        super().__init__(parent)
        
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(4, 4, 4, 4)

        # Tabs container
        self.tabs = QTabWidget(self)
        main_layout.addWidget(self.tabs)

        # Build tabs
        self._setup_tab_focused_channel()
        self._setup_tab_ica()
        self._setup_tab_xai()

    # -------------------------------------------------------------
    # TAB 1: Highlighted annotations
    # -------------------------------------------------------------
    def _setup_tab_focused_channel(self):
        tab = QWidget()
        layout = QVBoxLayout(tab)
        layout.setContentsMargins(6, 6, 6, 6)

        # Control bar: Channel selector and inspection options
        controls_layout = QHBoxLayout()
        controls_layout.addWidget(QLabel("Canal a visualizar:"))

        self.cmb_focus_channel = QComboBox()
        self.cmb_focus_channel.currentTextChanged.connect(self._on_focus_channel_changed)
        controls_layout.addWidget(self.cmb_focus_channel)

        self.chk_grid = QCheckBox("Grilla")
        self.chk_grid.setChecked(True)
        self.chk_grid.toggled.connect(lambda v: self.focus_plot.showGrid(x=v, y=v, alpha=0.2))
        controls_layout.addWidget(self.chk_grid)
        controls_layout.addStretch()
        layout.addLayout(controls_layout)

        # Individual channel draft
        self.focus_plot = pg.PlotWidget()
        self.focus_plot.setBackground("#FFFFFF")
        self.focus_plot.showGrid(x=True, y=True, alpha=0.2)
        self.focus_plot.setLabel('left', 'Voltaje', units='µV')
        self.focus_plot.setLabel('bottom', 'Tiempo', units='s')
        layout.addWidget(self.focus_plot)

        self.tabs.addTab(tab, "Canal Focalizado & Overlays")

    # -------------------------------------------------------------
    # TAB 2: ICA
    # -------------------------------------------------------------
    def _setup_tab_ica(self):
        tab = QWidget()
        layout = QVBoxLayout(tab)
        self.ica_plot = pg.PlotWidget()
        self.ica_plot.setBackground("#FFFFFF")
        self.ica_plot.showGrid(x=True, y=True, alpha=0.5)
        layout.addWidget(self.ica_plot)
        self.tabs.addTab(tab, "Componentes ICA / Fuentes")

    # -------------------------------------------------------------
    # TAB 3: XAI
    # -------------------------------------------------------------
    def _setup_tab_xai(self):
        tab = QWidget()
        layout = QVBoxLayout(tab)
        self.xai_plot = pg.PlotWidget()
        self.xai_plot.setBackground("#FFFFFF")
        #self.xai_plot.showGrid()
        layout.addWidget(self.xai_plot)
        self.ica_plot.showGrid(x=True, y=True, alpha=0.5)
        self.tabs.addTab(tab, "Explicabilidad (XAI)")

    # -------------------------------------------------------------
    # Updating functions and renders
    # -------------------------------------------------------------
    def populate_channels(self, ch_names: List[str]):
        """Fills combo with available channels."""
        self.cmb_focus_channel.clear()
        self.cmb_focus_channel.addItems(ch_names)

    def highlight_event_region(self, start_sec: float, end_sec: float, color: str = "#DC2626", label_text: str = ""):
        """Highligh into focalized channel"""
        print("[DEBUG] Start and end", start_sec, end_sec)
        region = pg.LinearRegionItem(
            values=[start_sec, end_sec],
            brush=pg.mkBrush(f"{color}33"),  # Transparent color
            movable=False
        )
        self.focus_plot.addItem(region)
        if label_text:
            text = pg.TextItem(label_text, color=color, anchor=(0, 1))
            text.setPos(start_sec, 0)
            self.focus_plot.addItem(text)

    def sync_time_window(self, center_time: float, span_sec: float = 10.0):
        self.focus_plot.setXRange(center_time - span_sec / 2, center_time + span_sec / 2, padding=0.0)

    def _on_focus_channel_changed(self, channel_name: str):
        pass

if __name__ == "__main__":
    import sys
    from PySide6.QtWidgets import QApplication, QMainWindow

    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setWindowTitle("Prueba Aislada: AnnotationViewer")
    win.resize(900, 450)

    viewer = AnnotationViewer(win)
    viewer.populate_channels(["FP1-F7", "F7-T3", "T3-T5", "T5-O1", "FP1-F3", "F3-C3"])
    viewer.highlight_event_region(2.5, 4.0, color="#DC2626", label_text="SPSW Detectado")
    viewer.sync_time_window(3.0, span_sec=8.0)

    win.setCentralWidget(viewer)
    win.show()
    sys.exit(app.exec())