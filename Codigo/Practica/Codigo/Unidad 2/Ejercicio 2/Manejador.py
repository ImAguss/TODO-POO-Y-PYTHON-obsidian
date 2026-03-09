from Tarjeta_Sube import Tarjeta_Sube

class ManejadorNegocio:
    __tarjeta:list
    
    def __init__(self):
        self.__tarjeta = []

    def test(self):
        for i in range(3):
            saldo = float(input("Ingrese Saldo: "))
            numero = int(input("Ingrese el numero de la tarjeta: "))
            unasube = Tarjeta_Sube(saldo, numero)
            self.__tarjeta.append(unasube)
    
    def mostrarTarjetas(self):
        for tarjeta in self.__tarjeta:
            print (tarjeta)
            print("\n")
            if tarjeta.Consultar_saldo() < 0:
                print ("Tarjeta con saldo Negativo")

    def Buscar_Tarjeta(self,numeroTarjeta):
        indice = 0
        bandera = False
        valorRetorno = None

        while not bandera and indice < len(self.__tarjeta):
            if self.__tarjeta[indice].Consultar_Numero() == numeroTarjeta:
                bandera = True
                valorRetorno = indice
            else:
                indice += 1
            
        return valorRetorno

    def Cargar_Saldo(self):
        numeroTarjeta = int(input("\nIngrese Numero De la Tarjeta: "))
        saldoparaCargar = float(input("Ingrese Saldo a Cargar: "))
        
        i = self.Buscar_Tarjeta(numeroTarjeta)
        if i is not None:
            self.__tarjeta[i].cargar_saldo(saldoparaCargar)
            print ("\nSu nuevo saldo es de: {} \n".format(self.__tarjeta[i].Consultar_saldo()))
        else:
            print ("\nEse numero de Tarjeta no existe")
    
    def Pagar_Pasaje(self):
        numeroTarjeta = int(input("\nIngrese Numero De la Tarjeta: "))
        saldoparaPagar = float(input("Ingrese Saldo a Pagar: "))
        
        i = self.Buscar_Tarjeta(numeroTarjeta)
        if i is not None:
            if self.__tarjeta[i].Pagar(saldoparaPagar) != -1:
                print("\n Se Acredito su pago Exitosamente!!!")
                print ("Su nuevo saldo es de: {} \n".format(self.__tarjeta[i].Consultar_saldo()))
            else:
                print("\n No posee suficiente Saldo")
        else:
            print ("\nEse numero de Tarjeta no existe")
