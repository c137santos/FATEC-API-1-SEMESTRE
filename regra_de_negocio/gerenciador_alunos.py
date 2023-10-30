import json


def listar_alunos():
    with open("dados/alunos.json", "r", encoding="utf-8") as f:
        alunos = json.load(f)
    return alunos

def editar_aluno_svc(id, alunos_editar):
    alunos = listar_alunos()
    if id in alunos.keys():
        aluno = alunos[id]
        aluno["nome"] = alunos_editar["nome"] if alunos_editar["nome"] else  aluno["nome"] 
        aluno["data_de_nascimento"] = alunos_editar["data_de_nascimento"] if alunos_editar["data_de_nascimento"] else aluno["data_de_nascimento"]
        aluno["sexo"] = alunos_editar["sexo"] if  alunos_editar["sexo"] else aluno["sexo"]
        _salvar_alunos(alunos)
        return True
    else:
        return False

def _salvar_alunos(alunos):
    dados = json.dumps(alunos, indent=4)
    with open("dados/alunos.json", "w", encoding="utf-8") as arquivo:
        arquivo.write(dados)
        return True