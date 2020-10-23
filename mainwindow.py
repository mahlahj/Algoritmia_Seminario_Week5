from PySide2.QtWidgets import QMainWindow
from PySide2.QtCore import Slot
from ui_mainwindow import Ui_MainWindow
from particula import Particula
from organizador import Organizador

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.abInicio.clicked.connect(self.click_agregar_inicio)
        self.ui.abFinal.clicked.connect(self.click_agregar_final)
        self.ui.abMostrar.clicked.connect(self.click_mostrar)


    @Slot()
    def click_mostrar(self):
        self.ui.plainTextEditor.clear()
        self.ui.plainTextEditor.insertPlainText(str(self.click_agregar))
    
    @Slot()
    def click_agregar_inicio(self):
        id = self.ui.id.Text()
        origen_x = self.ui.origenX.value()
        origen_y = self.ui.origenY.value()
        destino_x = self.ui.destinoX.value()
        destino_y = self.ui.destinoY.value()
        velocidad = self.ui.velocidad.text()
        rojo = self.ui.rojo.value()
        verde = self.ui.verde.value()
        azul = self.ui.azul.value()

        particula = Particula(id, origen_x, origen_y, destino_x, destino_y, velocidad, rojo, verde, azul)
        self.Organizador.agregar_inicio(particula)

    @Slot()
    def click_agregar_final(self):
        id = self.ui.id.Text()
        origen_x = self.ui.origenX.value()
        origen_y = self.ui.origenY.value()
        destino_x = self.ui.destinoX.value()
        destino_y = self.ui.destinoY.value()
        velocidad = self.ui.velocidad.text()
        rojo = self.ui.rojo.value()
        verde = self.ui.verde.value()
        azul = self.ui.azul.value()

        particula = Particula(id, origen_x, origen_y, destino_x, destino_y, velocidad, rojo, verde, azul)
        self.Organizador.agregar_final(particula)