import csv

from ClaseFacultad import Facultad

class ManejadorFacultades:
    __listaFacultades: list

    def __init__(self)->None:
        self.__listaFacultades = []

        with open (file="Facultades.csv", encoding='latin1') as archivo:
            reader = csv.reader(archivo, delimiter=';')

            for i,fila in enumerate(reader):
                if i == 0:
                    continue
                else:
                    unaFacultad = Facultad(codFacultad=fila[0],nombre=fila[1],direccion=fila[2],localidad=fila[3],telefono=fila[4]) 
                    self.__listaFacultades.append(unaFacultad)


    def ObtenerNombreFacultad(self, codigo) -> str:
        encontrado = False
        i = 0

        while not encontrado and i < len(self.__listaFacultades):
            if self.__listaFacultades[i].codFacultad == codigo:
                encontrado = True
            else:
                i+=1

        if not encontrado:
            print("No se encontro Facultad para dicha carrera")
            return ""
        else:
            return self.__listaFacultades[i].nombre

    def ObtenerCantidadFacultades(self) -> int:
        cant = 0

        for i in range(len(self.__listaFacultades)):
            cant+= 1
            
        return cant

    def ObtenerCodigoFacultad(self, nombre) -> int:

        encontrado = False
        i = 0

        while not encontrado and i < len(self.__listaFacultades):
            if self.__listaFacultades[i].nombre == nombre:
                encontrado = True
            else:
                i+=1

        if not encontrado:
            print("No se encontro")
            return 0
        else:
            return self.__listaFacultades[i].codFacultad
