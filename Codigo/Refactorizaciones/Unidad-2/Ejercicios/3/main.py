from Gestor import Gestor

def menu():
    gestor = Gestor()

    while True:
        print("\n--- MENU DE OPCIONES ---")
        print("1. Ver accidentes por mes")
        print("2. Ver departamento con más accidentes en un mes")
        print("3. Ver total de accidentes por departamento")
        print("4. Ver tabla completa de accidentes")
        print("0. Salir")

        opcion = input("Seleccioná una opción: ")

        if opcion == "1":
            nroMES = int(input("Ingresá el número de mes (1-12): "))
            gestor.enunciado_A(nroMES)

        elif opcion == "2":
            nroMES = int(input("Ingresá el número de mes (1-12): "))
            gestor.enunciado_B(nroMES)

        elif opcion == "3":
            nombre = input("Ingresá el nombre del departamento: ")
            gestor.enunciado_C(nombre)

        elif opcion == "4":
            gestor.enunciado_D()

        elif opcion == "0":
            print("Saliendo...")
            break

        else:
            print("Opción inválida. Probá de nuevo.")

if __name__ == "__main__":
    menu()
