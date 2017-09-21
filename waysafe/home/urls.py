from django.conf.urls import url
from . import views

urlpatterns = [
    #^$ means this is the default home page of the section..
    url(r'^$', views.index, name='index'),

]