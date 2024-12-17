class Animal():

    _cantidadAnimales = 0
    
    def __init__(self, nombre, edad, habitat, genero, zona = None):
        self._nombreAnimal = nombre
        self._edadAnimal = edad
        self._habitatAnimal = habitat
        self._generoAnimal = genero
        self._zonaAnimal = zona
        Animal._cantidadAnimales += 1

    def getNombre(self):
        return self._nombreAnimal
    
    def setNombre(self, nuevoNombre):
        self._nombreAnimal = nuevoNombre
    
    def getEdad(self):
        return self._edadAnimal
    
    def setEdad(self, nuevaEdad):
        self._edadAnimal = nuevaEdad

    def getHabitat(self):
        return self._habitatAnimal
    
    def setHabitat(self, nuevoHabitat):
        self._habitatAnimal = nuevoHabitat
    
    def getGenero(self):
        return self._generoAnimal
    
    def setGenero(self, nuevoGenero):
        self._generoAnimal = nuevoGenero

    def setZona(self, nuevaZona):
        self._zonaAnimal = nuevaZona
    
    def getZona(self):
        return self._zonaAnimal
    
    @classmethod
    def getTotalAnimales(cls):
        return cls._cantidadAnimales
    
    @classmethod
    def totalPorTipo(cls):
        from .mamifero import Mamifero
        from .ave import Ave
        from .reptil import Reptil
        from .pez import Pez
        from .anfibio import Anfibio
        return f"Mamíferos: {Mamifero.cantidadMamiferos()}\nAves: {Ave.cantidadAves()}\nReptiles: {Reptil.cantidadReptiles()}\nPeces: {Pez.cantidadPeces()}\nAnfibios: {Anfibio.cantidadAnfibios()}"
    
    def toString(self):
        if self.getZona() is None:
            return f"Mi nombre es {self.getNombre()}, tengo {self.getEdad()} años, habito en {self.getHabitat()} y mi género es {self.getGenero()}"
        else:
            return f"Mi nombre es {self.getNombre()}, tengo {self.getEdad()} años, habito en {self.getHabitat()} y mi género es {self.getGenero()}, la zona donde me encuentro es {self.getZona()} y el zoológico es {self.getZona().getZoo()}"
    
    @classmethod
    def movimiento(cls):
        return "desplazarse"
