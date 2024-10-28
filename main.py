import sys
from PyQt5.QtWidgets import QApplication
from gui import AplicacionGUI

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = AplicacionGUI()
    ventana.show()
    sys.exit(app.exec_())
