import json

from regra_de_negocio.gerenciador_ciclos import (
    listar_ciclos_por_id_turma,
    obter_ciclo,
    obter_ultimo_ciclo_por_id_turma,
)
from regra_de_negocio.gerenciador_turmas import obter_turma
from regra_de_negocio.service import gerenciador_turmas_alunos

from datetime import datetime, timedelta


def calcular_fee_turma_aluno(id_turma, id_aluno):
    id_turma_str = str(id_turma)
    id_aluno_str = str(id_aluno)
    notas_por_turma_aluno = listar_notas_por_turma_aluno(id_turma_str, id_aluno_str)
    soma_das_notas = 0.0
    soma_dos_pesos = 0.0
    for id_nota in notas_por_turma_aluno:
        ciclo = obter_ciclo(notas_por_turma_aluno[id_nota]["id_ciclo"])
        peso_nota = ciclo["peso_nota"]
        valor = notas_por_turma_aluno[id_nota]["valor"]
        soma_das_notas += peso_nota * valor
        soma_dos_pesos += peso_nota
    if len(notas_por_turma_aluno) > 0:
        media_fee = soma_das_notas / float(soma_dos_pesos)
        valor_fee = round(media_fee, 2)
    else:
        valor_fee = 0.0
    gerenciador_turmas_alunos.adicionar_fee_na_turma_aluno(
        id_aluno, id_turma, valor_fee
    )


def atualiza_todos_fee_da_turma(id_turma):
    alunos = gerenciador_turmas_alunos.listar_turmas_alunos()
    for id_aluno in alunos.keys():
        if alunos[id_aluno]["id_turma"] == id_turma:
            calcular_fee_turma_aluno(id_turma, id_aluno)


def listar_notas():
    with open("dados/notas.json", "r", encoding="utf-8") as f:
        notas = json.load(f)
        return notas


def filtrar_notas_por_id_turma_svc(notas, id_turma):
    if not id_turma:
        return {}
    id_turma_str = str(id_turma)
    notas_encontradas = {}
    for id_nota in notas.keys():
        if id_turma_str == notas[id_nota]["id_turma"]:
            if notas[id_nota]["fee"]:  # se for a média, pula
                continue
            notas_encontradas[id_nota] = notas[id_nota]
    return notas_encontradas


def listar_notas_por_id_aluno(notas, id_aluno):
    if not id_aluno:
        return {}
    id_aluno_str = str(id_aluno)
    notas_encontradas = {}
    for id_nota in notas.keys():
        if id_aluno_str == notas[id_nota]["id_aluno"]:
            if notas[id_nota]["fee"]:
                continue
            notas_encontradas[id_nota] = notas[id_nota]

    return notas_encontradas


def listar_notas_por_id_ciclo(notas, id_ciclo):
    if not id_ciclo:
        return {}
    id_ciclo_str = str(id_ciclo)
    notas_encontradas = {}
    for id_nota in notas.keys():
        if id_ciclo_str == notas[id_nota]["id_ciclo"]:
            if notas[id_nota]["fee"]:
                continue
            notas_encontradas[id_nota] = notas[id_nota]
    return notas_encontradas


def listar_notas_por_turma_aluno(id_turma, id_aluno):
    if not id_turma or not id_aluno:
        return {}
    notas = listar_notas()
    notas_por_turma = filtrar_notas_por_id_turma_svc(notas, id_turma)
    notas_por_turma_aluno = listar_notas_por_id_aluno(notas_por_turma, id_aluno)
    return notas_por_turma_aluno


def adicionar_nota(nova_nota):
    notas = listar_notas()
    novo_id_nota = _obter_novo_id_nota()
    notas[novo_id_nota] = nova_nota
    _salvar_notas(notas)
    calcular_fee_turma_aluno(
        notas[novo_id_nota]["aluno_id"], notas[novo_id_nota]["turma_id"]
    )


