from arbitro import Arbitro
from equipe import Equipe


class Jogo:
    def __init__(
        self,
        numero: int,
        local: str,
        arbitro: Arbitro,
        equipe_1: Equipe,
        equipe_2: Equipe,
    ) -> None:
        self.__numero = numero
        self.__local = local
        self.__arbitro = arbitro
        self.__equipe_1 = equipe_1
        self.__equipe_2 = equipe_2
        self.__gols_equipe_1 = 0
        self.__gols_equipe_2 = 0
        self.__finalizado = False

    @property
    def numero(self) -> int:
        return self.__numero

    @numero.setter
    def numero(self, numero: int) -> None:
        if isinstance(numero, int):
            self.__numero = numero
        else:
            raise TypeError("Parâmetro numero deve ser um inteiro.")

    @property
    def local(self) -> str:
        return self.__local

    @local.setter
    def local(self, local: str) -> None:
        if isinstance(local, str):
            self.__local = local
        else:
            raise TypeError("Parâmetro local deve ser uma string.")

    @property
    def arbitro(self) -> Arbitro:
        return self.__arbitro

    @arbitro.setter
    def arbitro(self, arbitro: Arbitro) -> None:
        if isinstance(arbitro, Arbitro):
            self.__arbitro = arbitro
        else:
            raise TypeError(
                "Parâmetro arbitro deve ser uma instância de Arbitro."
            )

    @property
    def equipe_1(self) -> Equipe:
        return self.__equipe_1

    @equipe_1.setter
    def equipe_1(self, equipe_1: Equipe) -> None:
        if isinstance(equipe_1, Equipe):
            self.__equipe_1 = equipe_1
        else:
            raise TypeError(
                "Parâmetro equipe_1 deve ser uma instância de Equipe."
            )

    @property
    def equipe_2(self) -> Equipe:
        return self.__equipe_2

    @equipe_2.setter
    def equipe_2(self, equipe_2: Equipe) -> None:
        if isinstance(equipe_2, Equipe):
            self.__equipe_2 = equipe_2
        else:
            raise TypeError(
                "Parâmetro equipe_2 deve ser uma instância de Equipe."
            )

    @property
    def gols_equipe_1(self) -> int:
        return self.__gols_equipe_1

    @gols_equipe_1.setter
    def gols_equipe_1(self, gols_equipe_1: int) -> None:
        if isinstance(gols_equipe_1, int):
            self.__gols_equipe_1 = gols_equipe_1
        else:
            raise TypeError("Parâmetro gols_equipe_1 deve ser um inteiro.")

    @property
    def gols_equipe_2(self) -> int:
        return self.__gols_equipe_2

    @gols_equipe_2.setter
    def gols_equipe_2(self, gols_equipe_2: int) -> None:
        if isinstance(gols_equipe_2, int):
            self.__gols_equipe_2 = gols_equipe_2
        else:
            raise TypeError("Parâmetro gols_equipe_2 deve ser um inteiro.")

    @property
    def finalizado(self) -> bool:
        return self.__finalizado

    @finalizado.setter
    def finalizado(self, finalizado: bool) -> None:
        if isinstance(finalizado, bool):
            self.__finalizado = finalizado
        else:
            raise TypeError("Parâmetro finalizado deve ser um booleano.")

    def vencedor(self) -> Equipe:
        if self.__gols_equipe_1 > self.__gols_equipe_2:
            return self.__equipe_1
        elif self.__gols_equipe_1 < self.__gols_equipe_2:
            return self.__equipe_2
        else:
            return None

    def finaliza_jogo(self) -> None:
        self.__finalizado = True

        vencedor = self.vencedor()

        if not vencedor:
            self.__equipe_1.pontos += 1
            self.__equipe_2.pontos += 1
        else:
            vencedor.pontos += 3

    def pontos_vencedor(self) -> int:
        vencedor = self.vencedor()

        if vencedor:
            return vencedor.pontos
        return 0
