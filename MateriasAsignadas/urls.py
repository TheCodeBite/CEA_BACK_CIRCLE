from django.urls import path, re_path
from django.conf.urls import include
from MateriasAsignadas import views

urlpatterns = [
    re_path(r'^$', views.MateriasAsignadasList.as_view()),
    re_path(r'^(?P<maestro>\d+)/$', views.MateriasAsignadasDetails.as_view()),
    re_path(r'^calificaciones/(?P<fecha>\d+)/(?P<tipo>\w{0,50})/$', views.MateriasAsignadasCalificaciones.as_view()),
]