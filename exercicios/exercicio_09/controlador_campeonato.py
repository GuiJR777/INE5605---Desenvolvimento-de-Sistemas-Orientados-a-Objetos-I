from typing import List
from jogo_duplicado_exception import JogoDuplicadoException

from jogo import Jogo


class ControladorCampeonato:
    def __init__(self) -> None:
        self.__jogos = []

    @property
    def jogos(self) -> List[Jogo]:
        return self.__jogos

    def busca_jogo_por_numero(self, numero: int) -> Jogo:
        for jogo in self.__jogos:
            if jogo.numero == numero:
                return jogo

        raise ValueError(f"Jogo com número {numero} não existe.")

    def add_jogo(self, jogo: Jogo) -> None:
        if not isinstance(jogo, Jogo):
            return None

        for jogo_cadastrado in self.__jogos:
            if jogo_cadastrado.numero == jogo.numero:
                raise JogoDuplicadoException()

        self.__jogos.append(jogo)

    def remove_jogo(self, numero) -> None:
        if not isinstance(numero, int):
            return None

        for jogo in self.__jogos:
            if jogo.numero == numero:
                index = self.__jogos.index(jogo)
                return self.__jogos.pop(index)
        return None

    def classificacao_campeonato(self) -> List[Jogo]:
        equipes = []

        for jogo in self.__jogos:
            if jogo.equipe_1 not in equipes:
                equipes.append(jogo.equipe_1)
            if jogo.equipe_2 not in equipes:
                equipes.append(jogo.equipe_2)
        if equipes:
            equipes.sort(key=lambda equipe: equipe.pontos, reverse=True)
        return equipes
