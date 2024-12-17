class Zona():

    def __init__(self, nombre, zoo=None):
        self._nombre = nombre
        self._zoo = zoo
        self._animales = []
    
    def getNombre(self):
        return self._nombre
    
    def setNombre(self, nuevoNombre):
        self._nombre = nuevoNombre

    def getZoo(self):
        return self._zoo
    
    def setZoo(self, nuevoZoo):
        self._zoo = nuevoZoo

    def getAnimales(self):  
        return self._animales

    def agregarAnimales(self, nuevoAnimal):
        self._animales.append(nuevoAnimal)

    def cantidadAnimales(self):
        return len(self._animales)
    
