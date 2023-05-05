from pessoa import Pessoa


class Cliente(Pessoa):
    def __init__(self, nome: str, codigo: int) -> None:
        super().__init__(nome, codigo)
