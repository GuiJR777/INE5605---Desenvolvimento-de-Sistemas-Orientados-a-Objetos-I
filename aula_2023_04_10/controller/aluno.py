from model.aluno import Aluno
from views.aluno import AlunoView


class AlunosController:
    def __init__(self) -> None:
        self.__alunos: list[Aluno] = []
        self.__tela_aluno = AlunoView(self)

    def include(self, aluno: Aluno) -> None:
        self.__alunos.append(aluno)

    def list_all(self) -> list[Aluno]:
        return self.__alunos

    def list(self, matricula: str) -> Aluno:
        for aluno in self.__alunos:
            if aluno.matricula == matricula:
                return aluno
        return None

    def update(self, aluno: Aluno) -> None:
        for index in range(len(self.__alunos)):
            if self.__alunos[index].matricula == aluno.matricula:
                self.__alunos[index] = aluno
                break

    def delete(self, matricula: str) -> None:
        for index in range(len(self.__alunos)):
            if self.__alunos[index].matricula == matricula:
                self.__alunos.pop(index)
                break
