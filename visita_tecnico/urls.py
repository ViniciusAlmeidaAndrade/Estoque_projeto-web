from django.urls import path
from . import views

urlpatterns = [
    path('', views.relatorio_vist, name = 'relatorio_vist' ),
    path('historico/', views.historico, name = 'historico' ),

    path('historico/deletar/<int:id_visita>/', views.deletar_visita, name='deletar_visita'), #Essa é a url responsavel por redirecionar para a página de deletar um produto, página essa, que so o gerente terá acesso

    path('logout/', views.logout_view, name = 'logout'), #URL responsavel por fazer o logout do usuario
]