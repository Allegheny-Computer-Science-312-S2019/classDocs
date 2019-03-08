a = Album(artist = "The Nelsonions",album_title = "Bluish-blue",genre="Rock",album_logo = "http://schmoesknow.com/wonder-woman-movie-review/50254/")
## above code is all on one line
a.save() # writes into the database
a.id # show the ID (primary key)

a = Album(artist = "The Bill-Browns",
album_title = "Ready or not",
genre="Rock",album_logo = "http://schmoesknow.com/wp-content/uploads/2017/05/Wonder-Woman-Movie-Artwork.jpg")
# above code is all on one line
##
a.save() # writes into the database
##
a.id # show the ID (primary key)


a = Album(artist = "DJ Cool-cumber",
album_title = "Ignite the night",
genre="Rock",album_logo = "http://schmoesknow.com/wp-content/uploads/2017/05/Wonder-Woman-Movie-Artwork.jpg")
# above code is all on one line
##
a.save() # writes into the database
##
a.id # show the ID (primary key)



# Add "Albums" and "Song" table entries: Rick Astley
#
from music.models import Album, Song
a = Album(artist="Rick Astley",
album_title ="Whenever You Need Somebody",
genre="rock", album_logo="https://www.cs.allegheny.edu/sites/obonhamcarter/cs312/graphics/rick.jpg") #Above line: all on one line
a.save()
#
# add a song for the album
s = Song()
s.album_id = 2
s.Album = "Whenever You Need Somebody"
s.song_title = "Never Gonna Give You Up"
s.file_type="mp3"
s.save()
