class Animal():

    _totalAnimales = 0

    # Constructor que inicializa los atributos básicos de cada animal.
    def __init__(self, nombre, edad, habitat, genero, zona = None):
        self._nombre = nombre
        self._edad = edad
        self._habitat = habitat
        self._genero = genero
        self._zona = zona
        Animal._totalAnimales += 1

    # Métodos para acceder a los atributos del animal.
    def getNombre(self):
        return self._nombre
    
    def setNombre(self, nuevoNombre):
        self._nombre = nuevoNombre

    def getEdad(self):
        return self._edad
    
    def setEdad(self, nuevaEdad):
        self._edad = nuevaEdad

    def getHabitat(self):
        return self._habitat
    
    def setHabitat(self, nuevaHabitat):
        self._habitat = nuevaHabitat
    
    def getGenero(self):
        return self._genero
    
    def setGenero(self, nuevoGenero):
        self._genero = nuevoGenero

    def setZona(self, nuevaZona):
        self._zona = nuevaZona
    
    def getZona(self):
        return self._zona
    
    # Método que devuelve la cantidad total de animales por tipo.
    @classmethod
    def totalPorTipo(cls):
        from .mamifero import Mamifero
        from .ave import Ave
        from .reptil import Reptil
        from .pez import Pez
        from .anfibio import Anfibio
        return "Mamiferos : " + str(Mamifero.cantidadMamiferos()) + "\n" + \
               "Aves : " + str(Ave.cantidadAves()) + "\n" + \
               "Reptiles : " + str(Reptil.cantidadReptiles()) + "\n" + \
               "Peces : " + str(Pez.cantidadPeces()) + "\n" + \
               "Anfibios : " + str(Anfibio.cantidadAnfibios())

    # Método para representar los detalles del animal en una cadena.
    def toString(self):
        if self.getZona() is None:
            return f"Mi nombre es {self.getNombre()}, tengo una edad de {self.getEdad()}, habito en {self.getHabitat()} y mi genero es {self.getGenero()}"
        else:
            return f"Mi nombre es {self.getNombre()}, tengo una edad de {self.getEdad()}, habito en {self.getHabitat()} y mi genero es {self.getGenero()}, " + \
                   f"la zona en la que me ubico es {self.getZona()}, en el {self.getZona().getZoo()}"

    # Método para obtener el tipo de movimiento de un animal.
    @classmethod
    def movimiento(cls):
        return "desplazarse"

    # Método para obtener la cantidad total de animales registrados.
    @classmethod
    def getTotalAnimales(cls):
        return cls._totalAnimales
