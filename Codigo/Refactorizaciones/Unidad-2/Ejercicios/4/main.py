from Gestor import Gestor as G

if __name__ == "__main__":

    bandera = True

    while bandera:
        menu:object = G()
        opcion = int(input("""
        Ingrese una opcion:
        1. Enunciado C
        2. Enunciado D
        3. Enunciado E
        0. Salir
        """))

        if opcion == 1:
            nombre_carrera:str = str(input("Ingrese el nombre de la carrera"))
            menu.enunciado_C(nombre=nombre_carrera)
        elif opcion == 2:
            menu.enunciado_D()
        elif opcion == 3:
            nombre_facultad:str = str(input("Ingrese el nombre de la facultad"))
            menu.enunciado_E(nombre=nombre_facultad)
        elif opcion == 0:
            bandera = False
