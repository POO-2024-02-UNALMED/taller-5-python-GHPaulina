from .animal import Animal

class Reptil(Animal):

    # Variables de clase para contar iguanas y serpientes
    iguanas = 0
    serpientes = 0
    _listado = []
    
    def __init__(self, nombre, edad, habitat, genero, colorEscamas, largoCola, zona = None):
        # Inicialización de los atributos heredados de la clase Animal y los nuevos atributos específicos de Reptil
        super().setNombre(nombre)
        super().setEdad(edad)
        super().setHabitat(habitat)
        super().setGenero(genero)
        super().setZona(zona)
        self._colorEscamas = colorEscamas
        self._largoCola = largoCola

    # Métodos para obtener y establecer el atributo "colorEscamas"
    def getColorEscamas(self):
        return self._colorEscamas
    
    def setColorEscamas(self, colorEscamas):
        self._colorEscamas = colorEscamas
    
    # Métodos para obtener y establecer el atributo "largoCola"
    def getLargoCola(self):
        return self._largoCola
    
    def setLargoCola(self, largoCola):
        self._largoCola = largoCola

    # Método de movimiento para los reptiles
    @classmethod
    def movimiento(cls):
        return "reptar"
    
    # Método para obtener el listado de todos los reptiles
    @classmethod
    def getListado(cls):
        return cls._listado
    
    # Método que devuelve la cantidad total de reptiles en el listado
    @classmethod
    def cantidadReptiles(cls):
        return len(Reptil.getListado())
    
    # Método para crear una iguana y agregarla al listado
    @classmethod
    def crearIguana(cls, nombre, edad, genero, zona = None):
        Reptil._listado.append(Reptil(nombre, edad, "humedal", genero, "verde", 3, zona))
        Reptil.iguanas += 1

    # Método para crear una serpiente y agregarla al listado
    @classmethod
    def crearSerpiente(cls, nombre, edad, genero, zona = None):
        Reptil._listado.append(Reptil(nombre, edad, "jungla", genero, "blanco", 1, zona))
        Reptil.serpientes += 1
