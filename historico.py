from datetime import datetime


class Historico:
    def __init__(self):
        self.__transacoes = []

    @property
    def transacoes(self):
        return  self.__transacoes

    def adicionar_transacao(self, transacao):
        self.__transacoes.append(
        {
        "tipo": transacao.__class__.__name__,
        "valor": transacao.valor,
        "data": datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        }
        )
        

    def gerar_relatorio(self, tipo_transacao=None):
        if not tipo_transacao:
            return self.__transacoes
        for transacao in self.__transacoes:
            if transacao["tipo"] == tipo_transacao:
                yield transacao