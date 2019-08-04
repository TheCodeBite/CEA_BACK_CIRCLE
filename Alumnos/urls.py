from django.urls import path, re_path
from django.conf.urls import include
from Alumnos import views

urlpatterns = [
    re_path(r'^$', views.AlumnosList.as_view()),
    re_path(r'^(?P<pk>\d+)/$', views.AlumnosDetails.as_view()),
]