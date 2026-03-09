class Tarjeta_Sube:
    __saldo: float
    __numero: int

    def __init__(self, saldo, numero):
        self.__saldo = saldo
        self.__numero = numero
    
    def cargar_saldo(self, saldo_cargar):
        self.__saldo += saldo_cargar

    def Pagar(self, saldo_pagar):
        
        if self.__saldo >= saldo_pagar:
            self.__saldo -= saldo_pagar
        elif self.__saldo < saldo_pagar :
            return -1
        
    def Consultar_saldo(self):
        return self.__saldo

    def Consultar_Numero(self):
        return self.__numero
    
    def __str__(self):
        return f"Numero = {self.__numero} saldo = {self.__saldo}"
    