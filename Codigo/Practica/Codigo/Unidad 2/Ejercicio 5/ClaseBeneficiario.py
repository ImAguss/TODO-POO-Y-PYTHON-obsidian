
class Beneficiario:
    
    __dni: str
    __nombre: str
    __apellido: str
    __carreraCursa: str
    __facultad: str
    __añoCursa: str
    __promedio: str
    __idbeca: str
    
    def __init__ (self, dni, nombre, apellido, carreraCursa, facultad, añoCursa, promedio, idbeca):
        self.__dni = dni
        self.__nombre = nombre
        self.__apellido = apellido
        self.__carreraCursa = carreraCursa
        self.__facultad = facultad
        self.__añoCursa = añoCursa
        self.__promedio = promedio
        self.__idbeca = idbeca
        
    def getIdBeca(self):
        return self.__idbeca
    
    def getNombre(self):
        return self.__nombre
    
    def getApellido(self):
        return self.__apellido
    
    def getDNI(self):
        return self.__dni
    
    def __str__(self):
        return "El beneficiario {} con apellido {}".format(self.__nombre, self.__apellido)
    
    def getFacultad(self):
        return self.__facultad
    
    def __gt__(self, otroBeneficiario):
        return str(self.__facultad) > str(otroBeneficiario.getFacultad())
    
    def getPromedio(self):
        return self.__promedio