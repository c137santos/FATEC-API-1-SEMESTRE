import json


# Esta função busca informações sobre as turmas a partir de um arquivo JSON e as retorna
def busca_turmas():
    with open("dados/turmas.json", "r", encoding="utf-8") as f:
        turmas_data = json.load(f)
    return turmas_data


def busca_grupos():
    with open("dados/grupos.json", "r", encoding="utf-8") as f:
        grupos_Data = json.load(f)
    return grupos_Data
