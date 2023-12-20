"""
URL configuration for ProyectoVinos project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from vinoteca import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('listado/', views.lista_vinos, name='listado'),
    path('contacto/', views.contacto, name='contacto'),
    path('registro/', views.registro, name='registro'),
    path('buscar/', views.buscar, name='buscar'),
    path('buscar_vino/', views.buscar_vino, name='buscar_vino'),
    path('resultado/', views.resultado, name='resultado'),
    path('guardarExcel/', views.guardarExcel, name='guardarExcel'),
    path('ver_vino/', views.ver_vino, name='ver_vino'),
]
