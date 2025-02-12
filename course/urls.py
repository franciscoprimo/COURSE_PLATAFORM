from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from cursos.views import home  # Adicionando a view 'home'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),  # Exibe a página de boas-vindas na URL raiz
    path('api/', include('cursos.urls')),  # Inclui as URLs do app cursos
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]