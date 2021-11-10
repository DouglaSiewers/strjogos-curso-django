from rest_framework.viewsets import ModelViewSet

from core.models import MotorGrafico
from core.serializers import MotorGraficoSerializer


class MotorGraficoViewSet(ModelViewSet):
    queryset = MotorGrafico.objects.all()
    serializer_class = MotorGraficoSerializer
