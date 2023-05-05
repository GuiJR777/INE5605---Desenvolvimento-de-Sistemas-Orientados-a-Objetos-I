from abstractOnibus import AbstractOnibus
from onibusJahCheioException import OnibusJahCheioException
from onibusJahDesligadoException import OnibusJahDesligadoException
from onibusJahLigadoException import OnibusJahLigadoException
from onibusJahVazioException import OnibusJahVazioException


class Onibus(AbstractOnibus):
    def __init__(
        self, capacidade: int, total_passageiros: int, ligado: bool
    ) -> None:
        self.__capacidade = capacidade
        self.__total_passageiros = total_passageiros
        self.__ligado = ligado

    @property
    def capacidade(self) -> int:
        return self.__capacidade

    @capacidade.setter
    def capacidade(self, capacidade: int) -> None:
        self.__capacidade = capacidade

    @property
    def total_passageiros(self) -> int:
        return self.__total_passageiros

    @property
    def ligado(self) -> bool:
        return self.__ligado

    def ligar(self) -> str:
        if self.__ligado:
            raise OnibusJahLigadoException()

        self.__ligado = True

        return "Onibus ligado com sucesso"

    def desligar(self) -> str:
        if not self.__ligado:
            raise OnibusJahDesligadoException()

        self.__ligado = False

        return "Onibus desligado com sucesso"

    def embarca_pessoa(self) -> str:
        if self.__total_passageiros >= self.__capacidade:
            raise OnibusJahCheioException()

        self.__total_passageiros += 1

        return "Passageiro embarcado"

    def desembarca_pessoa(self) -> str:
        if self.__total_passageiros == 0:
            raise OnibusJahVazioException()

        self.__total_passageiros -= 1

        return "Onibus já está vazio"
