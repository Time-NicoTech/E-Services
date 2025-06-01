from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from indexApp.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', loadIndexPage, name="indexPage"),
    path('login/', loadLoginPage, name='loginPage'),
    path('cadastro/', loadCadastroPage, name='cadastroPage'),
    path('api/', include('api.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


