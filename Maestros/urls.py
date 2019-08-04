from django.urls import path, re_path
from django.conf.urls import include
from Maestros import views

urlpatterns = [
    re_path(r'^$', views.MaestrosList.as_view()),
    re_path(r'^(?P<pk>\d+)/$', views.MaestrosDetails.as_view()),
]