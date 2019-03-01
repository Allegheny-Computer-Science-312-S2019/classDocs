from django.conf.urls import url, include
from django.contrib import admin
# pull the local views.py file from local dir
# The below is sometimes used
# for different vers of Django
#from . import views
urlpatterns = [
url(r'', admin.site.urls),
url(r'^admin/', admin.site.urls),
url(r'^hello/', include('hello.urls'))
]
