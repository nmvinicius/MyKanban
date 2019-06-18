from django import forms
from .models import Tarefa


class FormTarefa(forms.ModelForm):
    class Meta:
        model = Tarefa
        fields = ('titulo', 'descricao')
