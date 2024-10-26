from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import Produtos
from django.contrib.auth.decorators import login_required
from rolepermissions.decorators import has_role_decorator

# Create your views here.

@login_required
def estoque(request): #Aqui é a views responsavel pela parte do estoque em si
    #Isso assegura que o estoque seja atualizado toda vez que entrar na pagina, isso pela por conta da variavel 'verprod'
    if request.method == 'GET':
        verprod = Produtos.objects.all()
        return render(request, 'estoque/estoque.html', {'verprod': verprod})
    
@has_role_decorator('gerente')
def adicionar_produto(request): #Aqui é a view responsavel pela funcionalidade de adicionar produto ao estoque.
    #Primeiro eu renderizo a página pelo metódo GET
    if request.method == 'GET':
        return render(request, 'estoque/editar/adicionar.html')
    else:
        #Primeiro eu codei a verificação, isso para ver se existe um produto com o mesmo nome. 'Filter' = faz uma busca detalhada no banco de dados. 'first()' = busca o objeto.
        nome_prod = request.POST.get('nome')
        verificar = Produtos.objects.filter(nome_prod = nome_prod).first()

        #Aqui eu estou verificando se a variavel 'verificar' é verdadeira, se for, ela irá retornar um pop-up configurado no HTML, e após isso recarregar a página.
        if verificar:
            return render(request, 'estoque/editar/adicionar.html', {'nao_add': True})
        else:
            #Em resumo, eu estou salvando o produto no banco de dados, após salvar, ele irá redirecionar para a tela de estoque.
            produtos = Produtos(
            nome_prod=request.POST.get('nome'),
            vlr_prod=request.POST.get('valor'),
            qntd_prod=request.POST.get('qntd'),
            entrada_prod=request.POST.get('data_entrada'),
            user = request.user
            )
            produtos.save()

            return redirect('estoque')
        
@has_role_decorator('gerente')
def deletar_produto(request, id_prod): #Aqui é a view responsavel pela funcionalidade de remover o produto do estoque.
    #Estou puxando o objeto do banco de dados, se esse objeto por algum motivo não existir, vai retornar um erro 404. Eu estou puxando o produto pelo id, pois o id sempre será unico
    produto = get_object_or_404(Produtos, id_prod=id_prod)

    if request.method == 'POST':
        #Em resumo, estou deletando o produto, após isso, ele redireciona ao estoque
        produto.delete()
        return redirect('estoque')
    
    #Rendirizei a página junto ao produto que eu selecionei
    return render(request, 'estoque/editar/remover.html', {'produto': produto})

@has_role_decorator('gerente')
def modificar_produto(request, id_prod): #Aqui é a view responsavel pela funcionalidade de remover o produto do estoque.
    #Estou puxando o objeto do banco de dados, se esse objeto por algum motivo não existir, vai retornar um erro 404. Eu estou puxando o produto pelo id, pois o id sempre será unico
    produto = get_object_or_404(Produtos, id_prod = id_prod)

    if request.method == 'POST':
            #Em resumo, eu estou salvando a modificação do produto no banco de dados, após salvar, ele irá retornar um pop-up confirmando a alteração, e por fim, vai redirecionar para a tela de estoque.
            produto.nome_prod = request.POST.get('nome')
            produto.vlr_prod = request.POST.get('valor')
            produto.qtnd_prod = request.POST.get('quantidade')
            produto.entrada_prod = request.POST.get('data_entrada')

            verprod = Produtos.objects.all()
            produto.save()

            return render(request, 'estoque/estoque.html', {'add': True, 'verprod': verprod})
    
    #Rendirizei a página junto ao produto que eu selecionei
    return render(request, 'estoque/editar/modificar.html', {'produto': produto})