from conta import Conta
from transacao import Saque

class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite=500, limite_saques=3):
        super().__init__(numero, cliente)
        self.__limite = limite
        self.__limite_sauqes = limite_saques

    def sacar(self, valor):
        numero_saques = len([transacao for transacao  in self.historico.transacoes if transacao['tipo'] == Saque.__name__])
        excedeu_limite = valor > self.__limite
        excedeu_saques = numero_saques > self.__limite_saques

        if excedeu_limite:
            print("Operação inválida. Valor do saque excedeu limite")
        elif excedeu_saques:
            print("Operação inválida. Numero máximo de sauqes excedido")
        else:
            return super().sacar(valor)
        return False

    def __str__(self):
        return f"""
            Agencia:\t{self.agencia}
            C/C:\t\t{self.numero}
            Titular:\t\t{self.cliente.nome} 
        """