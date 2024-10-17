from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from sistema import urls

# Create your views here.

def tela_login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username = username, password = password)

        if user is None:
            return render(request, 'login.html', {'usuario_invalido': True})
        else:
            login(request, user)
            return redirect('sistema/estoque')
        