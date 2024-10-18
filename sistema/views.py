from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import Produtos
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def estoque(request):
    #Isso assegura que o estoque sejá atualizado todas as vezes que alguem entrar na home!
    if request.method == 'GET':
        verprod = Produtos.objects.all()
        return render(request, 'estoque/estoque.html', {'verprod': verprod})
    
@login_required
def adicionar_produto(request):

    if request.method == 'GET':
        #Aqui eu estou renderizando meu html
        return render(request, 'estoque/editar/adicionar.html')
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