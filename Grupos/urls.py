from django.urls import path, re_path
from django.conf.urls import include
from Grupos import views

urlpatterns = [
    re_path(r'^$', views.GruposList.as_view()),
    re_path(r'^(?P<pk>\d+)/$', views.GruposDetails.as_view()),
]