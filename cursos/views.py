from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Curso, Aluno, Matricula
from .serializers import CursoSerializer, AlunoSerializer, MatriculaSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListAPIView

# Página inicial
def home(request):
    return HttpResponse("Bem-vindo à plataforma de cursos!")

# Listar cursos
def listar_cursos(request):
    cursos = Curso.objects.all()
    return render(request, "cursos/cursos.html", {"cursos": cursos})

# Detalhes de um curso específico
def detalhes_curso(request, curso_id):
    curso = get_object_or_404(Curso, id=curso_id)
    return render(request, "cursos/curso_detalhes.html", {"curso": curso})

# Listar matrículas de um curso específico
def listar_matriculas(request, curso_id):
    curso = get_object_or_404(Curso, id=curso_id)
    matriculas = Matricula.objects.filter(curso=curso)
    return render(request, "cursos/matriculas.html", {"curso": curso, "matriculas": matriculas})

# ViewSet para Cursos
class CursoViewSet(viewsets.ModelViewSet):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer
    permission_classes = [IsAuthenticated]

# ViewSet para Alunos
class AlunoViewSet(viewsets.ModelViewSet):
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer
    permission_classes = [IsAuthenticated]

# ViewSet para Matrículas
class MatriculaViewSet(viewsets.ModelViewSet):
    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer
    permission_classes = [IsAuthenticated]

# API para listar matrículas de um aluno específico
class ListaMatriculasPorAluno(ListAPIView):
    serializer_class = MatriculaSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        aluno_id = self.kwargs['pk']
        return Matricula.objects.filter(aluno_id=aluno_id)