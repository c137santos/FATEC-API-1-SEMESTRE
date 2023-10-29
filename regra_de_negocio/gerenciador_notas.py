
import json

from regra_de_negocio.gerenciador_ciclos import obter_ciclo, obter_ultimo_ciclo_por_id_turma
from regra_de_negocio.gerenciador_turmas import obter_turma

from datetime import datetime
import datetime as dt

def _calcular_fee_turma_aluno(id_turma,id_aluno):
    id_aluno_str = str(id_aluno)
    id_turma_str = str(id_turma)
    turma = obter_turma(id_turma_str)
    notas_por_turma_aluno = listar_notas_por_turma_aluno(id_aluno_str, id_turma_str)
    soma_das_notas = 0.0
    soma_dos_pesos = 0.0
    for id_nota in notas_por_turma_aluno:
        ciclo = obter_ciclo(notas_por_turma_aluno[id_nota]["id_ciclo"])
        peso_nota = ciclo["peso_nota"]
        valor = notas_por_turma_aluno[id_nota]["valor"]
        soma_das_notas += (peso_nota * valor)
        soma_dos_pesos += peso_nota
    if len(notas_por_turma_aluno) > 0:
        return soma_das_notas / float(soma_dos_pesos)
    else:
        return 0.0

# Essa função é responsável por recuperar um fee
def obter_fee_turma_aluno(id_turma, id_aluno):
    id_turma_str = str(id_turma)
    id_aluno_str = str(id_aluno)
    id_ultimo_ciclo, ultimo_ciclo = obter_ultimo_ciclo_por_id_turma(id_turma_str)
    nova_nota = {}
    nova_nota["id_turma"] = id_turma_str
    nova_nota["id_aluno"] = id_aluno_str
    nova_nota["id_ciclo"] = id_ultimo_ciclo
    nova_nota["valor"] = _calcular_fee_turma_aluno(id_turma_str, id_aluno_str)
    nova_nota["fee"] = True
    # todo: remover o fee antigo quando já existir e criar no banco
    return nova_nota

def listar_notas():
    with open("dados/notas.json", "r", encoding="utf-8") as f:
        notas = json.load(f)
        return notas

def listar_notas_por_id_turma(notas, id_turma):
    if not id_turma:
        return {}
    id_turma_str = str(id_turma)
    notas_encontradas = {}
    for id_nota in notas.keys():
        if id_turma_str == notas[id_nota]["id_turma"]:
            if notas[id_nota]["fee"]: #se for a média, pula
                continue
            notas_encontradas[id_nota] = notas[id_nota]
    return notas_encontradas

def listar_notas_por_id_aluno(notas, id_aluno):
    if not id_aluno:
        return {}
    id_turma_str = str(id_aluno)
    notas_encontradas = {}
    for id_nota in notas.keys():
        if id_turma_str == notas[id_nota]["id_aluno"]:
            if notas[id_nota]["fee"]:
                continue
            notas_encontradas[id_nota] = notas[id_nota]
    return notas_encontradas
    
def listar_notas_por_id_ciclo(notas, id_ciclo):
    if not id_ciclo:
        return {}
    id_turma_str = str(id_ciclo)
    notas_encontradas = {}
    for id_nota in notas.keys():
        if id_turma_str == notas[id_nota]["id_ciclo"]:
            if notas[id_nota]["fee"]:
                continue
            notas_encontradas[id_nota] = notas[id_nota]
    return notas_encontradas


def listar_notas_por_turma_aluno(id_turma, id_aluno):
    if not id_turma or not id_aluno:
        return {}
    notas = listar_notas()
    notas_por_turma = listar_notas_por_id_turma(notas, id_turma)  
    notas_por_turma_aluno = listar_notas_por_id_aluno(notas_por_turma, id_aluno)
    return notas_por_turma_aluno

    
def adicionar_nota(nova_nota):
    notas = listar_notas()
    novo_id_nota = _obter_novo_id_nota()
    notas[novo_id_nota] = nova_nota
    return _salvar_notas(notas)

def editar_nota(id_nota_atualizada, nota_atualizada):
    if not nota_atualizada:
        return False
    notas = listar_notas()
    id_nota_atualizada_str = str(id_nota_atualizada)
    if id_nota_atualizada_str in notas.keys():
        notas[id_nota_atualizada_str] = nota_atualizada
        return _salvar_notas(notas)
    else:
        return False

    
def remover_nota(id_nota):
    id_nota_str = str(id_nota)
    notas = listar_notas()
    if id_nota_str in notas.keys():
        notas.pop(id_nota_str)
        return _salvar_notas(notas)
    else:
        return False


# Essa função verifica se já existe nota dentro de um ciclo
def verificar_existencia_nota_por_ciclo(nota):
    notas = listar_notas_por_turma_aluno(nota["id_turma"],nota["id_aluno"])
    notas_por_ciclo = listar_notas_por_id_ciclo(notas, nota["id_ciclo"])
    return len(notas_por_ciclo) != 0

def _obter_novo_id_nota():
    ids_numericos = []
    notas = listar_notas()
    for id_str in notas.keys():
        id_int = int(id_str)
        ids_numericos.append(id_int)
    id_max_int = max(ids_numericos)
    novo_id = str(id_max_int + 1)
    return novo_id

def _salvar_notas(notas):
    dados = json.dumps(notas, indent=4)
    with open("dados/notas.json", "w", encoding="utf-8") as f:
        f.write(dados)
        return True


def verificar_edicao_habilitada(notas, id_nota):
    id_nota_str = str(id_nota)
    notas = listar_notas()
    nota = notas[id_nota_str]
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
    id_turma_str = str(id_turma)
    ciclos = listar_notas_por_id_turma(id_turma_str)
    numero_ciclo = ciclo["numero_ciclo"]
    prazo_insercao_nota = 0
    for id_ciclo in ciclos.keys():
        ciclo_iteracao = ciclos[id_ciclo]
        if ciclo_iteracao["numero_ciclo"] <= numero_ciclo:
            prazo_insercao_nota += ciclo_iteracao["duracao"]
    return prazo_insercao_nota + 1 # o +1 é o dia seguinte do requisito
