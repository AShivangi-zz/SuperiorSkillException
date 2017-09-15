"""The URL declarations for this Django project; a “table of contents” of your Django-powered site. """

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]