from django.conf.urls import include, url
from django.contrib import admin
# pull the local views.py file from local dir
from . import views

urlpatterns = [
 url(r'^$', views.index, name = 'index'),
 url(r'^(?P<album_id>[0-9]+)$', views.detail, name = 'detail'),
]
