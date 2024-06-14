import re
from django.http import JsonResponse
from django.shortcuts import render

from .models import Cliente, Compra
from .utils import formatar_preco

# Create your views here.
def listar_clientes(request):
    clientes = Cliente.objects.all()

    for cliente in clientes:
        cliente.nivel_bruto = cliente.nivel()
        cliente.save()

    context = {
        'clientes': clientes
    }
    return render(request, 'listar_clientes.html', context)

def criar_cliente(request):
    return JsonResponse({'message': 'Criar cliente'})

def editar_cliente(request, id):
    return JsonResponse({'message': 'Editar cliente'})

def excluir_cliente(request, id):
    return JsonResponse({'message': 'Excluir cliente'})


def listar_compras(request):
    compras = Compra.objects.all()



    compras.valor = 0
    for compra in compras:
        compra.valor = compra.valor()
        compra.preco_formatado = formatar_preco(compra.valor)

    context = {
        'compras': compras
    }

    return render(request, 'listar_compras.html', context)


def criar_compra(request):
    return JsonResponse({'message': 'Criar compra'})

def editar_compra(request, id):
    return JsonResponse({'message': 'Editar compra'})

def excluir_compra(request, id):
    return JsonResponse({'message': 'Excluir compra'})
