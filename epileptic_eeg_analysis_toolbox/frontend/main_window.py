"""
# File: main_window.py
# Project: Trabajo de graduación
# Author: Maria Fernanda Andrade Recinos
 
Keep track and merge:
 - Status and models memory
 - Visualization of central area
 - Lateral panels
 - Menu Bar
  Cross signals wiring
"""
# System management libraries
import os
import sys
from pathlib import Path

# Required libraries for data management
from typing import Dict, Any, List
from PySide6.QtCore import Qt, QThread, QPropertyAnimation, Property, QRectF, QEasingCurve
from PySide6.QtGui import QPainter, QColor, QBrush
from PySide6.QtWidgets import (
    QMainWindow, QSplitter, QDockWidget, QWidget, QVBoxLayout,
    QHBoxLayout, QLabel, QComboBox, QCheckBox, QScrollArea, QListWidget, QListWidgetItem, 
    QFileDialog, QMessageBox
)

# Theme functions
import qdarktheme

# Visualization functions
from frontend.components.eeg_canvas import EEGCanvas
from frontend.components.event_panel import EventPanel
from frontend.components.annotation_viewer import AnnotationViewer

# Worker functions
from frontend.workers.analysis_worker import AnalysisWorker

# Theme Configuration for all visualization tools
THEME_COLORS = {
    "light": {
        "plot_background": "#FFFFFF",
        "plot_lines": "k",      # Black
        "alpha_lines": 0.2,
        "signal_lines": "#1E293B"
    },
    "dark": {
        "plot_background": "#1E1E2E", 
        "plot_lines": "w",      # White
        "alpha_lines": 0.4,   
        "signal_lines": "#C45A5A"
    }
}