def editar_nota(notas_atualizada):
    if not notas_atualizada:
        return False
    notas = listar_notas()
    for id_nota in notas_atualizada:
        id_nota_atualizada_str = str(id_nota)
        if id_nota_atualizada_str in notas.keys():
            notas[id_nota_atualizada_str]["valor"] = float(
                notas_atualizada[id_nota_atualizada_str]["valor"]
            )
            calcular_fee_turma_aluno(
                notas[id_nota_atualizada_str]["id_aluno"],
                notas[id_nota_atualizada_str]["id_turma"],
            )
        else:
            return False
    return _salvar_notas(notas)


def remover_nota(id_nota):
    id_nota_str = str(id_nota)
    notas = listar_notas()
    if id_nota_str in notas.keys():
        notas.pop(id_nota_str)
        _salvar_notas(notas)
        calcular_fee_turma_aluno(
            notas["id_nota_str"]["id_aluno"], notas["id_nota_str"]["id_turma"]
        )
    else:
        return False


# Essa função verifica se já existe nota dentro de um ciclo
def verificar_existencia_nota_por_ciclo(nota):
    notas = listar_notas_por_turma_aluno(nota["id_turma"], nota["id_aluno"])
    notas_por_ciclo = listar_notas_por_id_ciclo(notas, nota["id_ciclo"])
    return len(notas_por_ciclo) != 0


def _obter_novo_id_nota():
    ids_numericos = []
    ids_numericos.append(0)
    notas = listar_notas()
    for id_str in notas.keys():
        id_int = int(id_str)
        ids_numericos.append(id_int)
    ids_numericos.sort()
    id_max_int = ids_numericos.pop()
    novo_id = str(id_max_int + 1)
    return novo_id


def _salvar_notas(notas):
    dados = json.dumps(notas, indent=4)
    with open("dados/notas.json", "w", encoding="utf-8") as f:
        f.write(dados)
        return True


def verificar_edicao_habilitada(notas, id_nota):
    id_nota_str = str(id_nota)
    nota = notas[id_nota_str]
    ciclo = obter_ciclo(nota["id_ciclo"])
    turma = obter_turma(nota["id_turma"])
    if ciclo and turma:
        data_inicio = turma["data_de_inicio"]
        formato_data = "%d/%m/%Y"
        prazo_insercao_nota = _obter_prazo_insercao_nota(ciclo, nota["id_turma"])
        data_inicial_insercao_nota = datetime.strptime(
            data_inicio, formato_data
        ) + timedelta(days=prazo_insercao_nota)
        data_final_insercao_nota = data_inicial_insercao_nota + timedelta(
            days=ciclo["prazo_insercao_nota"]
        )
        data_atual = datetime.now()
        if data_inicial_insercao_nota <= data_atual <= data_final_insercao_nota:
            return True
        else:
            return False
    else:
        return False


def _obter_prazo_insercao_nota(ciclo, id_turma):
    id_turma_str = str(id_turma)
    ciclos = listar_ciclos_por_id_turma(id_turma_str)
    numero_ciclo = ciclo["numero_ciclo"]
    prazo_insercao_nota = 0
    for id_ciclo in ciclos.keys():
        ciclo_iteracao = ciclos[id_ciclo]
        if ciclo_iteracao["numero_ciclo"] <= numero_ciclo:
            prazo_insercao_nota += ciclo_iteracao["duracao"]
    return prazo_insercao_nota + 1  # o +1 é o dia seguinte do requisito


def excluir_notas_relacionadas_turma(id_turma):
    print("\n> Excluindo notas relacionados a turma...\n")
    todos_notas = listar_notas()
    for id in todos_notas.keys():
        if todos_notas["id"]["id_turma"] == id_turma:
            remover_nota(id)


def adicionar_notas_aluno_turma(ciclos, alunos, id_nova_turma_str):
    for id_aluno in alunos:
        for id_ciclo in ciclos:
            nova_nota = {}
            nova_nota["id_turma"] = id_nova_turma_str
            nova_nota["id_aluno"] = str(id_aluno)
            nova_nota["id_ciclo"] = str(id_ciclo)
            nova_nota["valor"] = 0.0
            nova_nota["fee"] = False
            adicionar_nota(nova_nota)
            calcular_fee_turma_aluno(id_aluno, int(id_nova_turma_str))
