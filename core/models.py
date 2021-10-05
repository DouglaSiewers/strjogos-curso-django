from django.db import models
from django.db.models.deletion import CASCADE, PROTECT
from django.contrib.auth.models import User

class Genero(models.Model):
    descricao = models.CharField(max_length=255)

    def __str__(self):
        return self.descricao

class MotorGrafico(models.Model):
    class Meta:
        verbose_name_plural = "Motores Graficos"
    nome = models.CharField(max_length= 255)

    def __str__(self):
        return self.nome


class Desenvolvedora(models.Model):
    class Meta:
        verbose_name_plural = "Desenvolvedoras"

    nome = models.CharField(max_length= 255)

    def __str__(self):
        return self.nome

class Jogo(models.Model):
    titulo = models.CharField(max_length= 255)
    classificacao = models.CharField(max_length=20)
    dataLancamento = models.DateField()
    genero = models.ForeignKey(Genero, on_delete=models.PROTECT, related_name="jogos")
    desenvolvedora = models.ForeignKey(Desenvolvedora,on_delete=models.PROTECT, related_name="jogos")
    motorgrafico = models.ForeignKey(MotorGrafico, on_delete=models.PROTECT, related_name="jogos")

    def __str__(self):
        return self.titulo

class PacoteAssinatura(models.Model):
    descricao = models.CharField(max_length=255)
    preco = models.FloatField()
    jogo = models.ManyToManyField(Jogo,related_name="pacote")

    def __str__(self):
        return self.descricao


class Assinatura(models.Model):

    class StatusAssinatura(models.IntegerChoices):
        NAOASSINANTE = 1, 'Não Assinante'
        ASSINANTE = 2, 'Assinante'

    usuario = models.ForeignKey(User, on_delete=models.PROTECT, related_name="Assinaturas")
    status = models.IntegerField(choices=StatusAssinatura.choices, default=StatusAssinatura.NAOASSINANTE)


class ItensAssinatura(models.Model):
    Assinatura = models.ForeignKey(Assinatura, on_delete=models.CASCADE, related_name='itens')
    PacoteAssinatura = models.ForeignKey(PacoteAssinatura, on_delete=models.PROTECT, related_name='+')
    quantidade = models.IntegerField()

