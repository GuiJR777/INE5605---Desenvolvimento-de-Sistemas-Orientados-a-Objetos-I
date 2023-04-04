from pessoa import Pessoa


class Aluno(Pessoa):
    def __init__(self, nome: str, matricula: int) -> None:
        super().__init__(nome)
        self.matricula = matricula
