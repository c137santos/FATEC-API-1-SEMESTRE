import json


def listar_alunos():
    with open("dados/alunos.json", "r", encoding="utf-8") as f:
        alunos = json.load(f)
    return alunos

def apagar_aluno(id):
    alunos = listar_alunos()
    if id in alunos.keys():
        alunos.pop(id)
        _salvar_alunos(alunos)
        return True
    else:
        return False

def _salvar_alunos(alunos):
    dados = json.dumps(alunos, indent=4)
    with open("dados/alunos.json", "w", encoding="utf-8") as arquivo:
        arquivo.write(dados)
        return True