from django.urls import path, re_path
from django.conf.urls import include
from Calificaciones import views

urlpatterns = [
    re_path(r'^$', views.CalificacionesList.as_view()),
    re_path(r'^(?P<pk>\d+)/$', views.CalificacionesDetails.as_view()),
]