"""
# File: main.py
# Project: Trabajo de graduación
# Author: María Fernanda Andrade
#
#  
"""
import sys
import mne
import numpy as np
import pyqtgraph as pg
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QFileDialog, QMessageBox, 
    QCheckBox, QVBoxLayout, QWidget
)

# Interface
from app.ui_interface import Ui_MainWindow

class EEGAnalyzerApp(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Variables
        self.raw_data = None        # Signal
        self.active_channels = []   # Plotting channels
        self.time_window = 10       # s
        self.current_start_time = 0 # s

        # User interface
        self.setup_ui_added()
        self.connect_signals()

    def setup_ui_added(self):
        """General visual configurations to update Qt designer output"""
        self.channels_container = QWidget()
        self.channels_layout = QVBoxLayout(self.channels_container)
        self.scroll_channels.setWidget(self.channels_container)
        self.scroll_channels.setWidgetResizable(True)

        toggle_dock_action = self.dockWidget.toggleViewAction()
        toggle_dock_action.setText("Hide/Show Channels Panel")
        toggle_dock_action.setShortcut("Ctrl+D")

        self.eeg_graphicsView.setBackground('w')
        self.eeg_graphicsView.showGrid(x=True, y=True, alpha=0.3)

        self.statusBar.showMessage("System started. Waiting for EDF file")

    def connect_signals(self):
        self.actionLoad_EDF_File_3.triggered.connect(self.load_edf_file)
    
    def load_edf_file(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self, "Select EEG file", "EDF files (*.edf);;All files (*.*)"
        )

        if file_path:
            try:
                self.statusBar.showMessage(f"Loading {file_path}")
                self.raw_data = mne.io.read_raw_edf(file_path, preload=True)
                mne.pick_types(self.raw_data.info, meg=False, eeg=True, eog=False, stim=False, exclude='bads')
                
                sfreq = self.raw_data.info['sfreq']
                self.statusBar.showMessage(f"EDF loaded | {len(self.raw_data.ch_names)} channels | Sampling: {sfreq} Hz")

                self.populate_channel_panel()
            
            except:
                QMessageBox.critical(self, "Loading error", f"EDF file not loaded:\n{str(e)}")
                self.statusBar.showMessage("Error while loading the file")

    def populate_channel_panel(self):
        for i in reversed(range(self.channels_layout.count())):
            widget = self.channels_layout.itemAt(i).widget()
            if widget:
                widget.setParent(None)

        self.active_channels.clear()

        for ch_name in self.raw_data.ch_names:
            chk= QCheckBox(ch_name)
            chk.setChecked(True)
            self.active_channels.append(ch_name)
            self.channels_layout.addWidget(chk)

        self.channels_layout.addStretch()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = EEGAnalyzerApp()
    window.show()
    sys.exit(app.exec())