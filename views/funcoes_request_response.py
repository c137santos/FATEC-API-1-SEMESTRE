from wgsi import JsonResponse
from regra_de_negocio.service import (
    busca_turmas,
    cria_turma,
)

from regra_de_negocio.gerenciador_turmas import excluir_turma_svc, editar_turma_svc

from regra_de_negocio import gerenciador_ciclos, gerenciador_notas, gerenciador_turmas_alunos

import regra_de_negocio.gerenciador_ciclos as gerenciador_ciclos
import regra_de_negocio.gerenciador_notas as gerenciador_notas
import regra_de_negocio.gerenciador_turmas_alunos as gerenciador_turmas_alunos

import json


def editar_aluno(request, id):
    return JsonResponse({"message": f"Editando o aluno com ID {id}."})

def listar_turmas(request):
    turmas_data = busca_turmas()
    return JsonResponse(turmas_data)

def obter_turma(request, id):
    turmas_data = busca_turmas()
    return JsonResponse(turmas_data[id])

def editar_turma(request, id):
    turma = json.loads(request.body)
    resultado = editar_turma_svc(
        id,
        turma["nome"],
        turma["professor"],
        turma["data_de_inicio"],
        turma["duracao_ciclo"],
    )
    return JsonResponse({"mensagem": resultado})

def criar_turma(request):
    nova_turma = json.loads(request.body)
    print(nova_turma)
    resposta = cria_turma(nova_turma)
    for i in range(resposta["nova_turma"]["quantidade_ciclos"]):
        gerenciador_ciclos.adicionar_ciclo(resposta["id_nova_turma"])
    return JsonResponse(resposta)

def excluir_turma(request, id):
    resultado = excluir_turma_svc(id)
    return JsonResponse({"mensagem": resultado})

def criar_ciclo(request):
    novo_ciclo = json.loads(request.body)
    resultado = gerenciador_ciclos.adicionar_ciclo(novo_ciclo)
    return JsonResponse({"mensagem":resultado})

def listar_ciclos(request):
    ciclos = gerenciador_ciclos.listar_ciclos()
    return JsonResponse(ciclos)

def listar_ciclos_por_id_turma(request, id_turma):
    ciclos = gerenciador_ciclos.listar_ciclos_por_id_turma(id_turma)
    return JsonResponse(ciclos)

def criar_nota(request):
    nova_nota = json.loads(request.body)
    if not gerenciador_notas.verificar_existencia_nota_por_ciclo(nova_nota):
        resultado = gerenciador_notas.adicionar_nota(nova_nota)
        return JsonResponse({"mensagem": resultado})
    else:
        return JsonResponse({"mensagem": False})

def editar_nota(request, id_nota):
    nota_atualizada = json.loads(request.body)
    resultado = gerenciador_notas.editar_nota(id_nota, nota_atualizada)
    return JsonResponse({"mensagem": resultado})

def excluir_nota(request, id_nota):
    resultado = gerenciador_notas.remover_nota(id_nota)
    return JsonResponse({"mensagem": resultado})

def listar_notas(request):
    notas = gerenciador_notas.listar_notas()
    for id_nota in notas:
        notas[id_nota]["edicao_habilitada"] = gerenciador_notas.verificar_edicao_habilitada(notas,id_nota)
    return JsonResponse(notas)

def listar_notas_por_id_turma_id_aluno(request, id_turma, id_aluno):
    notas = gerenciador_notas.listar_notas_por_turma_aluno(id_turma, id_aluno)
    print(notas)
    for id_nota in notas:
        notas[id_nota]["edicao_habilitada"] = gerenciador_notas.verificar_edicao_habilitada(notas,id_nota)
    print(notas)
    return JsonResponse(notas)

def listar_notas_por_id_turma(request, id_turma):
    notas = gerenciador_notas.listar_notas()
    notas_por_turma = gerenciador_notas.listar_notas_por_id_turma(notas, id_turma)
    for id_nota in notas_por_turma:
        notas_por_turma[id_nota]["edicao_habilitada"] = gerenciador_notas.verificar_edicao_habilitada(notas_por_turma,id_nota)
    return JsonResponse(notas_por_turma)

def listar_notas_por_id_aluno(request, id_aluno):
    notas = gerenciador_notas.listar_notas()
    notas_por_aluno = gerenciador_notas.listar_notas_por_id_aluno(notas, id_aluno)
    for id_nota in notas_por_aluno:
        notas_por_aluno[id_nota]["edicao_habilitada"] = gerenciador_notas.verificar_edicao_habilitada(notas_por_aluno,id_nota)
    return JsonResponse(notas_por_aluno)

def obter_fee_turma_aluno(request, id_turma, id_aluno):
    fee = gerenciador_notas.obter_fee_turma_aluno(id_turma, id_aluno)
    return JsonResponse(fee)

def criar_turmas_alunos(request):
    turma_aluno = json.loads(request.body)
    resultado = gerenciador_turmas_alunos.adicionar_turma_aluno(turma_aluno)
    return JsonResponse({"mensagem":resultado})

def remover_turmas_alunos(request, id_turmas_alunos):
    resultado = gerenciador_turmas_alunos.remover_turma_aluno(id_turmas_alunos)
    return JsonResponse({"mensagem": resultado})

def listar_turmas_alunos(request):
    turmas_alunos = gerenciador_turmas_alunos.listar_turmas_alunos()
    return JsonResponse(turmas_alunos)

def listar_alunos_turma(request, id_turma):
    alunos = gerenciador_turmas_alunos.listar_alunos_turma(id_turma)
    return JsonResponse(alunos)

def listar_turmas_aluno(request, id_aluno):
    turmas = gerenciador_turmas_alunos.listar_turmas_aluno(id_aluno)
    return JsonResponse(turmas)