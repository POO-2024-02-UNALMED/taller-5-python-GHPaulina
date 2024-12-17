from .animal import Animal

class Reptil(Animal):

    cantidad_iguanas = 0
    cantidad_serpientes = 0
    _registro = []
    
    def __init__(self, nombre, edad, habitat, genero, color_escamas, longitud_cola, zona = None):
        super().setNombre(nombre)
        super().setEdad(edad)
        super().setHabitat(habitat)
        super().setGenero(genero)
        super().setZona(zona)
        self._color_escamas = color_escamas
        self._longitud_cola = longitud_cola

    def obtenerColorEscamas(self):
        return self._color_escamas
    
    def modificarColorEscamas(self, color_escamas):
        self._color_escamas = color_escamas
    
    def obtenerLongitudCola(self):
        return self._longitud_cola
    
    def modificarLongitudCola(self, longitud_cola):
        self._longitud_cola = longitud_cola

    @classmethod
    def tipoMovimiento(cls):
        return "reptar"
    
    @classmethod
    def obtenerRegistro(cls):
        return cls._registro
    
    @classmethod
    def contarReptiles(cls):
        return len(Reptil.obtenerRegistro())
    
    @classmethod
    def crearIguana(cls, nombre, edad, genero, zona = None):
        Reptil._registro.append(Reptil(nombre, edad, "humedal", genero, "verde", 3, zona))
        Reptil.cantidad_iguanas += 1

    @classmethod
    def crearSerpiente(cls, nombre, edad, genero, zona = None):
        Reptil._registro.append(Reptil(nombre, edad, "jungla", genero, "blanco", 1, zona))
        Reptil.cantidad_serpientes += 1
