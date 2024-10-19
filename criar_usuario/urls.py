from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.criar_usuario, name = 'criar_usuario'),
    path('lista', views.lista_user, name = 'lista'),
    path('mudar_senha/<int:id>', views.mudar_senha, name = 'editar'), 
    path('deletar/<int:id>', views.deletar_usuario, name = 'deletar'),   
    path('mudar_informações/<int:id>', views.modificar_usuario, name = 'mudar_informações'),   

]