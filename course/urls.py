from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from cursos.views import home, listar_cursos  # Certifique-se de importar listar_cursos corretamente
from cursos import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name="home"),
    path('cursos/', listar_cursos, name='listar_cursos_frontend'),  # Nome correto para o frontend
    path('api/', include('cursos.urls')),  # API separada
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('cadastrar-aluno/', views.cadastrar_aluno, name='cadastrar_aluno'),
    path('cadastrar-matricula/', views.cadastrar_matricula, name='cadastrar_matricula'),
]