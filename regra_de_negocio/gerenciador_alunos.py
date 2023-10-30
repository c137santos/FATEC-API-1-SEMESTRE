import json


def listar_alunos():
    with open("dados/alunos.json", "r", encoding="utf-8") as f:
        alunos = json.load(f)
    return alunos

def criar_aluno(novo_aluno):
    alunos = listar_alunos()
    id_novo_aluno = _novo_id_aluno()
    aluno = {
        "nome": novo_aluno["nome"],
        "data_nascimento": novo_aluno["data_nascimento"],
        "sexo": novo_aluno["sexo"],
        "RA": id_novo_aluno
    }

    alunos[id_novo_aluno] = aluno
    _salvar_alunos(alunos)


def _salvar_alunos(alunos):
    dados = json.dumps(alunos, indent=4)
    with open("dados/alunos.json", "w", encoding="utf-8") as arquivo:
        arquivo.write(dados)
        return True


def _novo_id_aluno():
    ids_numericos = []
    alunos = listar_alunos()
    for id_str in alunos.keys():
        id_int = int(id_str)
        ids_numericos.append(id_int)
    id_max_int = max(ids_numericos)
    novo_id = str(id_max_int + 1)
    return novo_id
