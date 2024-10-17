from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import Produtos

# Create your views here.

def estoque(request):
    if request.method == 'GET':
        verprod = Produtos.objects.all()
        return render(request, 'estoque/estoque.html', {'verprod': verprod})
    
def adicionar_estoque(request):
    if request.method == 'GET':
        verprod = {
            'verprod': Produtos.objects.all()
        }
        return render(request, 'estoque/editar/adicionar.html', verprod)
    else:
        produto = Produtos(
            nome_prod=request.POST.get('nome'),
            vlr_prod=request.POST.get('valor'),
            qtnd_prod=request.POST.get('qntd'),
            entrada_prod=request.POST.get('data_entrada')
        )
        produto.save()
        
        if produto is None:
            return render(request, 'estoque/editar/adicionar.html', {'nao_add': True})
        else:
            return render(request, 'estoque/editar/adicionar.html', {'add': True})


def remover_estoque(request):
    if request.method == 'GET':
        return render(request, 'estoque/editar/remover.html')

def modificar_estoque(request):
    if request.method == 'GET':
        return render(request, 'estoque/editar/modificar.html')    