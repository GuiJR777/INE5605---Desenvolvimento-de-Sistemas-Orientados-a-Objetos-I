from utils import validate_parameter_with_type


class Locador:
    def __init__(
        self, cpf: int, nome: str, telefone: int, endereco: str
    ) -> None:
        self.__cpf = validate_parameter_with_type(cpf, int)
        self.__nome = validate_parameter_with_type(nome, str)
        self.__telefone = validate_parameter_with_type(telefone, int)
        self.__endereco = validate_parameter_with_type(endereco, str)

    @property
    def cpf(self) -> int:
        return self.__cpf

    @cpf.setter
    def cpf(self, cpf: int) -> None:
        self.__cpf = validate_parameter_with_type(cpf, int)

    @property
    def nome(self) -> str:
        return self.__nome

    @nome.setter
    def nome(self, nome: str) -> None:
        self.__nome = validate_parameter_with_type(nome, str)

    @property
    def telefone(self) -> int:
        return self.__telefone

    @telefone.setter
    def telefone(self, telefone: int) -> None:
        self.__telefone = validate_parameter_with_type(telefone, int)

    @property
    def endereco(self) -> str:
        return self.__endereco

    @endereco.setter
    def endereco(self, endereco: str) -> None:
        self.__endereco = validate_parameter_with_type(endereco, str)
