from django.urls import path, include
from . import views

urlpatterns = [
    path('estoque/', views.estoque, name = 'estoque'),
    path('estoque/adicionar/', views.adicionar_estoque, name = 'add_estoque'),
    path('estoque/remover/', views.remover_estoque, name = 'remov_estoque'),
    path('estoque/modificar/', views.modificar_estoque, name = 'mod_estoque'),

    
]
