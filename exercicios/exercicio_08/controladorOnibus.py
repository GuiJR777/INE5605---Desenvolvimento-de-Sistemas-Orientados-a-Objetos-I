from abstractControladorOnibus import AbstractControladorOnibus
from comandoInvalidoException import ComandoInvalidoException
from onibus import Onibus


class ControladorOnibus(AbstractControladorOnibus):
    def __init__(self) -> None:
        self.__onibus: Onibus = None

    @property
    def onibus(self) -> Onibus:
        return self.__onibus

    def ligar(self) -> str:
        return self.__onibus.ligar()

    def desligar(self) -> str:
        return self.__onibus.desligar()

    def embarca_pessoa(self) -> str:
        return self.__onibus.embarca_pessoa()

    def desembarca_pessoa(self) -> str:
        return self.__onibus.desembarca_pessoa()

    def inicializar_onibus(
        self, capacidade: int, total_passageiros: int, ligado: bool
    ) -> None:
        capacidade_e_inteiro = isinstance(capacidade, int)
        total_passageiros_e_inteiro = isinstance(total_passageiros, int)
        ligado_e_booleano = isinstance(ligado, bool)

        if (
            not capacidade_e_inteiro
            or not total_passageiros_e_inteiro
            or not ligado_e_booleano
        ):
            raise ComandoInvalidoException()

        capacidade_e_positivo = capacidade > 0
        total_passageiros_e_positivo = total_passageiros >= 0
        total_passageiros_e_menor_igual_a_capacidade = (
            total_passageiros <= capacidade
        )

        if (
            not capacidade_e_positivo
            or not total_passageiros_e_positivo
            or not total_passageiros_e_menor_igual_a_capacidade
            or not ligado
        ):
            raise ComandoInvalidoException()

        self.__onibus = Onibus(capacidade, total_passageiros, ligado)
