from typing import List

from imovel import Imovel


class Imobiliaria:
    def __init__(self) -> None:
        self.__imoveis: List[Imovel] = []

    @property
    def imoveis(self) -> List[Imovel]:
        return self.__imoveis

    def incluir_imovel(self, imovel_to_include: Imovel) -> None:
        if not isinstance(imovel_to_include, Imovel):
            return

        for imovel in self.__imoveis:
            if imovel.codigo == imovel_to_include.codigo:
                return

        self.__imoveis.append(imovel_to_include)

    def excluir_imovel(self, imovel: Imovel):
        if imovel in self.__imoveis:
            self.__imoveis.remove(imovel)
