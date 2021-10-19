from django.http import HttpResponse, JsonResponse
from django.utils.decorators import method_decorator
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.views import View

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.serializers import ModelSerializer, Serializer
from rest_framework.viewsets import ModelViewSet

from core.models import Genero
from core.models import MotorGrafico
from core.models import Desenvolvedora

import json

def teste(request):
    return HttpResponse("Olá mundo django")

def teste2(request):
    return HttpResponse(" Nova Pagina")


@method_decorator(csrf_exempt, name="dispatch")
class GeneroView(View):
    def get(self, request, id=None):
        if id:
            qs = Genero.objects.get(id=id)
            data = {}
            data['id'] = qs.id
            data['descricao'] = qs.descricao
            return JsonResponse(data)
        else:
                data = list(Genero.objects.values())
                formatted_data = json.dumps(data, ensure_ascii=False)
                return HttpResponse(formatted_data, content_type="application/json")

    def post(self, request):
        json_data = json.loads(request.body)
        novo_genero = Genero.objects.create(**json_data)
        data = {"id": novo_genero.id, "descricao":novo_genero.descricao}
        return JsonResponse(data)

    def patch(self, request, id):
        json_data = json.loads(request.body)
        qs = Genero.objects.get(id=id)
        qs.descricao = json_data['descricao']
        qs.save()
        data = {}
        data['id'] = qs.id
        data['descricao'] = qs.descricao
        return JsonResponse(data)

    def delete(self, request, id):
        qs = Genero.objects.get(id=id)
        qs.delete()
        data = {'mensagem': "Item excluido com sucesso."}
        return JsonResponse(data)


class GeneroSerializer(ModelSerializer):
    class Meta:
        model = Genero
        fields = '__all__'


class GeneroList(APIView):
    def get(self, resquest):
        generos = Genero.objects.all()
        serializer = GeneroSerializer(generos, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = GeneroSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else: 
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GeneroDetail(APIView):
    def get(self, request, id):
        genero = get_object_or_404(Genero.objects.all(), id=id)
        serializer = GeneroSerializer(genero)
        return Response(serializer.data)

    def put(self, request, id):
        genero = get_object_or_404(Genero.objects.all(), id=id)
        serializer = GeneroSerializer(genero, data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        genero = get_object_or_404(Genero.objects.all(), id=id)
        genero.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class GeneroListGeneric(ListCreateAPIView):
    queryset = Genero.objects.all()
    serializer_class = GeneroSerializer


class GeneroDetailGeneric(RetrieveUpdateDestroyAPIView):
    lookup_field = 'id'
    queryset = Genero.objects.all()
    serializer_class = GeneroSerializer

class GeneroViewSet(ModelViewSet):
    queryset = Genero.objects.all()
    serializer_class = GeneroSerializer

class MotorGraficoSerializer(ModelSerializer):
    class Meta:
        model = MotorGrafico
        fields = '__all__'

class MotorGraficoViewSet(ModelViewSet):
    queryset = MotorGrafico.objects.all()
    serializer_class = MotorGraficoSerializer

class DesenvolvedoraSerializer(ModelSerializer):
    class Meta:
        model = Desenvolvedora
        fields = '__all__'

class DesenvolvedoraViewSet(ModelViewSet):
    queryset = Desenvolvedora.objects.all()
    serializer_class = DesenvolvedoraSerializer