from .animal import Animal

class Pez(Animal):

    cantidad_salmones = 0
    cantidad_bacalaos = 0
    _registro = []
    
    def __init__(self, nombre, edad, habitat, genero, color_escamas, numero_aletas, zona = None):
        super().setNombre(nombre)
        super().setEdad(edad)
        super().setHabitat(habitat)
        super().setGenero(genero)
        super().setZona(zona)
        self._color_escamas = color_escamas
        self._numero_aletas = numero_aletas
    
    def obtenerColorEscamas(self):
        return self._color_escamas
    
    def modificarColorEscamas(self, color_escamas):
        self._color_escamas = color_escamas

    def obtenerCantidadAletas(self):
        return self._numero_aletas
    
    def modificarCantidadAletas(self, cantidad_aletas):
        self._numero_aletas = cantidad_aletas

    @classmethod
    def tipoMovimiento(cls):
        return "nadar"
    
    @classmethod
    def obtenerRegistro(cls):
        return cls._registro
    
    @classmethod
    def contarPeces(cls):
        return len(Pez.obtenerRegistro())
    
    @classmethod
    def crearSalmon(cls, nombre, edad, genero, zona = None):
        Pez._registro.append(Pez(nombre, edad, "océano", genero, "rojo", 6, zona))
        Pez.cantidad_salmones += 1
    
    @classmethod
    def crearBacalao(cls, nombre, edad, genero, zona = None):
        Pez._registro.append(Pez(nombre, edad, "océano", genero, "gris", 6, zona))
        Pez.cantidad_bacalaos += 1
