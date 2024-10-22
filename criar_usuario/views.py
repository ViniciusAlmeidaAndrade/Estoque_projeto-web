from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from rolepermissions.roles import assign_role
from django.contrib.auth.decorators import login_required
from rolepermissions.decorators import has_role_decorator

# Create your views here.

@has_role_decorator('gerente')
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

@has_role_decorator('gerente')
def lista_user(request):
    ver_user = User.objects.all()
    return render(request, 'lista_users/lista.html', {'ver_user': ver_user})
    
@has_role_decorator('gerente')    
def mudar_senha(request, id):
    #Segurança para verificar se o usuario existe, se não, ele retorna um erro 404
    user = get_object_or_404(User, id=id)
    
    if request.method == 'GET':
        return render(request, 'lista_users/editar.html', {'user': user})
    else:
        #Recebe a nova senha
        nova_senha = request.POST.get('senha')
        if nova_senha:
            user.set_password(nova_senha)
            user.save()
            return render(request, 'lista_users/editar.html', {'user': user , 'add': True})
        else:
            #Mensagem de erro(vai ser adicionada ainda)
            return render(request, 'lista_users/editar.html', {'user': user , 'nao_add': True})
        
def deletar_usuario(request, id):
    #Estou buscando o produto pelo id, se nao existir, da erro 404
    usuario = get_object_or_404(User, id = id)

    if request.method == 'POST':
        #Função para deletar o produto, produto esse que selecionei pelo id
        usuario.delete()
        return redirect('lista')  # Redireciona para o lista

    return render(request, 'lista_users/remover.html', {'usuario': usuario})    

def modificar_usuario(request, id):
    # Isso aqui vai ver se o usuário existe, se não existir, retorna uma página 404
    usuario = get_object_or_404(User, id=id)

    if request.method == 'POST':
        # Recebe os dados do form
        usuario.first_name = request.POST.get('first_name')
        usuario.last_name = request.POST.get('last_name')
        usuario.username = request.POST.get('username')
        usuario.email = request.POST.get('email')

        usuario.save()

        return render(request, 'lista_users/modificar_info.html', {'add': True, 'usuario': usuario})

    return render(request, 'lista_users/modificar_info.html', {'usuario': usuario})