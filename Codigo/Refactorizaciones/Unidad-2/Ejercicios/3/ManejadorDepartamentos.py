import csv

from Departamento import Departamento

class ManejadorDepartamento:
    __listaDepartamentos: list

    def __init__(self):
        self.__listaDepartamentos = []
        with open('Departamentos.csv', encoding='latin-1') as archivo:
            reader = csv.reader(archivo, delimiter=';')

            for i,fila in enumerate(reader):
                if i == 0:
                    print("Iniciando Lectura de Archivo CSV")
                else:
                    unDepartamento = Departamento(fila[0], fila[1])
                    self.__listaDepartamentos.append(unDepartamento)

            print("Carga de departamentos Finalizada")

    @property
    def listaDepartamentos(self):
        return self.__listaDepartamentos

    def ObtenerNumeroDepartamento(self, nombre):
        encontrado = False
        i = 0

        while not encontrado and i < len(self.__listaDepartamentos):
            if self.__listaDepartamentos[i].nombre_departamento == nombre:
                encontrado = True
            else:
                i+=1

        if not encontrado:
            return -1
        else:
            return self.__listaDepartamentos[i].numero_departamento
