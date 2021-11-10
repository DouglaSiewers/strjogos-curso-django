from rest_framework.serializers import ModelSerializer, CharField, SerializerMethodField

from core.models import Genero
from core.models import MotorGrafico
from core.models import Desenvolvedora
from core.models import Jogo
from core.models import PacoteAssinatura
from core.models import Assinatura
from core.models import ItensAssinatura


class GeneroSerializer(ModelSerializer):
    class Meta:
        model = Genero
        fields = "__all__"


class MotorGraficoSerializer(ModelSerializer):
    class Meta:
        model = MotorGrafico
        fields = "__all__"


class DesenvolvedoraSerializer(ModelSerializer):
    class Meta:
        model = Desenvolvedora
        fields = "__all__"


class JogoSerializer(ModelSerializer):
    class Meta:
        model = Jogo
        fields = "__all__"


class JogoDetailSerializer(ModelSerializer):
    genero = CharField(source="genero.descricao")
    desenvolvedora = DesenvolvedoraSerializer()

    class Meta:
        model = Jogo
        fields = "__all__"


class PacoteAssinaturaSerializer(ModelSerializer):
    class Meta:
        model = PacoteAssinatura
        fields = "__all__"


class ItensAssinaturaSerializer(ModelSerializer):
    total = SerializerMethodField()

    class Meta:
        model = ItensAssinatura()
        fields = ("PacoteAssinatura", "total")
        depth = 1

    def get_total(self, instance):
        return instance.quantidade * instance.PacoteAssinatura.preco


class AssinaturaSerializer(ModelSerializer):
    usuario = CharField(source="usuario.email")
    status = SerializerMethodField()
    itens = ItensAssinaturaSerializer(many=True)

    class Meta:
        model = Assinatura
        fields = ("id", "status", "usuario", "itens", "total")

    def get_status(self, instance):
        return instance.get_status_display()


class CriarEditarItensAssinaturaSerializer(ModelSerializer):
    class Meta:
        model = ItensAssinatura()
        fields = ("pacoteAssinatura", "quantidade")


class CriarEditarAssinaturaSerializer(ModelSerializer):
    itens = CriarEditarItensAssinaturaSerializer(many=True)

    class Meta:
        model = Assinatura
        fields = ("usuario", "itens")

    def create(self, validated_data):
        itens = validated_data.pop("itens")
        assinatura = Assinatura.objects.create(**validated_data)
        for item in itens:
            ItensAssinatura.objects.create(assinatura=assinatura, **item)
        assinatura.save()
        return assinatura

    def update(self, instance, validated_data):
        itens = validated_data.pop("itens")
        if itens:
            instance.itens.all().delete()
            for item in itens:
                ItensAssinatura.objects.create(assinatura=instance, **item)
            instance.save()
        return instance
