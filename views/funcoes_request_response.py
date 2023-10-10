from wgsi import HttpResponse, JsonResponse
from regra_de_negocio.service import busca_dados_json

def get_arquivos_json(request):
    dados = busca_dados_json()
    return JsonResponse(dados)

def editar_turma(request, id):
    print(request.body)
    print(id)
    return JsonResponse({"message": f"Editado a turma com ID {id}."})