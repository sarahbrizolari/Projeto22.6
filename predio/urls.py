from django.urls import path
#from django.contrib import admin

from .views import list_Morador, create_Morador, update_Morador, delete_Morador
from .views import list_Vaga, create_Vaga, update_Vaga, delete_Vaga
from .views import list_Carro, create_Carro, update_Carro, delete_Carro
from .views import list_Visitante, create_Visitante, update_Visitante, delete_Visitante
from .views import list_PrestadorDeServico, create_PrestadorDeServico, update_PrestadorDeServico, delete_PrestadorDeServico

urlpatterns = [

#MORADOR
path('', list_Morador, name='list_Morador'),
path('new_Morador', create_Morador, name='create_Morador'),
path('update_Morador/<int:id>/', update_Morador, name='update_Morador'),
path('delete_Morador/<int:id>/', delete_Morador, name='delete_Morador'),

#Vaga
path('list_Vaga', list_Vaga, name='list_Vaga'),
path('new_Vaga', create_Vaga, name='create_Vaga'),
path('update_Vaga/<int:id>/', update_Vaga, name='update_Vaga'),
path('delete_Vaga/<int:id>/', delete_Vaga, name='delete_Vaga'),

#Carro
path('list_Carro', list_Carro, name='list_Carro'),
path('new_Carro', create_Carro, name='create_Carro'),
path('update_Carro/<int:id>/', update_Carro, name='update_Carro'),
path('delete_Carro/<int:id>/', delete_Carro, name='delete_Carro'),

#Visitante
path('list_Visitante', list_Visitante, name='list_Visitante'),
path('new_Visitante', create_Visitante, name='create_Visitante'),
path('update_Visitante/<int:id>/', update_Visitante, name='update_Visitante'),
path('delete_Visitante/<int:id>/', delete_Visitante, name='delete_Visitante'),

#Prestador de servico
path('list_PrestadorDeServico', list_PrestadorDeServico, name='list_PrestadorDeServico'),
path('new_PrestadorDeServico', create_PrestadorDeServico, name='create_PrestadorDeServico'),
path('update_PrestadorDeServico/<int:id>/', update_PrestadorDeServico, name='update_PrestadorDeServico'),
path('delete_PrestadorDeServico/<int:id>/', delete_PrestadorDeServico, name='delete_PrestadorDeServico'),

]
