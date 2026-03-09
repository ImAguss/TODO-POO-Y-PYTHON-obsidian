from Manejador import ManejadorNegocio

if __name__ == '__main__':
    listaTarjetas = ManejadorNegocio()
    listaTarjetas.test()
    listaTarjetas.mostrarTarjetas()
    listaTarjetas.Cargar_Saldo()
    listaTarjetas.Pagar_Pasaje()
    listaTarjetas.mostrarTarjetas()