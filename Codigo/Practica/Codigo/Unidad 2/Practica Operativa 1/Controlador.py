from GestorGastos import GestorGastos
from GestorMovilidades import GestorMovilidades

class Controlador:
    
    def __init__(self):
        self.__GestorGastos = GestorGastos()
        self.__GestorMovilidades = GestorMovilidades(10)
        
        self.__GestorGastos.test()
        self.__GestorMovilidades.test()
        
    def EnunciadoA(self):
        totalGastado = 0
        listaGastosPorPatente = []
        indice = 0
        patente = input("Ingrese Patente: ")
        
        unMovil = self.__GestorMovilidades.ComplementoEnunciadoA(patente)
        
        if unMovil != None:
            listaGastosPorPatente = self.__GestorGastos.ComplementoEnunciadoA(patente)
            encabezado = "Patente: {:<10} Tipo: {:<10} Capacidad Carga: {:<10}".format(unMovil.getPatente(), unMovil.getTipo(), unMovil.getCapacidad())
            encabezado2 = "Importe Mensual:{:<10} Marca: {:<10} Modelo: {:<10}".format(unMovil.getImporteMensual(), unMovil.getMarca(), unMovil.getModelo())
            print (encabezado)
            print(encabezado2)
            print("Gastos")
            encabezados3 = "{:<15} {:<15} {:<15}".format("Fecha", "Importe", "Descripcion")
            print (encabezados3)
            
            for indice in range(len(listaGastosPorPatente)):
                print("{:<15} {:<15} {:<15}".format(listaGastosPorPatente[indice].getFecha(), listaGastosPorPatente[indice].getImporteGasto(), listaGastosPorPatente[indice].getDescripcion()))
                totalGastado += int(listaGastosPorPatente[indice].getImporteGasto())
            totalGastado += int(unMovil.getImporteMensual())
            print("\nTotal Gastos: {}".format(totalGastado))
        else:
            print("Nombre invalido o inexistente, intentelo de nuevo.")
    
    def EnunciadoB(self):
        importeTotal = 0
        fecha = input("Ingrese Fecha: ")
        
        importeTotal = self.__GestorGastos.ComplementoEnunciadoB(fecha)
        
        if importeTotal != -1:
            print ("El gasto que se produjo en la fecha {} es de: {}".format(fecha, importeTotal))
        else:
            print("No se realizo ningun gasto en la fecha {}".format(fecha))
            
    def EnunciadoC(self):
        listaOrdenada = []
        fecha = input("Ingrese Fecha: ")
        
        patente = self.__GestorGastos.ComplementoEnunciadoC(fecha)
        encabezado = "{:>15} {:>15} {:>15}".format("Patente", "Marca", "Modelo")
        print (encabezado)
        #No entiendo bien que quiere el Enunciado y me quede sin tiempo