from django.db import models

# Create your models here.

class Solicitações(models.Model):
    email = models.EmailField(max_length=254)
    assunto = models.CharField(max_length=100)
    mensagem = models.TextField()

    def __str__(self):
        return self.assunto