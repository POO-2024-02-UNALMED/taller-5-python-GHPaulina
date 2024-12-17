from zooAnimales.animal import Animal
class Ave(Animal):
    listado = []
    halcones = 0
    aguilas = 0

    def __init__(self, nombre=None, edad=0, habitat=None, genero=None, color_plumas=None):
        super().__init__(nombre, edad, habitat, genero)
        self.color_plumas = color_plumas
        Ave.listado.append(self)

    @classmethod
    def set_listado(cls, listado):
        cls.listado = listado

    @classmethod
    def get_listado(cls):
        return cls.listado

    def set_color_plumas(self, color_plumas):
        self.color_plumas = color_plumas

    def get_color_plumas(self):
        return self.color_plumas

    def cantidad_aves(self):
        return len(Ave.listado)

    def movimiento(self):
        return "volar"

    @staticmethod
    def crearHalcon(nombre, edad, genero):
        ave = Ave(nombre, edad, "montanas", genero, "cafe glorioso")
        Ave.halcones += 1
        return ave

    @staticmethod
    def crearAguila(nombre, edad, genero):
        ave = Ave(nombre, edad, "montanas", genero, "blanco y amarillo")
        Ave.aguilas += 1
        return ave
