from django.conf.urls import url
from . import views

urlpatterns = [
    #^$ means this is the default homepage page of the section..
    #/aisle/
    url(r'^$', views.index, name='index'),
    url(r'^babycare/$', views.babycare_item, name='babycare'),
    url(r'^beverages/$', views.beverage_item, name='beverages')
    # url(r'^aisle/$', views.aisle, name='aisle'),
]