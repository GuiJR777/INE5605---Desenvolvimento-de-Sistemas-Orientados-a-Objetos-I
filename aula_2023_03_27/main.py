# Exemplo de uso de classes em uma Composição

# from livro import Livro


# harry_potter_1 = Livro(
#     'Harry Potter e a Pedra Filosofal',
#     'Um menino que descobre que é um bruxo',
#     'Na rua dos alfeneiros, número 4, vive um menino chamado Harry Potter'
#     )

# harry_potter_2 = Livro(
#     'Harry Potter e a Câmara Secreta',
#     'Segundo ano de Harry Potter',
#     'Dobby, o elfo doméstico, aparece na porta da casa dos Dursley'
#     )


# harry_potter_1.add_pagina(2, 'Harry Potter é o menino sobrevivente de Lord Voldemort')



# Exemplo de uso de classes em uma Herança

from aluno import Aluno


aluno_1 = Aluno("Jão", 123456)

print(f"Aluno de matrícula {aluno_1.matricula} possui nome {aluno_1.nome}")
