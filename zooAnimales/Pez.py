from zooAnimales.animal import Animal
class Pez(Animal):
    listado = []
    salmones = 0
    bacalaos = 0

    def __init__(self, nombre=None, edad=0, habitat=None, genero=None, color_escamas=None, cantidad_aletas=0):
        super().__init__(nombre, edad, habitat, genero)
        self.color_escamas = color_escamas
        self.cantidad_aletas = cantidad_aletas
        Pez.listado.append(self)

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

    def set_cantidad_aletas(self, cantidad_aletas):
        self.cantidad_aletas = cantidad_aletas

    def get_cantidad_aletas(self):
        return self.cantidad_aletas

    def cantidad_peces(self):
        return len(Pez.listado)

    def movimiento(self):
        return "nadar"

    @staticmethod
    def crearSalmon(nombre, edad, genero):
        pez = Pez(nombre, edad, "oceano", genero, "rojo", 6)
        Pez.salmones += 1
        return pez

    @staticmethod
    def crearBacalao(nombre, edad, genero):
        pez = Pez(nombre, edad, "oceano", genero, "gris", 6)
        Pez.bacalaos += 1
        return pez