# Main Window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Epileptic EEG Analysis Toolbox")
        self.resize(1450, 900)

        # Status and threads memory
        self.current_file_path: str = ""
        self.analysis_thread: QThread = None
        self.analysis_worker: AnalysisWorker = None

        # Style
        self.dark_mode: bool = False

        # Central area
        self._setup_central_area()

        # Lateral docks
        self._setup_left_dock()
        self._setup_right_dock()

        # Menu Bar and Status Bar
        self._setup_menu_bar()
        self.statusBar().showMessage("Status: Active. Por favor cargue un estudio EDF...")

        # Signals and slots
        self._connect_signals()

        # AI Models
        core_path = self.get_base_path()
        self.models_default_path = os.path.join(core_path, 'models_weights')
        self.available_models(self.models_default_path)
        print("[DEBUG] Path for AI models search: ", self.models_default_path)

        # Default style assignment
        self.setStyleSheet(qdarktheme.load_stylesheet("light"))

    def _setup_central_area(self):
        self.central_splitter = QSplitter(Qt.Vertical, self)
        self.setCentralWidget(self.central_splitter)

        self.theme = THEME_COLORS["dark"] if self.dark_mode else THEME_COLORS["light"]

        self.eeg_canvas = EEGCanvas(self, color_sheet=self.theme)
        self.central_splitter.addWidget(self.eeg_canvas)

        self.annotation_viewer = AnnotationViewer(self)
        self.central_splitter.addWidget(self.annotation_viewer)
        self.annotation_viewer.hide()

    # LEFT DOCKER ----------------------------------------------------------------------
    def _setup_left_dock(self):
        self.dock_left = QDockWidget("Exploración & Montajes", self)
        self.dock_left.setAllowedAreas(Qt.LeftDockWidgetArea | Qt.RightDockWidgetArea)

        container = QWidget()
        layout = QVBoxLayout(container)

        # Informative banner
        layout.addWidget(QLabel("<b>Estudio Activo</b>"))
        self.lbl_study_info = QLabel("Ningún archivo cargado")
        layout.addWidget(self.lbl_study_info)

        # Visualization settings
        layout.addWidget(QLabel("<b>Visualización</b>"))
        self.lbl_study_info = QLabel("Ningún archivo cargado")
        layout.addWidget(self.lbl_study_info)


        # Montaje selection
        layout.addWidget(QLabel("<b>Montaje Clínico:</b>"))
        self.cmb_montage = QComboBox()
        self.cmb_montage.addItems(["Monopolar Referencial", "Bipolar Doble Banana"])
        layout.addWidget(self.cmb_montage)

        # Scroll area
        layout.addWidget(QLabel("<b>Canales Activos:</b>"))
        self.scroll_channels = QScrollArea()
        self.scroll_channels.setWidgetResizable(True)
        self.channels_container = QWidget()
        self.channels_layout = QVBoxLayout(self.channels_container)
        self.scroll_channels.setWidget(self.channels_container)
        layout.addWidget(self.scroll_channels)

        self.dock_left.setWidget(container)
        self.addDockWidget(Qt.LeftDockWidgetArea, self.dock_left)

    # RIGHT DOCKER --------------------------------------------------------------------
    def _setup_right_dock(self):
        self.dock_right = QDockWidget("Diagnóstico Asistido & Eventos", self)
        self.dock_right.setAllowedAreas(Qt.LeftDockWidgetArea | Qt.RightDockWidgetArea)

        self.right_dock_window_container = QWidget()
        self.right_dock_window = QVBoxLayout(self.right_dock_window_container)
        self.right_dock_window.setContentsMargins(0,0,0,0)

        switch_layout = QHBoxLayout()
        lbl_switch = QLabel("Mostrar resultados de IA")
        lbl_switch.setStyleSheet("font-weight: bold;")

        self.chk_show_ai = toggle_switch()
        self.chk_show_ai.setChecked(True)
        self.chk_show_ai.setEnabled(False)
        self.chk_show_ai.toggled.connect(self.toggle_ai_highlights)

        switch_layout.addWidget(lbl_switch)
        switch_layout.addStretch()
        switch_layout.addWidget(self.chk_show_ai)
        self.right_dock_window.addLayout(switch_layout)


        self.event_panel = EventPanel(self)
        self.right_dock_window.addWidget(self.event_panel)

        self.models_panel = QWidget()
        self.models_space = QVBoxLayout(self.models_panel)
        self.models_list =  QListWidget()

        label = QLabel("Modelos disponibles")
        self.models_space.addWidget(label)
        self.models_space.addWidget(self.models_list)

        self.right_dock_window.addWidget(self.models_panel)
        self.models_panel.hide()

        self.dock_right.setWidget(self.right_dock_window_container)
        self.addDockWidget(Qt.RightDockWidgetArea, self.dock_right)

    # AI models  ---------------------------------------------------------------------
    # Integration functions
    def available_models(self, path):
        """Lee una carpeta y agrega los archivos como opciones con checkbox."""      
        
        self.models_list.clear() 
        if not os.path.exists(path):
            print(f"Advertencia: La ruta {path} no existe.")
            return

        # Extensiones permitidas (ajusta según tus tipos de modelos)
        extensiones_validas = ('.pt', '.pth', '.h5', '.onnx')

        # Listar los archivos en el directorio
        for nombre_archivo in os.listdir(path):
            ruta_completa = os.path.join(path, nombre_archivo)
            
            # Verificar que sea un archivo y que termine en las extensiones deseadas
            if os.path.isfile(ruta_completa) and nombre_archivo.endswith(extensiones_validas):
                # Crear el ítem con el nombre del archivo
                name = nombre_archivo.rsplit('.',1)[0].replace("_", " ").title()
                item = QListWidgetItem(name)
                item.setData(Qt.UserRole, nombre_archivo)
                
                # Agregarlo al panel
                self.models_list.addItem(item)

    def get_base_path(self):
        if getattr(sys, 'frozen', False):
            return os.path.dirname(sys.executable)
        else:
            return os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "."))

    def toggle_ai_highlights(self, state:bool):
        if hasattr(self, 'eeg_canvas'):
            self.eeg_canvas.set_ai_regions_visibility(state)

    # MENU BAR ---------------------------------------------------------------------
    def _setup_menu_bar(self):
        bar = self.menuBar()

        # File Menu
        menu_file = bar.addMenu("&Archivo")
        self.action_open = menu_file.addAction("Cargar Estudio EDF...")
        self.action_open.setShortcut("Ctrl+O")
        self.action_open.triggered.connect(self.open_edf_file)

        # View Menu
        menu_view = bar.addMenu("&Ver")
        menu_view.addAction(self.dock_left.toggleViewAction())
        menu_view.addAction(self.dock_right.toggleViewAction())
        self.visualization_mode = menu_view.addAction("Light/Dark Mode")
        self.visualization_mode.triggered.connect(self.update_mode_theme)

        # IA Menu
        menu_ai = bar.addMenu("&Herramientas IA")
        self.action_toggle_ai = menu_ai.addAction("Mostrar Panel de Auditoría IA")
        self.action_toggle_ai.setCheckable(True)
        self.action_toggle_ai.setChecked(False)
        self.action_toggle_ai.setShortcut("Ctrl+Shift+A")
        self.action_toggle_ai.toggled.connect(self.toggle_ai_assistant)
        self.action_select_ai = menu_ai.addAction("Selección/Monitoreo de modelos aplicados")
        self.action_select_ai.setCheckable(True)
        self.action_select_ai.setChecked(False)
        self.action_select_ai.toggled.connect(self.panel_ai_assistants)

    # SIGNALS ------------------------------------------------------------------------
    def _connect_signals(self):
        self.event_panel.event_selected.connect(self.eeg_canvas.jump_to_timestamp)
        self.eeg_canvas.time_cursor_changed.connect(
            self.annotation_viewer.sync_time_window
        )

    # --------------------------------------------------------------------------------
    ## Action slots
    # --------------------------------------------------------------------------------
    def update_mode_theme(self):
        current_mode = not self.dark_mode
        self.theme = THEME_COLORS["dark"] if current_mode else THEME_COLORS["light"]
        self.setUpdatesEnabled(False)

        try:
            if current_mode:
                self.setStyleSheet(qdarktheme.load_stylesheet("dark"))
            else:
                self.setStyleSheet(qdarktheme.load_stylesheet("light"))

            self.dark_mode = current_mode
            self.eeg_canvas.apply_theme(self.theme)

        finally:
            self.setUpdatesEnabled(True)


    def toggle_ai_assistant(self, enabled: bool):
        if enabled:
            self.annotation_viewer.show()
            h = self.central_splitter.height()
            # 65% eeg canvas | 35% AI
            self.central_splitter.setSizes([int(h * 0.65), int(h * 0.35)])
            self.statusBar().showMessage("Asistente IA activado.")
        else:
            self.annotation_viewer.hide()
            self.statusBar().showMessage("Modo pantalla continua expandida.")

    def panel_ai_assistants(self, enabled:bool):
        self.models_panel.setVisible(enabled)

    def open_edf_file(self):
        if self.analysis_thread is not None:
            QMessageBox.information(self, "En curso", "Espera a que termine el análisis actual.")
            return
        
        file_path, _ = QFileDialog.getOpenFileName(self, "Seleccionar EDF", "", "Archivos EDF (*.edf)")
        if not file_path:
            return

        selected_model_filename = None
        selected_items = self.models_list.selectedItems()
        if selected_items:
            filename = selected_items[0].data(Qt.UserRole)
            selected_model_filename = os.path.join(self.models_default_path, filename)
            print(f"[DEBUG] Ruta de IA armada: {selected_model_filename}")

        thread = QThread(self)
        worker = AnalysisWorker(
            edf_path= file_path, 
            preprocessing_params={},
            model_filename=selected_model_filename
        )

        worker.moveToThread(thread)
        thread.started.connect(worker.run)
        worker.progress_updated.connect(self._on_worker_progress)
        worker.analysis_finished.connect(self._on_analysis_completed)
        worker.analysis_failed.connect(self._on_worker_error)
        worker.done.connect(thread.quit)
        thread.finished.connect(worker.deleteLater)
        thread.finished.connect(self._on_thread_finished)
        self.analysis_thread, self.analysis_thread = thread, worker
        self.action_open.setEnabled(False)
        thread.start()

    def _on_thread_finished(self):
        self.analysis_thread = self.analysis_thread = None
        self.action_open.setEnabled(True)

    def close_event(self, event):
        if self.analysis_thread is not None:
            self.analysis_thread.requestInterruption()
            self.analysis_thread.quit()
            self.analysis_thread.wait(5000)
        super().close_event(event)

    def _on_worker_progress(self, percent: int, message: str):
        self.statusBar().showMessage(f"[{percent}%] {message}")

    def _on_analysis_completed(self, results: Dict[str, Any]):
        self.statusBar().showMessage("Estudio procesado exitosamente.")
        
        # EEGCanvas signals input
        signal_matrix = results.get("signal_matrix")
        ch_names = results.get("ch_names", [])
        sfreq = results.get("sfreq", 256.0)
        events = results.get("events", [])

        print(f"[DEBUG] Canales recibidos: {len(ch_names)}")
        if signal_matrix is not None and len(ch_names) > 0:
            self.eeg_canvas.load_signals(signal_matrix, ch_names, sfreq=sfreq)

        # AnnotationViewer channels
        if hasattr(self, 'annotation_viewer'):
            self.annotation_viewer.populate_channels(ch_names)

        # Dock checkboxes for left docker
        self._populate_channel_checkboxes(ch_names)

        if events:
            self.eeg_canvas.draw_ai_events(events)
            self.chk_show_ai.setEnabled(True)
            self.eeg_canvas.set_ai_regions_visibility(self.chk_show_ai.isChecked())

        # Events table
        if hasattr(self, 'event_panel'):
            self.event_panel.set_events(events)


    def _on_worker_error(self, err_msg: str):
        msg = QMessageBox(self)
        msg.setIcon(QMessageBox.Critical)
        msg.setWindowTitle("Error de Procesamiento")
        msg.setText(f"Ocurrió un error:\n{err_msg}")
        msg.setTextFormat(Qt.PlainText) 
        msg.exec()
        #QMessageBox.critical(self, "Error de Procesamiento", f"Ocurrió un error:\n{err_msg}")
        #self.statusBar().showMessage("Error en el análisis.")

    def _populate_channel_checkboxes(self, ch_names: List[str]):
        # Clean previous data
        for i in reversed(range(self.channels_layout.count())):
            w = self.channels_layout.itemAt(i).widget()
            if w:
                w.setParent(None)

        for idx, ch in enumerate(ch_names):
            chk = QCheckBox(ch)
            chk.setChecked(True)
            chk.toggled.connect(lambda state, ch_idx=idx: self.eeg_canvas.toggle_channel_visibility(ch_idx, state))
            self.channels_layout.addWidget(chk)

        self.channels_layout.addStretch()

