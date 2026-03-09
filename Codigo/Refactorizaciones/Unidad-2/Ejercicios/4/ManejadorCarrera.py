import csv

from ClaseCarrera import Carrera

class ManejadorCarreras:
    __listaCarreras: list[Carrera]

    def __init__(self) -> None:
        self.__listaCarreras = []

        with open ("Carreras.csv", encoding='latin1') as archivo:
            reader = csv.reader(archivo, delimiter=';')

            for i,fila in enumerate(reader):
                if i == 0:
                    continue
                else:
                    unaCarrera: Carrera = Carrera(codigo=fila[0],nombre=fila[1],fecha_inicio=fila[2],duracion=fila[3],titulo=fila[4],codFacultad=fila[5]) 
                    self.__listaCarreras.append(unaCarrera)

    def ObtenerCodigoFacultad(self, nombre) -> int:
        encontrado = False
        i = 0

        while not encontrado and i < len(self.__listaCarreras):
            if self.__listaCarreras[i].nombre.lower() == nombre.lower():
                encontrado = True
            else: 
                i+=1

        if not encontrado:
            print("No se encontro")
            return -1
        else:
            return self.__listaCarreras[i].codFacultad


    def CalcularCantidadCarreras(self,codigo) -> int:
        cant = 0

        for i in range(len(self.__listaCarreras)):
            if self.__listaCarreras[i].codFacultad == codigo:
                cant+=1

        return cant

    def ObtenerListaOrdenadaCarreras(self, codigo) -> list:
        lista_desordenada:list[Carrera] = []
        for carrera in self.__listaCarreras:
            if(carrera.codFacultad == codigo):
                lista_desordenada.append(carrera)

        lista_ordenada:list[Carrera] = sorted(lista_desordenada, key= lambda x: x.nombre)
        return lista_ordenada
        

