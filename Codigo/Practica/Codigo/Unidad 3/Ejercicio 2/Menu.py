from GestorBiblioteca import GestorBiblioteca

class Menu:
    __gestor : GestorBiblioteca
    
    def __init__(self):
        self.__gestor = GestorBiblioteca()
        self.__gestor.CargaCsv()

    def mostrar_menu(self):
        bandera = True
        
        while bandera:
            print("\n--- Menú Biblioteca ---")
            print("1. Agregar libro a una biblioteca")
            print("2. Eliminar libro por título")
            print("3. Buscar libro por título")
            print("4. Listar Libros")
            print("5. Salir")
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                self.__gestor.ListarBibliotecas()
                indice = int(input("Seleccione el número de biblioteca: ")) - 1
                self.__gestor.IncisoA(indice)
            elif opcion == "2":
                self.__gestor.ListarBibliotecas()
                indice = int(input("Seleccione el número de biblioteca: ")) - 1
                titulo = input("Ingrese el título del libro: ")
                self.__gestor.IncisoByC(titulo, indice, "ELIMINAR")
            elif opcion == "3":
                self.__gestor.ListarBibliotecas()
                indice = int(input("Seleccione el número de biblioteca: ")) - 1
                titulo = input("Ingrese el título del libro: ")
                self.__gestor.IncisoByC(titulo, indice, "BUSCAR")
            elif opcion == "4":
                self.__gestor.ListarBibliotecas()
                indice = int(input("Seleccione el número de biblioteca: ")) - 1
                self.__gestor.IncisoD(indice)
            elif opcion == "5":
                print("Saliendo del programa.")
                bandera = False
            else:
                print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    menu = Menu()
    menu.mostrar_menu()
