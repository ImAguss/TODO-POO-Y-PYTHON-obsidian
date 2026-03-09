class Departamento:
    __id: int
    __nombre: str
    
    def __init__(self, id, nombre):
        self.__id = id
        self.__nombre = nombre
        
    def GetId(self):
        return self.__id
    
    def GetNombre(self):
        return self.__nombre
    
    