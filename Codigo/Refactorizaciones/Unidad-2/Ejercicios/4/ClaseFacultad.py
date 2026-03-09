class Facultad:
    __codFacultad:int
    __nombre: str
    __direccion:str
    __localidad:str
    __telefono:int

    def __init__(self,codFacultad, nombre, direccion, localidad, telefono):
        self.__codFacultad = int(codFacultad)
        self.__nombre = nombre
        self.__direccion = direccion
        self.__localidad = localidad
        self.__telefono = telefono

    @property
    def nombre(self)->str:
        return self.__nombre

    @property
    def codFacultad(self) -> int:
        return self.__codFacultad

