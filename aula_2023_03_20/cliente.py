class Cliente:
    def __init__(self, rg: int, nome: str) -> None:
        self.__rg = rg
        self.__nome = nome

    @property
    def rg(self) -> int:
        return self.__rg

    @rg.setter
    def rg(self, rg: int) -> None:
        if isinstance(rg, int):
            self.__rg = rg
        else:
            raise ValueError("Parâmetro RG deve ser inteiro.")

    @property
    def nome(self) -> str:
        return self.__nome

    @nome.setter
    def nome(self, nome: str) -> None:
        if isinstance(nome, str):
            self.__nome = nome
        else:
            raise ValueError("Parâmetro NOME deve ser inteiro.")
