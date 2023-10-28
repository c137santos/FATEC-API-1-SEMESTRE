
import json

def listar_alunos():
    try:
        with open("dados/teste/alunos.json", "r", encoding="utf-8") as f:
            alunos = json.load(f)
            return alunos
    except:
        return {}