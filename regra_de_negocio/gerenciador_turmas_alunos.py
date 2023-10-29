
import json

from regra_de_negocio.gerenciador_alunos import listar_alunos
from regra_de_negocio.gerenciador_turmas import busca_turmas

def listar_turmas_alunos():
    with open("dados/turmas_alunos.json", "r", encoding="utf-8") as f:
        turmas_alunos = json.load(f)
        return turmas_alunos

# Essa função retorna todos os alunos de uma turma
def listar_alunos_turma(id_turma):
    if not id_turma:
        return {}
    turmas_alunos = listar_turmas_alunos()
    alunos = listar_alunos()
    id_turma_str = str(id_turma)
    alunos_da_turma = {}
    for id_turmas_alunos in turmas_alunos.keys():
        turma_aluno = turmas_alunos[id_turmas_alunos]
        if turma_aluno["id_turma"] == id_turma_str:
            if turma_aluno["id_aluno"] in alunos.keys():
                alunos_da_turma[turma_aluno["id_aluno"]] = alunos[turma_aluno["id_aluno"]]
    return alunos_da_turma

# Essa função retorna todas as turmas que um aluno frequenta
def listar_turmas_aluno(id_aluno):
    if not id_aluno:
        return {}
    turmas_alunos = listar_turmas_alunos()
    turmas = busca_turmas()
    id_aluno_str = str(id_aluno)
    turmas_do_aluno = {}
    for id_turmas_alunos in turmas_alunos.keys():
        turma_aluno = turmas_alunos[id_turmas_alunos]
        if turma_aluno["id_aluno"] == id_aluno_str:
            if turma_aluno["id_turma"] in turmas.keys():
                turmas_do_aluno[turma_aluno["id_turma"]] = turmas[turma_aluno["id_turma"]]
    return turmas_do_aluno
    
def adicionar_turma_aluno(turma_aluno):
    if not turma_aluno:
        return False
    alunos = listar_alunos_turma(turma_aluno["id_turma"])
    if turma_aluno["id_aluno"] in alunos.keys():
        return False
    else:
        turmas_alunos = listar_turmas_alunos()
        novo_id_turmas_alunos = _obter_novo_id_turmas_alunos()
        turmas_alunos[novo_id_turmas_alunos] = turma_aluno
        return _salvar_turmas_alunos(turmas_alunos)


def remover_turma_aluno(id_turma_aluno):
    id_turma_aluno_str = str(id_turma_aluno)
    turmas_alunos = listar_turmas_alunos()
    if id_turma_aluno_str in turmas_alunos.keys():
        turmas_alunos.pop(id_turma_aluno_str)
        return _salvar_turmas_alunos(turmas_alunos)
    else:
        return False

def _obter_novo_id_turmas_alunos():
    ids_numericos = []
    for id_str in listar_turmas_alunos.keys():
        id_int = int(id_str)
        ids_numericos.append(id_int)
    id_max_int = max(ids_numericos)
    novo_id = str(id_max_int + 1)
    return novo_id

def _salvar_turmas_alunos(turmas_alunos):
    dados = json.dumps(turmas_alunos, indent=4)
    with open("dados/turmas_alunos.json", "w", encoding="utf-8") as f:
        f.write(dados)
        return True