<<<<<<< HEAD
from wgsi import HttpResponse, JsonResponse
from regra_de_negocio.service import (
    busca_dados_json,
    busca_turmas,
    buscar_grupos,
    cria_turma,
)

from regra_de_negocio.global_settings import read_global_settings, edit_global_settings
from regra_de_negocio.gerenciador_turmas import excluir_turma, editar_turma_svc
=======
from wgsi import JsonResponse
from regra_de_negocio.service import (
    busca_turmas,
    cria_turma,
)

from regra_de_negocio.gerenciador_turmas import excluir_turma_svc, editar_turma_svc

import regra_de_negocio.gerenciador_ciclos as gerenciador_ciclos
import regra_de_negocio.gerenciador_notas as gerenciador_notas
import regra_de_negocio.gerenciador_turmas_alunos as gerenciador_turmas_alunos
import regra_de_negocio.gerenciador_alunos as gerenciador_alunos
>>>>>>> padrao_datas_MOMENTJS#142

import json


<<<<<<< HEAD
def hola_mundinho(request):
    return HttpResponse("Olá Mundo")


def get_arquivos_json(request):
    dados = busca_dados_json()
    return JsonResponse(dados)


def edit_aluno(request, id):
    return JsonResponse({"message": f"Editando o aluno com ID {id}."})


def get_global_settings(request):
    global_settings = read_global_settings()
    return JsonResponse(global_settings)


def alterar_global_settings(request):
    alteracoes = json.loads(request.body)
    try:
        edit_global_settings(alteracoes["sprints"], alteracoes["dias"])
        return JsonResponse({"message": "Editou global settings"})

    except Exception as error:
        JsonResponse(error)


def get_turmas(request):
=======
def criar_aluno(request):
    novo_aluno = json.loads(request.body)
    gerenciador_alunos.criar_aluno(novo_aluno)
    return JsonResponse({"message": "Aluno criado"})


def deletar_aluno(request, id):
    gerenciador_alunos.apagar_aluno(id)
    return JsonResponse({"message": f"Deletado o aluno com ID {id}."})


def listar_alunos(request):
    alunos_data = gerenciador_alunos.listar_alunos()
    return JsonResponse(alunos_data)


def editar_aluno(request, id):
    aluno = json.loads(request.body)
    gerenciador_alunos.editar_aluno_svc(id, aluno)
    return JsonResponse({"message": f"Editando o aluno com ID {id}."})


def listar_turmas(request):
>>>>>>> padrao_datas_MOMENTJS#142
    turmas_data = busca_turmas()
    return JsonResponse(turmas_data)


<<<<<<< HEAD
def obtem_turma_especifica(request, id):
=======
def obter_turma(request, id):
>>>>>>> padrao_datas_MOMENTJS#142
    turmas_data = busca_turmas()
    return JsonResponse(turmas_data[id])


def editar_turma(request, id):
    turma = json.loads(request.body)
    resultado = editar_turma_svc(
<<<<<<< HEAD
        id, turma["nome"], turma["professor"], turma["data_de_inicio"]
=======
        id,
        turma["nome"],
        turma["professor"],
        turma["data_de_inicio"],
        turma["duracao_ciclo"],
>>>>>>> padrao_datas_MOMENTJS#142
    )
    return JsonResponse({"mensagem": resultado})


<<<<<<< HEAD
def get_grupos(request):
    grupos_data = buscar_grupos()
    return JsonResponse(grupos_data)


def post_turma(request):
    dados_nova_turma = request.body
    resposta = cria_turma(dados_nova_turma)
    return JsonResponse(resposta)


def api_v1_turmas_excluir(request, id):
    resultado = excluir_turma(id)
    return JsonResponse({"mensagem": resultado})
=======
def criar_turma(request):
    nova_turma = json.loads(request.body)
    resposta = cria_turma(nova_turma)
    quantidade_ciclos = resposta["nova_turma"]["quantidade_ciclos"]
    for i in range(quantidade_ciclos):
        # cria um ciclo padrão para a quantidade de ciclos desejada
        ciclo = {}
        ciclo["id_turma"] = resposta["id_nova_turma"]
        ciclo["duracao"] = 15
        ciclo["peso_nota"] = float(i+1)
        ciclo["numero_ciclo"] = i+1
        ciclo["prazo_insercao_nota"] = 5
        gerenciador_ciclos.adicionar_ciclo(ciclo)
    return JsonResponse(resposta)


