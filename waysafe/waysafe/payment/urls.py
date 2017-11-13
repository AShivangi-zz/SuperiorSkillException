from django.conf.urls import url
from . import views

urlpatterns = [
    #^$ means this is the default homepage page of the section..
    #/homepage/
    url(r'^$', views.index, name='index'),
    url(r'payment_successful.html/$', views.success, name='pay')
]