from django.http import HttpResponse

def teste(request):
    return HttpResponse("Olá mundo django")

def teste2(request):
    return HttpResponse(" Nova Pagina")