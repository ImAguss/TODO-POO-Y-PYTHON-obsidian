import csv
import numpy as np

from ClaseMovilidad import Movilidad

class GestorMovilidades:
    
    __arregloMovilidades: np.ndarray
    __dimension: int
    __incremento: int
    __cantidad: int
    
    def __init__(self, dimension, incremento = 5):
        self.__arregloMovilidades = np.empty(dimension, dtype = Movilidad)
        self.__dimension = dimension
        self.__cantidad = 0
    
    def AgregarElemento(self, unaMovilidad):
        if self.__dimension == self.__cantidad:
            self.__dimension += self.__incremento
            self.__arregloMovilidades.resize(self.__dimension)
        
        self.__arregloMovilidades[self.__cantidad] = unaMovilidad
        self.__cantidad += 1
        
    def test(self):
        
        with open ("movilidades.csv") as archivo:
            reader = csv.reader(archivo, delimiter = ';')
            bandera = True
            
            for fila in reader:
                if bandera:
                    bandera = not bandera
                else:
                    patente = fila[0]
                    tipo = fila[1]
                    capacidad = fila[2]
                    importeMensual = fila[3]
                    marca = fila[4]
                    modelo = fila[5]
                
                    unaMovilidad = Movilidad(patente,tipo,capacidad,importeMensual,marca,modelo)
                    self.AgregarElemento(unaMovilidad)
    
    def ComplementoEnunciadoA(self, patente):
        indice = 0
        bandera = False
        retorno = None
        
        while not bandera and indice < self.__cantidad:
            if self.__arregloMovilidades[indice].getPatente() == patente:
                retorno = self.__arregloMovilidades[indice]
                bandera = True
            else:
                indice += 1
        
        return retorno
    
    def ComplementoEnunciadoC(self,patente):
        indice = 0
        bandera = False
        retorno = None
        
        for indice in range(self.__cantidad):
            if self.__arregloMovilidades[indice].getPatente() == patente:
                retorno += self.__arregloMovilidades[indice]
                bandera = True
            else:
                indice += 1
        
        return retorno        