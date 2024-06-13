from django import forms
from django.forms import ModelForm
from .models import Carro

from crispy_forms.helper import FormHelper
from crispy_forms.bootstrap import PrependedAppendedText, FormActions
from crispy_forms.layout import Layout, Row, Column, Button, Field, Submit

class FormCarro(ModelForm):

    class Meta:
        model = Carro
        fields = ['marca', 'modelo', 'ano', 'preco', 'cor', 'estoque', 'imagem']
        labels = {
            'marca': 'Marca',
            'modelo': 'Modelo',
            'ano': 'Ano',
            'preco': 'Preço',
            'cor': 'Cor',
            'estoque': 'Estoque',
            'imagem': 'Imagem',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-3 col-form-label'  # Ajuste a largura do label
        self.helper.field_class = 'col-lg-9'  # Ajuste a largura do campo
        self.helper.layout = Layout(
            Row(
                Column(Field('marca', css_class='form-control'), css_class='form-group col-md-6 mb-3'),
                Column(Field('modelo', css_class='form-control'), css_class='form-group col-md-6 mb-3'),
            ),
            Row(
                Column(Field('ano', css_class='form-control'), css_class='form-group col-md-6 mb-3'),
                Column(PrependedAppendedText('preco', 'R$', '.00', css_class='form-control'), css_class='form-group col-md-6 mb-3'),
            ),
            Row(
                Column(Field('cor', css_class='form-control'), css_class='form-group col-md-6 mb-3'),
                Column(Field('estoque', css_class='form-control'), css_class='form-group col-md-6 mb-3'),
            ),
            Row(
                Column(Field('imagem', css_class='form-control'), css_class='form-group col-md-12 mb-3'),
            ),
            Row(
                Column(
                    FormActions(
                        Submit('save', ' Save changes', css_class='btn btn-success btn-lg mr-2 fas fa-save'),
                        Button('cancel', ' Cancel', css_class='btn btn-danger btn-lg fas fa-times', onclick="window.history.back()")
                    ), css_class='form-group col-md-12'
                )
            )
        )
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
            field.required = False  # Remove o asterisco

    def save(self, commit=True):
        carro = super().save(commit=False)
        if commit:
            carro.save()
        return carro
