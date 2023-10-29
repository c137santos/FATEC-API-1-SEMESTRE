
import json

def listar_alunos():
    with open("dados/alunos.json", "r", encoding="utf-8") as f:
        alunos = json.load(f)
        return alunos