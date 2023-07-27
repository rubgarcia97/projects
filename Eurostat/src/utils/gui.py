import sys
import os

from PyQt6.QtWidgets import QApplication, QComboBox, QMainWindow, QPushButton, QTreeWidget
from PyQt6.QtGui import QScreen,QIcon
from PyQt6.QtWidgets import QLabel
from PyQt6.QtWidgets import QWidget

from client import EurostatAPIClient, GUIToolkit


class MainWindow(QMainWindow):
    
    def __init__(self):

        super().__init__()

        self.setWindowTitle('Eurostat API Interface')
        self.setGeometry(100,100,700,350)

        window_width = self.width()
        window_height = self.height()

        label = QLabel('<h2>Welcome to the Data Source selector</h2>',self).adjustSize()


## Configuración del desplegable


        dropdown = QComboBox(self)
        dropdown.setMinimumWidth(200)

        repository = EurostatAPIClient().get_repository()
        dropdown.addItems(repository.keys())

        dropdown_width = dropdown.width()
        dropdown_height = dropdown.height()
        dropdown.move(round((window_width - dropdown_width) / 2), round((window_height - dropdown_height) / 2))
        dropdown.currentTextChanged.connect(lambda text: self.current_text(repository[text]))
        
## Configuración del boton "download" 

        button = QPushButton('Download',self)
        button_width = button.width()
        button.move(round((window_width - button_width) / 2),round((window_height - dropdown_height) / 2)+50)

        
        button.clicked.connect(self.download_database)

        self.selected_option = dropdown.currentText()





    def current_text(self, s):
        self.selected_option = s

    def push_button (self):
        pass

    def download_database(self):
        if self.selected_option is not None:

            print("------------INICIANDO DESCARGA-------------")

            try:
                 EurostatAPIClient().get_database(self.selected_option)
                 print("La descarga ha comenzando a ejecutarse correctamente")

            except Exception as e:
                print(f'Error al ejecutar la funcion de descarga: {str(e)}')
            




if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainWindow()
    app.setWindowIcon(QIcon('./assets/Ditto.png'))
    win.show()
    sys.exit(app.exec())

