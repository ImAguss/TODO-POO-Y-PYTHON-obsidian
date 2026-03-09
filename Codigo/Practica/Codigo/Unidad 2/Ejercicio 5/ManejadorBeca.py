import csv 

from ClaseBeca import Beca

class ManejadorBeca:
    
    __listaBecas: list
    
    def __init__(self):
        self.__listaBecas = []
        
    def test(self):
        with open ("becas.csv") as archivo:
            reader = csv.reader(archivo, delimiter = ';')
            bandera = True
        
            for fila in reader:
                if bandera:
                    bandera = not bandera
                else:
                    idbeca = fila[0]
                    tipo = fila[1]
                    importe = fila[2]
                    unabeca = Beca(idbeca, tipo, importe)
                    self.__listaBecas.append(unabeca)
                   
    def obtenerIDporTipo(self, tipo):
        indice = 0
        bandera = False
        Retorno = None
        
        while not bandera and indice < len(self.__listaBecas):
            if self.__listaBecas[indice].getTipo() == tipo:
                Retorno = self.__listaBecas[indice].getIdBeca()
                bandera = True
            else:
                indice +=1
        
        return Retorno
    
    def CalcularImporteTotal(self, cantidadDePersonas, id):
        
        importeTotal = int(cantidadDePersonas) * int(self.__listaBecas[id - 1].getImporte())
        
        return importeTotal
    
    def getIdBecaPorNombre(self, nombreBeca):
        indice = 0
        id = -1
        bandera = False
        
        while not bandera and indice < len(self.__listaBecas):
            if self.__listaBecas[indice].getTipo() == nombreBeca:
                id = self.__listaBecas[indice].getIdBeca()
                bandera = True
            else:
                indice += 1
        
        return id