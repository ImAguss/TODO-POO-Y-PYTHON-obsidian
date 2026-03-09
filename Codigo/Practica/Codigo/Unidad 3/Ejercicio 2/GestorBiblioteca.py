import csv

from ClaseBiblioteca import Biblioteca
from ClaseLibro import Libro

class GestorBiblioteca:
    __listaBibliotecas: list
    
    def __init__(self):
        self.__listaBibliotecas = []
        
    def CargaCsv(self):
        
        with open ("Biblioteca.csv") as archivo:
            reader = csv.reader(archivo, delimiter = ';')
            
            for fila in reader:
                if len(fila) == 3:
                    unabiblio = Biblioteca(fila[0],fila[1],fila[2])
                    self.__listaBibliotecas.append(unabiblio)
                else:
                    unlibro = Libro(fila[0],fila[1],fila[2],fila[3])
                    unabiblio.AgregarLibro(unlibro)
    
    def IncisoA(self,indice):
        
        print("Ingreso de Datos\n")
        titulo = input("Ingrese Titulo: ")
        autor = input("Ingrese el autor: ")
        lsbn = input("Ingrese LSBN: ")
        genero = input("Ingrese genero: ")
        
        unlibro = Libro(titulo,autor,lsbn,genero)
        self.__listaBibliotecas[indice].AgregarLibro(unlibro)
    
    def IncisoByC(self, titulo,indice,condicion):
        self.__listaBibliotecas[indice].ComplementoIncisoByC(titulo,condicion)
        
    def IncisoD(self,indice):
        self.__listaBibliotecas[indice].ListarLibros()
        
    def ListarBibliotecas(self):
        indice = 0
        print("---Elija una Biblioteca---")
        for indice in range (len(self.__listaBibliotecas)):
            print("Opcion: {}".format(indice + 1))
            print (self.__listaBibliotecas[indice])
        
    