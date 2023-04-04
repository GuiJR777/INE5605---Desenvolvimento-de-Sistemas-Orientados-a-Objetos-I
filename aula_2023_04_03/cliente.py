from typing import Self
from pessoa import Pessoa


class Cliente(Pessoa):
    def __init__(self, nome: str, cpf: str, codigo: int) -> None:
        super().__init__(nome, cpf)
        self.__codigo = codigo

    @property
    def codigo(self) -> None:
        return self.__codigo

    @codigo.setter
    def codigo(self, codigo: int) -> None:
        self.__codigo = codigo
