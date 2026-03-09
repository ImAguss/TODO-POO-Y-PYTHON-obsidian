from ManejadorDepartamentos import ManejadorDepartamento
from Accidente import Accidente

class Gestor:
    __ManejadorDepartamentos:object
    __Accidentes:object

    def __init__ (self):
        self.__ManejadorDepartamentos = ManejadorDepartamento() 
        self.__Accidentes = Accidente()

    def enunciado_A(self, nroMES):
        for departamento in self.__ManejadorDepartamentos.listaDepartamentos:
            cantidad_accidentes = self.__Accidentes.AccidentesPorMes(departamento.numero_departamento,nroMES)
            print(f"""
            Departamento:{departamento.nombre_departamento}
            Cantidad de accidentes en el mes {nroMES}: {cantidad_accidentes}""")

    def enunciado_B(self,nroMES):
        max_accidentes = 0
        for departamento in self.__ManejadorDepartamentos.listaDepartamentos:
            cantidad_accidentes = self.__Accidentes.AccidentesPorMes(departamento.numero_departamento,nroMES)
            if cantidad_accidentes > max_accidentes:
                max_accidentes = cantidad_accidentes
                departamento_max = departamento.nombre_departamento

        print(f"""
        El departamento que registro la mayor cantidad de accidentes es:
        {departamento_max}
        Cantidad de accidentes: {max_accidentes}""")

    def enunciado_C(self,nombre):
        cantidad_accidentes = 0
        nroDepa = self.__ManejadorDepartamentos.ObtenerNumeroDepartamento(nombre)
        if nroDepa == -1: print("No se encontro"); return

        for i in range(1,13):
            cantidad_accidentes += self.__Accidentes.AccidentesPorMes(nroDepa, i)

        print(f"Cantidad total de accidentes para {nombre}: {cantidad_accidentes}")

    def enunciado_D(self):
        print(f"{'Departamento:':<15}", end='')
        for i in range(1,13):
            print(f"Mes {i:<8}", end='')
        print()

        for i in range(19):
            print(f"{self.__ManejadorDepartamentos.listaDepartamentos[i].nombre_departamento:<15}", end='')
            for j in range(1,13):
                print(f"{self.__Accidentes.AccidentesPorMes(i+1, j):<12}", end='')
            print()

