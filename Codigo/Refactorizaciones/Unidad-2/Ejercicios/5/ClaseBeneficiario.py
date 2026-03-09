class Beneficiario:
    def __init__(
        self, dni, nombre, appelido, carrera, facultad, año, promedio, idBeca
    ) -> None:
        self.__dni: int = int(dni)
        self.__nombre: str = str(nombre)
        self.__apellido: str = str(appelido)
        self.__carrera: str = str(carrera)
        self.__facultad: str = str(facultad)
        self.__año: int = int(año)
        self.__promedio: float = float(promedio)
        self.__idBeca: int = int(idBeca)

    @property
    def idBeca(self) -> int:
        return self.__idBeca

    def __str__(self) -> str:
        return f"Nombre: {self.__nombre} Apellido: {self.__apellido}"

    @property
    def dni(self) -> int:
        return self.__dni

    @property
    def facultad(self) -> str:
        return self.__facultad

    def __gt__(self, otro) -> object:
        return self.__facultad > otro.__facultad

    @property
    def promedio(self) -> float:
        return self.__promedio
