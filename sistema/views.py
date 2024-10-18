from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import Produtos
from django.contrib.auth.decorators import login_required
from rolepermissions.decorators import has_role_decorator
# Create your views here.

@login_required
def estoque(request):
    #Isso assegura que o estoque sejá atualizado todas as vezes que alguem entrar na home!
    if request.method == 'GET':
        verprod = Produtos.objects.all()
        return render(request, 'estoque/estoque.html', {'verprod': verprod})
    
@has_role_decorator('gerente')
def adicionar_produto(request):

    if request.method == 'GET':
        #Aqui eu estou renderizando meu html
        return render(request, 'estoque/editar/adicionar.html')
    else:
        #Primeiro eu estou faazendo uma verificação para assegurar que não tenha um produto com o mesmo nome, caso tenha, aparece um pop-up na tela
        nome_prod = request.POST.get('nome')
        verificar = Produtos.objects.filter(nome_prod = nome_prod).first()

        if verificar:
            return render(request, 'estoque/editar/adicionar.html', {'nao_add': True})
        else:
            produtos = Produtos(
            nome_prod=request.POST.get('nome'),
            vlr_prod=request.POST.get('valor'),
            qtnd_prod=request.POST.get('qntd'),
            entrada_prod=request.POST.get('data_entrada')
            )
            produtos.save()

            return redirect('estoque')
        
@has_role_decorator('gerente')
def deletar_produto(request, id_prod):
    #Estou buscando o produto pelo id, se nao existir, da erro 404
    produto = get_object_or_404(Produtos, id_prod=id_prod)

    if request.method == 'POST':
        #Função para deletar o produto, produto esse que selecionei pelo id
        produto.delete()
        return redirect('estoque')  # Redireciona para o estoque

    return render(request, 'estoque/editar/remover.html', {'produto': produto})

@has_role_decorator('gerente')
def modificar_produto(request, id_prod):
    #Isso aqui vai ver se o produto existe, se nao existir, retorna uma página 404
    produto = get_object_or_404(Produtos, id_prod = id_prod)

    if request.method == 'POST':
            # Recebe os dados do formulários
            produto.nome_prod = request.POST.get('nome')
            produto.vlr_prod = request.POST.get('valor')
            produto.qtnd_prod = request.POST.get('quantidade')
            produto.entrada_prod = request.POST.get('data_entrada')

            verprod = Produtos.objects.all()
            produto.save()

            return render(request, 'estoque/estoque.html', {'add': True, 'verprod': verprod})
              
    return render(request, 'estoque/editar/modificar.html', {'produto': produto})