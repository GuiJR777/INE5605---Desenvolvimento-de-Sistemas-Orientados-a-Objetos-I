from typing import List

from jogador import Jogador
from pessoa import Pessoa


class Equipe:
    def __init__(self, pais: str, tecnico: Pessoa) -> None:
        self.__pais = pais
        self.__tecnico = tecnico
        self.__jogadores = []
        self.__pontos = 0

    @property
    def pais(self) -> str:
        return self.__pais

    @pais.setter
    def pais(self, pais: str) -> None:
        if isinstance(pais, str):
            self.__pais = pais
        else:
            raise TypeError("")

    @property
    def tecnico(self) -> Pessoa:
        return self.__tecnico

    @tecnico.setter
    def tecnico(self, tecnico: Pessoa) -> None:
        if isinstance(tecnico, Pessoa):
            self.__tecnico = tecnico
        else:
            raise TypeError("")

    @property
    def pontos(self) -> int:
        return self.__pontos

    @pontos.setter
    def pontos(self, pontos: int) -> None:
        if isinstance(pontos, int):
            self.__pontos = pontos
        else:
            raise TypeError("")

    @property
    def jogadores(self) -> List[Jogador]:
        return self.__jogadores

    def add_jogador(self, jogador: Jogador) -> None:
        if not isinstance(jogador, Jogador):
            return None

        for jogador_cadastrado in self.__jogadores:
            if (
                jogador_cadastrado.numero_camisa == jogador.numero_camisa
                or jogador_cadastrado.nome == jogador.nome
            ):
                return None

        if len(self.jogadores) >= 11:
            return None

        self.__jogadores.append(jogador)

    def remove_jogador(self, jogador: Jogador) -> None:
        if not isinstance(jogador, Jogador):
            return None

        if jogador not in self.__jogadores:
            return None

        index = self.__jogadores.index(jogador)
        return self.__jogadores.pop(index)

    def total_cartoes_time(self) -> int:
        total_cartoes = 0

        for jogador in self.__jogadores:
            total_cartoes += jogador.numero_cartoes_amarelos

        return total_cartoes
