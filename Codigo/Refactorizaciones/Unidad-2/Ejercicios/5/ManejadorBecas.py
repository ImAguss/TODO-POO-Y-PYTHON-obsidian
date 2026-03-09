import csv

from ClaseBeca import Beca


class ManejadorBecas:
    def __init__(self) -> None:

        self.__listaBecas: list[Beca] = []

        with open(file="becas.csv", encoding="latin1") as archivo:
            reader = csv.reader(archivo, delimiter=";")

            for i, fila in enumerate(reader):
                if i == 0:
                    continue
                else:
                    unaBeca: Beca = Beca(idBeca=fila[0], tipo=fila[1], importe=fila[2])
                    self.__listaBecas.append(unaBeca)

    def ObtenerIDbeca(self, tipo) -> int:
        encontrado = False
        i = 0

        while not encontrado and i < len(self.__listaBecas):
            if self.__listaBecas[i].tipo == tipo:
                encontrado = True
            else:
                i += 1

        if not encontrado:
            print("No se encontro")
            return 0
        else:
            return self.__listaBecas[i].idBeca

    def ObtenerImporte(self, tipo) -> float:
        encontrado = False
        i = 0

        while not encontrado and i < len(self.__listaBecas):
            if self.__listaBecas[i].tipo == tipo:
                encontrado = True
            else:
                i += 1

        if not encontrado:
            print("No se encontro")
            return 0
        else:
            return self.__listaBecas[i].importe
