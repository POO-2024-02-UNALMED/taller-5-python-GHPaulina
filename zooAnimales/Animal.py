from zooAnimales.anfibio import Anfibio, Animal
from zooAnimales.ave import Animal, Ave
from zooAnimales.mamifero import Animal, Mamifero
from zooAnimales.pez import Animal, Pez
from zooAnimales.reptil import Animal, Reptil

class Animal:
    total_animales = 0

    def __init__(self, nombre=None, edad=0, habitat=None, genero=None):
        self.nombre = nombre
        self.edad = edad
        self.habitat = habitat
        self.genero = genero
        self.zona = None
        Animal.total_animales += 1

    @classmethod
    def set_total_animales(cls, total_animales):
        cls.total_animales = total_animales

    @classmethod
    def get_total_animales(cls):
        return cls.total_animales

    def set_nombre(self, nombre):
        self.nombre = nombre

    def get_nombre(self):
        return self.nombre

    def set_edad(self, edad):
        self.edad = edad

    def get_edad(self):
        return self.edad

    def set_habitat(self, habitat):
        self.habitat = habitat

    def get_habitat(self):
        return self.habitat

    def set_genero(self, genero):
        self.genero = genero

    def get_genero(self):
        return self.genero

    def set_zona(self, zona):
        self.zona = zona

    def get_zona(self):
        return self.zona

    def movimiento(self):
        return "desplazarse"

    @classmethod
    def total_por_tipo(cls):
        return f"Mamiferos: {len(Mamifero.listado)}\n" \
               f"Aves: {len(Ave.listado)}\n" \
               f"Reptiles: {len(Reptil.listado)}\n" \
               f"Peces: {len(Pez.listado)}\n" \
               f"Anfibios: {len(Anfibio.listado)}"

    def __str__(self):
        if self.get_zona() is not None:
            return f"Mi nombre es {self.get_nombre()}, tengo una edad de {self.get_edad()}, " \
                   f"habito en {self.get_habitat()} y mi genero es {self.get_genero()}, " \
                   f"la zona en la que me ubico es {self.get_zona().get_nombre()}, en el {self.get_zona().get_zoo().get_nombre()}"
        else:
            return f"Mi nombre es {self.get_nombre()}, tengo una edad de {self.get_edad()}, " \
                   f"habito en {self.get_habitat()} y mi genero es {self.get_genero()}"
