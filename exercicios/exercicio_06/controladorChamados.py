from abstractControladorChamados import AbstractControladorChamados
from tipoChamado import TipoChamado
from chamado import Chamado
from datetime import date as Date
from cliente import Cliente
from tecnico import Tecnico
from utils import is_already_registered_in_list


class ControladorChamados(AbstractControladorChamados):
    def __init__(self) -> None:
        self.__chamados = []
        self.__tipos_chamados = []

    def total_chamados_por_tipo(self, tipo: TipoChamado) -> int:
        return len(
            [chamado for chamado in self.__chamados if chamado.tipo == tipo]
        )

    def inclui_chamado(
        self,
        data: Date,
        cliente: Cliente,
        tecnico: Tecnico,
        titulo: str,
        descricao: str,
        prioridade: int,
        tipo: TipoChamado,
    ) -> Chamado:
        try:
            chamado_to_include = Chamado(
                data=self.__validate_parameter_type(data, "data", Date),
                cliente=self.__validate_parameter_type(
                    cliente, "cliente", Cliente
                ),
                tecnico=self.__validate_parameter_type(
                    tecnico, "tecnico", Tecnico
                ),
                titulo=self.__validate_parameter_type(titulo, "titulo", str),
                descricao=self.__validate_parameter_type(
                    descricao, "descricao", str
                ),
                prioridade=self.__validate_parameter_type(
                    prioridade, "prioridade", int
                ),
                tipo=self.__validate_parameter_type(tipo, "tipo", TipoChamado),
            )
        except TypeError:
            return None

        if not self.__chamado_is_already_registered(chamado_to_include):
            self.__chamados.append(chamado_to_include)

            return chamado_to_include

    def __validate_parameter_type(
        self, parameter: any, parameter_name: str, parameter_type: any
    ) -> None:
        if not isinstance(parameter, parameter_type):
            raise TypeError(
                f"{parameter_name} deve ser do tipo {parameter_type.__name__}"
            )
        return parameter

    def __chamado_is_already_registered(
        self, chamado_to_include: Chamado
    ) -> bool:
        for chamado in self.__chamados:
            if (
                chamado.data == chamado_to_include.data
                and chamado.cliente == chamado_to_include.cliente
                and chamado.tecnico == chamado_to_include.tecnico
                and chamado.tipo == chamado_to_include.tipo
            ):
                return True
        return False

    def inclui_tipochamado(
        self, codigo: int, nome: str, descricao: str
    ) -> TipoChamado:
        tipo_chamado_to_include = TipoChamado(codigo, nome, descricao)

        if not is_already_registered_in_list(
            list_to_check=self.__tipos_chamados,
            codigo_to_check=tipo_chamado_to_include.codigo,
        ):
            self.__tipos_chamados.append(tipo_chamado_to_include)

            return tipo_chamado_to_include

    @property
    def tipos_chamados(self):
        return self.__tipos_chamados
