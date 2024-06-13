from django.urls import  path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('criar', views.criar_carro, name='criar_carro'),
    path('editar/<int:id>', views.editar_carro, name='editar_carro'),
    path('excluir/<int:id>', views.excluir_carro, name='deletar_carro'),
]
