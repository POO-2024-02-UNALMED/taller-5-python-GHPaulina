from .animal import Animal

class Pez(Animal):

    # Variables de clase para contar el número de cada tipo de pez
    salmones = 0
    bacalaos = 0
    _listado = []
    
    def __init__(self, nombre, edad, habitat, genero, colorEscamas, cantidadAletas, zona = None):
        # Inicialización de los atributos heredados y propios de Pez
        super().setNombre(nombre)
        super().setEdad(edad)
        super().setHabitat(habitat)
        super().setGenero(genero)
        super().setZona(zona)
        self._colorEscamas = colorEscamas
        self._cantidadAletas = cantidadAletas
    
    # Métodos para obtener y establecer el atributo "colorEscamas"
    def getColorEscamas(self):
        return self._colorEscamas
    
    def setColorEscamas(self, colorEscamas):
        self._colorEscamas = colorEscamas

    # Métodos para obtener y establecer el atributo "cantidadAletas"
    def getCantidadAletas(self):
        return self._cantidadAletas
    
    def setCantidadAletas(self, cantidadAletas):
        self._cantidadAletas = cantidadAletas

    # Método de movimiento para los peces
    @classmethod
    def movimiento(cls):
        return "nadar"
    
    # Método para obtener el listado de todos los peces
    @classmethod
    def getListado(cls):
        return cls._listado
    
    # Método que devuelve la cantidad total de peces en el listado
    @classmethod
    def cantidadPeces(cls):
        return len(Pez.getListado())
    
    # Método para crear un salmón y agregarlo al listado
    @classmethod
    def crearSalmon(cls, nombre, edad, genero, zona = None):
        Pez._listado.append(Pez(nombre, edad, "ocenao", genero, "rojo", 6, zona))
        Pez.salmones += 1
    
    # Método para crear un bacalao y agregarlo al listado
    @classmethod
    def crearBacalao(cls, nombre, edad, genero, zona = None):
        Pez._listado.append(Pez(nombre, edad, "ocenao", genero, "gris", 6, zona))
        Pez.bacalaos += 1
