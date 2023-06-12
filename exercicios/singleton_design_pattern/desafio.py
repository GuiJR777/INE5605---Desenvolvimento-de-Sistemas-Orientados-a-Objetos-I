# Factory Method Desing Pattern
from typing import Self


class NaoRepetivel:
    def __init__(self, nome) -> None:
        self.nome = nome


class NaopRepetivelCreator:
    def __init__(self) -> None:
        self.__instance = None

    def factory_method(self) -> NaoRepetivel:
        if not self.__instance:
            self.__instance = NaoRepetivel("É a instancia 1")
        return self.__instance


# Singleton Desing Pattern
class Singleton:
    __instance = None

    @classmethod
    def __new__(cls, *args, **kwargs) -> Self:
        if not cls.__instance:
            cls.__instance = object.__new__(cls)
        return cls.__instance

    def __init__(self, nome) -> None:
        self.nome = nome
