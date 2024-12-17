from .animal import Animal

class Anfibio(Animal):

    ranas = 0
    salamandras = 0
    _listado = []
    
    def __init__(self, nombre, edad, habitat, genero, colorPiel, venenoso, zona = None):

        super().setNombre(nombre)
        super().setEdad(edad)
        super().setHabitat(habitat)
        super().setGenero(genero)
        super().setZona(zona)
        self._colorPiel = colorPiel
        self._venenoso = venenoso

    def isVenenoso(self):
        return self._venenoso
    
    def setVenenoso(self, venenoso):
        self._venenoso = venenoso
    
    def getColorPiel(self):
        return self._colorPiel
    
    def setColorPiel(self, colorPiel):
        self._colorPiel = colorPiel

    #método movimiento()
    @classmethod
    def movimiento(cls):
        return "saltar"

    @classmethod
    def getListado(cls):
        return cls._listado
    
    #método cantidadAnfibios
    @classmethod
    def cantidadAnfibios(cls):
        return len(Anfibio.getListado())

     #método crearRana()
    @classmethod
    def crearRana(cls, nombre, edad, genero, zona = None):
        Anfibio._listado.append(Anfibio(nombre, edad, "selva", genero, "rojo", True, zona))
        Anfibio.ranas += 1
    
    #método crearSalamandra()
    @classmethod
    def crearSalamandra(cls, nombre, edad, genero, zona = None):
        Anfibio._listado.append(Anfibio(nombre, edad, "selva", genero, "negro y amarillo", False, zona))
        Anfibio.salamandras += 1
