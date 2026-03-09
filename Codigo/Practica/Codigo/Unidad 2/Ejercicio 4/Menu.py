from Controlador import Controlador

class Menu:
    
    def test(self):
        self.__controladorInterfaz = Controlador()
        
    def MenuOpciones(self):
        bandera = True
       
        while bandera:
            print("-" * 140)
            print("\nSeleccione una Opcion:\n")
            print("1.Dado el Nombre de una Carrera, mostrar el nombre de la Facultad en la que se dicta")
            print("2.Para todas las facultades calcular y mostrar la cantidad de carreras que se dictan en cada una de ellas")
            print("3.Dado el nombre de una Facultad, generar un listado ordenado alfabéticamente, que muestre: nombre y duración de de las carreras que en ella se dictan")
            
            Opcion = int(input("Ingrese 0 en caso de que desee cerrar el programa: "))
            print("-" * 140)
            print("\n") 
            if Opcion == 1:
                self.__controladorInterfaz.EnunciadoC()
            elif Opcion == 2:
                self.__controladorInterfaz.EnunciadoD()
            elif Opcion == 3:
                self.__controladorInterfaz.EnunciadoE()
            elif Opcion == 0:
                bandera = False
            else:
                print("\nLa opcion seleccionada no es valida")
        
        