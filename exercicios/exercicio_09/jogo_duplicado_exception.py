class JogoDuplicadoException(Exception):
    def __init__(self) -> None:
        super().__init__("Jogo já cadastrado.")
