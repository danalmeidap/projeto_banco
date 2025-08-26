from conta import Conta
from saque import Saque
import datetime


class ContaCorrente(Conta):
    def __init__(
        self,
        numero,
        cliente,
        limite=500,
        limite_saques=3,
        transacoes=0,
        limite_transacoes=10,
    ):
        super().__init__(numero, cliente)
        self.__limite = limite
        self.__limite_saques = limite_saques
        self.__transacoes = transacoes
        self.__limite_transacoes = limite_transacoes
        self.__data_ultimna_transacao = datetime.date.today()

    def sacar(self, valor):
        hoje = datetime.date.today()
        if hoje != self.__data_ultimna_transacao:
            self.__transacoes = 0
            self.__data_ultimna_transacao = hoje

        numero_saques = len(
           [
            transacao
            for transacao in self.historico.transacoes
            if transacao["tipo"] == Saque.__name__ and transacao["data"][0:10] == hoje.strftime("%d-%m-%Y")
           ]
        )

        if self.__transacoes >= self.__limite_transacoes:
            print("Operação inválida. Número máximo de transações excedido.")
            return False
        elif valor > self.__limite:
            print("Operação inválida. Valor do saque excedeu o limite.")
            return False
        elif numero_saques >= self.__limite_saques:
            print("Operação inválida. Número máximo de saques excedido.")
            return False
        else:
            self.__transacoes += 1
            return super().sacar(valor)

    def depositar(self, valor):
        hoje = datetime.date.today()
        if hoje != self.__data_ultimna_transacao:
            self.__transacoes = 0
            self.__data_ultimna_transacao = hoje

        if self.__transacoes >= self.__limite_transacoes:
            print("Operação inválida. Número máximo de transações excedido.")
            return False
        else:
            self.__transacoes += 1
            return super().depositar(valor)

    def __str__(self):
        return f"""
            Agencia:\t{self.agencia}
            C/C:\t\t{self.numero}
            Titular:\t\t{self.cliente.nome} 
        """
