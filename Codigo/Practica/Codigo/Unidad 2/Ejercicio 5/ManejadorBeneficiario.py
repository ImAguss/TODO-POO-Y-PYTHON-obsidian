import csv

from ClaseBeneficiario import Beneficiario

class ManejadorBeneficiario:
    
    __listaBeneficiarios: list
    
    def __init__(self):
        self.__listaBeneficiarios = []
        
    def test(self):
        with open ("beneficiarios.csv") as archivo:
            reader = csv.reader(archivo, delimiter = ";")
            bandera = True
        
            for fila in reader:
                if bandera:
                    bandera = False
                else:
                    dni = fila[0]
                    nombre = fila[1]
                    apellido = fila[2]
                    carreraCursa = fila[3]
                    facultad = fila[4]
                    añoCursa = fila[5]
                    promedio = fila[6]
                    idbeca = fila[7]
                
                    unbeneficiario = Beneficiario(dni,nombre,apellido,carreraCursa,facultad,añoCursa,promedio,idbeca)
                    self.__listaBeneficiarios.append(unbeneficiario)
    
    def ObtenerBeneficiariosConTipoBeca(self, id):
        indice = 0
        listaBeneficiariosConMismoTipo = []
        
        for indice in range (len(self.__listaBeneficiarios)):
            if self.__listaBeneficiarios[indice].getIdBeca() == id:
                unBeneficiario = self.__listaBeneficiarios[indice]
                listaBeneficiariosConMismoTipo.append(unBeneficiario)
        
        return listaBeneficiariosConMismoTipo
    
    def MostrarLosBeneficiariosConMasDeUnaBeca (self, dni):
        indice = 0
        cont = 0
        valor = 0
        
        for indice in range (len(self.__listaBeneficiarios)):
            if self.__listaBeneficiarios[indice].getDNI() == str(dni):
                cont += 1
                valor = indice

        if cont >= 2:
            print (self.__listaBeneficiarios[valor], end = "")
            print (" Posee mas de una Beca")
        else:
            print("El usuario con DNI {} no posee mas de una Beca".format(dni))
    
    def ListaOrdenadaPorFacultad (self):
        i = 0
        j = 0
        n = len(self.__listaBeneficiarios)
        
        for i in range (n-1):
            for j in range (n - i - 1):
                if self.__listaBeneficiarios [j + 1] > self.__listaBeneficiarios[j]:
                    temp = self.__listaBeneficiarios[j]
                    self.__listaBeneficiarios[j] = self.__listaBeneficiarios[j+1]
                    self.__listaBeneficiarios[j+1] = temp
                        
        encabezado = "{:<10} {:<10} {:<10}".format("Nombre","Apellido","Facultad")
        print(encabezado)
        print("-" * 30)                
        for beneficiario in self.__listaBeneficiarios:
            print("{:<10}".format(beneficiario.getNombre()), end = " ")
            print("{:<10}".format(beneficiario.getApellido()), end = " ")
            print("{:<10}".format(beneficiario.getFacultad()))
            
    def ComplementoEnunciadoD(self, id):
        indice = 0
        listaBeneficiariosSinAyudaEconomica = []
        
        for indice in range(len(self.__listaBeneficiarios)):
            if self.__listaBeneficiarios[indice].getPromedio() > "8":
                listaBeneficiariosSinAyudaEconomica.append(self.__listaBeneficiarios[indice])
                
        for beneficiario in listaBeneficiariosSinAyudaEconomica[:]:
            if beneficiario.getIdBeca() == id:
                listaBeneficiariosSinAyudaEconomica.remove(beneficiario)
                
        return listaBeneficiariosSinAyudaEconomica