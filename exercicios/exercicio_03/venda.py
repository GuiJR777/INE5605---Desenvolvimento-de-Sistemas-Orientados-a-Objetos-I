from cliente import Cliente
from pacote_viagem import PacoteViagem

class Venda:
    def __init__(self, codigo: int, cliente: Cliente, descricao: str, pacote: PacoteViagem, quantidade: int):
        if isinstance(codigo, int):
            self.__codigo = codigo 
        else:
            raise TypeError("codigo precisa ser inteiro")

        if isinstance(cliente, Cliente):
            self.__cliente = cliente 
        else:
            raise TypeError("cliente precisa ser da classe Cliente")    

        if isinstance(descricao, str):
            self.__descricao = descricao 
        else:
            raise TypeError("descricao precisa ser uma string")    

        if isinstance(pacote, PacoteViagem):
            self.__pacote = PacoteViagem 
        else:
            raise TypeError("pacote precisa ser da classe Cliente")

        if isinstance(quantidade, int):
            self.__quantidade = quantidade 
        else:
            raise TypeError("quantidade precisa ser inteiro")    


    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def codigo(self,codigo: int):
        if isinstance(codigo,int):
            self.__codigo = codigo
        else:
            raise TypeError("codigo deve ser inteiro")

    @property
    def cliente(self):
        return self.__cliente

    @cliente.setter
    def cliente(self,cliente: Cliente):
        if isinstance(cliente,Cliente):
            self.__cliente = cliente
        else:
            raise TypeError("cliente deve ser da classe Cliente")

    @property
    def descricao(self):
        return self.__descricao

    @descricao.setter
    def descricao(self,descricao: str):
        if isinstance(descricao,str):
            self.__descricao = descricao
        else:
            raise TypeError("descricao deve ser string")    

    @property
    def pacote(self):
        return self.__pacote

    @pacote.setter
    def pacote(self pacote: PacoteViagem):
        if isinstance (pacote,PacoteViagem):
            self.__codigo = pacote
        else:
            raise TypeError("pacote deve ser inteiro")  

    @property
    def quantidade(self):
        return self.__quantidade

    @quantidade.setter
    def quantidade(self,quantidade: int):
        if isinstance(quantidade,int):
            self.__quantidade = quantidade
        else:
            raise TypeError("quantidade deve ser inteiro")  

    def preco_total(self) -> float :
        return self.__pacote.custo_unitario * self.__quantidade                                    
