
class Beca:
    
    __idbeca: str
    __tipo: str
    __importe: str
    
    def __init__(self, idbeca, tipo, importe):
        self.__idbeca = idbeca
        self.__tipo = tipo
        self.__importe = importe
    
    def getIdBeca(self):
        return self.__idbeca
    
    def getTipo(self):
        return self.__tipo
    
    def getImporte(self):
        return self.__importe