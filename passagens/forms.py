from django import forms
from django.forms.widgets import Textarea
from tempus_dominus.widgets import DatePicker
from datetime import datetime
from passagens.classe_viagem import tipos_de_classe
class PassagemForms(forms.Form):
    origem = forms.CharField(label='Origem', max_length=100)
    destino = forms.CharField(label='Destino', max_length=100)
    data_ida = forms.DateField(label='Ida', widget=DatePicker())
    data_volta = forms.DateField(label='Volta', widget=DatePicker())
    classe_viagem = forms.ChoiceField(label='Classe do vôo', choices=tipos_de_classe)
    data_pesquisa = forms.DateField(label='Data da pesquisa', disabled=True, initial=datetime.today())
    informacoes = forms.CharField(label='Informações Extras', max_length=200, widget=forms.Textarea(), required=False)
    email = forms.EmailField(label='Email', max_length=150)