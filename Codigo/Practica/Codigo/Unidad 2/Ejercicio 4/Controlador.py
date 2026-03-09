from ManejadorCarreras import ManejadorCarrera
from ManejadorFacultades import ManejadorFacultad

class Controlador:
    __ManejadorCarrera: ManejadorCarrera
    __ManejadorFacultades: ManejadorFacultad
    
    def __init__(self):
        self.__ManejadorCarrera = ManejadorCarrera(40)
        self.__ManejadorFacultades = ManejadorFacultad(6)
        
        self.__ManejadorCarrera.test()
        self.__ManejadorFacultades.test()
    
    def EnunciadoC(self):
        nombre = str(input("Ingrese el nombre de la Carrera: "))
        
        codigoFacultad = self.__ManejadorCarrera.getCodigoFacultadEnListaCarrera(nombre)
        
        if codigoFacultad == -1:
            print("Nombre de carrera invalido")
            print("\n") 
        
        nombreFacultad = self.__ManejadorFacultades.getNombreEnListaFacultad(codigoFacultad)
        
        if nombreFacultad != "":
            print("La carrera {} está en la Facultad:  {}".format(nombre, nombreFacultad))
        else:
            print("No se encontró la facultad para la carrera ingresada.")
    
    def EnunciadoD(self):
        listaCarrerasPorFacultad = self.__ManejadorCarrera.getListaConIdFacultad()
        cantidadCarrerasPorFacultad = [0] * 6
        listaNombresFacultades = self.__ManejadorFacultades.GetNombres()
        indice = 0
        
        for indice in range(self.__ManejadorFacultades.getCantidadFacultades()):
            cantidadCalculada = self.__ManejadorFacultades.CalcularCantidadEnunciadoD(
                listaCarrerasPorFacultad, 0, indice + 1
            )
            cantidadCarrerasPorFacultad[indice] += cantidadCalculada

        for indice in range(len(cantidadCarrerasPorFacultad)):
                print ("La facultad {} posee: {}".format(listaNombresFacultades[indice], cantidadCarrerasPorFacultad[indice]))            

    def EnunciadoE(self):
        
        NombreFacultad = input("Ingrese el nombre de la facultad: ")
        listaCarrerasSinOrdenar = []
        listaCarrerasOrdenadas = []
        id = self.__ManejadorFacultades.GetIdPorNombre(NombreFacultad)
        
        if id == -1:
            print("No se ha encontrado la facultad con ese nombre, Intentelo de nuevo mas tarde")
        else:
            listaCarrerasSinOrdenar = self.__ManejadorCarrera.ObtenerListaObjetosConID(id)
            listaCarrerasOrdenadas = self.__ManejadorCarrera.OrdenarListaObjetosConID(listaCarrerasSinOrdenar)
            self.__ManejadorCarrera.ImprimirMensaje(listaCarrerasOrdenadas)


