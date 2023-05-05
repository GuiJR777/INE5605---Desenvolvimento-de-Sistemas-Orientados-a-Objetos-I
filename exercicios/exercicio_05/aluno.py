from abc import ABC, abstractmethod

from usuario_bu import UsuarioBU


MENSAGEM_DE_ACRESSIMO = 'Aluno de matricula "{matricula}"'


class Aluno(UsuarioBU, ABC):
    def __init__(
        self, cpf: int, dias_de_emprestimo: int, matricula: int
    ) -> None:
        super().__init__(cpf, dias_de_emprestimo)
        self.__matricula = matricula

    @property
    def matricula(self) -> int:
        return self.__matricula

    @matricula.setter
    def matricula(self, matricula: int) -> None:
        self.__matricula = matricula

    @abstractmethod
    def emprestar(self, titulo_livro: str) -> str:
        mensagem = MENSAGEM_DE_ACRESSIMO.format(matricula=self.matricula)

        return f"{mensagem} {super().emprestar(titulo_livro)}"

    @abstractmethod
    def devolver(self, titulo_livro: str) -> str:
        mensagem = MENSAGEM_DE_ACRESSIMO.format(matricula=self.matricula)

        return f"{mensagem} {super().devolver(titulo_livro)}"
