from django.contrib import admin
from .models import Produtos

# Register your models here.

@admin.register(Produtos)
class ProdutosAdmin(admin.ModelAdmin):
    list_display = ('id_prod', 'nome_prod', 'vlr_prod', 'qtnd_prod', 'entrada_prod') #Isso é para aparece a tabela no /admin, caso queira alterar por lá.

