from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import RelatoriosVisitas
from django.contrib.auth.decorators import login_required
from rolepermissions.decorators import has_role_decorator

@login_required
def relatorio_vist(request):
    if request.method == "GET":
        return render(request, 'relatorio_vist.html')
    else:
        nom_tecnicos = request.POST.get("nom_tecnicos")
        verificar = User.objects.filter(username = nom_tecnicos).first()
        
        if verificar:
            relatorio = RelatoriosVisitas(
                nom_tecnico = nom_tecnicos,
                nom_cliente = request.POST.get("nom_clientes"),
                endereco = request.POST.get("enderecos"),
                data = request.POST.get("datas"),
                prod_usado = request.POST.get("prod_usados"),
                observacao = request.POST.get("observacoes"),
                user = request.user
            )
            relatorio.save()
            return render(request, 'relatorio_vist.html', {'add': True})
        else:
            return render(request, 'relatorio_vist.html', {'erro': True})


        
@login_required
def historico(request): #Aqui é a views responsavel pela parte do historico em si
    #Isso assegura que o estoque seja atualizado toda vez que entrar na pagina, isso pela por conta da variavel 'verprod'
    if request.method == 'GET':
        verrelat = RelatoriosVisitas.objects.all()
        return render(request, 'historico.html', {'verrelat': verrelat})