import sys

from PyQt6.QtWidgets import QApplication, QComboBox, QMainWindow
from PyQt6.QtGui import QScreen
from PyQt6.QtWidgets import QLabel
from PyQt6.QtWidgets import QWidget

from client import EurostatAPIClient


class MainWindow(QMainWindow):
    
    def __init__(self):

        super().__init__()

        self.setWindowTitle('Pruebas')
        self.setGeometry(100,100,700,350)

        label = QLabel('<h2>Probando mas cosas y mas y mas cosas</h2>',self).adjustSize()

        desplegable = QComboBox(self)
        desplegable.move(350,100)
        desplegable.addItems(EurostatAPIClient().get_repository())







if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec())

