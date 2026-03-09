from Gestor import Gestor

def menu():
    gestor = Gestor()
    gestor.CargaCsv()
    while True:
        print("\nHoteles disponibles:")
        gestor.listarHoteles()
        print("\n1. Agregar habitación")
        print("2. Reservar habitación")
        print("3. Liberar habitación")
        print("4. Mostrar habitaciones por tipo")
        print("5. Mostrar habitaciones libres por piso")
        print("6. Mostrar detalle por tipo")
        print("0. Salir")
        op = input("Opción: ")
        if op == "1":
            nombre = input("Ingrese el nombre del hotel: ")
            gestor.AgregarHabitacion(nombre)
        elif op == "2":
            nombre = input("Ingrese el nombre del hotel: ")
            numero = input("Ingrese el número de habitación a reservar: ")
            gestor.ReservarHabitacion(numero, nombre)
        elif op == "3":
            nombre = input("Ingrese el nombre del hotel: ")
            numero = input("Ingrese el número de habitación a liberar: ")
            gestor.LiberarHabitacion(numero, nombre)
        elif op == "4":
            nombre = input("Ingrese el nombre del hotel: ")
            tipo = input("Ingrese el tipo de habitación (sencilla, doble, suite): ")
            gestor.Inciso4(nombre, tipo)
        elif op == "5":
            nombre = input("Ingrese el nombre del hotel: ")
            gestor.HabitacionLibrePorPiso(nombre)
        elif op == "6":
            nombre = input("Ingrese el nombre del hotel: ")
            gestor.MostrarDetallesPorTipo(nombre)
        elif op == "0":
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    menu()