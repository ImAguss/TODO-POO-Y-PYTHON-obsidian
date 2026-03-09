from Manejador import Manejador

if __name__ == "__main__":

    manejador = Manejador()
    manejador.Test()

    while True:
        opcion = int(input("""
Ingrese la opcion correspondiente:
    1. Cargar Saldo en sube
    2. Pagar pasaje
    3. Consultar Saldo
    0. SALIR
> """))

        if opcion == 1:
            manejador.Cargar_sube()
        elif opcion == 2:
            manejador.Pagar_pasaje()
        elif opcion == 3:
            manejador.Verificar_saldo()
        elif opcion == 0:
            break
