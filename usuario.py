from typing import Dict, List, Union


def criar_usuario(nome: str, data_nascimento: str, cpf: str, endereco: str) -> str:
    if not valida_usuario(cpf):
        raise ValueError("Usuário já cadastrado com este CPF.")
    cpf_limpo = cpf.replace(".", "").replace("-", "")
    cliente = {
        "nome": nome,
        "data_nascimento": data_nascimento,
        "cpf": cpf_limpo,
        "endereco": endereco,
    }
    usuarios.append({cpf_limpo: cliente})
    return "Usuário criado com sucesso: {}.".format(nome)


def buscar_usuario(cpf: str) -> Union[Dict[str, str], None]:
    cpf_limpo = cpf.replace(".", "").replace("-", "")
    for usuario in usuarios:
        if cpf_limpo in usuario:
            return usuario[cpf_limpo]
    return None


def valida_usuario(cpf: str) -> bool:
    return True if buscar_usuario(cpf) else False


usuarios: List = []
