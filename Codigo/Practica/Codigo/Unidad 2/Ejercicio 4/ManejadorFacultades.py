import csv
import numpy as np

from ClaseFacultad import Facultad

class ManejadorFacultad:
    
    __listaFacultades: np.ndarray
    __dimension: int
    __incremento: int
    __cantidad: int
    
    def __init__(self, dimension, incremento = 5):
        self.__listaFacultades = np.empty(dimension, dtype = Facultad)
        self.__dimension = dimension
        self.__cantidad = 0
        
    def AgregarElemento(self, unaFacultad):
        
        if self.__dimension == self.__cantidad:
            self.__dimension += self.__incremento
            self.__listaFacultades.resize(self.__dimension)
        
        self.__listaFacultades[self.__cantidad] = unaFacultad
        self.__cantidad += 1
                   
    def test(self):
        archivo = open("Facultades.csv")
        reader = csv.reader(archivo,delimiter = ";")
        
        bandera = True
        
        for fila in reader:
            
            if bandera:
                bandera = False
            else:
                codigoFacultad = int (fila[0])
                nombre = fila[1]
                direccion = fila[2]
                telefonoContacto = fila[3]
                
                unaFacultad = Facultad(codigoFacultad, nombre, direccion, telefonoContacto)
                self.AgregarElemento(unaFacultad)
                
        archivo.close()
            
    def getNombreEnListaFacultad(self,codigo):
        bandera = False
        indice = 0
        Retorno = ""
        
        while not bandera and indice < self.__cantidad:
            if str(self.__listaFacultades[indice].getCodigoFacultad()) == codigo:
                bandera = True
                Retorno = self.__listaFacultades[indice].getNombre()
            else:
                indice += 1
        return Retorno
    
    def getCantidadFacultades(self):
        return self.__cantidad
    
    def CalcularCantidadEnunciadoD(self, listaconID, cantidadCalculada, ID):

        indice = 0

        for indice in range (len(listaconID)):
            if listaconID[indice] == str(ID):
                cantidadCalculada += 1
                
        return cantidadCalculada
    
    def GetNombres(self):
        
        indice = 0
        listaNombres = []
        nombre = ""
        for indice in range (self.__cantidad):
            nombre = self.__listaFacultades[indice].getNombre()
            listaNombres.append(nombre)
        
        return listaNombres

    def GetIdPorNombre(self, nombre):
        bandera = False
        indice = 0
        id = -1
        
        while not bandera and indice < self.__cantidad:
            if self.__listaFacultades[indice].getNombre() == nombre:
                id = indice + 1
                bandera = True
            else:
                indice += 1
                     
        return id
             