
import json

from regra_de_negocio.gerenciador_ciclos import obter_ciclo
from regra_de_negocio.gerenciador_turmas import obter_turma

from datetime import datetime
import datetime as dt

def calcular_fee(id_aluno, id_turma):
    notas_por_turma_aluno = listar_notas_por_id_turma_id_aluno(id_aluno, id_turma)
    fee = 0.0
    for id_nota in notas_por_turma_aluno:
        # ð ?????
        ciclo = obter_ciclo(notas_por_turma_aluno[id_nota]["id_ciclo"])
        peso_nota = ciclo["peso_nota"]
        valor = notas_por_turma_aluno[id_nota]["valor"]
        fee = fee + (peso_nota * valor)
    if len(notas_por_turma_aluno) > 0:
        fee = fee / float(len(notas_por_turma_aluno))
    else:
        fee = 0.0
    return fee

def listar_notas():
    try:
        with open("dados/notas.json", "r", encoding="utf-8") as f:
            notas = json.load(f)
            return notas
    except:
        return {}

def listar_notas_por_id_turma(notas, id_turma):
    if not id_turma:
        return {}
    try:
        id_turma_textual = str(id_turma)
        notas_encontradas = {}
        for id_nota in notas.keys():
            if id_turma_textual == notas[id_nota]["id_turma"]:
                notas_encontradas[id_nota] = notas[id_nota]
        return notas_encontradas
    except:
        return {}

def listar_notas_por_id_aluno(notas, id_aluno):
    if not id_aluno:
        return {}
    try:
        id_turma_textual = str(id_aluno)
        notas_encontradas = {}
        for id_nota in notas.keys():
            if id_turma_textual == notas[id_nota]["id_aluno"]:
                notas_encontradas[id_nota] = notas[id_nota]
        return notas_encontradas
    except:
        return {}
    
def listar_notas_por_id_ciclo(notas, id_ciclo):
    if not id_ciclo:
        return {}
    try:
        id_turma_textual = str(id_ciclo)
        notas_encontradas = {}
        for id_nota in notas.keys():
            if id_turma_textual == notas[id_nota]["id_ciclo"]:
                notas_encontradas[id_nota] = notas[id_nota]
        return notas_encontradas
    except:
        return {}

def listar_notas_por_id_turma_id_aluno(id_turma, id_aluno):
    if not id_turma or not id_aluno:
        return {}
    try:
        notas = listar_notas()
        notas_por_turma = listar_notas_por_id_turma(notas, id_turma)    
        notas_por_turma_aluno = listar_notas_por_id_aluno(notas_por_turma, id_aluno)
        return notas_por_turma_aluno
    except:
        return {}
    
def adicionar_nota(nova_nota):
    try:
        notas = listar_notas()
        novo_id_nota = _obter_novo_id_nota()
        notas[novo_id_nota] = nova_nota
        return _salvar_notas(nova_nota)
    except:
        return False

def editar_nota(id_nota_atualizada, nota_atualizada):
    try:
        if not nota_atualizada:
            return False
        notas = listar_notas()
        id_nota_atualizada_textual = str(id_nota_atualizada)
        if id_nota_atualizada_textual in notas.keys():
            notas[id_nota_atualizada_textual] = nota_atualizada
            return _salvar_notas(notas)
        else:
            return False
    except:
        return False
    
def remover_nota(id_nota):
    try:
        id_nota_textual = str(id_nota)
        notas = listar_notas()
        if id_nota_textual in notas.keys():
            notas.pop(id_nota_textual)
            return _salvar_notas(notas)
        else:
            return False
    except:
        return False

# Essa função verifica se já existe nota dentro de um ciclo
def verificar_existencia_nota_por_ciclo(nota):
    notas = listar_notas_por_id_turma_id_aluno(nota["id_turma"],nota["id_aluno"])
    notas_por_ciclo = listar_notas_por_id_ciclo(notas, nota["id_ciclo"])
    return len(notas_por_ciclo) != 0
    # Formas alternativas:
    # if len(notas_por_ciclo) == 0:
    #     return False
    # else:
    #     return True
    #return False if len(notas_por_ciclo) == 0 else True

def _obter_novo_id_nota():
    ids_numericos = []
    for id_textual in listar_notas.keys():
        id_inteiro = int(id_textual)
        ids_numericos.append(id_inteiro)
    id_max_inteiro = max(ids_numericos)
    novo_id = str(id_max_inteiro + 1)
    return novo_id

def _salvar_notas(ciclos):
    try:
        dados = json.dumps(ciclos, indent=4)
        with open("dados/notas.json", "w", encoding="utf-8") as f:
            f.write(dados)
            return True
    except:
        return False

def verificar_edicao_habilitada(notas, id_nota):
    notas = listar_notas()
    nota = notas[id_nota]
    ciclo = obter_ciclo(nota["id_ciclo"])
    turma = obter_turma(nota["id_turma"])
    if ciclo and turma:
        data_inicio = turma["data_de_inicio"]
        formato_data = '%d/%m/%Y'
        prazo_insercao_nota = _obter_prazo_insercao_nota(ciclo, nota["id_turma"])
        data_inicial_insercao_nota = datetime.strptime(data_inicio, formato_data) + dt.timedelta(days=prazo_insercao_nota)
        data_final_insercao_nota = data_inicial_insercao_nota + ciclo["prazo_insercao_nota"]
        data_atual = datetime.now()
        if data_inicial_insercao_nota >= data_atual and data_atual <= data_final_insercao_nota:
            return True
        else:
            return False
    else:
        return False

def _obter_prazo_insercao_nota(ciclo, id_turma):
    ciclos = listar_notas_por_id_turma(id_turma)
    numero_ciclo = ciclo["numero_ciclo"]
    prazo_insercao_nota = 0
    for id_ciclo in ciclos.keys():
        ciclo_iteracao = ciclos[id_ciclo]
        if ciclo_iteracao["numero_ciclo"] <= numero_ciclo:
            prazo_insercao_nota += ciclo_iteracao["duracao"]
    return prazo_insercao_nota + 1 # o +1 é o dia seguinte do requisito
