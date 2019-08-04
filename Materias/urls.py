from django.urls import path, re_path
from django.conf.urls import include
from Materias import views

urlpatterns = [
    re_path(r'^$', views.MateriasList.as_view()),
    re_path(r'^(?P<pk>\d+)/$', views.MateriasDetails.as_view()),
]