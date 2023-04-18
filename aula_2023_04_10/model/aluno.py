class Aluno:
    def __init__(self, matricula: str) -> None:
        self.__matricula = matricula

    @property
    def matricula(self) -> str:
        return self.__matricula

    @matricula.setter
    def matricula(self, matricula: str) -> None:
        if isinstance(matricula, str):
            self.__matricula = matricula
        else:
            raise TypeError("")
