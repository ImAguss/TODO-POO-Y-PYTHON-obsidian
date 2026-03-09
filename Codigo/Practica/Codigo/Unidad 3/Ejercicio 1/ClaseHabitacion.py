
class Habitacion:
    __numero: int
    __piso: int
    __tipo:str
    __precio:float
    __disponibilidad: bool
    
    def __init__(self,numero, piso,tipo,precio, disponibilidad):
        self.__numero = numero
        self.__piso = int(piso)
        self.__tipo = tipo
        self.__precio = precio
        self.__disponibilidad = disponibilidad
    
    def getDisponibilidad(self):
        return self.__disponibilidad
    
    def getTipo(self):
        return self.__tipo
    
    def getPiso(self):
        return self.__piso
    
    def getNumero(self):
        return self.__numero
    
    def getPrecio(self):
        return self.__precio
    
    def setDisponibilidad(self, nuevaDisp):
        self.__disponibilidad = nuevaDisp
        return self.__disponibilidad
    
    def __lt__(self, other):
        return self.__tipo < other.__tipo
    
    def __str__(self):
        encabezado = "Tipo Habitacion: {}\n".format(self.__tipo)
        datos = "Numero: {} Piso: {} Precio: {} Disponibilidad: {}".format(
            self.__numero, self.__piso, self.__precio, self.__disponibilidad
        )
        return encabezado + datos + "\n"