from abc import ABC, abstractmethod
from conta import Conta

class Transacao(ABC):
    @property
    @abstractmethod
    def valor(self):
        pass

    @abstractmethod
    def registrar(self, valor):
        pass


class Saque(Transacao):
    def __init__(self, valor):
        self.__valor = valor
    
    @property
    def valor(self):
        return self.__valor

    def registrar(self, conta:Conta):
        sucesso_transacao = conta.sacar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)


class Deposito(Transacao):
    def __init__(self, valor):
        self.__valor = valor

    @property
    def valor(self):
        return self.__valor

    def registrar(self, conta:Conta):
        sucesso_transacao = conta.depositar(self.valor)

        if sucesso_transacao:
            conta.historico .adiconar_transacao(self)       