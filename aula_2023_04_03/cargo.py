class Cargo:
    def __init__(self, salario: float, descricao: str) -> None:
        self.__salario = salario
        self.__descricao = descricao

    @property
    def salario(self) -> float:
        return self.__salario

    @salario.setter
    def salario(self, salario: float) -> None:
        if isinstance(salario, float):
            self.__salario = salario
        else:
            raise TypeError("")

    @property
    def descricao(self) -> str:
        return self.__descricao

    @descricao.setter
    def descricao(self, descricao: str) -> None:
        if isinstance(descricao, str):
            self.__descricao = descricao
        else:
            raise TypeError("")
