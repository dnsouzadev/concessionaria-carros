from genericpath import exists
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render

from .forms import ClienteForm

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
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_clientes')
    else:
        form = ClienteForm()
        return render(request, 'criar_cliente.html', {'form': form})

def editar_cliente(request, id):
    cliente = Cliente.objects.get(id=id)
    if cliente is None:
        return redirect('listar_clientes')
    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('listar_clientes')
    else:
        form = ClienteForm(instance=cliente)
        return render(request, 'criar_cliente.html', {'form': form})


def excluir_cliente(request, id):
    cliente = Cliente.objects.get(id=id)
    if cliente is None:
        return redirect('listar_clientes')
    cliente.delete()
    return JsonResponse({'message': 'Cliente excluído com sucesso!'})


def listar_compras(request):
    return render(request, 'listar_compras.html')


def criar_compra(request):
    return JsonResponse({'message': 'Criar compra'})

def editar_compra(request, id):
    return JsonResponse({'message': 'Editar compra'})

def excluir_compra(request, id):
    return JsonResponse({'message': 'Excluir compra'})

def compra(request, id):
    try:
        compras = Compra.objects.filter(cliente_id=id)

        compras.valor = 0
        for compra in compras:
            compra.valor = compra.valor()
            compra.preco_formatado = formatar_preco(compra.valor)

        context = {
            'compras': compras
        }

        return render(request, 'compra.html', context)
    except Compra.DoesNotExist:
        return HttpResponse('nao existe compra para este cliente')
