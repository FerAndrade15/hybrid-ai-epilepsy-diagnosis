"""
# File: event_panel.py
# Project: Trabajo de graduación
# Author: Maria Fernanda Andrade Recinos

Structure and data process for the creation of the panel
with the results/identification of events.
"""
from typing import List, Dict, Any, Optional
from PySide6.QtCore import Qt, Signal
from PySide6.QtWidgets import (
    QAbstractItemView, QWidget, QVBoxLayout, QHBoxLayout, QTableWidget,
    QTableWidgetItem, QHeaderView, QLabel, QLineEdit
)

# Event panel
class EventPanel(QWidget):
    event_selected = Signal(float)

    def __init__(self, parent: Optional[QWidget] = None):
        super().__init__(parent)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(6, 6, 6, 6)
        layout.setSpacing(6)

        # Bar
        header_layout = QHBoxLayout()
        self.lbl_count = QLabel("Eventos detectados: 0")
        self.lbl_count.setStyleSheet("lblCount")
        header_layout.addWidget(self.lbl_count)

        self.txt_filter = QLineEdit()
        self.txt_filter.setPlaceholderText("Filtrar (ej, SPWS, eyeb ...)")
        self.txt_filter.textChanged.connect(self._apply_filter)
        header_layout.addWidget(self.txt_filter)
        layout.addLayout(header_layout)

        # Events table
        self.table = QTableWidget(0, 5)
        self.table.setHorizontalHeaderLabels([
            "Inicio (s)", "Duración (s)", "Canal", "Tipo", "Confianza"
        ])

        # Visualization
        self.table.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.table.setSelectionMode(QTableWidget.SingleSelection)
        self.table.setAlternatingRowColors(True)
        self.table.setEditTriggers(QTableWidget.NoEditTriggers)

        # Proporcionated columns
        header = self.table.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(1, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(2, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(3, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(4, QHeaderView.ResizeToContents)

        self.table.cellClicked.connect(self._on_row_clicked)
        layout.addWidget(self.table)

        self._raw_events: List[Dict[str, Any]] = []

    def set_events(self, events: List[Dict[str, Any]]) -> None:
        self._raw_events = events
        self.table.setRowCount(0)
        self.lbl_count.setText(f"Eventos detectados: {len(events)}")

        for row_idx, ev in enumerate(events):
            self.table.insertRow(row_idx)

            # Cell format
            start_val = ev.get("start", ev.get("start_time", 0.0))
            dur_val = ev.get("duration", ev.get("stop_time", start_val) - start_val)
            ch_val = str(ev.get("channel", "Todos / Global"))
            label_val = str(ev.get("type", ev.get("label", "Desconocido")))

            conf = ev.get("confidence", ev.get("prob", None))
            conf_str = f"{conf * 100:.1f}%" if conf is not None else "N/A"

            item_start = QTableWidgetItem(f"{float(start_val):.2f}")
            item_dur = QTableWidgetItem(f"{float(dur_val):.2f}")
            item_ch = QTableWidgetItem(ch_val)
            item_label = QTableWidgetItem(label_val)
            item_conf = QTableWidgetItem(conf_str)

            # Aligment
            item_start.setTextAlignment(Qt.AlignCenter)
            item_dur.setTextAlignment(Qt.AlignCenter)
            item_conf.setTextAlignment(Qt.AlignCenter)

            self.table.setItem(row_idx, 0, item_start)
            self.table.setItem(row_idx, 1, item_dur)
            self.table.setItem(row_idx, 2, item_ch)
            self.table.setItem(row_idx, 3, item_label)
            self.table.setItem(row_idx, 4, item_conf)

    def clear_events(self) -> None:
        """Clean table content"""
        self._raw_events = []
        self.table.setRowCount(0)
        self.lbl_count.setText("Eventos detectados: 0")

    def _on_row_clicked(self, row: int, column: int) -> None:
        """Start and time stamp of event"""
        item = self.table.item(row, 0)
        if item:
            try:
                start_sec = float(item.text())
                self.event_selected.emit(start_sec)
            except ValueError:
                pass

    def _apply_filter(self, text: str) -> None:
        """Hide not matched results in the searching"""
        query = text.lower().strip()
        for row in range(self.table.rowCount()):
            match = False
            for col in range(self.table.columnCount()):
                cell = self.table.item(row, col)
                if cell and query in cell.text().lower():
                    match = True
                    break
            self.table.setRowHidden(row, not match)


if __name__ == "__main__":
    import sys
    from PySide6.QtWidgets import QApplication, QMainWindow

    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setWindowTitle("Prueba Aislada: Panel de Eventos Clínicos")
    win.resize(600, 400)

    panel = EventPanel(win)
    win.setCentralWidget(panel)

    # Datos clínicos sintéticos para verificar el poblado
    mock_events = [
        {"start": 4.25, "duration": 1.5, "channel": "FP1-F3", "type": "eyeb", "confidence": 0.95},
        {"start": 14.80, "duration": 0.8, "channel": "C3-P3", "type": "SPSW", "confidence": 0.88},
        {"start": 27.10, "duration": 3.2, "channel": "T3-T5", "type": "SEIZ", "confidence": 0.91},
        {"start": 38.60, "duration": 2.0, "channel": "F7-T3", "type": "musc", "confidence": 0.79}
    ]
    panel.set_events(mock_events)
    panel.event_selected.connect(lambda t: print(f"[Salto Solicitado] Navegar a t = {t} s"))

    win.show()
    sys.exit(app.exec())