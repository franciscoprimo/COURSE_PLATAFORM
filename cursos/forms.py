from django import forms
from .models import Aluno, Matricula

class AlunoForm(forms.ModelForm):
    class Meta:
        model = Aluno
        fields = ['nome', 'email', 'data_nascimento']

class MatriculaForm(forms.ModelForm):
    class Meta:
        model = Matricula
        fields = ['curso', 'aluno']