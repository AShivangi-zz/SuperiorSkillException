from django.conf.urls import url
from . import views

app_name = 'music' # this is to specify which app to use for templat

urlpatterns = [
    #^$ means this is the default home page of the section..
    # /music/
    url(r'^$',views.index, name='index'), #index is the variable used in index. See #!1! in index.html

    #/music/<album_id>/
    #/music/712/
    #the '()' tells the script to view the numbers as a group. for example 712 is seven hundered twelve instead of seven one two
    #the [0-9] means it will take any regular integer 0 - 9.. the plus means it will take multiple of those integers
    url(r'^(?P<album_id>[0-9]+)/$', views.detail,name ='detail'),

    #/music/<album_id>/favorite/
    url(r'^(?P<album_id>[0-9]+)/favorite/$', views.favorite, name='favorite'),
]
