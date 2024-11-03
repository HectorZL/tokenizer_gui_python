import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QPushButton, QFileDialog, QLabel, QWidget, QToolBar, QLineEdit
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt, QSize
from logic import dividir_archivo, count_tokens

class AplicacionGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.tema_actual = "dark"  # Tema por defecto
        self.initUI()
        
    def initUI(self):
        self.setGeometry(100, 100, 400, 300)
        self.setWindowTitle("DIVISOR DE ARCHIVOS DE TEXTO")
        self.setupToolbar()
        self.setupWidgets()
        self.cambiar_tema()  # Establecer tema predeterminado

    def setupToolbar(self):
        toolbar = QToolBar(self)
        toolbar.setIconSize(QSize(20, 20))
        self.boton_tema = QPushButton()
        self.boton_tema.setIcon(QIcon("resources/sun.png"))
        self.boton_tema.clicked.connect(self.cambiar_tema)
        toolbar.addWidget(self.boton_tema)
        self.addToolBar(Qt.TopToolBarArea, toolbar)

    def setupWidgets(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout_principal = QVBoxLayout()
        central_widget.setLayout(layout_principal)

        # Sección de selección de archivo
        layout_archivo = QHBoxLayout()
        boton_seleccionar = QPushButton("SELECCIONAR ARCHIVO")
        boton_seleccionar.clicked.connect(self.seleccionar_archivo)
        self.etiqueta_archivo = QLabel("NO HAY ARCHIVO SELECCIONADO")
        layout_archivo.addWidget(boton_seleccionar)
        layout_archivo.addWidget(self.etiqueta_archivo)
        layout_principal.addLayout(layout_archivo)

        # Input para contar tokens por archivo
        layout_tokens = QHBoxLayout()
        self.input_tokens = QLineEdit()
        self.input_tokens.setPlaceholderText("TOKENS POR ARCHIVO (ej. 512)")
        layout_tokens.addWidget(self.input_tokens)
        layout_principal.addLayout(layout_tokens)

        # Botón para dividir el archivo
        boton_dividir = QPushButton("DIVIDIR ARCHIVO")
        boton_dividir.clicked.connect(self.dividir_texto)
        layout_principal.addWidget(boton_dividir)

        # Botón para contar tokens
        boton_contar = QPushButton("CONTAR TOKENS")
        boton_contar.clicked.connect(self.contar_tokens)
        layout_principal.addWidget(boton_contar)

        # Etiqueta para salida del conteo de tokens
        self.etiqueta_tokens = QLabel("TOKENS: ")
        layout_principal.addWidget(self.etiqueta_tokens)

    def seleccionar_archivo(self):
        archivo, _ = QFileDialog.getOpenFileName(self, "Seleccionar archivo", "", "Archivos de Texto (*.txt)")
        if archivo:
            self.etiqueta_archivo.setText(archivo.split('/')[-1])
            self.archivo = archivo

    def dividir_texto(self):
        if hasattr(self, 'archivo'):
            tokens_por_archivo = int(self.input_tokens.text()) if self.input_tokens.text().isdigit() else 512
            dividir_archivo(self.archivo, tokens_por_archivo=tokens_por_archivo)
            self.etiqueta_tokens.setText("ARCHIVO DIVIDIDO EXITOSAMENTE.")
        else:
            self.etiqueta_tokens.setText("SELECCIONA UN ARCHIVO PARA DIVIDIR.")

    def contar_tokens(self):
        if hasattr(self, 'archivo'):
            num_tokens = count_tokens(self.archivo)
            self.etiqueta_tokens.setText(f"TOKENS: {num_tokens}")
        else:
            self.etiqueta_tokens.setText("SELECCIONA UN ARCHIVO PARA CONTAR LOS TOKENS.")

    def cambiar_tema(self):
        if self.tema_actual == "light":
            self.tema_actual = "dark"
            self.boton_tema.setIcon(QIcon("resources/sun.png"))
            self.setStyleSheet("""
                background-color: #121212; 
                color: #E0E0E0; 
                QPushButton { background-color: #BB86FC; color: #121212; font-weight: bold; }
            """)
        else:
            self.tema_actual = "light"
            self.boton_tema.setIcon(QIcon("resources/moon.png"))
            self.setStyleSheet("""
                background-color: #FFFFFF; 
                color: #000000; 
                QPushButton { background-color: #6200EE; color: #FFFFFF; font-weight: bold; }
            """)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = AplicacionGUI()
    ventana.show()
    sys.exit(app.exec_())
