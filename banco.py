from utils import check_float


def depositar(valor):
    if check_float(valor):
        global saldo, extrato
        saldo += valor
        extrato += 'Depósito: R$ {:.2f}\n'.format(valor)
        print('Depósito realizado com sucesso!')
    else:
        print('Valor inválido para depósito.')


def sacar(valor):
    pass


def exibir_extrato(valor):
    pass



saldo = 0.0
limite = 500.0
extrato = ''
numero_saques = 0
LIMITE_SAQUES = 3