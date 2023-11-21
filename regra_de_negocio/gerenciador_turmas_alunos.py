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
                alunos_da_turma[turma_aluno["id_aluno"]] = alunos[
                    turma_aluno["id_aluno"]
                ]
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
                turmas_do_aluno[turma_aluno["id_turma"]] = turmas[
                    turma_aluno["id_turma"]
                ]
    return turmas_do_aluno


# dado id da turma e do aluno busca o objeto exato
def busca_determinada_turma_do_aluno(id_aluno, id_turma):
    turmas_aluno = listar_turmas_alunos()
    for turma in turmas_aluno:
        if (
            turmas_aluno[turma]["id_turma"] == id_turma
            and turmas_aluno[turma]["id_aluno"] == id_aluno
        ):
            return turmas_aluno[turma]


def adicionar_turma_aluno(turma_aluno):
    if not turma_aluno:
        return False
    alunos_da_turma = listar_alunos_turma(turma_aluno[0]["id_turma"])
    if turma_aluno[0]["id_aluno"] in alunos_da_turma.keys():
        return False
    else:
        turmas_alunos = listar_turmas_alunos()
        novo_id_turmas_alunos = _obter_novo_id_turmas_alunos()
        turmas_alunos[novo_id_turmas_alunos] = turma_aluno[0]
        return _salvar_turmas_alunos(turmas_alunos)


def remover_turma_aluno(id_turma):
    id_turma = str(id_turma)
    turmas_alunos = listar_turmas_alunos()
    turmas_alunos_copia = turmas_alunos.copy()
    for id_turma_aluno in turmas_alunos_copia:
        if id_turma == turmas_alunos_copia[id_turma_aluno]["id_turma"]:
            turmas_alunos.pop(id_turma_aluno)
    return _salvar_turmas_alunos(turmas_alunos)


def remover_aluno_da_turma(id_turma, id_aluno):
    id_turma = str(id_turma)
    id_aluno = str(id_aluno)
    turmas_alunos = listar_turmas_alunos()
    turmas_alunos_copia = turmas_alunos.copy()
    for id_turma_aluno in turmas_alunos_copia:
        if (
            id_turma == turmas_alunos_copia[id_turma_aluno]["id_turma"]
            and id_aluno == turmas_alunos_copia[id_turma_aluno]["id_aluno"]
        ):
            turmas_alunos.pop(id_turma_aluno)
    return _salvar_turmas_alunos(turmas_alunos)


def adicionar_fee_na_turma_aluno(aluno_id, turma_id, valor_fee):
    turmas_alunos = listar_turmas_alunos()
    for id in turmas_alunos.keys():
        if (
            turmas_alunos[id]["id_aluno"] == aluno_id
            and turmas_alunos[id]["id_turma"] == turma_id
        ):
            turmas_alunos[id]["fee"] = valor_fee
    _salvar_turmas_alunos(turmas_alunos)


def _obter_novo_id_turmas_alunos():
    ids_numericos = []
    ids_numericos.append(0)
    ids_turmas_alunos = listar_turmas_alunos()
    for id in ids_turmas_alunos.keys():
        id_int = int(id)
        ids_numericos.append(id_int)
    ids_numericos.sort()
    id_max_int = ids_numericos.pop()
    novo_id = str(id_max_int + 1)
    return novo_id


def _salvar_turmas_alunos(turmas_alunos):
    dados = json.dumps(turmas_alunos, indent=4)
    with open("dados/turmas_alunos.json", "w", encoding="utf-8") as f:
        f.write(dados)
        return True
