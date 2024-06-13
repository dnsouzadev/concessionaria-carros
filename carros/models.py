from django.db import models

# Create your models here.
class Carro(models.Model):
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    ano = models.IntegerField()
    preco = models.FloatField()
    cor = models.CharField(max_length=100)
    data_criacao = models.DateTimeField(auto_now_add=True)
    estoque = models.IntegerField()

    def __str__(self):
        return self.marca + ' ' + self.modelo + ' ' + str(self.ano)

