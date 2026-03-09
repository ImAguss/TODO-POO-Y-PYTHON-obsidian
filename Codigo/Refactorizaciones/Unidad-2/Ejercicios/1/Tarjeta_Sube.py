class Tarjeta_Sube:
    __saldo: int
    __id: int

    def __init__(self, id):
        self.__saldo = 0
        self.__id = id
        print(f"Sube creada exitosamente, su saldo es de: {self.__saldo}, su ID de sube es: {self.__id + 1}")

    def Cargar_saldo(self, importe:int):

        if importe < 0:
            print("Valor de importe invalido")
            return
        else:
            self.__saldo += importe
            print("Carga realizada de forma exitosa")


    def Pagar_pasaje(self, importe:int):

        if self.__saldo < importe:
            print ("SALDO INSUFICIENTE")
            return
        else:
            self.__saldo -= importe
            print("Pago del pasaje realizado correctamente")


    @property
    def Consultar_saldo(self):
        return self.__saldo

