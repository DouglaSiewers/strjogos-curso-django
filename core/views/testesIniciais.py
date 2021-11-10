from django.http import HttpResponse, JsonResponse

import json


def teste(request):
    return HttpResponse("Olá mundo django")


def teste2(request):
    return HttpResponse(" Nova Pagina")
