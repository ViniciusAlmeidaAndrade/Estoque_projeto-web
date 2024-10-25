from django.shortcuts import render
from django.http import HttpResponse
from.models import Relatorio_vist

def relatorio_vist(request):
    if request.method == "GET":
        nome = 'caio'
        return render(request, 'relatorio_vist.html', {'nome': nome})
    
    elif request.method == "POST":
        nom_tecnicos= request.POST.get("nom_tecnicos")
        nom_clientes=request.POST.get("nom_clientes")
        if not nom_tecnicos or not nom_clientes:
            return HttpResponse("Os campos 'nome do técnico' e 'nome do cliente' são obrigatórios.", status=400)
        
        enderecos = request.POST.get("enderecos")
        datas = request.POST.get("datas")
        prod_usados = request.POST.get("prod_usados")
        observacoes = request.POST.get("observacoes", "")
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