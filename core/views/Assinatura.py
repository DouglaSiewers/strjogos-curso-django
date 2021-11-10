from rest_framework.viewsets import ModelViewSet

from core.models import Assinatura
from core.serializers import AssinaturaSerializer
from core.serializers import CriarEditarAssinaturaSerializer


class AssinaturaViewSet(ModelViewSet):
    queryset = Assinatura.objects.all()
    # serializer_class = AssinaturaSerializer

    def get_serializer_class(self):
        if self.action == "list" or self.action == "retrieve":
            return AssinaturaSerializer
        return CriarEditarAssinaturaSerializer
