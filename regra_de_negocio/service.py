import json
from regra_de_negocio import gerenciador_grupos
from regra_de_negocio import gerenciador_turmas



def busca_dados_json():
    with open("dados/alunos.json", "r") as f:
        data = json.load(f)
        return data

def criacao_turma(dados_nova_turma):
    grupos = gerenciador_grupos.buscando_grupos()
    resposta = gerenciador_turmas.criacao_turma(dados_nova_turma, grupos)
    gerenciador_grupos._salvar_grupos(grupos)
    return resposta

