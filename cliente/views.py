import re
from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
def listar_clientes(request):
    return JsonResponse({'message': 'Listar clientes'})

def criar_cliente(request):
    return JsonResponse({'message': 'Criar cliente'})

def editar_cliente(request, id):
    return JsonResponse({'message': 'Editar cliente'})

def excluir_cliente(request, id):
    return JsonResponse({'message': 'Excluir cliente'})
