
from zooAnimales.animal import Animal

class Mamifero(Animal):
    listado = []
    caballos = 0
    leones = 0

    def __init__(self, nombre=None, edad=0, habitat=None, genero=None, pelaje=False, patas=0):
        super().__init__(nombre, edad, habitat, genero)
        self.pelaje = pelaje
        self.patas = patas
        Mamifero.listado.append(self)

    @classmethod
    def set_listado(cls, listado):
        cls.listado = listado

    @classmethod
    def get_listado(cls):
        return cls.listado

    def set_pelaje(self, pelaje):
        self.pelaje = pelaje

    def is_pelaje(self):
        return self.pelaje

    def set_patas(self, patas):
        self.patas = patas

    def get_patas(self):
        return self.patas

    def cantidad_mamiferos(self):
        return len(Mamifero.listado)

    @staticmethod
    def crearCaballo(nombre, edad, genero):
        mamifero = Mamifero(nombre, edad, "pradera", genero, True, 4)
        Mamifero.caballos += 1
        return mamifero

    @staticmethod
    def crearLeon(nombre, edad, genero):
        mamifero = Mamifero(nombre, edad, "selva", genero, True, 4)
        Mamifero.leones += 1
        return mamifero
