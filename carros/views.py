import json
from django.forms import Form, ModelForm
from django.http import JsonResponse
from django.shortcuts import redirect, render
from .forms import FormCarro
from .models import Carro
from django.core.exceptions import ObjectDoesNotExist
from .utils import formatar_preco

# Create your views here.
def listar_carros(request):
    carros = Carro.objects.all()
    for carro in carros:
        carro.preco_formatado = formatar_preco(carro.preco)

    return render(request, 'listar_carros.html', {'carros': carros})


def criar_carro(request):
    if request.method == 'POST':
        form = FormCarro(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('listar_carros')
    else:
        form = FormCarro()
        return render(request, 'criar_carro.html', {'form': form})


def editar_carro(request, id):
    carro = Carro.objects.get(id=id)
    if request.method == 'POST':
        form = FormCarro(request.POST, request.FILES, instance=carro)
        if form.is_valid():
            form.save()
            return redirect('listar_carros')
    else:
        form = FormCarro(instance=carro)
        return render(request, 'editar_carro.html', {'form': form})


def excluir_carro(request, id):
    try:
        carro = Carro.objects.get(id=id)
        carro.delete()
        return JsonResponse({'message': 'Carro excluído com sucesso!'})
    except ObjectDoesNotExist:
        return JsonResponse({}, status=204)  # Status 204 significa "No Content"


def buscar_carro(request, q):
    if request.method == 'GET':
        query = q
        carros = Carro.objects.filter(modelo__icontains=query)
        carros = list(carros.values())
        for carro in carros:
            carro['preco_formatado'] = formatar_preco(carro['preco'])
        return JsonResponse({'carros': carros})


def carro(request, id):
    carro = Carro.objects.get(id=id)
    carro.preco_formatado = formatar_preco(carro.preco)
    return render(request, 'carro.html', {'carro': carro})
