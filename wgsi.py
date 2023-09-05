from wsgiref.simple_server import make_server
import json
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

    def __init__(
    self,
    content="",
    status="200 OK",
    headers=None,
    content_type="text/html;charset=UTF-8",
    ):
        self.content = content
        self.status = status
        self.headers = headers or {}
        self.headers["content-type"] = content_type

    def __iter__(self):
        # iterável que será escrito no body do response
        yield self.content.encode("utf-8")
## Função retorna um response dado o request

class JsonResponse(HttpResponse):
    """
    Adicionar aqui a difereça entre http response e json response
    Atributos: 
     
    Methods:
        __init__ (self, header, body, content_type, status): Inicializa a instância HTTP
            
    """
    def __init__(self, content="{}", status="200 OK",
    headers=None, content_type="application/json"):
        self.content = json.dumps(content)
        self.status = status
        self.headers = headers or {}
        self.headers["content-type"] = content_type

class HTTPRequest:
    def __init__(self, environ):
        self.method = environ.get("REQUEST_METHOD", "GET")
        # URL
        self.path = environ.get("PATH_INFO", "/")
        # 'PATH_INFO' é uma das chaves no dicionário environ. 
        # Ela contém a parte da URL da solicitação após o nome do domínio e a porta, 
        # ou seja, a parte do caminho da URL que segue a barra (/). 
        # Por exemplo, para a URL "http://example.com/pagina", 'PATH_INFO' conteria "/pagina".
        self.query_string = environ.get("QUERY_STRING", "")
        self.content_type = environ.get("CONTENT_TYPE", "")
        # Por padrão os headers começam com HTTP_
        # retira o HTTP_ e deixa tudo em minúscilo
        self.headers = {
            key[5:].lower(): value
            for key, value in environ.items()
            if key.startswith("HTTP_")
        }
        self.environ = environ
        try:
            request_body_size = int(environ.get("CONTENT_LENGTH", 0))
        except ValueError:
            request_body_size = 0

        # lê o corpo do request HTTP
        self.body = environ["wsgi.input"].read(request_body_size).decode("utf-8")



def retorna_response(environ, start_response):
    from urls import url_match
    """
    Essa é a função desenhada no padrão WSGI. Recebe request do navegador e gera response adequado.

    Args:
        environ (dict): Conteúdo preenchido pelo servidor. 
        Como o método HTTP, cabeçalhos, URL, parâmetros de consulta e outras informações relacionadas à solicitação.
        start_response (str): callback enviado pelo servidor para acionar a requisição
        """
    request = HTTPRequest(environ)
    view = url_match(request.path)
    response = view(request)
    start_response(response.status, list(response.headers.items()))
    return response

if __name__ == '__main__':
    server = make_server("127.0.0.1", 8080, retorna_response)
    server.serve_forever()