from wgsi import JsonResponse
from regra_de_negocio.service import (
    busca_turmas,
    cria_turma,
)

from regra_de_negocio.gerenciador_turmas import excluir_turma_svc, editar_turma_svc

import regra_de_negocio.gerenciador_ciclo as gerenciar_ciclo

import json


def edit_aluno(request, id):
    return JsonResponse({"message": f"Editando o aluno com ID {id}."})

def get_turmas(request):
    turmas_data = busca_turmas()
    return JsonResponse(turmas_data)

def obtem_turma_especifica(request, id):
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
    dados_nova_turma = json.loads(request.body)
    resposta = cria_turma(dados_nova_turma)
    return JsonResponse(resposta)

def excluir_turma(request, id):
    resultado = excluir_turma_svc(id)
    return JsonResponse({"mensagem": resultado})

def criar_ciclo(request):
    novo_ciclo = json.loads(request.body)
    resultado = gerenciar_ciclo.adicionar_ciclo(novo_ciclo)
    return JsonResponse({"mensagem":resultado})

def listar_ciclos(request):
    ciclos = gerenciar_ciclo.listar_ciclos()
    return JsonResponse(ciclos)

def listar_ciclos_por_id_turma(request, id_turma):
    ciclos = gerenciar_ciclo.listar_ciclos_por_id_turma(id_turma)
    return JsonResponse(ciclos)