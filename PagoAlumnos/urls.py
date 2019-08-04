from django.urls import path, re_path
from django.conf.urls import include
from PagoAlumnos import views

urlpatterns = [
    re_path(r'^$', views.PagoAlumnosList.as_view()),
    re_path(r'^(?P<pk>\d+)/$', views.PagoAlumnosDetails.as_view()),
]