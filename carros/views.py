from django.forms import Form, ModelForm
from django.shortcuts import redirect, render
from .forms import FormCarro
from .models import Carro

# Create your views here.
def index(request):
    carros = Carro.objects.all()
    return render(request, 'index.html', {'carros': carros})


def criar_carro(request):
    form = FormCarro()
    if request.method == 'POST':
        carro = Carro()
        carro.marca = request.POST['marca']
        carro.modelo = request.POST['modelo']
        carro.ano = request.POST['ano']
        carro.preco = request.POST['preco']
        carro.cor = request.POST['cor']
        carro.estoque = request.POST['estoque']
        carro.save()
        return redirect('index')
    return render(request, 'criar_carro.html', {'form': form})
