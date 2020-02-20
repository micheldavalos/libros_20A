from PySide2.QtWidgets import QMainWindow, QFileDialog
from ui_mainwindow import Ui_MainWindow
from PySide2.QtCore import Slot
import json

class MainWindow(QMainWindow):
    libros = []
    def __init__(self):
        super(MainWindow, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.agregar.clicked.connect(self.agregar)
        self.ui.mostrar.clicked.connect(self.mostrar)

        self.ui.actionGuardar.triggered.connect(self.guardar)
        self.ui.actionAbrir.triggered.connect(self.abrir)

    @Slot()
    def abrir(self):
        ubicacion = QFileDialog.getOpenFileName(self, "Abrir libros", ".", "JSON (*.json)")

        with open(ubicacion[0], 'r') as archivo:
            self.libros = json.load(archivo)

    @Slot()
    def guardar(self):
        ubicacion = QFileDialog.getSaveFileName(self, "Guardar libros", ".", "JSON (*.json)")
        print(ubicacion)

        with open(ubicacion[0], 'w') as archivo:
            json.dump(self.libros, archivo, indent=5)

        # with open(ubicacion[0], 'w') as archivo:
        #     for libro in self.libros:
        #         archivo.write(libro['titulo']+'\n')
        #         archivo.write(libro['autor']+'\n')
        #         archivo.write(str(libro['year'])+'\n')
        #         archivo.write(libro['editorial']+'\n')

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