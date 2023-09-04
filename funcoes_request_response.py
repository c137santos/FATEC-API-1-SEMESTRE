from wgsi import HttpResponse

def hola_mundinho(request):
   response  =  HttpResponse({}, "hey mundinho", "", "200 OK")

   return response
