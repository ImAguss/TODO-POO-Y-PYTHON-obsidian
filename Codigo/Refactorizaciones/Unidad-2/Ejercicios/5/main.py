from Gestor import Gestor


def main():
    gestor = Gestor()

    while True:
        print("\n=== MENU DE OPCIONES ===")
        print("A) Listar beneficiarios por tipo de beca")
        print("B) Ver si un beneficiario tiene más de una beca")
        print("C) Listar beneficiarios ordenados por facultad (Z a A)")
        print("D) Listar beneficiarios sin ayuda económica con promedio > 8")
        print("X) Salir")
        opcion = input("Seleccione una opción: ").strip().upper()

        if opcion == "A":
            tipo = input(
                "Ingrese el tipo de beca (Residencia, Fotocopia, Transporte, Ayuda economica, Guarderia y jardin, Investigacion): "
            )
            gestor.enunciado_A(tipo)

        elif opcion == "B":
            dni = int(input("Ingrese el DNI del beneficiario: "))
            gestor.enunciado_B(dni)

        elif opcion == "C":
            gestor.enunciado_C()

        elif opcion == "D":
            gestor.enunciado_D()

        elif opcion == "X":
            print("Saliendo...")
            break

        else:
            print("Opción no válida, intente de nuevo.")


if __name__ == "__main__":
    main()
