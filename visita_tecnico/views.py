from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import RelatoriosVisitas
from django.contrib.auth.decorators import login_required
from rolepermissions.decorators import has_role_decorator
from django.contrib.auth import logout

def logout_view(request):
    logout(request)
    return redirect('tela_login')

@login_required
def relatorio_vist(request):
    if request.method == "GET":
        return render(request, 'relatorio_vist.html')
    else:
        nom_tecnicos = request.POST.get("nom_tecnicos")
        
        if nom_tecnicos == request.user.username:
            relatorio = RelatoriosVisitas(
                nom_tecnico = request.POST.get("nom_tecnicos_real"),
                nom_tecnico_f = request.POST.get("nom_tecnicos_real_f"),
                usuario = nom_tecnicos,
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
    

@has_role_decorator('gerente')
def deletar_visita(request, id_visita):
    #Estou puxando o objeto do banco de dados, se esse objeto por algum motivo não existir, vai retornar um erro 404. Eu estou puxando o produto pelo id, pois o id sempre será unico
    visita = get_object_or_404(RelatoriosVisitas, id_visita = id_visita)

    if request.method == 'POST':
        #Em resumo, estou deletando o produto, após isso, ele redireciona ao estoque
        visita.delete()
        return redirect('historico')
    
    #Rendirizei a página junto ao produto que eu selecionei
    return render(request, 'deletar_visita.html', {'visita': visita})