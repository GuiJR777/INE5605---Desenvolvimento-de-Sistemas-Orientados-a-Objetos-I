from desafio import NaopRepetivelCreator, Singleton


creator = NaopRepetivelCreator()
instancia_1 = creator.factory_method()
instancia_2 = creator.factory_method()

print(instancia_1.nome, instancia_2.nome)

instancia_de_singleton_1 = Singleton("Instancia 1")
print(instancia_de_singleton_1.nome)

instancia_de_singleton_2 = Singleton("Instancia 2")
print(instancia_de_singleton_2.nome)

