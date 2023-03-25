class PacoteViagem:
    def __init__(self, origem: str, destino: str, duracao: int, custo_unitario: int) -> None:
        if isinstance(origem, str):
            self.__origem = origem
        else:
            raise TypeError("Origem deve ser uma string")

        if isinstance(destino, str):
            self.__destino = destino
        else:
            raise TypeError("Destino deve ser uma string")

        if isinstance(duracao, int):
            self.__duracao = duracao
        else:
            raise TypeError("Duração deve ser um inteiro")

        if isinstance(custo_unitario, int):
            self.__custo_unitario = custo_unitario
        else:
            raise TypeError("Custo unitário deve ser um inteiro")

        @property
        def origem(self) -> str:
            return self.__origem

        @origem.setter
        def origem(self, origem: str) -> None:
            if isinstance(origem, str):
                self.__origem = origem
            else:
                raise TypeError("Origem deve ser uma string")

        @property
        def destino(self) -> str:
            return self.__destino

        @destino.setter
        def destino(self, destino: str) -> None:
            if isinstance(destino, str):
                self.__destino = destino
            else:
                raise TypeError("Destino deve ser uma string")

        @property
        def duracao(self) -> int:
            return self.__duracao

        @duracao.setter
        def duracao(self, duracao: int) -> None:
            if isinstance(duracao, int):
                self.__duracao = duracao
            else:
                raise TypeError("Duração deve ser um inteiro")

        @property
        def custo_unitario(self) -> int:
            return self.__custo_unitario

        @custo_unitario.setter
        def custo_unitario(self, custo_unitario: int) -> None:
            if isinstance(custo_unitario, int):
                self.__custo_unitario = custo_unitario
            else:
                raise TypeError("Custo unitário deve ser um inteiro")
