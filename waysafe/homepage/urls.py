from django.conf.urls import url
from . import views

urlpatterns = [
    #^$ means this is the default homepage page of the section..
    #/homepage/
    url(r'^$', views.index, name='index'),
    url(r'^signIn/$', views.signIn, name='signIn'),
    url(r'^guest/$', views.guest, name='guest'),
    url(r'^createAccount/$', views.createAccount, name='createAccount'),

]