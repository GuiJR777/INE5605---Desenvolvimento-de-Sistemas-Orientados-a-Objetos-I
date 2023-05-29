class Pessoa:
    def __init__(self, nome: str, telefone: str) -> None:
        self.__nome = nome
        self.__telefone = telefone

    @property
    def nome(self) -> str:
        return self.__nome

    @nome.setter
    def nome(self, nome: str) -> None:
        if isinstance(nome, str):
            self.__nome = nome
        else:
            raise TypeError("Parâmetro nome deve ser uma string.")

    @property
    def telefone(self) -> str:
        return self.__telefone

    @telefone.setter
    def telefone(self, telefone: str) -> None:
        if isinstance(telefone, str):
            self.__telefone = telefone
        else:
            raise TypeError("Parâmetro telefone deve ser uma string.")
