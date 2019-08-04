from django.urls import path, re_path
from django.conf.urls import include
from Carreras import views

urlpatterns = [
    re_path(r'^$', views.CarrerasList.as_view()),
    re_path(r'^(?P<pk>\d+)/$', views.CarrerasDetails.as_view()),
]