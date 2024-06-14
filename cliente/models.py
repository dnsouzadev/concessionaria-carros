from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
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
        if not self.compras.all():
            return 0
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

@receiver(post_save, sender=Compra)
def atualizar_estoque(sender, instance, **kwargs):
    if instance.pk:  # Verifica se é uma atualização ou uma nova compra
        # Reduz o estoque do carro associado à compra
        instance.carro.estoque -= 1
        instance.carro.save()

@receiver(post_delete, sender=Compra)
def atualizar_estoque_apos_exclusao(sender, instance, **kwargs):
    # Ao excluir uma compra, incrementa o estoque do carro associado em 1
    instance.carro.estoque += 1
    instance.carro.save()



