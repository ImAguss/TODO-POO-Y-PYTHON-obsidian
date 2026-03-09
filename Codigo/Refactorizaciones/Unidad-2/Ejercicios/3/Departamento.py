class Departamento:
    __nro: int
    __nombre: str

    def __init__ (self, numero, nombre):
        self.__nro = int(numero)
        self.__nombre = nombre

    @property
    def numero_departamento(self):
        return self.__nro
    
    @property
    def nombre_departamento(self):
        return self.__nombre

    def __str__(self):
        return f"{self.__nombre}"
