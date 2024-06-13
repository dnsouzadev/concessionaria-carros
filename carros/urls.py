from django.urls import  path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('criar', views.criar_carro, name='criar_carro'),
]
