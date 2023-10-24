import json
import regra_de_negocio.gerenciador_grupos as gerenciador_grupos
import regra_de_negocio.gerenciador_turmas as gerenciador_turmas



def busca_dados_json():
    with open("dados/alunos.json", "r") as f:
        data = json.load(f)
        return data

def criacao_turma(dados_nova_turma):
    grupos = gerenciador_grupos.buscando_grupos()
    resposta = gerenciador_turmas.criacao_turma(dados_nova_turma, grupos)
    gerenciador_grupos._salvar_grupos(grupos)
    return resposta

