from wsgiref.simple_server import make_server
import pdb
# Implementação do protocolo de comunicação entre o python e a web
# WSGI - Web Server Gateway Interface
# Esse padrão permitirá que o navegador possa executar nosso código para internet
# Referência PEP333

class HttpResponse:
    """
    Essa classe montar o objeto de resposta HTTP, por meio das informações da requisição web.

    Atributos: 
        header (dict): Esse é um dicionário para as informações header's HTTP
        body (str): O texto da resposta.
        content_type (str): O tipo que é composto o texto; Str, binário, html.
        status (str): Um dos códigos HTTP de status, ok, not_found. etc.

    Methods:
        __init__ (self, header, body, content_type, status): Inicializa a instância HTTP
        __iter__(self): Permite tornar o objeto iterável
    """

    def __init__(self, header, body, content_type, status) -> None:
        self.header = header
        self.body = body
        self.content_type = content_type
        self.status = status

    def __iter__(self):
        """
        Permite o body ser interável
        """
        yield self.body.encode("utf-8")
    
## Função retorna um response dado o request

def retorna_response(environ, start_response):
    from urls import url_match
    """
    Essa é a função desenhada no padrão WSGI. Recebe request do navegador e gera response adequado.

    Args:
        environ (dict): Conteúdo preenchido pelo servidor. 
        Como o método HTTP, cabeçalhos, URL, parâmetros de consulta e outras informações relacionadas à solicitação.
        start_response (str): callback enviado pelo servidor para acionar a requisição
        """
    start_response("200 OK", [])
    url = environ.get('PATH_INFO', "/")
    view = url_match(url)
    response = view(None)
    return response

# 'PATH_INFO' é uma das chaves no dicionário environ. 
# Ela contém a parte da URL da solicitação após o nome do domínio e a porta, 
# ou seja, a parte do caminho da URL que segue a barra (/). 
# Por exemplo, para a URL "http://example.com/pagina", 'PATH_INFO' conteria "/pagina".

if __name__ == '__main__':
    server = make_server("127.0.0.1", 8080, retorna_response)
    server.serve_forever()