# main.py
import sys
from PyQt5.QtWidgets import QApplication
from gui import AplicacionGUI

def main():
    app = QApplication(sys.argv)
    ventana = AplicacionGUI()
    ventana.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
