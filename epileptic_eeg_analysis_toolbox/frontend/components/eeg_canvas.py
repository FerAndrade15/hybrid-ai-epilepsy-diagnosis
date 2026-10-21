"""
# File: eeg_canvas.py
# Project: Trabajo de graduación
# Author: Maria Fernanda Andrade Recinos
# 
# Interactive canvas for high performace EEG visualization and annotation.
"""
from typing import List, Optional, Tuple, Dict, Any
import numpy as np
import pyqtgraph as pg
from PySide6.QtCore import Qt, Signal
from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QComboBox

class EEGCanvas(QWidget):
    """
    EEGCanvas is a QWidget that provides an interactive canvas for high-performance EEG visualization and annotation.
    It allows users to visualize EEG signals, annotate events, and interact with the data in real-time.
    """
    # Signal emitted when an annotation is added
    annotation_added = Signal(str, float, float)  # event_type, start_time, end_time

    # Signal emitted when the time cursor is changed
    time_cursor_changed = Signal(float)

    def __init__(self, parent: Optional[QWidget] = None, color_sheet: Dict[str, Any] = None):
        super().__init__(parent)
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)

        # Graphics view for EEG visualization
        self.plot_widget = pg.PlotWidget()

        # Vertical zoom lock
        self.plot_widget.setMouseEnabled(x=True, y=False)
        layout.addWidget(self.plot_widget)

        # Interactive time line
        self.cursor_line = pg.InfiniteLine(
            angle=90, 
            movable=True, 
            pen=pg.mkPen(color='r', width=1)
        )
        self.cursor_line.sigPositionChanged.connect(self._on_cursor_moved)
        self.plot_widget.addItem(self.cursor_line)

        self._n_channels: int = 0
        self._sfreq: float = 256.0
        self._spacing: float = 150.0        # uV spacing between channels
        self._visible_channels: int = 16
        self._top_channel_idx: int = 0
        self.curves: List[pg.PlotDataItem] = []

        # Default visualization
        y_axis = self.plot_widget.getAxis('left')
        y_axis.setLabel('Canales')
        x_axis = self.plot_widget.getAxis('bottom')
        x_axis.setLabel('Tiempo', units='s')
        self.plot_widget.setXRange(0.0, 10.0, padding=0.0)
        y_min = -self._spacing * 0.0
        y_max = self._n_channels * self._spacing

        self.apply_theme(color_sheet)

        # Keyboard reaction
        self.setFocusPolicy(Qt.StrongFocus)

    def apply_theme(self, color_sheet: Dict[str, Any] = None):
        self.color_sheet = color_sheet
        self.plot_widget.setBackground(self.color_sheet.get("plot_background", "#FFFFFF"))
        for curve in self.curves:
            curve.setPen(pg.mkPen(color=self.color_sheet.get("plot_lines", "k")), width=1)
        self.plot_widget.showGrid(x=True, y=True, alpha=self.color_sheet.get("alpha_lines", "k"))
        

    def load_signals(
            self, 
            signal_matrix: np.ndarray,
            ch_names: List[str],
            sfreq: float = 256.0,
            scale_uv: float = 150.0,
            initial_window_secs: float = 10.0
        ) -> None:
        """
        Loads EEG signals into the canvas for visualization.

        Args:
            signal_matrix (np.ndarray): 2D array of shape (n_channels, n_samples) containing EEG signals.
            ch_names (List[str]): List of channel names corresponding to the rows of signal_matrix.
            sfreq (float): Sampling frequency of the EEG signals in Hz. Default is 256.0.
            scale_uv (float): Vertical spacing between channels in microvolts. Default is 150.0.
            initial_window_secs (float): Initial time window to display in seconds. Default is 10.0.
        """
        self.plot_widget.clear()
        self.plot_widget.addItem(self.cursor_line)
        self.signal_matrix = signal_matrix
        self.ch_names = ch_names
        self.sfreq = sfreq

        self._n_channels, n_samples = signal_matrix.shape
        total_duration_sec = n_samples / sfreq
        print("[DEBUG] Tiempo registrado / calculado:", total_duration_sec)

        time_axis = np.linspace(0, total_duration_sec, n_samples)
        self._spacing = scale_uv
        ticks_y = []

        # PyQtGraph optimization
        self.curves = []
        self.plot_widget.setDownsampling(mode='peak')
        self.plot_widget.setClipToView(True)
        
        for idx in range(self._n_channels):
            baseline_y = (self._n_channels - 1 - idx) * self._spacing
            trace_data = signal_matrix[idx, :] + baseline_y

            curve_item = self.plot_widget.plot(
                time_axis,
                trace_data,
                pen=pg.mkPen(color="#1E293B", width=1.0)
            )
            self.curves.append(curve_item)
            ticks_y.append((baseline_y, ch_names[idx]))

        self._visible_channels = self._n_channels
        self._top_channel_idx = 0

        y_axis = self.plot_widget.getAxis('left')
        y_axis.setTicks([ticks_y])
        y_axis.setLabel('Derivación / Canal')

        x_axis = self.plot_widget.getAxis('bottom')
        x_axis.setLabel('Tiempo', units='s')
        self.plot_widget.setXRange(0.0, min(10.0, total_duration_sec), padding=0.0)

        self.plot_widget.setLimits(xMin=0.0, xMax=total_duration_sec)
        
        y_min = -0.5 * self._spacing
        y_max = (self._n_channels -0.5) * self._spacing
        self.plot_widget.setYRange(y_min, y_max, padding=0.00)
        self.plot_widget.enableAutoRange(axis='x', enable=False)
        self.plot_widget.setMouseEnabled(
            x=True, y=False
        )

    def jump_to_timestamp(
            self,
            start_time: float,
            window_span: float = 10.0
        ) -> None:
        self.plot_widget.setXRange(start_time, start_time + window_span, padding=0.0)
        self.cursor_line.setValue(start_time)

    def fit_all_channels(self) -> None:
        if self._n_channels == 0:
            return
        self._top_channel_idx = 0
        self._visible_channels = self._n_channels
        self._update_vertical_window()
    
    def set_visible_channels_count(self, count: int) -> None:
        self._visible_channels = max(1, min(count, self._n_channels))
        self._update_vertical_window()

    def _update_vertical_window(self) -> None:
        if self._n_channels == 0:
            return
        
        bottom_idx = min(self._top_channel_idx + self._visible_channels, self._n_channels) - 1        
        y_top = (self._n_channels - 1 - self._top_channel_idx) * self._spacing
        y_bottom = (self._n_channels - 1 - bottom_idx) * self._spacing

        pad = self._spacing * 0.8
        self.plot_widget.setYRange(y_bottom - pad, y_top + pad, padding=0.0)

    def scroll_to_channel(self, top_channel_idx: int) -> None:
        max_top = max(0, self._n_channels - self._visible_channels)
        self._top_channel_idx = max(0, min(top_channel_idx, max_top))
        self._update_vertical_window()

    def _on_cursor_moved(self) -> None:
        """
        Slot called when the cursor line is moved. Emits the current timestamp of the cursor.
        """
        current_time = self.cursor_line.value()
        self.time_cursor_changed.emit(current_time)

    def toggle_channel_visibility(self, ch_idx: int, visible: bool) -> None:
        if hasattr(self, 'curves') and 0 <= ch_idx < len(self.curves):
            self.curves[ch_idx].setVisible(visible)

    def keyPressEvent(self, event) -> None:
        try:
            view_x = self.plot_widget.viewRange()[0]
            x_min, x_max = view_x[0], view_x[1]
            window_span = x_max - x_min
            step = window_span * 0.2
            max_duration = self.signal_matrix.shape[1] / self.sfreq if hasattr(self, 'signal_matrix') else float('inf')
            print(max_duration)

            if event.key() == Qt.Key_Right and x_max != max_duration:
                #print("[DEBUG] > Recognized")
                self.plot_widget.setXRange(x_min + step, x_max + step, padding=0.0)
                self.cursor_line.setValue(self.cursor_line.value() + step)
            elif event.key() == Qt.Key_Left and x_min != 0:
                #print("[DEBUG] < Recognized")
                self.plot_widget.setXRange(x_min - step, x_max - step, padding=0.0)
                self.cursor_line.setValue(self.cursor_line.value() - step)
        except:
            pass

    def draw_ai_events(self, events: List[Dict[str, Any]]) -> None:
        if not hasattr(self, 'ai_regions'):
            self.ai_regions = []

        for region in self.ai_regions:
            self.plot_widget.removeItem(region)
        self.ai_regions.clear()
        for event in events:
            start = event["start_time"]
            end = event["stop_time"]

            region = pg.LinearRegionItem(values=[start, end], brush=(255,0,0,50))
            region.lines[0].setPen(pg.mkPen(None))
            region.lines[1].setPen(pg.mkPen(None))

            self.plot_widget.addItem(region)
            self.ai_regions.append(region)

    def set_ai_regions_visibility(self, visible: bool):
        if hasattr(self, 'ai_regions'):
            for region in self.ai_regions:
                region.setVisible(visible)


if __name__ == "__main__":
    import sys
    from PySide6.QtWidgets import QApplication, QMainWindow
    app = QApplication(sys.argv)
    
    # Ventana mínima para probarlo
    win = QMainWindow()
    win.setWindowTitle("Smoke Test: EEG Canvas")
    win.resize(1100, 700)
    
    canvas = EEGCanvas(win)
    win.setCentralWidget(canvas)
    
    # Cargar datos sintéticos rápidos
    sfreq = 256.0
    samples = int(sfreq * 30.0)
    time = np.arange(samples) / sfreq
    ch_names = ["FP1-F7", "F7-T3", "T3-T5", "T5-O1", "FP2-F8", "F8-T4", "T4-T6", "T6-O2"]
    
    # Señal senoidal con ruido
    test_data = np.array([50.0 * np.sin(2 * np.pi * (8 + i) * time) for i in range(len(ch_names))])
    canvas.load_signals(test_data, ch_names, sfreq=sfreq, scale_uv=120.0)
    
    win.show()
    sys.exit(app.exec())