from django import forms
from .models import Cliente
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column, Submit, HTML

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome', 'sobrenome', 'cpf', 'email', 'telefone', 'data_nascimento']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-sm-2 col-form-label'
        self.helper.field_class = 'col-sm-10'
        self.helper.layout = Layout(
            Row(
                Column('nome', css_class='form-group col-md-6 mb-3'),
                Column('sobrenome', css_class='form-group col-md-6 mb-3'),
            ),
            Row(
                Column('cpf', css_class='form-group col-md-6 mb-3'),
                Column('email', css_class='form-group col-md-6 mb-3'),
            ),
            Row(
                Column('telefone', css_class='form-group col-md-6 mb-3', type='tel'),
                Column('data_nascimento', css_class='form-group col-md-6 mb-3', type='date'),
            ),
            Row(
                Column(
                    HTML('<div class="col-sm-10 offset-sm-2">'),
                    Submit('submit', 'Criar', css_class='btn btn-primary me-2'),
                    HTML('<a class="btn btn-secondary" href="javascript:history.back()">Cancelar</a>'),
                    HTML('</div>'),
                ),
            ),
        )
