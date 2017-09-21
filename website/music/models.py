from django.db import models as m #when just using from django.db impoort models it was confusing models.py with models from django so I used m


class Album(m.Model):#always use models.Model for param
    #each variable is a column in database
    artist = m.CharField(max_length= 250)
    album_title = m.CharField(max_length = 500)
    genre = m.CharField(max_length =100)
    album_logo = m.CharField(max_length = 1000)

class Song(m.Model):

    #each song will be linked to an album
    album = m.ForeignKey(Album, on_delete = m.CASCADE) #fooreighKey means get unique ID of album.  On_delete - models.CASCADE means that if an album is deleted, we need to erase the songs associated with it.
    file_type = m.CharField(max_length= 10)
    song_title = m.CharField(max_length= 250)