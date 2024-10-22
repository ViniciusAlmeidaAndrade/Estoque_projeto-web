from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from .models import Solicitações
from django.contrib.auth.decorators import login_required

@login_required
def solicitar(request):
    if request.method == 'GET':
        return render(request, 'solicitação.html')
    
    email = request.POST.get('email')
    assunto = request.POST.get('assunto')
    mensagem = request.POST.get('mensagem')

    if email and assunto and mensagem:
        solicitar = Solicitações(
            email=email,
            assunto=assunto,
            mensagem=mensagem
        )
        solicitar.save()

        send_mail(
            assunto, 
            (f'''{mensagem}
enviado por: {email}'''), 
            settings.EMAIL_HOST_USER,
            ['gerenteabreuweb@gmail.com'],
            fail_silently=False,
        )
        return render(request, 'solicitação.html', {'feito': True})
    else:
        return render(request, 'solicitação.html', {'erro': True})
