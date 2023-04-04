from pagina import Pagina


class Livro:
    def __init__(
        self,
        titulo: str,
        resumo: str,
        texto_primeira_pagina: str,
        numero: int = 1,
    ) -> None:
        self.titulo = titulo
        self.resumo = resumo
        self.paginas = [
            Pagina(numero, texto_primeira_pagina),
        ]

    def add_pagina(self, numero: int, texto: str) -> None:
        self.paginas.append(Pagina(numero, texto))
