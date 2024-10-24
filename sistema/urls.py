from django.urls import path, include
from . import views
from solicitacao import urls
urlpatterns = [
    path('estoque/', views.estoque, name = 'estoque'), #Essa aqui sera a nossa home
    path('estoque/adicionar/', views.adicionar_produto, name = 'add_estoque'), #Essa aqui será o caminho para o gerente add o produto
    path('estoque/editar/<int:id_prod>/', views.modificar_produto, name='editar_produto'), #Esse aqui é o caminho para o gerente modificar o produto
    path('estoque/deletar/<int:id_prod>/', views.deletar_produto, name='deletar_produto'), #Esse aqui é o caminho para o gerente apagar o produto
    
    path('criar_usuario/', include('criar_usuario.urls'), name = 'criar_usuario'),
    path('solicitação/', include('solicitacao.urls'), name = 'enviar_solicitação'),
    path('visita_tecnica/', include('produtos.urls'), name = 'visita_tecnica'),

]