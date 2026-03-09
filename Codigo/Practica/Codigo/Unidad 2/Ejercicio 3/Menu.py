from Controlador import Controlador

class Menu:
    
    def test(self):
        self.__controladorInterfaz = Controlador()
        self.__controladorInterfaz.test()
        
    def MenuOpciones(self):
        bandera = True
       
        while bandera:
            print("\nSeleccione una Opcion:\n")
            print("1. Dado un NroMes, se mostrara nombres de departamentos y cantidad de accidentes")
            print("2. Dado un NroMes, se mostrara nombres de departamento con la mayor cantidad de accidentes")
            print("3. Dado un Nombre de departamento se indicara la cantidad de accidentes en el año")
            print("4. Mostrar tabla con los datos de todos los departamentos en todos los meses")
            Opcion = int(input("Ingrese 0 en caso de que desee cerrar el programa\n")) 
            if Opcion == 1:
                self.__controladorInterfaz.EnunciadoA()
            elif Opcion == 2:
                self.__controladorInterfaz.EnunciadoB()
            elif Opcion == 3:
                self.__controladorInterfaz.EnunciadoC()
            elif Opcion == 4:
                self.__controladorInterfaz.EnunciadoD()
            elif Opcion == 0:
                bandera = False
            else:
                print("\nLa opcion seleccionada no es valida")
        
        