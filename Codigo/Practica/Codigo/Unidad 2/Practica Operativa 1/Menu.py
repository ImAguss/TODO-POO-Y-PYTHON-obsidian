from Controlador import Controlador

class Menu:
    
    def test(self):
        self.__controladorInterfaz = Controlador()
        
    def MenuOpciones(self):
        bandera = True
       
        while bandera:
            print("-" * 140)
            print("\nSeleccione una Opcion:\n")
            print("1.Enunciado A")
            print("2.Enunciado B")
            print("3.Enunciado C")
            
            Opcion = int(input("Ingrese 0 en caso de que desee cerrar el programa: "))
            print("-" * 140)
            print("\n") 
            if Opcion == 1:
                self.__controladorInterfaz.EnunciadoA()
            elif Opcion == 2:
                self.__controladorInterfaz.EnunciadoB()
            elif Opcion == 3:
                self.__controladorInterfaz.EnunciadoC()
            elif Opcion == 0:
                bandera = False
            else:
                print("\nLa opcion seleccionada no es valida")
        
        