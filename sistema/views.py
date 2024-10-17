from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User

# Create your views here.

def estoque(request):
    if request.method == 'GET':
        return render(request, 'estoque/estoque.html')
    
def adicionar_estoque(request):
    if request.method == 'GET':
        return render(request, 'estoque/editar/adicionar.html')

def remover_estoque(request):
    if request.method == 'GET':
        return render(request, 'estoque/editar/remover.html')

def modificar_estoque(request):
    if request.method == 'GET':
        return render(request, 'estoque/editar/modificar.html')    