from django.conf.urls import include, url
# pull the local views.py file from local dir
from . import views
urlpatterns = [
url(r'^$', views.index, name = 'index'),
]
