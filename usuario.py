from typing import Dict, List


def criar_usuario(nome: str, data_nascimento: str, cpf: str, endereco: str) -> str:
    if cpf in usuarios:
        raise ValueError("Usuário já cadastrado com este CPF.")
    cpf_limpo= cpf.replace(".", "").replace("-", "")
    cliente = {
        "nome": nome,
        "data_nascimento": data_nascimento,
        "cpf": cpf_limpo,
        "endereco": endereco,
    }
    usuarios.append({cpf_limpo: cliente})
    return "Usuário criado com sucesso: {}.".format(nome)


def buscar_usuario(cpf: str) -> Dict or None:  # type: ignore
    print(usuarios)
    cpf_limpo = cpf.replace(".", "").replace("-", "")
    for usuario in usuarios:
        if cpf_limpo in usuario:
            return usuario[cpf_limpo]
    return None


usuarios: List = []
