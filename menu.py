from utils import is_valid_option
from banco import (
    sacar,
    depositar,
    exibir_extrato,
    exibir_operacoes_do_dia,
    criar_conta_corrente,
    listar_contas_correntes,
    criar_cliente,
    CONTAS,
    CLIENTES,
)


def exibir_menu_principal() -> None:
    """Exibe as opções principais do menu do banco."""
    print(
        """\n
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [t] Transações do Dia
    [nu] Novo Usuário
    [nc] Criar Conta Corrente
    [l] Listar Contas Correntes
    [q] Sair
    """
    )


def obter_opcao_menu() -> str:
    """Obtém e retorna a opção escolhida pelo usuário."""
    return input("Escolha uma opção: ").lower()


def processar_transacao(option: str) -> None:
    global CONTAS, CLIENTES
    if option == "d":
        depositar(CLIENTES)

    if option == "s":
        sacar(CLIENTES)

    if option == "e":
        exibir_extrato(CLIENTES)

    if option == "t":
        exibir_operacoes_do_dia(CLIENTES)

    if option == "nu":
        criar_cliente(CLIENTES)

    if option == "nc":
        numero_conta = len(CONTAS) - 1
        criar_conta_corrente(numero_conta, CLIENTES, CONTAS)

    if option == "l":
        listar_contas_correntes(CONTAS)


def menu_banco() -> None:
    """Função principal que gerencia o fluxo do menu do banco."""
    while True:
        exibir_menu_principal()
        option = obter_opcao_menu()

        if is_valid_option(option):
            processar_transacao(option)
        if option == "q":
            break
