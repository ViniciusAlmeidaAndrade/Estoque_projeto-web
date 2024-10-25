from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.solicitar, name = 'enviar_solicitação'), #Responsavel pela tela inicial do redirect
]
