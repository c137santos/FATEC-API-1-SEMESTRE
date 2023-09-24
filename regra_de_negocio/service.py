import json


def busca_dados_json():
    with open("dados/alunos.json", "r") as f:
        data = json.load(f)
        return data
