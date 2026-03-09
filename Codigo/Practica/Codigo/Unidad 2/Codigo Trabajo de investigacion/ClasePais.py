class Pais:
    __nombre: str
    __poblacion: int

    def __init__(self, nombre, poblacion):
        self.__nombre = nombre
        self.__poblacion = poblacion

    def getNombre(self):
        return self.__nombre

    def getPoblacion(self):
        return self.__poblacion

    def setNombre(self, nombre):
        self.__nombre = nombre

    def setPoblacion(self, poblacion):
        self.__poblacion = poblacion
