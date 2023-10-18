import json

def buscando_alunos():
    with open("dados/alunos.json", "r", encoding="utf-8") as f:
        alunos_data = json.load(f)
    return alunos_data