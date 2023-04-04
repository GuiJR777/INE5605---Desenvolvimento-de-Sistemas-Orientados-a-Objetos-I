class Locatario:
    def __init__(self, codigo: int, nome: str, telefone: int) -> None:
        self.__codigo = codigo
        self.__nome = nome
        self.__telefone = telefone

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
    def nome(self) -> str:
        return self.__nome

    @nome.setter
    def nome(self, nome: str) -> None:
        if isinstance(nome, str):
            self.__nome = nome
        else:
            raise TypeError("nome precisa ser uma string")

    @property
    def telefone(self) -> int:
        return self.__telefone

    @telefone.setter
    def telefone(self, telefone: int) -> None:
        if isinstance(telefone, int):
            self.__telefone = telefone
        else:
            raise TypeError("telefone precisa ser um inteiro")
