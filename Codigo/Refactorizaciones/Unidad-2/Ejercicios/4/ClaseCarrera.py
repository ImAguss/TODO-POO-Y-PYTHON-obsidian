class Carrera:
    __codigo: int
    __nombre: str
    __fecha_inicio:int
    __duracion: int
    __titulo: str
    __codFacultad:int

    def __init__(self,codigo,nombre,fecha_inicio,duracion,titulo,codFacultad):
        self.__codigo = int(codigo)
        self.__nombre = nombre
        self.__fecha_inicio = fecha_inicio
        self.__duracion = duracion
        self.__titulo = titulo
        self.__codFacultad = int(codFacultad)

    def __str__(self) -> str:
        return  f"""
        Carrera: {self.__nombre}
        Duracion: {self.__duracion}"""

    @property
    def codFacultad(self) ->int:
        return self.__codFacultad

    @property
    def nombre(self) -> str:
        return self.__nombre
    
    def __lt__(self, otro) -> None:
        return self.__nombre < otro.__nombre
