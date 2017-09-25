from .models import Album, Song
#from django.template import loader #we need this for using templates
from django.shortcuts import render, get_object_or_404

def index(request): #always put in request
    all_albums = Album.objects.all()

    # info your template needs
    context = {'all_albums': all_albums,}
    return render(request, 'music/index.html', context)#context is from index.html
    ##### Moving all this code into template
    # all_albums = Album.objects.all()
    # html = ''
    # for album in all_albums:
    #
    #     url = '/music/' +  str(album.id) + '/'
    #     html += '<a href= "' + url + '">' + album.album_title  + '</a><br>'
    # return HttpResponse(html)
    #
    # #return HttpResponse("<h1>This is the music app homepage</h1>")

def detail(request,album_id):
    album = get_object_or_404(Album, pk=album_id)

    return render(request, 'music/detail.html', {'album': album})

def favorite(request,album_id):
    album = get_object_or_404(Album, pk=album_id)
    try:
        selected_song = album.song_set.get(pk = request.POST['song'])#This gets the ID of the song that the user selected
    except (KeyError, Song.DoesNotExist):
        return render(request, 'music/detail.html', {
            'album': album,
            'error_message': "You did not select a valid song",

        })
    else:
        selected_song.is_favorite = True
        selected_song.save()
        return render(request, 'music/detail.html', {'album': album})

# def detail(request, album_id): #request is just the html request from the user
#     return HttpResponse("<h2>Details for album id: " + str(album_id) + "</h2>")

