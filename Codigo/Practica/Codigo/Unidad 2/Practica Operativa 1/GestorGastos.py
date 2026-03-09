import csv

from ClaseGasto import Gasto

class GestorGastos:
    __listaGastos: list
    
    def __init__(self):
        self.__listaGastos = []
        
    def test(self):
        
        with open ("gastosAbril2025.csv") as archivo:
            reader = csv.reader(archivo, delimiter = ';')
            bandera = True
            
            for fila in reader:
                if bandera:
                    bandera = not bandera
                else:
                    patente = fila[0]
                    fecha = fila[1]
                    importeGastos = fila[2]
                    descripcion = fila[3]
                    unGasto = Gasto(patente,fecha,importeGastos,descripcion)
                    self.__listaGastos.append(unGasto)
    
    def ComplementoEnunciadoA(self, patente):
        indice = 0
        listaGastosPorPatente = []

        for indice in range (len(self.__listaGastos)):
            if self.__listaGastos[indice].getPatente() == patente:
                listaGastosPorPatente.append(self.__listaGastos[indice])
        
        return listaGastosPorPatente
                
    def ComplementoEnunciadoB(self, fecha):
        indice = 0
        bandera = False
        importeTotal = -1

        while not bandera and indice < len(self.__listaGastos):
            if self.__listaGastos[indice].getFecha() == fecha:
                importeTotal = self.__listaGastos[indice].getImporteGasto()
                bandera = True
            else:
                indice += 1
    
        return importeTotal
    
    def ComplementoEnunciadoC(self, fecha):
        indice = 0
        bandera = False
        patente = ""

        while not bandera and indice < len(self.__listaGastos):
            if self.__listaGastos[indice].getFecha() == fecha:
                patente = self.__listaGastos[indice].getPatente()
                bandera = True
            else:
                indice += 1
    
        return patente