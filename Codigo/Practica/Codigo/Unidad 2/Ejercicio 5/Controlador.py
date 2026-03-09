from ManejadorBeneficiario import ManejadorBeneficiario
from ManejadorBeca import ManejadorBeca

class Controlador:
    
    def __init__(self):
        self.__ManejadorBeneficiario = ManejadorBeneficiario()
        self.__ManejadorBeca = ManejadorBeca()

        self.__ManejadorBeneficiario.test()
        self.__ManejadorBeca.test()
        
    def EnunciadoA(self):
        
        listaBeneficiariosConMismoTipo = []
        indice = 0
        tipo = str(input("Ingrese el tipo de Beca:"))
        id = self.__ManejadorBeca.obtenerIDporTipo(tipo)
        importeTotal = 0
        
        if id is not None:
            listaBeneficiariosConMismoTipo = self.__ManejadorBeneficiario.ObtenerBeneficiariosConTipoBeca(id)
            importeTotal = self.__ManejadorBeca.CalcularImporteTotal(len(listaBeneficiariosConMismoTipo), int(id))
            
            for indice in range (len(listaBeneficiariosConMismoTipo)):
                print(listaBeneficiariosConMismoTipo[indice])
            print("\nPoseen la beca del tipo: {}".format(tipo))
            
            print ("\nEl importe total a pagar serian: {}".format(importeTotal))
        else:
            print("Ingrese un Tipo de Beca Valido.")
            
    def EnunciadoB (self):
        
        dni = str(input("Ingrese DNI: "))
        
        self.__ManejadorBeneficiario.MostrarLosBeneficiariosConMasDeUnaBeca(dni)
        
    def EnunciadoC(self):
        self.__ManejadorBeneficiario.ListaOrdenadaPorFacultad()
        
    def EnunciadoD(self):
        listaBeneficiariosSinAyudaEconomica = []
        indice = 0
        
        nombreBeca = str(input("Ingrese el nombre de la Beca: "))
        print("\n")
        id = self.__ManejadorBeca.getIdBecaPorNombre(nombreBeca)
        
        if id != -1:
            listaBeneficiariosSinAyudaEconomica = self.__ManejadorBeneficiario.ComplementoEnunciadoD(id)
            print("Los siguiente alumnos no poseen la beca {}:".format(nombreBeca))
            encabezado = "{:<10} {:<10} {:<10}".format("Nombre","Apellido","Promedio")
            print(encabezado)
            print("-" * 30) 
            for indice in range(len(listaBeneficiariosSinAyudaEconomica)): 
                print("{:<10}".format(listaBeneficiariosSinAyudaEconomica[indice].getNombre()), end = " ")
                print("{:<10}".format(listaBeneficiariosSinAyudaEconomica[indice].getApellido()), end = " ")
                print("{:<10}".format(listaBeneficiariosSinAyudaEconomica[indice].getPromedio()))
        else:
            print("Nombre de Beca Invalido, Intentelo de nuevo.")


if __name__ == "__main__":
    controlador = Controlador()
    controlador.EnunciadoD()