# myapp/forms.py
from django import forms
from .models import Aluno

class AlunoForm(forms.ModelForm):
    class Meta:
        model = Aluno
        fields = ['nome', 'email', 'matricula']

class FiltroDataForm(forms.Form):
    data_filtro = forms.DateField(label='Data')