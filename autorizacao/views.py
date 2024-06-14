from django.contrib.auth import authenticate, logout
from django.shortcuts import redirect, render

from carros.models import Carro
from cliente.models import Cliente, Compra
from .forms import LoginForm, CadastroForm
from .utils import formatar_preco

# Create your views here.

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            return redirect('dashboard')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

def dashboard(request):
    carros = Carro.objects.all()
    compras = Compra.objects.all()
    clientes = Cliente.objects.all()

    carros_quant = carros.count()
    compras_quant = compras.count()
    clientes_quant = clientes.count()

    valor_total_vendas = 0
    for compra in compras:
        valor_total_vendas += compra.valor()
    valor_total_vendas = formatar_preco(valor_total_vendas)

    context = {
        'carros_quant': carros_quant,
        'compras_quant': compras_quant,
        'clientes_quant': clientes_quant,
        'valor_total_vendas': valor_total_vendas,
    }

    return render(request, 'dashboard.html', context)