def excluir_turma(request, id):
    resultado = excluir_turma_svc(id)
    return JsonResponse({"mensagem": resultado})


def criar_ciclo(request):
    novo_ciclo = json.loads(request.body)
    resultado = gerenciador_ciclos.adicionar_ciclo(novo_ciclo)
    return JsonResponse({"mensagem": resultado})


def listar_ciclos(request):
    ciclos = gerenciador_ciclos.listar_ciclos()
    return JsonResponse(ciclos)


def listar_ciclos_por_id_turma(request, id_turma):
    ciclos = gerenciador_ciclos.listar_ciclos_por_id_turma(id_turma)
    return JsonResponse(ciclos)

def editar_ciclo(request, id_ciclo):
    ciclo = json.loads(request.body)
    resultado = gerenciador_ciclos.editar_ciclo(id_ciclo, ciclo)
    return JsonResponse({"mensagem":resultado})

def criar_nota(request):
    nova_nota = json.loads(request.body)
    if not gerenciador_notas.verificar_existencia_nota_por_ciclo(nova_nota):
        resultado = gerenciador_notas.adicionar_nota(nova_nota)
        return JsonResponse({"mensagem": resultado})
    else:
        return JsonResponse({"mensagem": False})


def editar_nota(request):
    notas_atualizada = json.loads(request.body)
    print(notas_atualizada)
    resultado = gerenciador_notas.editar_nota(notas_atualizada)
    return JsonResponse({"mensagem": resultado})


def excluir_nota(request, id_nota):
    resultado = gerenciador_notas.remover_nota(id_nota)
    return JsonResponse({"mensagem": resultado})


def listar_notas(request):
    notas = gerenciador_notas.listar_notas()
    for id_nota in notas:
        notas[id_nota][
            "edicao_habilitada"
        ] = gerenciador_notas.verificar_edicao_habilitada(notas, id_nota)
    return JsonResponse(notas)


def listar_notas_por_id_turma_id_aluno(request, id_turma, id_aluno):
    notas = gerenciador_notas.listar_notas_por_turma_aluno(id_turma, id_aluno)
    print(notas)
    for id_nota in notas:
        notas[id_nota][
            "edicao_habilitada"
        ] = gerenciador_notas.verificar_edicao_habilitada(notas, id_nota)
    print(notas)
    return JsonResponse(notas)


def filtrar_notas_por_id_turma(request, id_turma):
    notas = gerenciador_notas.listar_notas()
    notas_por_turma = gerenciador_notas.filtrar_notas_por_id_turma_svc(notas, id_turma)
    for id_nota in notas_por_turma:
        notas_por_turma[id_nota][
            "edicao_habilitada"
        ] = gerenciador_notas.verificar_edicao_habilitada(notas_por_turma, id_nota)
    return JsonResponse(notas_por_turma)


def listar_notas_por_id_aluno(request, id_aluno):
    notas = gerenciador_notas.listar_notas()
    notas_por_aluno = gerenciador_notas.listar_notas_por_id_aluno(notas, id_aluno)
    for id_nota in notas_por_aluno:
        notas_por_aluno[id_nota][
            "edicao_habilitada"
        ] = gerenciador_notas.verificar_edicao_habilitada(notas_por_aluno, id_nota)
    return JsonResponse(notas_por_aluno)


def obter_fee_turma_aluno(request, id_turma, id_aluno):
    fee = gerenciador_notas.obter_fee_turma_aluno(id_turma, id_aluno)
    return JsonResponse(fee)


def criar_turmas_alunos(request):
    turma_aluno = json.loads(request.body)
    resultado = gerenciador_turmas_alunos.adicionar_turma_aluno(turma_aluno)
    return JsonResponse({"mensagem": resultado})


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
>>>>>>> padrao_datas_MOMENTJS#142
