import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QPushButton, QFileDialog, QLabel, QWidget, QToolBar
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt, QSize
import logic
from excepciones import IdiomaNoSoportadoError, ModeloNoEncontradoError  # Remove the dot prefix

class AplicacionGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.tema_actual = "light"
        self.language = "english"

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

        # Botón para seleccionar archivo
        layout_archivo = QHBoxLayout()
        boton_seleccionar = QPushButton("Seleccionar archivo")
        boton_seleccionar.clicked.connect(self.seleccionar_archivo)
        self.etiqueta_archivo = QLabel("No hay archivo seleccionado")
        layout_archivo.addWidget(boton_seleccionar)
        layout_archivo.addWidget(self.etiqueta_archivo)
        layout_principal.addLayout(layout_archivo)


        # Botones de acción
        layout_acciones = QHBoxLayout()
        boton_contar = QPushButton("Contar tokens")
        boton_contar.clicked.connect(self.contar_tokens)
        boton_dividir = QPushButton("Dividir texto")
        boton_dividir.clicked.connect(self.dividir_texto)
        layout_acciones.addWidget(boton_contar)
        layout_acciones.addWidget(boton_dividir)
        layout_principal.addLayout(layout_acciones)

        # Etiqueta de tokens
        self.etiqueta_tokens = QLabel("Tokens: ")
        layout_principal.addWidget(self.etiqueta_tokens)

    def seleccionar_archivo(self):
        archivo, _ = QFileDialog.getOpenFileName(self, "Seleccionar archivo", "", "Archivos de Texto (*.txt)")
        if archivo:
            self.etiqueta_archivo.setText(archivo.split('/')[-1])
            with open(archivo, 'r', encoding='utf-8') as f:
                self.text_content = f.read()

    def detectar_idioma(self):
        try:
            token_count, _ = logic.count_tokens(self.text_content, "spanish")
            self.language = "spanish"
        except IdiomaNoSoportadoError:
            try:
                token_count, _ = logic.count_tokens(self.text_content, "english")
                self.language = "english"
            except IdiomaNoSoportadoError:
                self.etiqueta_tokens.setText("Idioma no soportado")

    def contar_tokens(self):
        try:
            token_count, _ = logic.count_tokens(self.text_content, self.language)
            self.etiqueta_tokens.setText(f"Tokens: {token_count}")
        except (IdiomaNoSoportadoError, AttributeError):
            self.etiqueta_tokens.setText("Selecciona un archivo e idioma válidos.")

    def dividir_texto(self):
        try:
            partes = logic.divide_text(self.text_content, 7500, self.language)
            for i, parte in enumerate(partes):
                with open(f"output_parte_{i+1}.txt", "w", encoding="utf-8") as f:
                    f.write(parte)
            self.etiqueta_tokens.setText("Texto dividido y guardado.")
        except (IdiomaNoSoportadoError, AttributeError):
            self.etiqueta_tokens.setText("Selecciona un archivo e idioma válidos.")

    def cambiar_tema(self):
        if self.tema_actual == "light":
            self.tema_actual = "dark"
            self.boton_tema.setIcon(QIcon("resources/sun.png"))
            self.setStyleSheet("background-color: #333; color: #f5f5f5;")
        else:
            self.tema_actual = "light"
            self.boton_tema.setIcon(QIcon("resources/moon.png"))
            self.setStyleSheet("background-color: #f5f5f5; color: #333;")
