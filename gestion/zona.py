class Zona():
    
    def __init__(self, nombre, zoo=None):
        self._nombre = nombre
        self._zoo = zoo  # Asegúrate de que el zoológico asociado se maneje correctamente
        self._animales = []  # Lista de animales en esta zona

    def cantidadAnimales(self):
        return len(self._animales)  # Devuelve el número de animales en la zona

    def agregarAnimales(self, nuevoAnimal):
        if nuevoAnimal not in self._animales:
            self._animales.append(nuevoAnimal)  # Agrega un animal solo si no está repetido

    def getNombre(self):
        return self._nombre

    def setNombre(self, nuevoNombre):
        self._nombre = nuevoNombre

    def getZoo(self):
        return self._zoo  # Devuelve el zoológico asociado a esta zona

    def setZoo(self, nuevoZoo):
        self._zoo = nuevoZoo  # Establece un nuevo zoológico para esta zona

    def getAnimales(self):
        return self._animales  # Devuelve la lista de animales de la zona

