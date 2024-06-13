from django.forms import ModelForm
from .models import Carro

class FormCarro(ModelForm):
    class Meta:
        model = Carro
        exclude = ['data_criacao']
