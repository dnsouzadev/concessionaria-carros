import json
from django.forms import Form, ModelForm
from django.http import JsonResponse
from django.shortcuts import redirect, render
from .forms import FormCarro
from .models import Carro
from django.core.exceptions import ObjectDoesNotExist
from .utils import formatar_preco

# Create your views here.
def index(request):
    carros = Carro.objects.all()
    for carro in carros:
        carro.preco_formatado = formatar_preco(carro.preco)

    return render(request, 'index.html', {'carros': carros})


def criar_carro(request):
    if request.method == 'POST':
        form = FormCarro(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = FormCarro()
        return render(request, 'criar_carro.html', {'form': form})


def editar_carro(request, id):
    carro = Carro.objects.get(id=id)
    if request.method == 'POST':
        form = FormCarro(request.POST, instance=carro)
        if form.is_valid():
            form.save()
            return redirect('index')
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

