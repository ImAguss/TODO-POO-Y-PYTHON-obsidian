import numpy as np

class Accidente:
    __tablaAccidentes: np.ndarray

    def __init__(self):
        self.__tablaAccidentes = np.empty((19,12), dtype = object)
        self.__tablaAccidentes = np.load("accidentes.npy")

    def AccidentesPorMes (self, departamento,mes):
        return self.__tablaAccidentes[departamento - 1][mes - 1]


