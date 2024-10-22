from django.urls import path, include
from . import views
#    path('solicitação/', include('solicitacao.urls'), name = 'solicitacao_sis')

urlpatterns = [
    path('', views.solicitar, name = 'enviar_solicitação'),
]
