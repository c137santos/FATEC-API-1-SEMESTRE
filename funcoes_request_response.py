from wgsi import HttpResponse
from regra_de_negocio.service import busca_dados_json

def hola_mundinho(request):
   response  =  HttpResponse({}, "hey mundinho", "", "200 OK")

   return response

def busca_arquivos_json(request):
   dados = busca_dados_json()
   dados_string = str(dados)
   response  =  HttpResponse({}, dados_string, "", "200 OK")

   return response

