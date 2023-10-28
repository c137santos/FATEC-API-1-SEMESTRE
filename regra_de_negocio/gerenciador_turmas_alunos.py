
import json

from gerenciador_alunos import listar_alunos
from gerenciador_turmas import busca_turmas

def listar_turmas_alunos():
    try:
        with open("dados/teste/turmas_alunos.json", "r", encoding="utf-8") as f:
            turmas_alunos = json.load(f)
            return turmas_alunos
    except:
        return {}

# Essa função retorna todos os alunos de uma turma
def listar_alunos_turma(id_turma):
    if not id_turma:
        return {}
    try:
        turmas_alunos = listar_turmas_alunos()
        alunos = listar_alunos()
        id_turma_textual = str(id_turma)
        alunos_da_turma = {}
        for id_turmas_alunos in turmas_alunos.keys():
            turma_aluno = turmas_alunos[id_turmas_alunos]
            if turma_aluno["id_turma"] == id_turma_textual:
                if turma_aluno["id_aluno"] in alunos.keys():
                    alunos_da_turma[turma_aluno["id_aluno"]] = alunos[turma_aluno["id_aluno"]]
        return alunos_da_turma
    except:
        return {}

# Essa função retorna todas as turmas que um aluno frequenta
def listar_turmas_aluno(id_aluno):
    if not id_aluno:
        return {}
    try:
        turmas_alunos = listar_turmas_alunos()
        turmas = busca_turmas()
        id_aluno_textual = str(id_aluno)
        turmas_do_aluno = {}
        for id_turmas_alunos in turmas_alunos.keys():
            turma_aluno = turmas_alunos[id_turmas_alunos]
            if turma_aluno["id_aluno"] == id_aluno_textual:
                if turma_aluno["id_turma"] in turmas.keys():
                    turmas_do_aluno[turma_aluno["id_turma"]] = turmas[turma_aluno["id_turma"]]
        return turmas_do_aluno
    except:
        return {}
    
def adicionar_turma_aluno(turma_aluno):
    if not turma_aluno:
        return False
    try:
        alunos = listar_alunos_turma(turma_aluno["id_turma"])
        if turma_aluno["id_aluno"] in alunos.keys():
            return False
        else:
            turmas_alunos = listar_turmas_alunos()
            novo_id_turmas_alunos = _obter_novo_id_turmas_alunos()
            turmas_alunos[novo_id_turmas_alunos] = turma_aluno
            return _salvar_turmas_alunos(turmas_alunos)
    except:
        return False 

def remover_turma_aluno(id_turma_aluno):
    try:
        id_turma_aluno_textual = str(id_turma_aluno)
        turmas_alunos = listar_turmas_alunos()
        if id_turma_aluno_textual in turmas_alunos.keys():
            turmas_alunos.pop(id_turma_aluno_textual)
            return _salvar_turmas_alunos(turmas_alunos)
        else:
            return False
    except:
        return False

def _obter_novo_id_turmas_alunos():
    ids_numericos = []
    for id_textual in listar_turmas_alunos.keys():
        id_inteiro = int(id_textual)
        ids_numericos.append(id_inteiro)
    id_max_inteiro = max(ids_numericos)
    novo_id = str(id_max_inteiro + 1)
    return novo_id

def _salvar_turmas_alunos(turmas_alunos):
    try:
        dados = json.dumps(turmas_alunos, indent=4)
        with open("dados/teste/notas.json", "w", encoding="utf-8") as f:
            f.write(dados)
            return True
    except:
        return False