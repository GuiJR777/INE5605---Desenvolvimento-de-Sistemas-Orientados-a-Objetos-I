from abstractControladorPessoas import AbstractControladorPessoas
from cliente import Cliente
from tecnico import Tecnico
from utils import is_already_registered_in_list


class ControladorPessoas(AbstractControladorPessoas):
    def __init__(self) -> None:
        self.__clientes = []
        self.__tecnicos = []

    @property
    def clientes(self) -> list:
        return self.__clientes

    @property
    def tecnicos(self) -> list:
        return self.__tecnicos

    def inclui_cliente(self, codigo: int, nome: str) -> Cliente:
        cliente_to_include = Cliente(codigo, nome)

        if not is_already_registered_in_list(
            list_to_check=self.clientes,
            codigo_to_check=cliente_to_include.codigo,
        ):
            self.__clientes.append(cliente_to_include)
            return cliente_to_include

    def inclui_tecnico(self, codigo: int, nome: str) -> Tecnico:
        tecnico_to_include = Tecnico(codigo, nome)

        if not is_already_registered_in_list(
            list_to_check=self.tecnicos,
            codigo_to_check=tecnico_to_include.codigo,
        ):
            self.__tecnicos.append(tecnico_to_include)
            return tecnico_to_include
