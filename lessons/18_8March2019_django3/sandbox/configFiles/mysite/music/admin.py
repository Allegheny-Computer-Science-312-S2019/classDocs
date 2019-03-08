#from django.contrib import admin
#from .models import Album
## from music/models.py class
###
#
## Register your models here.
#admin.site.register(Album)
##admin.site.register(Song)


from django.contrib import admin
from .models import Album, Song
# these tables are from the music/models.py class file
admin.site.register(Album)
admin.site.register(Song)
# Register your models here.
