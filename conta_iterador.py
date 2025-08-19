from typing import List

class ContaIterador:
    def __init__(self, contas: List):
        self.__contas = contas
        self.__indice = 0

    def __iter__(self):
        return self

    def __next__(self):
        try:
            conta = self.__contas[self.__indice]
            self.__indice += 1
            return conta
        except IndexError:
            raise StopIteration