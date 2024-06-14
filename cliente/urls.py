from django.urls import  path
from . import views

urlpatterns = [
    path('', views.listar_clientes, name='listar_clientes'),
    path('criar', views.criar_cliente, name='criar_cliente'),
    path('editar/<int:id>', views.editar_cliente, name='editar_cliente'),
    path('excluir/<int:id>', views.excluir_cliente, name='deletar_cliente'),

    path('compras', views.listar_compras, name='listar_compras'),
    path('compras/criar', views.criar_compra, name='criar_compra'),
    path('compras/editar/<int:id>', views.editar_compra, name='editar_compra'),
    path('compras/excluir/<int:id>', views.excluir_compra, name='deletar_compra'),
    path('compras/<int:id>', views.compra, name='compra'),
]
