from historico import Historico

class Conta:
    def __init__(self, numero, cliente):
        self.__saldo = 0
        self.__numero = 0
        self.__agencia = "0001"
        self.__cliente = cliente
        self.__historico = Historico()


    @classmethod
    def nova_conta(cls, numero, cliente):
        return cls(numero, cliente)

    @property
    def saldo(self):
        return self.__saldo

    @property
    def numero(self):
        return self.__numero

    @property
    def agencia(self):
        return self.__agencia
    
    @property
    def cliente(self):
        return self.__cliente

    @property
    def historico(self):
        return self.__historico

    def sacar(self, valor):
        saldo = self.__saldo
        excedido = valor > saldo
         
        if excedido:
            print("Operação falhou, você não possue saldo")

        elif valor > 0:
            self__saldo -= valor
            print("Operação concluida com sucesso")
            return True
        else:
            print("Operação falhou, valor informado inválido")
        return False
    
    def depositar(self, valor):
        if valor < 0 :
            print("Operação falhou, valor não pode ser menor que zero")
            return False
        self.__saldo += valor
        print("Depósito realizado com sucesso")
        return True

    
            