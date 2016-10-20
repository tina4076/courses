from django.conf.urls import url
#from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url(r'^add$', views.add),
    url(r'^destroy/(?P<id>\d+)$', views.destroy),
    url(r'^confirm/(?P<id>\d+)$', views.confirm)
]
