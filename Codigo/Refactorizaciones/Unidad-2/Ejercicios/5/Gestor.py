from ManejadorBecas import ManejadorBecas as Becas
from ManejadorBeneficiarios import ManejadorBeneficiarios as Beneficiarios


class Gestor:
    def __init__(self) -> None:
        self.__becas: Becas = Becas()
        self.__beneficiarios: Beneficiarios = Beneficiarios()

    def enunciado_A(self, tipo) -> None:
        idBeca: int = self.__becas.ObtenerIDbeca(tipo)
        importe: float = self.__becas.ObtenerImporte(tipo)

        if idBeca:
            self.__beneficiarios.ListarBeneficiariosPorTipo(idBeca)
            print(f"El importe necesario para la beca es de {importe}")

    def enunciado_B(self, dni) -> None:
        beneficiario: object | None = self.__beneficiarios.BeneficiarioMasBeca(dni)

        if beneficiario:
            print(f"El beneficiario {beneficiario} posee mas de una beca")

    def enunciado_C(self) -> None:
        self.__beneficiarios.ListarBeneficiariosOrdenados()

    def enunciado_D(self) -> None:
        self.__beneficiarios.BeneficiariosSinEconomia()


