from pessoa import Pessoa


class Arbitro(Pessoa):
    def __init__(
        self, nome: str, telefone: str, nacionalidade: str, numero_jogos: int
    ) -> None:
        super().__init__(nome, telefone)
        self.__nacionalidade = nacionalidade
        self.__numero_jogos = numero_jogos

    @property
    def nacionalidade(self) -> str:
        return self.__nacionalidade

    @nacionalidade.setter
    def nacionalidade(self, nacionalidade: str) -> None:
        if isinstance(nacionalidade, str):
            self.__nacionalidade = nacionalidade
        else:
            raise TypeError("Parâmetro nacionalidade deve ser uma string.")

    @property
    def numero_jogos(self) -> int:
        return self.__numero_jogos

    @numero_jogos.setter
    def numero_jogos(self, numero_jogos: int) -> None:
        if isinstance(numero_jogos, int):
            self.__numero_jogos = numero_jogos
        else:
            raise TypeError("Parâmetro numero_jogos deve ser um inteiro.")
