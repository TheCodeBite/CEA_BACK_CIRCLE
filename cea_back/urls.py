"""back URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path, re_path, include
from rest_framework import routers
from django.conf import settings

router = routers.DefaultRouter()
urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^', include(router.urls)),
    re_path(r'^api/v1/alumnos/',include('Alumnos.urls')),
    re_path(r'^api/v1/maestros/',include('Maestros.urls')),
    re_path(r'^api/v1/carreras/',include('Carreras.urls')),
    re_path(r'^api/v1/grupos/',include('Grupos.urls')),
    re_path(r'^api/v1/pagoMaestros/',include('PagoMaestros.urls')),
    re_path(r'^api/v1/pagoAlumnos/',include('PagoAlumnos.urls')),
    re_path(r'^api/v1/materias/',include('Materias.urls')),
    re_path(r'^api/v1/materiasAsignadas/',include('MateriasAsignadas.urls')),
    re_path(r'^api/v1/calificaciones/',include('Calificaciones.urls')),
]
