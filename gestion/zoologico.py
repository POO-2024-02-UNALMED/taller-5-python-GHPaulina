class Zoologico():
    
    def __init__(self, nombre, ubicacion):
        self._nombre = nombre
        self._ubicacion = ubicacion
        self._zonas = []
    
    def agregarZonas(self, nuevaZona):
        self._zonas.append(nuevaZona)

    def getZonas(self):
        return self._zonas

    def getZona(self):
        # Si solo deseas la primera zona
        if self._zonas:
            return [self._zonas[0]]  # Devuelve una lista con la primera zona
        return []
    
    def getNombre(self):
        return self._nombre
    
    def setNombre(self, nuevoNombre):
        self._nombre = nuevoNombre
    
    def getUbicacion(self):
        return self._ubicacion
    
    def setUbicacion(self, nuevaUbicacion):
        self._ubicacion = nuevaUbicacion

    def cantidadTotalAnimales(self):
        cantidadTotalAnimales = 0
        for zona in self._zonas:  # Iterar directamente sobre las zonas
            cantidadTotalAnimales += zona.cantidadAnimales()  # Asumiendo que cada zona tiene el método cantidadAnimales
        return cantidadTotalAnimales
