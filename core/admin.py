from django.contrib import admin
from core.models import Estabelecimento


class EstabelecimentoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'logradouro', 'numero', 'cidade', 'estado')
    list_filter = ('nome',)


admin.site.register(Estabelecimento, EstabelecimentoAdmin)
