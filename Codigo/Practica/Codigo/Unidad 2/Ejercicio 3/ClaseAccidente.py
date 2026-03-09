import numpy as np

class Accidente:
    __cant: np.ndarray
    
    def __init__(self):
        self.__cant = np.empty((19,12), dtype = object)
    
    def test(self):
        self.__cant = np.load("accidentes.npy")
    "La funcion test es opcional, cargo un archivo que ya contiene el arreglo con los accidentes"
        
    def GetCantMes(self,fila, columna):
        return self.__cant[fila,columna]
    
    def SetArray (self,fila, columna, valor):
        self.__cant[fila,columna] = valor
             
            