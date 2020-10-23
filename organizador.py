from particula import Particula

class Organizador:
    def __init__(self):
        self.organizador = []

    def agregar_inicio(self, part):
        self.organizador.insert(0,part)

    def agregar_final(self, part):
        self.organizador.append(part)

    def mostrar(self):
        for i in self.organizador:
            print(i)