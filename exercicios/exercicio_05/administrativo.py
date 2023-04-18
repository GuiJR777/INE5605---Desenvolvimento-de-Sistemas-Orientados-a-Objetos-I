from funcionario import Funcionario


TYPE = "Funcionario administrativo"
DIAS_DE_EMPRESTIMO = 10


class Administrativo(Funcionario):
    def __init__(self, departamento: str, cpf: int) -> None:
        super().__init__(departamento, cpf, DIAS_DE_EMPRESTIMO)

    def emprestar(self, titulo_livro: str) -> str:
        return f"{TYPE} {super().emprestar(titulo_livro)}"

    def devolver(self, titulo_livro: str) -> str:
        return f"{TYPE} {super().devolver(titulo_livro)}"
