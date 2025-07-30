from cliente import Cliente


class Pessoa_Fisica(Cliente):
    def __init__(self, nome, data_nascimento, cpf, endereco):
        super().__init__(endereco)
        self.__nome = nome
        self.__data_nascimento = data_nascimento
        self.__cpf = cpf

    @property
    def nome(self):
        return self.__nome

    @property
    def data_nascimento(self):
        return self.__data_nascimento

    @property
    def cpf(self):
        return self.__cpf

    @nome.setter
    def nome(self, novo_nome):
        if not isinstance(novo_nome, str) or not novo_nome.strip():
            raise TypeError("O nome precisa ser uma string não vazia.")
        self.__nome = novo_nome

    @data_nascimento.setter
    def data_nascimento(self, nova_data):
        if not isinstance(nova_data, str) or not nova_data.strip():
            raise ValueError(
                "Data de nascimento deve ser uma string não vazia."
            )
        self.__data_nascimento = nova_data

    @cpf.setter
    def cpf(self, novo_cpf):
        if not isinstance(novo_cpf, str) or len(novo_cpf) != 11:
            raise ValueError("CPF inválido.")
        self.__cpf = novo_cpf
