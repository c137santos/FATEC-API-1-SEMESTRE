import json


def busca_dados_json():
    with open("dados/alunos.json", "r") as f:
        data = json.load(f)
        return data
    
def busca_turmas():
    with open("dados/turmas.json", "r", encoding="utf-8") as f:
        turmas_data = json.load(f)
    return turmas_data

def busca_grupos():
    with open("dados/grupos.json", "r", encoding="utf-8") as f:
        turmas_data = json.load(f)
    return turmas_data    

def busca_grupo_alunos():
    with open("dados/grupo_alunos.json", "r", encoding="utf-8") as f:
        grupo_alunos_data = json.load(f)
    return grupo_alunos_data

def busca_alunos():
    with open("dados/alunos.json", "r", encoding="utf-8") as f:
        alunos_data = json.load(f)
    return alunos_data