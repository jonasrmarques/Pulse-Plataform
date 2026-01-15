#Essa daqui é a rota principal do nosso projeto, nosso redirecionamento pras páginas do app dependem exclusivamente dessa rota

from django.contrib import admin
from django.urls import path, include #Por padrão é necessário importar o include para incluir as rotas dos nossos apps.

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path("api/", include("main.api.urls")),
]
