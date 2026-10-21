# Generic test code
import sys
import time
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget
from PySide6.QtCore import QThread, Signal, QTimer

# Thread
class FactorialThread(QThread):
    result_ready = Signal(object)

    def run(self):
        tic = time.perf_counter()
        result = 1
        for i in range(1, 100000):
            result *= i
        toc = time.perf_counter()
        self.result_ready.emit(toc - tic)

# Original
def calculate_factorial():
    tic = time.perf_counter()
    result = 1
    for i in range(1, 100000):
        result *= i
    toc = time.perf_counter()
    return toc - tic

class MainWindow(QMainWindow):
    def __init__(self, method):
        super().__init__()

        self.setWindowTitle("Prueba de Intefaz")
        self.resize(350, 300)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        self.current_method = method

        # --- WIDGETS ---
        self.lbl_tick = QLabel("GUI Ticks: 0", self)
        self.lbl_method = QLabel(f"Uso de Threads: {'Sí' if method else 'No'}")
        self.lbl_status = QLabel("Estado: Esperando para calcular")
        self.label = QLabel("") 
        
        self.button_calcular = QPushButton("1. Iniciar Cálculo Pesado")
        self.button_calcular.clicked.connect(self.on_button_click)

        # --- NUEVA ACTIVIDAD PARALELA ---
        self.contador_clics = 0
        self.lbl_clics = QLabel("Clics paralelos: 0")
        self.lbl_clics.setStyleSheet("color: blue; font-weight: bold;")
        
        self.button_interactivo = QPushButton("2. Presióname mientras calcula")
        self.button_interactivo.clicked.connect(self.on_interactivo_click)

        # --- AGREGAR AL LAYOUT ---
        layout.addWidget(self.lbl_tick)
        layout.addWidget(self.lbl_method)
        layout.addWidget(self.lbl_status)
        layout.addWidget(self.label)
        layout.addWidget(self.button_calcular)
        
        # Agregamos un separador visual simple
        layout.addWidget(QLabel("--------------------------------------------------"))
        
        layout.addWidget(self.lbl_clics)
        layout.addWidget(self.button_interactivo)

        # --- CONFIGURACIÓN DE HILOS Y TIMERS ---
        if self.current_method:
            self.thread = FactorialThread()
            self.thread.result_ready.connect(self.on_factorial_calculated)

        self.gui_timer = QTimer(self)
        self.gui_timer.timeout.connect(self.update_gui_tick)
        self.tick_count = 0
        self.gui_timer.start(100)

    # Función de la actividad paralela
    def on_interactivo_click(self):
        self.contador_clics += 1
        self.lbl_clics.setText(f"Clics: {self.contador_clics}")

    def update_gui_tick(self):
        self.tick_count += 1
        self.lbl_tick.setText(f"GUI Ticks: {self.tick_count}")

    def on_button_click(self):
        self.button_calcular.setEnabled(False)
        self.label.setText("Calculando...")
        self.lbl_status.setText("Estado: Trabajando...")

        if self.current_method:
            self.thread.start()
        else:
            sys.set_int_max_str_digits(500000)
            QApplication.processEvents()
            
            tiempo = calculate_factorial()
            
            self.label.setText(f"¡Cálculo finalizado exitosamente!\nTomó: {tiempo:.4f} segundos")
            self.lbl_status.setText("Estado: Terminado")
            self.button_calcular.setEnabled(True)
    
    def on_factorial_calculated(self, result):
        self.label.setText(f"¡Cálculo finalizado exitosamente!\nTomó: {result:.4f} segundos")
        self.lbl_status.setText("Estado: Terminado")
        self.button_calcular.setEnabled(True)

if __name__ == "__main__":
    # ¡Prueba cambiando esto a False y luego a True!
    qthread_status = True
    
    app = QApplication(sys.argv)
    window = MainWindow(qthread_status)
    window.show()
    sys.exit(app.exec())