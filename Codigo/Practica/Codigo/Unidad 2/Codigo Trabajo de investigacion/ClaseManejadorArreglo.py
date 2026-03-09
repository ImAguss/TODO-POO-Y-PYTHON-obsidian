import numpy as np
from ClasePais import Pais

class ManejadorArreglo:
    __arregloPaises: np.ndarray

    def __init__(self):
        self.__arregloPaises = np.empty(3, dtype=Pais)

    def test(self):
        # Creación de objetos
        pais1 = Pais("Argentina", 25000000)
        pais2 = Pais("Francia", 123000000)
        pais3 = Pais("España", 59000000)

        # Asignar los países en el arreglo
        self.__arregloPaises[0] = pais1
        self.__arregloPaises[1] = pais2
        self.__arregloPaises[2] = pais3

    def mostrarElementos(self):
        # Recorrer el arreglo y mostrar los países
        for pais in self.__arregloPaises:
            if pais is not None:
                print("País: {}, Población: {}".format(pais.getNombre(), pais.getPoblacion()))

        # Eliminar un país
        # Lo seteamos como None para simular eliminación ya que numpy no posee eliminacion de objetos
        self.__arregloPaises[1] = None

        print("\nDespués de eliminar:")
        for pais in self.__arregloPaises:
            if pais is not None:
                print("País: {}, Población: {}".format(pais.getNombre(), pais.getPoblacion()))
