
from zooAnimales.animal import Animal
from zooAnimales.mamifero import Mamifero
from zooAnimales.ave import Ave
from zooAnimales.reptil import Reptil
from zooAnimales.pez import Pez
from zooAnimales.anfibio import Anfibio

class Zoologico:
    def __init__(self, nombre=None, ubicacion=None):
        self.nombre = nombre
        self.ubicacion = ubicacion
        self.zonas = []

    def set_nombre(self, nombre):
        self.nombre = nombre

    def get_nombre(self):
        return self.nombre

    def set_ubicacion(self, ubicacion):
        self.ubicacion = ubicacion

    def get_ubicacion(self):
        return self.ubicacion

    def set_zonas(self, zonas):
        self.zonas = zonas

    def get_zona(self):
        return self.zonas

    def agregarZonas(self, zona):
        self.zonas.append(zona)

    def cantidad_total_animales(self):
        total_animales = 0
        for zona in self.zonas:
            total_animales += zona.cantidad_animales()
        return total_animales
