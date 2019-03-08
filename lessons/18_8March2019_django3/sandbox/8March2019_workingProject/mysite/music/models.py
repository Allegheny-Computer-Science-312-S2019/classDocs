from django.db import models

# Create your models here.

class Album(models.Model):
#The following is a method of Album class
   def __str__(self):
    # show the album_title, artist
#      return self.album_title+ ' +--+ ' + self.artist
      return self.artist + " +--+ " + self.album_title+ " +--+ " + self.artist
#end of __str__()


   # holds the name of max length 250 chars
   artist = models.CharField(max_length = 250)
##
   # holds album name
   album_title = models.CharField(max_length = 500)
##
   # holds the genre
   genre = models.CharField(max_length = 100)
##
   # holds a url for music logo (link to graphic)
   album_logo = models.CharField(max_length = 1000)
#end of class Album()

class Song(models.Model):
    # Add to Song Class
   def __str__(self):
        return self.song_title
 # Class links the songs to the album class
 # foreign keys link the songs to a particular album.
 # when you delete an album, remove its
 # associated songs, as well.
##
   album = models.ForeignKey(Album,on_delete=models.CASCADE) # all on one line
##
   # holds the type of file containing music
   file_type = models.CharField(max_length = 10)
##
 # holds the song title.
   song_title = models.CharField(max_length = 250)
# end of class Song ()
