def depositar(valor):
    global saldo, extrato
    saldo += valor
    extrato += "Depósito: R$ {:.2f}\n".format(valor)
    print("Depósito realizado com sucesso!")


def saque_valido(valor):
    global saldo, extrato, numero_saques
    if numero_saques < LIMITE_SAQUES and valor <= limite and valor <= saldo:
        return True
    return False


def sacar(valor):
    global saldo, extrato, numero_saques
    if saque_valido(valor):
        saldo -= valor
        extrato += "Saque: R$ {:.2f}\n".format(valor)
        numero_saques += 1
        print("Saque realizado com sucesso!")
    else:
        print(
            "Saque inválido! Verifique o valor, limite ou número de saques realizados."
        )


def exibir_extrato():
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
