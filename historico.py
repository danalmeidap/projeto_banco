from datetime import datetime


class Historico:
    def __init__(self):
        self.__trancacoes = []

    @property
    def transacoes(self):
        return self.__transacoes

    def adiconar_transacao(self, transacao):
        self.__trancacoes.append
        (
            {
                "tipo": transacao.__class__.__name__,
                "valor": transacao.valor,
                "data": datetime.now().strftime("%d- %m- %Y %H:%M:%s")
            }
        )