import json
import regra_de_negocio.gerenciador_turmas as gt
from regra_de_negocio.gerenciador_grupos import buscando_grupos


def busca_dados_json():
    with open("dados/alunos.json", "r") as f:
        data = json.load(f)
        return data


def busca_turmas():  # retorna todas turmas
    turmas_data = gt.busca_turmas()
    return turmas_data


def buscar_grupos():  # retorna todos os grupos
    grupos_data = gt.buscando_grupos()
    return grupos_data


def cria_turma(dados_nova_turma):
    resposta = gt.criacao_turma(dados_nova_turma)
    return resposta
