from rest_framework.viewsets import ModelViewSet

from core.models import PacoteAssinatura
from core.serializers import PacoteAssinaturaSerializer


class PacoteAssinaturaViewSet(ModelViewSet):
    queryset = PacoteAssinatura.objects.all()
    serializer_class = PacoteAssinaturaSerializer
