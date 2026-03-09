from ManejadorDepartamento import ManejadorDepartamento
from ClaseAccidente import Accidente

class Controlador:
         
    def test (self):
        self.__CantACCIDENTESdepartamentos = Accidente()
        self.__CantACCIDENTESdepartamentos.test()
        self.__ListaDepartamentos = ManejadorDepartamento()
        self.__ListaDepartamentos.testDepartamentos()
        Rta = str(input("Desea Ingresar la cantidad de Accidentes a un Departamento? : 'S' 'N' \n"))
        
        while Rta == 'S':
            fila = int (input("Ingrese ID Departamento: "))
            columna = int(input("Ingrese Numero del mes:"))
            valor = int (input("Ingrese la cantidad de Accidentes: "))
            
            self.__CantACCIDENTESdepartamentos.SetArray(fila - 1, columna - 1, valor)
            
            Rta = str(input("\nDesea seguir ingresando la cantidad de Accidentes a un Departamento? : 'S' 'N' \n"))
            
    def EnunciadoA (self):
        nroMes = int(input("\nIngrese el mes el cual desea saber la cantidad de Accidentes: "))
        
        for id in range (19):
            print("Para el mes {} el departamento {} registro {} accidentes\n".format(nroMes,self.__ListaDepartamentos.GetNombreEnListaDepartamentos(id),self.__CantACCIDENTESdepartamentos.GetCantMes(id,nroMes-1)))
    
    def EnunciadoB (self):
        nroMes = int(input("\nIngrese el mes para el cual desea saber la maxima cantidad de accidentes de un departamento:"))
        max = 0
        nombreDepartamento = ''
        
        for id in range(19):
            if self.__CantACCIDENTESdepartamentos.GetCantMes(id,nroMes-1) > max:
                max = self.__CantACCIDENTESdepartamentos.GetCantMes(id, nroMes-1)
                nombreDepartamento = self.__ListaDepartamentos.GetNombreEnListaDepartamentos(id)
        
        print ("\nEl departamento {} fue el que mas accidentes registro, con un total de: {}".format(nombreDepartamento, max))
    
    def CalcularTotalAccidentes(self, id):
        acum = 0
        
        for mes in range (12):
            acum += int(self.__CantACCIDENTESdepartamentos.GetCantMes(id,mes))
        
        return acum    
    
    def EnunciadoC(self):
        nombreDepartamento = str(input("\nIngrese el Nombre del Departamento: "))
        bandera = False
        indice = 0
        
        while not bandera and indice < 19:
            if self.__ListaDepartamentos.GetNombreEnListaDepartamentos(indice) == nombreDepartamento:
                acum = self.CalcularTotalAccidentes(indice)
                bandera = True
                print("\nEl departamento {} registro un total de {} accidentes".format(self.__ListaDepartamentos.GetNombreEnListaDepartamentos(indice), acum))
            else:
                indice+=1
        if not bandera:
            print("\nNo se encontro el departamento")
        
    def EnunciadoD(self):
        encabezados_formateados = "{:<15}".format("Departamento") + "".join("{:<8}".format(mes + 1)for mes in range(12))
        
        print(encabezados_formateados)
        print ("-" * len(encabezados_formateados))
        
        for id in range (19):
            nombreDepartamentos = self.__ListaDepartamentos.GetNombreEnListaDepartamentos(id)
            datosAccidente = (self.__CantACCIDENTESdepartamentos.GetCantMes(id,mes)for mes in range(12))

            datosAccidente_formateados = "".join("{:<8}".format(dato) for dato in datosAccidente)
            
            print ("{:<15}{}".format(nombreDepartamentos, datosAccidente_formateados))
        
        