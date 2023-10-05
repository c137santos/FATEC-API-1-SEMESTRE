from wgsi import HttpResponse, JsonResponse
from regra_de_negocio.service import busca_dados_json, busca_turmas, busca_grupos, busca_grupo_alunos, busca_alunos, busca_grupos_alunos_turma


def hola_mundinho(request):
    return HttpResponse("Olá Mundo")

def get_arquivos_json(request):
    dados = busca_dados_json()
    return JsonResponse(dados)

def get_turmas(request):
    dados = busca_turmas()
    return JsonResponse(dados)

def get_grupos(request):
    dados = busca_grupos()
    return JsonResponse(dados)

def get_grupo_alunos(request):
    dados = busca_grupo_alunos()
    return JsonResponse(dados)

def get_alunos(request):
    dados = busca_alunos()
    return JsonResponse(dados)

# Esta função é uma view que lida com uma solicitação HTTP para obter informações sobre grupos e alunos de uma turma específica
def get_grupos_alunos_turma(request, id):
    # Passo 1: Chama a função para buscar grupos e alunos associados à turma
    grupos_data, alunos_data = busca_grupos_alunos_turma(id)
    # Passo 2: Organiza os dados em um dicionário de resposta
    response_data = {
        "grupos_data": grupos_data,  # Dados dos grupos associados à turma
        "alunos_data": alunos_data   # Dados dos alunos associados aos grupos
    }
    # Passo 3: Retorna uma resposta JSON contendo os dados organizados
    return JsonResponse(response_data)

def edit_aluno(request, id):
    return JsonResponse({"message": f"Editando o aluno com ID {id}."})
