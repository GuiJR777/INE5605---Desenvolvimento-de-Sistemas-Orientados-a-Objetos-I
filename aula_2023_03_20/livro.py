from cliente import Cliente


class Livro:
    def __init__(self, title: str) -> None:
        self.__title = title
        self.__cliente: Cliente = None

    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str) -> None:
        if isinstance(title, str):
            self.__title = title
        else:
            ValueError("Parâmetro title deve ser uma string.")

    @property
    def cliente(self) -> str:
        return self.__cliente

    @cliente.setter
    def cliente(self, cliente: Cliente) -> None:
        if isinstance(cliente, Cliente):
            self.__cliente = cliente
        else:
            ValueError("Parâmetro cliente deve ser do tipo Cliente.")
