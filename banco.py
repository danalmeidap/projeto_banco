from usuario import usuarios, buscar_usuario
from typing import Dict, List, Union

SALDO: float = 0.0
LIMITE: float = 500.0
EXTRATO: str = ""
NUMERO_SAQUES: int = 0
LIMITE_SAQUES: int = 3
AGENCIA: str = "0001"
LISTA_USUARIOS: List = usuarios
numero_conta: int = 1
proximo_numero_conta = 1
CONTAS_CORRENTES: List[Dict[str, str]] = []


def gerar_novo_numero_conta() -> int:
    global proximo_numero_conta
    numero_atual = proximo_numero_conta
    proximo_numero_conta += 1
    return numero_atual


def depositar(valor: float, saldo: float, extrato: str, /) -> Union[float, str]:
    if valor > 0:
        saldo += valor
        extrato += "Depósito: R$ {:.2f}\n".format(valor)
        print("Depósito realizado com sucesso!")
    else:
        print("Operação falhou! O valor do depósito deve ser positivo.")
    return saldo, extrato


def criar_conta_corrente(agencia: str, cpf_usuario: str) -> Dict[str, str]:
    novo_numero: int = gerar_novo_numero_conta()
    if not valida_usuario(cpf_usuario):
        raise ValueError("Usuário não encontrado. Por favor, crie um usuário primeiro.")
    cpf_limpo = cpf_usuario.replace(".", "").replace("-", "")
    conta = {
        "agencia": agencia,
        "numero_conta": novo_numero,
        "usuario": buscar_usuario(cpf_limpo),
    }
    print("Conta corrente criada com sucesso!")
    CONTAS_CORRENTES.append(conta)
    return conta


def saque_valido(
    saldo: int, valor: float, numero_saques: int, limite: float, limite_saques
) -> bool:
    if numero_saques < limite_saques and valor <= limite and valor <= saldo:
        return True
    return False


def sacar(
    *, saldo: float, valor: float, extrato: str, limite: float, numero_saques: int
) -> Union[float, str]:
    if saque_valido(saldo, valor, numero_saques, limite, LIMITE_SAQUES):
        saldo -= valor
        extrato += "Saque: R$ {:.2f}\n".format(valor)
        numero_saques += 1
        print("Saque realizado com sucesso!")
    else:
        print(
            "Saque inválido! Verifique o valor, limite ou número de saques realizados."
        )
    return saldo, extrato


def exibir_extrato(saldo: float, /, *, extrato: str) -> Union[float, str]:
    print("\n================== Extrato ==================")
    if not extrato:
        print("Nenhuma transação realizada.")
    else:
        print(extrato)
    print("Saldo: R$ {:.2f}".format(saldo))
    print("=============================================\n")
    return saldo, extrato


def listar_contas_correntes(contas_correntes: Dict[str, str]) -> None:
    """Lista todas as contas correntes cadastradas."""
    if not contas_correntes:
        print("Nenhuma conta corrente cadastrada.")
    print("\n================== Contas Correntes ==================")
    for conta in contas_correntes:
        print(
            f"Agência: {conta['agencia']}, Número da Conta: {conta['numero_conta']}, "
            f"Usuário: {conta['usuario']['nome']}, CPF: {conta['usuario']['cpf']}"
        )
    print("========================================================\n")


def valida_usuario(cpf_usuario: str) -> None:
    return True if buscar_usuario(cpf_usuario) else False
