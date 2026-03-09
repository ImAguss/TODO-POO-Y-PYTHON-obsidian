import csv

from ClaseBeneficiario import Beneficiario


class ManejadorBeneficiarios:
    def __init__(self) -> None:
        self.__listaBeneficiarios: list[Beneficiario] = []

        with open(file="beneficiarios.csv", encoding="latin1") as archivo:
            reader = csv.reader(archivo, delimiter=";")

            for i, fila in enumerate(reader):
                if i == 0:
                    continue
                else:
                    unBeneficiario: Beneficiario = Beneficiario(
                        dni=fila[0],
                        nombre=fila[1],
                        appelido=fila[2],
                        carrera=fila[3],
                        facultad=fila[4],
                        año=fila[5],
                        promedio=fila[6],
                        idBeca=fila[7],
                    )
                    self.__listaBeneficiarios.append(unBeneficiario)

    def ListarBeneficiariosPorTipo(self, idBeca) -> None:

        for beneficiario in self.__listaBeneficiarios:
            if beneficiario.idBeca == idBeca:
                print(beneficiario)

    def BeneficiarioMasBeca(self, dni) -> object | None:
        encontrado = False
        i = 0
        contador = 0

        while not encontrado and i < len(self.__listaBeneficiarios):
            if self.__listaBeneficiarios[i].dni == dni:
                encontrado = True
                idbeca: int = self.__listaBeneficiarios[i].idBeca
            else:
                i += 1

        if not encontrado:
            print("No se encontro")
        else:
            for beneficiario in self.__listaBeneficiarios:
                if beneficiario.idBeca == idbeca:
                    contador += 1

        if contador > 1:
            return self.__listaBeneficiarios[i]
        else:
            return None

    def ListarBeneficiariosOrdenados(self) -> None:
        listaOrdenada: list[object] = sorted(
            self.__listaBeneficiarios,
            reverse=True,
        )

        for beneficiario in listaOrdenada:
            print(beneficiario)

    def BeneficiariosSinEconomia(self) -> None:

        for beneficiario in self.__listaBeneficiarios:
            if beneficiario.idBeca != 4 and beneficiario.promedio > 8:
                print(beneficiario, end=" ")
                print(f"Promedio {beneficiario.promedio}")
