import json


def busca_dados_json():
    with open("dados/alunos.json", "r") as f:
        data = json.load(f)
        return data
    
def listar_turmas_gerenciamento():
    with open("dados/turmas.json", "r", encoding="utf-8") as f:
        data = json.load(f)    
        return data
