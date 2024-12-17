from .animal import Animal

class Mamifero(Animal):

    # Variables de clase para contar mamíferos específicos
    caballos = 0
    leones = 0
    _listado = []
    
    def __init__(self, nombre, edad, habitat, genero, pelaje, patas, zona = None):
        # Inicialización de los atributos heredados y propios de Mamifero
        super().setNombre(nombre)
        super().setEdad(edad)
        super().setHabitat(habitat)
        super().setGenero(genero)
        super().setZona(zona)
        self._pelaje = pelaje
        self._patas = patas
    
    # Métodos para obtener y establecer el atributo "patas"
    def getPatas(self):
        return self._patas
    
    def setPatas(self, patas):
        self._patas = patas

    # Métodos para obtener y establecer el atributo "pelaje"
    def isPelaje(self):
        return self._pelaje
    
    def setPelaje(self, pelaje):
        self._pelaje = pelaje

    # Método para obtener el listado de mamíferos
    @classmethod
    def getListado(cls):
        return cls._listado
    
    # Método que devuelve la cantidad total de mamíferos en el listado
    @classmethod
    def cantidadMamiferos(cls):
        return len(Mamifero.getListado())
    
    # Método para crear un caballo y agregarlo al listado
    @classmethod
    def crearCaballo(cls, nombre, edad, genero, zona = None):
        Mamifero._listado.append(Mamifero(nombre, edad, "pradera", genero, True, 4, zona))
        Mamifero.caballos += 1

    # Método para crear un león y agregarlo al listado
    @classmethod
    def crearLeon(cls, nombre, edad, genero, zona = None):
        Mamifero._listado.append(Mamifero(nombre, edad, "selva", genero, True, 4, zona))
        Mamifero.leones += 1
