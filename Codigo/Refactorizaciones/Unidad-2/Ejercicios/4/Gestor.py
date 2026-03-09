from ManejadorCarrera import ManejadorCarreras as Carreras
from ManejadorFacultad import ManejadorFacultades as Facultades

class Gestor():

    __Carreras: Carreras
    __Facultades: Facultades

    def __init__(self) -> None:
        self.__Carreras = Carreras()
        self.__Facultades = Facultades()

    def enunciado_C(self, nombre) -> None:
        codigo:int = self.__Carreras.ObtenerCodigoFacultad(nombre)
        if codigo == -1:
            return

        nombre_Facultad:str = self.__Facultades.ObtenerNombreFacultad(codigo)

        if nombre_Facultad:
            print(f"La carrera {nombre} pertenece a la facultad: {nombre_Facultad}")

    def enunciado_D(self) -> None:

        cant_facultades:int = self.__Facultades.ObtenerCantidadFacultades()

        for i in range(cant_facultades):
            nombre_Facultad:str = self.__Facultades.ObtenerNombreFacultad(codigo=i+1)
            cantidad_carreras:int = self.__Carreras.CalcularCantidadCarreras(codigo=i+1)
            print(f"La facultad {nombre_Facultad} tiene {cantidad_carreras} carreras")

    def enunciado_E(self, nombre) -> None:
        codigo_facultad:int = self.__Facultades.ObtenerCodigoFacultad(nombre)
        if codigo_facultad:
            lista_ordenada:list = self.__Carreras.ObtenerListaOrdenadaCarreras(codigo=codigo_facultad)
        else:
            return

        for carrera in lista_ordenada:
            print(carrera)

