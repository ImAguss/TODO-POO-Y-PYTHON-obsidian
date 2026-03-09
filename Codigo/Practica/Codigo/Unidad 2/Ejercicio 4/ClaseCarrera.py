
class Carrera:
    __codigoCarrera: int
    __nombre: str
    __fechaInicio: int
    __duracion: int
    __titulo: str
    __codigoFacultad: int
    
    def __init__(self, codigoCarrera, nombre, fechaInicio, duracion, titulo, codigoFacultad):
        self.__codigoCarrera = codigoCarrera
        self.__nombre = nombre
        self.__fechaInicio = fechaInicio
        self.__duracion = duracion
        self.__titulo = titulo
        self.__codigoFacultad = codigoFacultad
        
    def getNombre(self):
        return self.__nombre
    
    def getCodigoFacultad(self):
        return self.__codigoFacultad
    
    def __lt__(self, otro):
        return self.__nombre < otro.getNombre()
    
    def __str__(self):
        return "\nNombre: {} \nDuracion:{}".format(self.__nombre, self.__duracion)