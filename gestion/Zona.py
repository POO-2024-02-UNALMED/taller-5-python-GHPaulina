
from zooAnimales.animal import Animal
class Zona:
    def __init__(self, nombre=None, zoo=None):
        self.nombre = nombre
        self.zoo = zoo
        self.animales = []

    def set_nombre(self, nombre):
        self.nombre = nombre

    def get_nombre(self):
        return self.nombre

    def set_zoo(self, zoo):
        self.zoo = zoo

    def get_zoo(self):
        return self.zoo

    def set_animales(self, animales):
        self.animales = animales

    def get_animales(self):
        return self.animales

    def agregarAnimales(self, animal):
        self.animales.append(animal)

    def cantidad_animales(self):
        return len(self.animales)
