from zooAnimales.animal import Animal
class Anfibio(Animal):
    listado = []
    ranas = 0
    salamandras = 0

    def __init__(self, nombre=None, edad=0, habitat=None, genero=None, color_piel=None):
        super().__init__(nombre, edad, habitat, genero)
        self.color_piel = color_piel
        Anfibio.listado.append(self)

    @classmethod
    def set_listado(cls, listado):
        cls.listado = listado

    @classmethod
    def get_listado(cls):
        return cls.listado

    def set_color_piel(self, color_piel):
        self.color_piel = color_piel

    def get_color_piel(self):
        return self.color_piel

    def cantidad_anfibios(self):
        return len(Anfibio.listado)

    def movimiento(self):
        return "saltar"

    @staticmethod
    def crearRana(nombre, edad, genero):
        anfibio = Anfibio(nombre, edad, "humedal", genero, "verde")
        Anfibio.ranas += 1
        return anfibio

    @staticmethod
    def crearSalamandra(nombre, edad, genero):
        anfibio = Anfibio(nombre, edad, "bosque", genero, "amarillo")
        Anfibio.salamandras += 1
        return anfibio
