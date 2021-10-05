from django.contrib import admin

from core.models import Assinatura, Desenvolvedora, Genero, Jogo, MotorGrafico, PacoteAssinatura, ItensAssinatura

admin.site.register(Genero)
admin.site.register(Desenvolvedora)
admin.site.register(Jogo)
admin.site.register(MotorGrafico)
admin.site.register(PacoteAssinatura)

class itensInline(admin.TabularInline):
    model = ItensAssinatura

@admin.register(Assinatura)
class AssinAdmin(admin.ModelAdmin):
    inlines = (itensInline, )



