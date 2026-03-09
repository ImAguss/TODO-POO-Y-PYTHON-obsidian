import csv
import numpy as np

from ClaseCarrera import Carrera

class ManejadorCarrera:
    
    __listaCarreras: np.ndarray
    __dimension: int
    __incremento: int
    __cantidad: int
    
    def __init__(self, dimension, incremento = 5):
        self.__listaCarreras = np.empty(dimension, dtype = Carrera)
        self.__dimension = dimension
        self.__cantidad = 0
        
    def AgregarElemento(self, unaCarrera):
        
        if self.__dimension == self.__cantidad:
            self.__dimension += self.__incremento
            self.__listaCarreras.resize(self.__dimension)
        
        self.__listaCarreras[self.__cantidad] = unaCarrera
        self.__cantidad += 1
        
    def test(self):
        archivo = open("Carreras.csv")
        reader = csv.reader(archivo,delimiter = ";")
        
        bandera = True
        
        for fila in reader:
            
            if bandera:
                bandera = False
            else:
                codigoCarrera = int (fila[0])
                nombre = fila[1]
                fechaInicio = fila[2]
                duracion = fila[3]
                titulo = fila[4]
                codigoFacultad = fila[5]
                
                unaCarrera = Carrera(codigoCarrera,nombre,fechaInicio, duracion, titulo, codigoFacultad)
                self.AgregarElemento(unaCarrera)
                        
        archivo.close()
    
    def getCodigoFacultadEnListaCarrera(self,nombre):
        bandera = False
        indice = 0
        Retorno = -1
        
        while not bandera and indice < self.__cantidad:
            if self.__listaCarreras[indice].getNombre() == nombre:
                bandera = True
                Retorno = self.__listaCarreras[indice].getCodigoFacultad()
            indice += 1
        
        return Retorno
    
    def getLen(self):
        return len(self.__listaCarreras)
    
    def getListaConIdFacultad(self):
        
        indice = 0
        listaConIdFacultad = []
        id = 0
        
        for indice in range (self.__cantidad):
            id = self.__listaCarreras[indice].getCodigoFacultad()
            listaConIdFacultad.append(id)
            
        return listaConIdFacultad
    
    def ObtenerListaObjetosConID(self, id):
        
        indice = 0
        listaCarrerasConID = []
        
        for indice in range (self.__cantidad):
            if self.__listaCarreras[indice].getCodigoFacultad() == str(id):
                listaCarrerasConID.append(self.__listaCarreras[indice])
                
        return listaCarrerasConID
    
    def OrdenarListaObjetosConID(self, lista_ordenada):
        
        n= len(lista_ordenada)
        
        for i in range(n - 1):
            for j in range (n - i - 1):
                if lista_ordenada[j + 1] < lista_ordenada [j]:
                    temp = lista_ordenada[j]
                    lista_ordenada[j] = lista_ordenada[j+1]
                    lista_ordenada[j+1] = temp
                    
        return lista_ordenada
    
    def ImprimirMensaje(self, lista_ordenada):
        
        for unaCarrera in lista_ordenada:
            print(unaCarrera)
            
