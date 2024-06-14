from calendar import c
from django.db import models
from carros.models import Carro
# Create your models here.

NIVEL_CHOICES = (
    ('BRONZE', 'Bronze'),
    ('PRATA', 'Prata'),
    ('OURO', 'Ouro'),
    ('DIAMANTE', 'Diamante'),
)


class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    sobrenome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11, unique=True)
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=11)
    data_nascimento = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    nivel_bruto = models.CharField(max_length=8, choices=NIVEL_CHOICES, default='BRONZE')

    def __str__(self):
        return self.nome + ' ' + self.sobrenome

    def nivel(self):
        valor_gasto = self.total_valor_gasto()
        if valor_gasto < 50000:
            return 'BRONZE'
        elif valor_gasto < 100000:
            return 'PRATA'
        elif valor_gasto < 500000:
            return 'OURO'
        else:
            return 'DIAMANTE'

    def total_valor_gasto(self):
        # Calcula o total gasto pelo cliente em todas as compras
        return sum(compra.valor() for compra in self.compras.all())


class Compra(models.Model):
    cliente = models.ForeignKey(Cliente, related_name='compras', on_delete=models.CASCADE)
    carro = models.ForeignKey(Carro, on_delete=models.CASCADE)
    data_compra = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.cliente.nome} {self.cliente.sobrenome}'

    def valor(self):
        return self.carro.preco

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for carro in Carro.objects.all():
            if carro.estoque > 0:
                carro.estoque -= 1
                carro.save()
                break



