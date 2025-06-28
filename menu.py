from utils import is_valid_option, check_float
from banco import (
    depositar,
    sacar,
    exibir_extrato,
    criar_conta_corrente,
    listar_contas_correntes,
    AGENCIA,
    SALDO,
    LIMITE,
    EXTRATO,
    NUMERO_SAQUES,
    CONTAS_CORRENTES,
)
from usuario import criar_usuario, buscar_usuario


def exibir_menu_principal():
    """Exibe as opções principais do menu do banco."""
    print("""\n
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [u] Novo Usuário
    [b] Buscar Usuário
    [c] Criar Conta Corrente
    [l] Listar Contas Correntes
    [q] Sair
    """)


def obter_opcao_menu():
    """Obtém e retorna a opção escolhida pelo usuário."""
    return input("Escolha uma opção: ").lower()


def processar_transacao(option):
    global SALDO, EXTRATO, LIMITE_SAQUES, NUMERO_SAQUES, CONTAS_CORRENTES
    """Processa as opções de transação (depósito, saque, extrato)."""
    if option == "d":
        valor = check_float("Digite o valor a ser depositado: ")
        SALDO, EXTRATO = depositar(
            valor,
            SALDO,
            EXTRATO,
        )
    elif option == "s":
        valor = check_float("Digite o valor a ser sacado: ")
        SALDO, EXTRATO = sacar(
            valor=valor,
            saldo=SALDO,
            extrato=EXTRATO,
            limite=LIMITE,
            numero_saques=NUMERO_SAQUES,
        )
        print(SALDO)
    elif option == "e":
        SALDO, EXTRATO = exibir_extrato(SALDO, extrato=EXTRATO)
    else:
        print("Opção inválida para transação.")


def obter_dados_usuario():
    """Solicita e retorna os dados para criação de um novo usuário."""
    nome = input("Digite o nome do usuário: ")
    data_nascimento = input("Digite a data de nascimento (DD/MM/AAAA): ")
    cpf = input("Digite o CPF (XXX.XXX.XXX-XX): ")
    endereco = input("Digite o endereço: (Logradouro- Bairro- cidade/sigla estado): ")
    return nome, data_nascimento, cpf, endereco


def obter_cpf_conta_corrente():
    """Solicita e retorna o CPF do usuário para criação de conta corrente."""
    return input(
        "Digite o CPF do usuário para criar a conta corrente (XXX.XXX.XXX-XX):"
    )


def menu_banco():
    global CONTAS_CORRENTES
    """Função principal que gerencia o fluxo do menu do banco."""
    while True:
        exibir_menu_principal()
        option = obter_opcao_menu()

        if is_valid_option(option):
            if option in ("d", "s", "e"):
                processar_transacao(option)
            elif option == "u":
                dados_usuario = obter_dados_usuario()
                criar_usuario(*dados_usuario)
            elif option == "b":
                cpf_usuario = input(
                    "Digite o CPF do usuário a ser buscado (XXX.XXX.XXX-XX): "
                )
                print(buscar_usuario(cpf_usuario))
            elif option == "c":
                cpf_usuario = obter_cpf_conta_corrente()
                criar_conta_corrente(AGENCIA, cpf_usuario)
            elif option == "l":
                print("Listando contas correntes...")
                listar_contas_correntes(CONTAS_CORRENTES)
            elif option == "q":
                print("Saindo do sistema...")
                break
        else:
            print("Opção inválida. Por favor, tente novamente.")
