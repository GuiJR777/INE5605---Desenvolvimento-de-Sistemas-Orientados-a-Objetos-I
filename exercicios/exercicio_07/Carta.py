from AbstractCarta import AbstractCarta
from Personagem import Personagem


class Carta(AbstractCarta):
    def __init__(self, personagem: Personagem) -> None:
        if isinstance(personagem, Personagem):
            self.__personagem = personagem

    """
    Soma e retorna todos os valores dos atributos do personagem da Carta
    @return Retorna o somatorio de todos os atributos do personagem da Carta
    """

    def valor_total_carta(self) -> int:
        personagem = self.__personagem
        sum = (
            personagem.energia
            + personagem.habilidade
            + personagem.resistencia
            + personagem.velocidade
        )
        return sum

    @property
    def personagem(self) -> Personagem:
        return self.__personagem
