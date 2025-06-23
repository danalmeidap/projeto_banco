def depositar(valor):
    global saldo, extrato
    saldo += valor
    extrato += "Depósito: R$ {:.2f}\n".format(valor)
    print("Depósito realizado com sucesso!")


def sacar(valor):
    global saldo, extrato, numero_saques
    if numero_saques < LIMITE_SAQUES and valor <= limite and valor <= saldo:
        saldo -= valor
        extrato += "Saque: R$ {:.2f}\n".format(valor)
        numero_saques += 1
        print("Saque realizado com sucesso!")
    else:
        if numero_saques >= LIMITE_SAQUES:
            print("Número máximo de saques diários atingido.")
        elif valor > limite:
            print("Valor do saque excede o limite permitido.")
        else:
            print("Valor inválido para saque.")


def exibir_extrato(valor):
    global saldo, extrato
    print("\n================== Extrato ==================")
    if not extrato:
        print("Nenhuma transação realizada.")
    else:
        print(extrato)
    print("Saldo: R$ {:.2f}".format(saldo))
    print("=============================================\n")


saldo = 0.0
limite = 500.0
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
