class Beca:
    def __init__(self, idBeca, tipo, importe) -> None:
        self.__idBeca: int = int(idBeca)
        self.__tipo: str = str(tipo)
        self.__importe: float = float(importe)

    @property
    def tipo(self) -> str:
        return self.__tipo

    @property
    def idBeca(self) -> int:
        return self.__idBeca

    @property
    def importe(self) -> float:
        return self.__importe