# Visual resource (checkbox and slide)
class toggle_switch(QCheckBox):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFixedSize(50, 26)
        self.setCursor(Qt.PointingHandCursor)
        self._position = 0.0

        self.animation = QPropertyAnimation(self, b"position")
        self.animation.setEasingCurve(QEasingCurve.InOutQuad)
        self.animation.setDuration(200)
        self.stateChanged.connect(self.setup_animation)

    @Property(float)
    def position(self):
        return self._position

    @position.setter
    def position(self, pos):
        self._position = pos
        self.update()

    def setup_animation(self, value):
        self.animation.stop()
        self.animation.setEndValue(1.0 if value else 0.0)
        self.animation.start()

    def paintEvent(self, event):
        p = QPainter(self)
        p.setRenderHint(QPainter.Antialiasing)
        p.setPen(Qt.NoPen)

        track_color = QColor("#C45A5A") if self.isChecked() else QColor("#555555")
        thumb_color = QColor("#FFFFFF")

        p.setBrush(QBrush(track_color))
        p.drawRoundedRect(0, 0, self.width(), self.height(), self.height()/2, self.height()/2)
        thumb_radius = self.height() - 4
        thumb_x = 2 + self._position * (self.width() - thumb_radius - 4)
        p.setBrush(QBrush(thumb_color))
        p.drawEllipse(QRectF(thumb_x, 2, thumb_radius, thumb_radius))
        p.end()


if __name__ == "__main__":
    import sys
    from PySide6.QtGui import QPalette
    from PySide6.QtWidgets import QApplication

    app = QApplication(sys.argv)
    win = MainWindow()
    # app.setStyleSheet(qdarktheme.load_stylesheet())
    win.show()
    sys.exit(app.exec())