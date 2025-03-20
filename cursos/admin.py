from django.contrib import admin
from .models import Curso, Aluno, Matricula

# registrando modelos no adm
admin.site.register(Curso)
admin.site.register(Aluno)
admin.site.register(Matricula)

