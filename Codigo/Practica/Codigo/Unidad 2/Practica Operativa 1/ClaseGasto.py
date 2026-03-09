
class Gasto:
    
    __patente: str
    __fecha: str
    __importeGasto: str
    __descripcion: str
    
    def __init__(self,patente,fecha,importeGasto,descripcion):
        self.__patente = patente
        self.__fecha = fecha
        self.__importeGasto = importeGasto
        self.__descripcion = descripcion
        
    def getPatente(self):
        return self.__patente
    
    def getFecha(self):
        return self.__fecha
    
    def getImporteGasto(self):
        return self.__importeGasto
    
    def getDescripcion(self):
        return self.__descripcion
    
    def __lt__(self, otroGasto):
        return self.__patente < otroGasto.getPatente()