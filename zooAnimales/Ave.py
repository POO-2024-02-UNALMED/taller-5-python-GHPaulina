from .animal import Animal

class Ave(Animal):
    
    # Variables de clase para contar las aves
    halcones = 0
    aguilas = 0
    _listado = []

    def __init__(self, nombre, edad, habitat, genero, colorPlumas, zona = None):
        # Inicialización de atributos heredados y específicos
        super().setNombre(nombre)
        super().setEdad(edad)
        super().setHabitat(habitat)
        super().setGenero(genero)
        super().setZona(zona)
        self._colorPlumas = colorPlumas
    
    def getColorPlumas(self):
        return self._colorPlumas
    
    def setColorPlumas(self, colorPlumas):
        self._colorPlumas = colorPlumas
    
    # Método movimiento que es específico para la clase Ave
    @classmethod
    def movimiento(cls):
        return "volar"
    
    @classmethod
    def getListado(cls):
        return cls._listado
    
    # Método que devuelve la cantidad total de aves en la lista
    @classmethod
    def cantidadAves(cls):
        return len(Ave.getListado())
    
    # Método para crear un halcón y agregarlo al listado
    @classmethod
    def crearHalcon(cls, nombre, edad, genero, zona = None):
        Ave._listado.append(Ave(nombre, edad, "montanas", genero, "cafe glorioso", zona))
        Ave.halcones += 1

    # Método para crear un águila y agregarla al listado
    @classmethod
    def crearAguila(cls, nombre, edad, genero, zona = None):
        Ave._listado.append(Ave(nombre, edad, "montanas", genero, "blanco y amarillo", zona))
        Ave.aguilas += 1
