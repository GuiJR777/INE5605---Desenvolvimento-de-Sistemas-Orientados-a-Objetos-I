"""Universidade Federal de Santa Catarina.
   CTC - Centro Tecnologico - http://ctc.ufsc.br
   INE - Departamento de Informatica e Estatistica - http://inf.ufsc.br

   Aluno: Guilherme J Ramires
"""

class Ordenacao():

    def __init__(self, list_to_order: list) -> None:
        """Recebe o array com o conteudo a ser ordenado"""
        self.__list_to_order = list_to_order
        self.__ordered_list = self.__list_to_order.copy()

    def ordena(self) -> None:
        """Realiza a ordenacao do conteudo do array recebido no construtor"""
        for index, number in enumerate(self.__list_to_order):
            new_index = 0
            while number > self.__ordered_list[new_index]:
                new_index += 1

            del(self.__ordered_list[index])
            self.__ordered_list.insert(new_index, number)


        return self.to_string()

    def to_string(self) -> str:
        """Converte o conteudo do array em String formatado
           Exemplo:
           Para o conteudo do array: [1,2,3,4,5]
           Retorna: "1,2,3,4,5"
           @return String com o conteudo do array formatado
     """

        return ','.join([str(number) for number in self.__ordered_list])


if __name__ == '__main__':
    # Instancia a classe de ordenacao
    ordenacao = Ordenacao([5, 4, 3, 2, 1, 1, 2, 3, 4, 5])

    # Realiza a ordenacao
    print(ordenacao.ordena())
