class Mobilia:
    def __init__(self, codigo: int, descricao: str) -> None:
        self.__codigo = codigo
        self.__descricao = descricao

    @property
    def codigo(self) -> int:
        return self.__codigo

    @codigo.setter
    def codigo(self, codigo: int) -> None:
        if isinstance(codigo, int):
            self.__codigo = codigo
        else:
            raise TypeError("codigo precisa ser inteiro")

    @property
    def descricao(self) -> str:
        return self.__descricao

    @descricao.setter
    def descricao(self, descricao: str) -> None:
        if isinstance(descricao, str):
            self.__descricao = descricao
        else:
            raise TypeError("descricao precisa ser uma string")
