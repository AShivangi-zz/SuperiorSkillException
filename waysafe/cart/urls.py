from django.conf.urls import url
from . import views

urlpatterns = [
    #^$ means this is the default homepage page of the section..
    #/homepage/
    url(r'^$', views.index, name='index'),
    url(r'^delete/(?P<item_id>\d+)/$', views.delete_item, name='delete')
    # url(r'^lastOrder/$', views.lastOrder, name='lastOrder'),
    # url(r'^previousOrders/$', views.previousOrders, name='previousOrders'),
    # url(r'^savedItems/$', views.savedItems, name='savedItems'),
]
