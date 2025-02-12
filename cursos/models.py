from django.db import models

class Curso(models.Model):
    nome = models.CharField(max_length=200)
    descricao = models.TextField()
    data_criacao = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return self.nome


class Aluno(models.Model):
    nome = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    data_nascimento = models.DateField()

    def _str_(self):
        return self.nome


class Matricula(models.Model):
    curso = models.ForeignKey(Curso, related_name='matriculas', on_delete=models.CASCADE)
    aluno = models.ForeignKey(Aluno, related_name='matriculas', on_delete=models.CASCADE)
    data_matricula = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return f"{self.aluno.nome} matriculado em {self.curso.nome}"
