class Cliente:
    def __init__(self, nome: str, fone: int, email: str) -> None:
        if isinstance(nome, str):
            self.__nome = nome
        else:
            raise TypeError("Nome deve ser uma string")

        if isinstance(fone, int):
            self.__fone = fone
        else:
            raise TypeError("Fone deve ser um inteiro")

        if isinstance(email, str):
            self.__email = email
        else:
            raise TypeError("Email deve ser uma string")

    @property
    def nome(self) -> str:
        return self.__nome

    @nome.setter
    def nome(self, nome: str) -> None:
        if isinstance(nome, str):
            self.__nome = nome
        else:
            raise TypeError("Nome deve ser uma string")

    @property
    def fone(self) -> int:
        return self.__fone

    @fone.setter
    def fone(self, fone: int) -> None:
        if isinstance(fone, int):
            self.__fone = fone
        else:
            raise TypeError("Fone deve ser um inteiro")

    @property
    def email(self) -> str:
        return self.__email

    @email.setter
    def email(self, email: str) -> None:
        if isinstance(email, str):
            self.__email = email
        else:
            raise TypeError("Email deve ser uma string")
