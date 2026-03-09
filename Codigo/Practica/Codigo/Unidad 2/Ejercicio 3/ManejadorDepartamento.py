import csv

from ClaseDepartamento import Departamento

class ManejadorDepartamento:
    __listaDepartamentos: list
    def __init__(self):
        self.__listaDepartamentos = []
        
    def testDepartamentos(self):
        archivo = open('/media/imaguss/POO/Practica/Codigo/Unidad  2/Ejercicio 3/Departamentos.csv', encoding='latin-1')
        reader = csv.reader(archivo,delimiter = ';')
        bandera = True
        
        for fila in reader:
            if bandera:
                bandera = not bandera
            else:
                idDepa = fila[0]
                nombreDepa = fila[1]
                unDepa = Departamento(idDepa, nombreDepa)
                self.__listaDepartamentos.append(unDepa)
                
        archivo.close()
        
    def GetNombreEnListaDepartamentos(self, id):
        return self.__listaDepartamentos[id].GetNombre()
    