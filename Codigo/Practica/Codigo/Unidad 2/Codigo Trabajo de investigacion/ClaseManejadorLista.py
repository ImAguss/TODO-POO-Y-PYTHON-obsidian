from ClasePais import Pais

class ManejadorLista:
    __listaPaises: list

    def __init__(self):
        self.__listaPaises = []

    def test(self):
        # Creación de objetos
        pais1 = Pais("Argentina", 46000000)
        pais2 = Pais("Brasil", 213000000)
        pais3 = Pais("Chile", 19000000)

        # Uso de métodos básicos de manipulación
        self.__listaPaises.append(pais1)    # Agregar un elemento al final
        self.__listaPaises.append(pais2)
        self.__listaPaises.insert(1, pais3) # Insertar en la posición 1

    def mostrarElementos(self):
        # Recorrer la lista y mostrar los países
        for pais in self.__listaPaises:
            print("País: {}, Población: {}".format(pais.getNombre(), pais.getPoblacion()))

        # Eliminar un elemento de la lista
        self.__listaPaises.remove(self.__listaPaises[1])

        print("\nDespués de eliminar:")
        for pais in self.__listaPaises:
            print("País: {}, Población: {}".format(pais.getNombre(), pais.getPoblacion()))
