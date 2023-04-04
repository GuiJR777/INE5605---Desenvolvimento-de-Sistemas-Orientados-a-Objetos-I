from imovel import Imovel
from locador import Locador


minha_casa = Imovel(
    123, "minha casa", 70.0, Locador(123, "John Due", 123, "Rua")
)

minha_casa.incluir_mobilia(321, "copo")
minha_casa.incluir_mobilia(321, "copo")

print(minha_casa.mobilias)
