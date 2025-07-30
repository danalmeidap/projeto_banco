from utils import check_float
from conta import Conta
from deposito import Deposito
from saque import Saque
from cliente import Cliente
from conta_corrente import ContaCorrente
from pessoa_fisica import Pessoa_Fisica


CONTAS = []
CLIENTES = []


def recuperar_conta_corrente(cliente):
    if not cliente.contas:   
        print("Cliente não localizado")
        return 
    return cliente.contas[0]


def depositar(CLIENTES):
    cpf = input("Digite o CPF: ")
    cliente:Cliente = filtar_cliente(cpf, CLIENTES)
    valor  = check_float("Digite o valor do depósito: ")
    transacao = Deposito(valor)
    conta = recuperar_conta_corrente(cliente)
    if not conta:
        print("Conta não localizada")
        return 
    cliente.realizar_transacao(conta, transacao)


def criar_conta_corrente(numero_conta, clientes, conta):
    cpf = input("Digite o CPF (XXX.XXX.XXX-XX)")
    cpf_limpo = cpf.replace(".", "").replace("-", "")
    cliente:Cliente = filtar_cliente(cpf_limpo, clientes)
    conta = ContaCorrente.nova_conta(numero_conta, cliente)
    CONTAS.append(conta)
    cliente.contas.append(conta)
    print("Conta criada com sucesso")
    

def sacar(CLIENTES):
    cpf = input("Digite o CPF (XXX.XXX.XXX-XX)")
    cpf_limpo = cpf.replace(".", "").replace("-", "")
    cliente:Cliente = filtar_cliente(cpf_limpo, CLIENTES)
    valor  = check_float("Digite o valor do depósito: ")
    transacao = Saque(valor)
    conta = recuperar_conta_corrente(cliente)
    if not conta:
        print("Conta não localizada")
        return
    cliente.realizar_transacao(conta, transacao)


def exibir_extrato(CLIENTES):
    cpf = input("Digite o CPF")
    cliente:Cliente = filtar_cliente(cpf, CLIENTES)
    if not cliente:
        return
    conta:Conta  = recuperar_conta_corrente(cliente)
    if not conta:
        return 

    print("==============EXTRATO==================")
    transacoes = conta.historico.transacoes

    extrato = ""
    if not transacoes:
        extrato += "Não foram encontradas operações."
        return
    else:
        for transacao in transacoes:
            extrato += f"\n{transacao['tipo']}:\n\t R${transacao['valor']:.2f}"
    print(extrato)
    print(f"Saldo de: R$ {conta.saldo:.2f}")
    print("==============EXTRATO==================")


def listar_contas_correntes(contas):
    for conta in contas:
        print(conta)
    

def criar_cliente(CLIENTES):
    cpf = input("Digite o CPF (XXX.XXX.XXX-XX)")
    cpf_limpo = cpf.replace(".", "").replace("-", "")
    cliente:Cliente = filtar_cliente(cpf_limpo, CLIENTES)
    if cliente:
        print("Cliente já existente com esse cpf")
        return 
    nome, data_nascimento, endereco = obter_dados_usuario()
    cliente = Pessoa_Fisica(nome, data_nascimento, cpf_limpo, endereco)
    CLIENTES.append(cliente)
    print('Cliente criado com sucesso!')


def obter_dados_usuario():
    """Solicita e retorna os dados para criação de um novo usuário."""
    nome = input("Digite o nome do usuário: ")
    data_nascimento = input("Digite a data de nascimento (DD/MM/AAAA): ")
    endereco = input("Digite o endereço: (Logradouro- Bairro- cidade/sigla estado): ")
    return nome, data_nascimento,endereco


def filtar_cliente(cpf, CLIENTES):
    clientes_filtrados = [cliente for cliente in CLIENTES if cliente.cpf == cpf]
    return clientes_filtrados[0] if clientes_filtrados else None