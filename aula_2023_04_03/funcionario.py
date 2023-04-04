from typing import List

from cargo import Cargo
from dependente import Dependente
from pessoa import Pessoa


class Funcionario(Pessoa):
    def __init__(self, nome: str, cpf: str, cargo: Cargo) -> None:
        super().__init__(nome, cpf)
        self.__cargo = cargo
        self.__dependentes: List[Dependente] = []

    def add_dependente(self, nome: str, cpf: str) -> None:
        if isinstance(nome, str) and isinstance(cpf, str):
            dependente_to_add = Dependente(nome, cpf)

            if dependente_to_add not in self.__dependentes:
                self.__dependentes.append(dependente_to_add)

    def remove_dependente(self, cpf_to_remove: str) -> None:
        for dependente in self.__dependentes:
            if dependente.cpf == cpf_to_remove:
                self.__dependentes.remove(dependente)
