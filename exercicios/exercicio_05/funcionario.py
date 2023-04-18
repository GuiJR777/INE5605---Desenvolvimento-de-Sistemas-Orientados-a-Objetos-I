from abc import ABC, abstractmethod

from usuario_bu import UsuarioBU

MENSAGEM_DE_ACRESSIMO = 'do departamento "{departamento}"'


class Funcionario(UsuarioBU, ABC):
    def __init__(
        self, departamento: str, cpf: int, dias_de_emprestimo: int
    ) -> None:
        super().__init__(cpf, dias_de_emprestimo)
        self.__departamento = departamento

    @property
    def departamento(self) -> str:
        return self.__departamento

    @departamento.setter
    def departamento(self, departamento: str) -> None:
        self.__departamento = departamento

    @abstractmethod
    def emprestar(self, titulo_livro: str) -> str:
        mensagem = MENSAGEM_DE_ACRESSIMO.format(departamento=self.departamento)

        return f"{mensagem} {super().emprestar(titulo_livro)}"

    @abstractmethod
    def devolver(self, titulo_livro: str) -> str:
        mensagem = MENSAGEM_DE_ACRESSIMO.format(departamento=self.departamento)

        return f"{mensagem} {super().devolver(titulo_livro)}"
