from PySide2.QtWidgets import QMainWindow, QFileDialog, QTableWidgetItem, QMessageBox
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

        self.ui.mostrar_tabla.clicked.connect(self.mostrar_tabla)
        self.ui.buscar.clicked.connect(self.buscar)

    @Slot()
    def buscar(self):
        print('buscar')
        texto = self.ui.lineEdit_buscar.text()
        libros = []
        for libro in self.libros:
            if texto == libro['autor']:
                libros.append(libro)

        if len(libros) == 0:
            QMessageBox.warning(self, "Libros", "No encontraron libros")
        else:
            self.libros_tabla(libros)


    def libros_tabla(self, libros):
        self.ui.tabla.clear()
        self.ui.tabla.setColumnCount(4)
        self.ui.tabla.setRowCount(len(libros))

        labels = ["Título", "Autor", "Año", "Editorial"]
        self.ui.tabla.setHorizontalHeaderLabels(labels)

        row = 0
        for libro in libros:
            titulo = libro['titulo']
            autor = libro['autor']
            year = libro['year']
            editorial = libro['editorial']

            titulo_item = QTableWidgetItem(titulo)
            autor_item = QTableWidgetItem(autor)
            year_item = QTableWidgetItem(str(year))
            editorial_item = QTableWidgetItem(editorial)

            self.ui.tabla.setItem(row, 0, titulo_item)
            self.ui.tabla.setItem(row, 1, autor_item)
            self.ui.tabla.setItem(row, 2, year_item)
            self.ui.tabla.setItem(row, 3, editorial_item)

            row += 1




    @Slot()
    def mostrar_tabla(self):
        print('mostrar')
        self.libros_tabla(self.libros)

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
        for libro in self.libros:
            self.ui.salida.insertPlainText("Título:" + libro['titulo'] + "\n")
            self.ui.salida.insertPlainText("Autor:" + libro['autor'] + "\n")
            self.ui.salida.insertPlainText("Año:" + str(libro['year']) + "\n")
            self.ui.salida.insertPlainText("Editorial:" + libro['editorial'] + "\n")