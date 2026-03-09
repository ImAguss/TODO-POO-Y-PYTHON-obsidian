
class Movilidad:
    
    __patente: str
    __tipo: str
    __capacidad: str
    __importeMensual: str
    __marca: str
    __modelo: str
    
    def __init__(self,patente,tipo,capacidad,importeMensual,marca,modelo):
        self.__patente = patente
        self.__tipo = tipo
        self.__capacidad = capacidad
        self.__importeMensual = importeMensual
        self.__marca = marca
        self.__modelo = modelo
        
    def getPatente(self):
        return self.__patente
    
    def getTipo(self):
        return self.__tipo
    
    def getCapacidad(self):
        return self.__capacidad
    
    def getImporteMensual(self):
        return self.__importeMensual
    
    def getMarca(self):
        return self.__marca
    
    def getModelo(self):
        return self.__modelo