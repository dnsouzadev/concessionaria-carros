from genericpath import exists
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render

from .forms import ClienteForm, CompraForm

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
    compras = Compra.objects.all()

    for compra in compras:
        compra.preco_formatado = formatar_preco(compra.valor())
        compra.nome_cliente = compra.cliente.nome + ' ' + compra.cliente.sobrenome

    context = {
        'compras': compras,
    }
    return render(request, 'listar_compras.html', context)


def criar_compra(request):
    if request.method == 'POST':
        form = CompraForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_compras')
    else:
        form = CompraForm()
        return render(request, 'criar_compra.html', {'form': form})

def editar_compra(request, id):
    compra = Compra.objects.get(id=id)
    if compra is None:
        return redirect('listar_compras')
    if request.method == 'POST':
        form = CompraForm(request.POST, instance=compra)
        if form.is_valid():
            form.save()
            return redirect('listar_clientes')
    else:
        form = CompraForm(instance=compra)
        return render(request, 'criar_compra.html', {'form': form})

def excluir_compra(request, id):
    compra = Compra.objects.get(id=id)
    if compra is None:
        return redirect('listar_compras')
    compra.delete()
    return JsonResponse({'message': 'Compra excluída com sucesso!'})

def compra(request, id):
    compra_q = Compra.objects.filter(id=id)
    print(compra_q)
    if not compra_q:
        return HttpResponse('Cliente não possui compras')

    preco_formatado = formatar_preco(compra_q[0].valor())

    context = {
        'compra': compra_q[0],
        'preco_formatado': preco_formatado
    }

    return render(request, 'compra.html', context)
