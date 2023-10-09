from wgsi import HttpResponse, JsonResponse
from regra_de_negocio.service import busca_dados_json

def hola_mundinho(request):
    return HttpResponse("Olá Mundo")


def get_arquivos_json(request):
    dados = busca_dados_json()
    return JsonResponse(dados)


def edit_aluno(request, id):
    return JsonResponse({"message": f"Editando o aluno com ID {id}."})

def pagina_editar_grupo(request):
    with open("static/editar_grupo.html", "r") as arquivo:
        html = arquivo.read()
    return HttpResponse(html)

def editar_grupo(requisicao, id):
    print(requisicao.body)
    print(id)
    return JsonResponse({"mensagem":f"Editando o grupo com ID {id}."})
