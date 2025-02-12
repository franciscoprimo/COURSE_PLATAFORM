from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CursoViewSet, AlunoViewSet, MatriculaViewSet, listar_cursos, detalhes_curso,  listar_matriculas, ListaMatriculasPorAluno


# Criação do roteador para as APIs
router = DefaultRouter()
router.register(r'cursos', CursoViewSet)      # Rota para os cursos
router.register(r'alunos', AlunoViewSet)        # Rota para os alunos
router.register(r'matriculas', MatriculaViewSet)  # Rota para as matrículas

# Adiciona as URLs
urlpatterns = [
    path('', include(router.urls)),  # Use o prefixo vazio aqui
    path("cursos/", listar_cursos, name = "listar_cursos"),
    path("cursos/<int:curso_id>/", detalhes_curso, name="detalhes_curso"),
    path("cursos/<int:curso_id>/matriculas/", listar_matriculas, name="listar_matriculas"),
    path('api/alunos/<int:pk>/matriculas/', ListaMatriculasPorAluno.as_view(), name='aluno-matriculas'),
]