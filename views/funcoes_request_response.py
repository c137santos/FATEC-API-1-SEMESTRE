from wgsi import HttpResponse, JsonResponse
from regra_de_negocio.service import busca_dados_json, busca_info_turmas_json, busca_turmas_json, busca_grupo_semTurma

def hola_mundinho(request):
    return HttpResponse("Olá Mundo")

def get_arquivos_json(request):
    dados = busca_dados_json()
    return JsonResponse(dados)

def edit_aluno(request, id):
    return JsonResponse({"message": f"Editando o aluno com ID {id}."})

def get_turmas(request):
    turmas_data = busca_turmas_json()
    return JsonResponse(turmas_data)

# Esta função é uma view que lida com uma solicitação HTTP para obter informações sobre grupos e alunos de uma turma específica
def get_grupos_alunos(request, id):
    grupos_data, alunos_data = busca_info_turmas_json(id)
    response_data = {
        "grupos_data": grupos_data,  # Dados dos grupos associados à turma
        "alunos_data": alunos_data   # Dados dos alunos associados aos grupos
    }
    # Passo 3: Retorna uma resposta JSON contendo os dados organizados
    return JsonResponse(response_data)

def grupo_semTurma(request):
    grupos_Data, grupo_semTurma_data = busca_grupo_semTurma()
    response_data = {
        "grupos_data": grupos_Data,
        "grupo_semTurma_data": grupo_semTurma_data
    }
    return JsonResponse(response_data)
    

