from .animal import Animal

class Mamifero(Animal):

    cantidad_caballos = 0
    cantidad_leones = 0
    _registro = []
    
    def __init__(self, nombre, edad, habitat, genero, tiene_pelaje, numero_patas, zona = None):
        super().setNombre(nombre)
        super().setEdad(edad)
        super().setHabitat(habitat)
        super().setGenero(genero)
        super().setZona(zona)
        self._tiene_pelaje = tiene_pelaje
        self._numero_patas = numero_patas
    
    def obtenerPatas(self):
        return self._numero_patas
    
    def modificarPatas(self, patas):
        self._numero_patas = patas

    def tienePelaje(self):
        return self._tiene_pelaje
    
    def cambiarPelaje(self, pelaje):
        self._tiene_pelaje = pelaje

    @classmethod
    def obtenerRegistro(cls):
        return cls._registro
    
    @classmethod
    def contarMamiferos(cls):
        return len(Mamifero.obtenerRegistro())
    
    @classmethod
    def crearCaballo(cls, nombre, edad, genero, zona = None):
        Mamifero._registro.append(Mamifero(nombre, edad, "pradera", genero, True, 4, zona))
        Mamifero.cantidad_caballos += 1

    @classmethod
    def crearLeon(cls, nombre, edad, genero, zona = None):
        Mamifero._registro.append(Mamifero(nombre, edad, "selva", genero, True, 4, zona))
        Mamifero.cantidad_leones += 1
