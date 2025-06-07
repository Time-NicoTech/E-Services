from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from indexApp.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', loadIndexPage, name="indexPage"),
    path('login/', loadLoginPage, name='loginPage'),
    path('logout/', logout, name='logout'),
    path('cadastro/', loadCadastroPage, name='cadastroPage'),
    path('cadastroService/', loadCadastroServicePage, name="cadastroServicePage"),
    path('api/', include('api.urls')),
    path('searchAll/', loadSearchPage, name='searchPage'),
    path('myServices/', loadMyServicesPage, name='myServicesPage')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


