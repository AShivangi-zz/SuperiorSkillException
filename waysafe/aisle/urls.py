from django.conf.urls import url
from . import views

urlpatterns = [
    #^$ means this is the default homepage page of the section..
    #/aisle/
    url(r'^$', views.index, name='index'),

    url(r'^aisle/$', views.aisle, name='aisle'),
]