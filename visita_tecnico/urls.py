from django.urls import path
from . import views

urlpatterns = [
    path('', views.relatorio_vist, name = 'relatorio_vist' ),
    
]