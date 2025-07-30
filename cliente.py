from transacao import Transacao
from conta import Conta
    
class Cliente:
    def __init__(self, endereco):
        self.__endereco = endereco
        self.__contas = []

    @property
    def endereco(self):
        return self.__endereco

    @endereco.setter
    def endereco(self, novo_endereco):
        if not isinstance(novo_endereco, str):
            raise ValueError("O endereço precisa ser uma string não vazia")
        self.__endereco = novo_endereco


    @property
    def contas(self):
        return self.__contas

    def realizar_transacao(self, conta, transacao:Transacao):
        transacao.registrar(conta)

    def adiconar_conta(self, conta:Conta):
        self.__contas.append(conta)
    