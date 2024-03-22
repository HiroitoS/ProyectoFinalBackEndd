"""
URL configuration for app_colegio project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings # importa todas las variables 
from drf_yasg.views import get_schema_view # genera mi vista para poder acceder a la documentacion
from drf_yasg import openapi # es la  herramienta que usa swagger por detras

swagger_view=get_schema_view(
    openapi.Info(
        title='APi de Colegio',
        default_version='v1',
        description='Api para registrar informacion de un colegio ',
        contact=openapi.Contact(name='Hiroito Sanchez', email='hitoito.sanchez@gmail.com')

), 
public=True,
)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('colegio/', include('colegio.urls')),
    path('documentacion/', swagger_view.with_ui('swagger', cache_timeout=0))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # agregamos las rutas del proyecto con todas sus rutas declaradas en media_root (archivos)