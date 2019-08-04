from django.urls import path, re_path
from django.conf.urls import include
from PagoMaestros import views

urlpatterns = [
    re_path(r'^$', views.PagoMaestrosList.as_view()),
    re_path(r'^(?P<pk>\d+)/$', views.PagoMaestrosDetails.as_view()),
]