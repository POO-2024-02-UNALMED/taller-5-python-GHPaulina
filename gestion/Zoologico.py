class Zoologico():

    def __init__(self, nombre, ubicacion):
        self._nombre_zoologico = nombre
        self._ubicacion_zoologico = ubicacion
        self._zonas_animales = []
    
    def obtenerNombre(self):
        return self._nombre_zoologico
    
    def modificarNombre(self, nuevoNombre):
        self._nombre_zoologico = nuevoNombre
    
    def obtenerUbicacion(self):
        return self._ubicacion_zoologico
    
    def cambiarUbicacion(self, nuevaUbicacion):
        self._ubicacion_zoologico = nuevaUbicacion

    def anadirZona(self, zona):
        self._zonas_animales.append(zona)

    def obtenerZonas(self):
        return self._zonas_animales
    
    def obtenerPrimeraZona(self):
        if self._zonas_animales:
            return [self._zonas_animales[0]]
        return []
    
    def contarAnimales(self):
        total_animales = 0
        for zona in self._zonas_animales:
            total_animales += zona.cantidadAnimales()
        return total_animales
