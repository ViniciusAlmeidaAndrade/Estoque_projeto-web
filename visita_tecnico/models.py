from django.db import models

class Relatorio_vist(models.Model):
    nom_tecnicos = models.CharField(max_length=50)
    nom_clientes =  models.CharField(max_length=50)
    enderecos = models.CharField(max_length=150)
    datas = models.DateField((""), auto_now=False, auto_now_add=True)
    prod_usados =  models.CharField(max_length=255)
    observacoes =  models.CharField(max_length=255)
    
    def _str_(self) -> str:
        return self.nome