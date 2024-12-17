from .animal import Animal

class Ave(Animal):
    
    cantidad_halcones = 0
    cantidad_aguilas = 0
    _registro = []

    def __init__(self, nombre, edad, habitat, genero, color_plumas, zona = None):
        super().setNombre(nombre)
        super().setEdad(edad)
        super().setHabitat(habitat)
        super().setGenero(genero)
        super().setZona(zona)
        self._color_plumas = color_plumas
    
    def obtenerColorPlumas(self):
        return self._color_plumas
    
    def modificarColorPlumas(self, color_plumas):
        self._color_plumas = color_plumas
    
    @classmethod
    def tipoMovimiento(cls):
        return "volar"
    
    @classmethod
    def obtenerRegistro(cls):
        return cls._registro
    
    @classmethod
    def contarAves(cls):
        return len(Ave.obtenerRegistro())
    
    @classmethod
    def crearHalcon(cls, nombre, edad, genero, zona = None):
        Ave._registro.append(Ave(nombre, edad, "montañas", genero, "café glorioso", zona))
        Ave.cantidad_halcones += 1

    @classmethod
    def crearAguila(cls, nombre, edad, genero, zona = None):
        Ave._registro.append(Ave(nombre, edad, "montañas", genero, "blanco y amarillo", zona))
        Ave.cantidad_aguilas += 1
