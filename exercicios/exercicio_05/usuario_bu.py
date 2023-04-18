from abc import ABC, abstractmethod


MENSAGEM_DE_EMPRESTIMO = (
    "pegou emprestado o livro: {titulo} com {dias} dias de prazo"
)
MENSAGEM_DE_DEVOLUCAO = "devolveu o livro: {titulo}"


class UsuarioBU(ABC):
    def __init__(self, cpf: int, dias_de_emprestimo: int = 0) -> None:
        self.__cpf = cpf
        self.__dias_de_emprestimo = dias_de_emprestimo

    @property
    def cpf(self) -> int:
        return self.__cpf

    @cpf.setter
    def cpf(self, cpf) -> None:
        self.__cpf = cpf

    @property
    def dias_de_emprestimo(self) -> int:
        return self.__dias_de_emprestimo

    @dias_de_emprestimo.setter
    def dias_de_emprestimo(self, dias_de_emprestimo: int) -> None:
        self.__dias_de_emprestimo = dias_de_emprestimo

    @abstractmethod
    def emprestar(self, titulo_livro: str) -> str:
        return MENSAGEM_DE_EMPRESTIMO.format(
            titulo=titulo_livro, dias=self.dias_de_emprestimo
        )

    @abstractmethod
    def devolver(self, titulo_livro: str) -> str:
        return MENSAGEM_DE_DEVOLUCAO.format(titulo=titulo_livro)
