from django.urls import  path
from . import views

urlpatterns = [
    path('', views.listar_carros, name='listar_carros'),
    path('criar', views.criar_carro, name='criar_carro'),
    path('editar/<int:id>', views.editar_carro, name='editar_carro'),
    path('excluir/<int:id>', views.excluir_carro, name='deletar_carro'),
    path('buscar_carro/<str:q>', views.buscar_carro, name='buscar_carro'),
    path('carro/<int:id>', views.carro, name='carro')
]
