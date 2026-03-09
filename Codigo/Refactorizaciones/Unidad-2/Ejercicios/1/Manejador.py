from Tarjeta_Sube import Tarjeta_Sube

class Manejador:
    __subes:list

    def __init__(self):
        self.__subes = []

    def Test(self):
        for i in range (3):
            unaSube = Tarjeta_Sube(i)
            self.__subes.append(unaSube)

    def Cargar_sube(self):
        importe = int(input("Ingrese la cantidad a cargar: "))
        id = int(input("Ingrese su ID: "))
        if 1 <= id <= 3:
            self.__subes[id - 1].Cargar_saldo(importe)
        else:
            print("ID no encontrada")

    def Pagar_pasaje(self):
        importe = 1000
        id = int(input("Ingrese su ID: "))

        if 1 <= id <= 3:
            self.__subes[id - 1].Pagar_pasaje(importe)
        else:
            print("ID no encontrada")


    def Verificar_saldo(self):
        id = int(input("Ingrese su ID: "))
        if 1 <= id <= 3:
            saldo = self.__subes[id - 1].Consultar_saldo
            print(f"Su saldo es de {saldo}")
        else:
            print("ID no encontrada")
