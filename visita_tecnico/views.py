from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import Relatorio_vist
from django.contrib.auth.decorators import login_required
from rolepermissions.decorators import has_role_decorator
def relatorio_vist(request):
    if request.method == "GET":
        return render(request, 'relatorio_vist.html')
    
    elif request.method == "POST":
        nom_tecnicos= request.POST.get("nom_tecnicos")
        nom_clientes=request.POST.get("nom_clientes")
        if not nom_tecnicos or not nom_clientes:
            return HttpResponse("Os campos 'nome do técnico' e 'nome do cliente' são obrigatórios.", status=400)
        
        enderecos = request.POST.get("enderecos")
        datas = request.POST.get("datas")
        prod_usados = request.POST.get("prod_usados")
        observacoes = request.POST.get("observacoes")
        try:
            relatorio = Relatorio_vist(
                nom_tecnicos = nom_tecnicos,
                nom_clientes = nom_clientes,
                enderecos = enderecos, 
                datas = datas, 
                prod_usados = prod_usados, 
                observacoes = observacoes
            )
            relatorio.save()
            return HttpResponse("Dados salvos")
        except Exception as e:
            return HttpResponse(f"Erro ao salvar: {str(e)}", status=500)


@login_required
def historico(request): #Aqui é a views responsavel pela parte do estoque em si
    #Isso assegura que o estoque seja atualizado toda vez que entrar na pagina, isso pela por conta da variavel 'verprod'
    if request.method == 'GET':
        verprod = Relatorio_vist.objects.all()
        return render(request, 'historico.html', {'verprod': verprod})