from .animal import Animal

class Anfibio(Animal):

    cantidad_ranas = 0
    cantidad_salamandras = 0
    _registro = []
    
    def __init__(self, nombre, edad, habitat, genero, color_piel, es_venenoso, zona = None):
        super().setNombre(nombre)
        super().setEdad(edad)
        super().setHabitat(habitat)
        super().setGenero(genero)
        super().setZona(zona)
        self._color_piel = color_piel
        self._es_venenoso = es_venenoso

    def obtenerColorPiel(self):
        return self._color_piel
    
    def modificarColorPiel(self, color_piel):
        self._color_piel = color_piel
    
    def esVenenoso(self):
        return self._es_venenoso
    
    def cambiarVenenoso(self, es_venenoso):
        self._es_venenoso = es_venenoso
    
    @classmethod
    def tipoMovimiento(cls):
        return "saltar"
    
    @classmethod
    def obtenerRegistro(cls):
        return cls._registro
    
    @classmethod
    def contarAnfibios(cls):
        return len(Anfibio.obtenerRegistro())
    
    @classmethod
    def crearRana(cls, nombre, edad, genero, zona = None):
        Anfibio._registro.append(Anfibio(nombre, edad, "selva", genero, "rojo", True, zona))
        Anfibio.cantidad_ranas += 1
    
    @classmethod
    def crearSalamandra(cls, nombre, edad, genero, zona = None):
        Anfibio._registro.append(Anfibio(nombre, edad, "selva", genero, "negro y amarillo", False, zona))
        Anfibio.cantidad_salamandras += 1
