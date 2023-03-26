"""Universidade Federal de Santa Catarina.
   CTC - Centro Tecnologico - http://ctc.ufsc.br
   INE - Departamento de Informatica e Estatistica - http://inf.ufsc.br

   Aluno: Guilherme J Ramires
"""


class CalculaCarta:
    def __init__(
        self,
        money_available,
        envelope_price,
        stamp_price,
        stamps_in_storage,
        envelope_in_storage,
    ) -> None:
        self.__money_available = money_available
        self.__envelope_price = envelope_price
        self.__stamp_price = stamp_price
        self.__stamps_in_storage = stamps_in_storage
        self.__envelope_in_storage = envelope_in_storage
        self.__letter_price = self.__envelope_price + self.__stamp_price
        self.__finished_letters = 0

    def letters_that_can_be_sent(self) -> int:
        self.__finished_letters += (
            self.__letters_that_can_be_sent_without_buying_anything()
        )
        self.__makes_stock_quantities_equal()
        self.__fills_stock_quantities()
        self.__makes_letters()

        return self.__finished_letters

    def __letters_that_can_be_sent_without_buying_anything(self) -> int:
        if self.__stamps_in_storage == 0 or self.__envelope_in_storage == 0:
            return 0

        letters = 0
        if self.__stamps_in_storage > self.__envelope_in_storage:
            letters = self.__envelope_in_storage

        elif self.__envelope_in_storage >= self.__stamps_in_storage:
            letters = self.__stamps_in_storage

        self.__stamps_in_storage -= letters
        self.__envelope_in_storage -= letters

        return letters

    def __makes_stock_quantities_equal(self) -> None:
        if self.__envelope_in_storage == 0 and self.__stamps_in_storage == 0:
            return

        if self.__envelope_in_storage > self.__stamps_in_storage:
            for _ in range(
                self.__envelope_in_storage - self.__stamps_in_storage
            ):
                self.__buy_stamps(1)

        elif self.__stamps_in_storage > self.__envelope_in_storage:
            for _ in range(
                self.__stamps_in_storage - self.__envelope_in_storage
            ):
                self.__buy_envelopes(1)

    def __buy_envelopes(self, quantity: int) -> None:
        if self.__money_available < quantity * self.__envelope_price:
            return

        self.__envelope_in_storage += quantity
        self.__money_available -= quantity * self.__envelope_price

    def __buy_stamps(self, quantity: int) -> None:
        if self.__money_available < quantity * self.__stamp_price:
            return

        self.__stamps_in_storage += quantity
        self.__money_available -= quantity * self.__stamp_price

    def __fills_stock_quantities(self) -> None:
        letters_can_buy = self.__money_available // self.__letter_price
        self.__buy_envelopes(letters_can_buy)
        self.__buy_stamps(letters_can_buy)

    def __makes_letters(self) -> None:
        while self.__envelope_in_storage > 0 and self.__stamps_in_storage > 0:
            self.__finished_letters += 1
            self.__envelope_in_storage -= 1
            self.__stamps_in_storage -= 1


RS = float(input())
PE = float(input())
PS = float(input())
QS = int(input())
QE = int(input())

# RS: quantia em dinheiro que uma pessoa tem para enviar cartas
# PE: preço de um envelope
# PS: preço de um selo
# QS: quantidade de selos que a pessoa já dispõe
# QE: quantidade de envelopes que a pessoa também já dispõe


# calcular a quandidade de cartas e armazenar na variavel: cartas
cartas = CalculaCarta(RS, PE, PS, QS, QE).letters_that_can_be_sent()

print(cartas)
