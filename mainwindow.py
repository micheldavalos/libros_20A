from PySide2.QtWidgets import QMainWindow
from ui_mainwindow import Ui_MainWindow
from PySide2.QtCore import Slot

class MainWindow(QMainWindow):
    libros = []
    def __init__(self):
        super(MainWindow, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.agregar.clicked.connect(self.agregar)
        self.ui.mostrar.clicked.connect(self.mostrar)

    @Slot()
    def agregar(self):
        titulo = self.ui.titulo.text()
        autor = self.ui.autor.text()
        year = self.ui.year.value()
        editorial = self.ui.editorial.text()

        # print(titulo, autor, year, editorial)
        libro = {
            'titulo': titulo,
            'autor': autor,
            'year': year,
            'editorial': editorial
        }
        #print(libro)
        self.libros.append(libro)

    @Slot()
    def mostrar(self):
        for libro in self.libros:
            print(libro)