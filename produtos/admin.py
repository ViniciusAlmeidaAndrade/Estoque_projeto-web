from django.contrib import admin
from.models import Relatorio_vist

@admin.register(Relatorio_vist)
class Relatorio_Visitas(admin.ModelAdmin):
    list_display = ('nom_tecnicos', 'nom_clientes', 'enderecos', 'datas', 'prod_usados', 'observacoes') #Isso é para aparece a tabela no /admin, caso queira alterar por lá.

