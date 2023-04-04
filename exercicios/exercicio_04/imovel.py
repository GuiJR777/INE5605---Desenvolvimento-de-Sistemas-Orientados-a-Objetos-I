from typing import List

from locatario import Locatario
from locador import Locador
from mobilia import Mobilia
from utils import validate_parameter_with_type


class Imovel:
    def __init__(
        self, codigo: int, descricao: str, valor: float, locador: Locador
    ) -> None:
        self.__codigo = validate_parameter_with_type(codigo, int)
        self.__descricao = validate_parameter_with_type(descricao, str)
        self.__valor = validate_parameter_with_type(valor, float)
        self.__locador = validate_parameter_with_type(locador, Locador)
        self.__locatarios: List[Locatario] = []
        self.__mobilias: List[Mobilia] = []

    @property
    def codigo(self) -> int:
        return self.__codigo

    @codigo.setter
    def codigo(self, codigo: int) -> None:
        self.__codigo = validate_parameter_with_type(codigo, int)

    @property
    def descricao(self) -> str:
        return self.__descricao

    @descricao.setter
    def descricao(self, descricao: str) -> None:
        self.__descricao = validate_parameter_with_type(descricao, str)

    @property
    def valor(self) -> float:
        return self.__valor

    @valor.setter
    def valor(self, valor: float) -> None:
        self.__valor = validate_parameter_with_type(valor, float)

    @property
    def locador(self) -> Locador:
        return self.__locador

    @locador.setter
    def locador(self, locador: Locador) -> None:
        self.__locador = validate_parameter_with_type(locador, Locador)

    @property
    def locatarios(self) -> List[Locatario]:
        return self.__locatarios

    def incluir_locatario(self, locatario: Locatario) -> None:
        valid_locatorio = validate_parameter_with_type(locatario, Locatario)

        for locatario in self.__locatarios:
            if locatario.codigo == valid_locatorio.codigo:
                return

        self.__locatarios.append(valid_locatorio)

    def excluir_locatario(self, codigo_locatario: int) -> None:
        for locatario in self.__locatarios:
            if locatario.codigo == codigo_locatario:
                self.__locatarios.remove(locatario)
                break

    @property
    def mobilias(self) -> List[Mobilia]:
        return self.__mobilias

    def incluir_mobilia(self, codigo_mobilia: int, descricao: str) -> None:
        for mobilia in self.__mobilias:
            if mobilia.codigo == codigo_mobilia:
                return

        mobilia_to_include = Mobilia(codigo_mobilia, descricao)

        self.__mobilias.append(mobilia_to_include)

    def excluir_mobilia(self, codigo_mobilia: int) -> None:
        for mobilia in self.__mobilias:
            if mobilia.codigo == codigo_mobilia:
                self.__mobilias.remove(mobilia)
                break

    def find_locatario_by_codigo(self, codigo_locatario: int) -> Locatario:
        for locatario in self.__locatarios:
            if locatario and locatario.codigo == codigo_locatario:
                return locatario
        return None
