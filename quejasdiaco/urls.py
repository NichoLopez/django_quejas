"""quejasdiaco URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from Views.HomeView import HomeView
from Aplicaciones.Gestion.views import FormularioQuejaView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls, name='administrar'),
    path('', HomeView.home, name='home'),
    path('formulario/', HomeView.formulario ,name='formulario'),
    path('registrarQueja/', FormularioQuejaView.index, name='registrarQueja'),
    path('guardarQueja/', FormularioQuejaView.procesar_formulario, name='guardarQueja'),
    path('grafico/', HomeView.grafico, name='grafico'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
