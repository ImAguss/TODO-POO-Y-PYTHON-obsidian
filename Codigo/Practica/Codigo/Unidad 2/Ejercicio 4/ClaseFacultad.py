

class Facultad:
    __codigoFacultad: int
    __nombre: str
    __direccion: str
    __telefonoContacto: int
    
    def __init__(self,codigoFacultad, nombre, direccion,telefonoContacto):
        self.__codigoFacultad = codigoFacultad
        self.__nombre = nombre
        self.__direccion = direccion
        self.__telefonoContacto = telefonoContacto
    
    def getNombre(self):
        return self.__nombre
    
    def getCodigoFacultad(self):
        return self.__codigoFacultad
    
    def getID(self):
        return self.__codigoFacultad