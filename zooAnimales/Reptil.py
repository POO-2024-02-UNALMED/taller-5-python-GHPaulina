from zooAnimales.animal import Animal
class Reptil(Animal):
    listado = []
    iguanas = 0
    serpientes = 0

    def __init__(self, nombre=None, edad=0, habitat=None, genero=None, color_escamas=None, largo_cola=0):
        super().__init__(nombre, edad, habitat, genero)
        self.color_escamas = color_escamas
        self.largo_cola = largo_cola
        Reptil.listado.append(self)

    @classmethod
    def set_listado(cls, listado):
        cls.listado = listado

    @classmethod
    def get_listado(cls):
        return cls.listado

    def set_color_escamas(self, color_escamas):
        self.color_escamas = color_escamas

    def get_color_escamas(self):
        return self.color_escamas

    def set_largo_cola(self, largo_cola):
        self.largo_cola = largo_cola

    def get_largo_cola(self):
        return self.largo_cola

    def cantidad_reptiles(self):
        return len(Reptil.listado)

    def movimiento(self):
        return "reptar"

    @staticmethod
    def crearIguana(nombre, edad, genero):
        reptil = Reptil(nombre, edad, "humedal", genero, "verde", 3)
        Reptil.iguanas += 1
        return reptil

    @staticmethod
    def crearSerpiente(nombre, edad, genero):
        reptil = Reptil(nombre, edad, "jungla", genero, "blanco", 1)
        Reptil.serpientes += 1
        return reptil
