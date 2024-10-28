# gui.py
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QPushButton, QFileDialog, QLabel, QWidget, QToolBar
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt, QSize
from logic import dividir_archivo, count_tokens

class AplicacionGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.tema_actual = "light"

    def initUI(self):
        self.setGeometry(100, 100, 400, 300)
        self.setWindowTitle("DIVISOR DE ARCHIVOS DE TEXTO")
        self.setupToolbar()
        self.setupWidgets()

    def setupToolbar(self):
        toolbar = QToolBar(self)
        toolbar.setIconSize(QSize(20, 20))
        self.boton_tema = QPushButton()
        self.boton_tema.setIcon(QIcon("resources/moon.png"))
        self.boton_tema.clicked.connect(self.cambiar_tema)
        toolbar.addWidget(self.boton_tema)
        self.addToolBar(Qt.TopToolBarArea, toolbar)

    def setupWidgets(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout_principal = QVBoxLayout()
        central_widget.setLayout(layout_principal)

        layout_archivo = QHBoxLayout()
        boton_seleccionar = QPushButton("Seleccionar archivo")
        boton_seleccionar.clicked.connect(self.seleccionar_archivo)
        self.etiqueta_archivo = QLabel("No hay archivo seleccionado")
        layout_archivo.addWidget(boton_seleccionar)
        layout_archivo.addWidget(self.etiqueta_archivo)
        layout_principal.addLayout(layout_archivo)

        # Button for dividing the file
        boton_dividir = QPushButton("Dividir archivo")
        boton_dividir.clicked.connect(self.dividir_texto)
        layout_principal.addWidget(boton_dividir)

        # Button for counting tokens
        boton_contar = QPushButton("Contar tokens")
        boton_contar.clicked.connect(self.contar_tokens)
        layout_principal.addWidget(boton_contar)

        # Label for token count output
        self.etiqueta_tokens = QLabel("Tokens: ")
        layout_principal.addWidget(self.etiqueta_tokens)

    def seleccionar_archivo(self):
        archivo, _ = QFileDialog.getOpenFileName(self, "Seleccionar archivo", "", "Archivos de Texto (*.txt)")
        if archivo:
            self.etiqueta_archivo.setText(archivo.split('/')[-1])
            self.archivo = archivo

    def dividir_texto(self):
        if hasattr(self, 'archivo'):
            dividir_archivo(self.archivo)
            self.etiqueta_tokens.setText("Archivo dividido exitosamente.")
        else:
            self.etiqueta_tokens.setText("Selecciona un archivo para dividir.")

    def contar_tokens(self):
        if hasattr(self, 'archivo'):
            num_tokens = count_tokens(self.archivo)
            self.etiqueta_tokens.setText(f"Tokens: {num_tokens}")
        else:
            self.etiqueta_tokens.setText("Selecciona un archivo para contar los tokens.")

    def cambiar_tema(self):
        if self.tema_actual == "light":
            self.tema_actual = "dark"
            self.boton_tema.setIcon(QIcon("resources/sun.png"))
            self.setStyleSheet("background-color: #333; color: #f5f5f5;")
        else:
            self.tema_actual = "light"
            self.boton_tema.setIcon(QIcon("resources/moon.png"))
            self.setStyleSheet("background-color: #f5f5f5; color: #333;")
