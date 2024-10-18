from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from rolepermissions.roles import assign_role

# Create your views here.

def criar_usuario(request):
    if request.method == 'GET':
        return render(request, 'cadastro.html')
    else:
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        user = User.objects.filter(username = username).first()

        if user:
            return render(request, 'cadastro.html', {'duplicado': True})
        else:                         
            user = User.objects.create_user(first_name = first_name, last_name = last_name, username = username, email = email, password = password)
            user.save()
            assign_role(user, 'tecnico')
            return render(request, 'cadastro.html', {'add': True})

        
