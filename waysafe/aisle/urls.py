from django.conf.urls import url
from . import views

urlpatterns = [
    #^$ means this is the default homepage page of the section..
    #/aisle/
    url(r'^$', views.index, name='index'),
    url(r'^babycare/$', views.babycare_item, name='babycare'),
    url(r'^beverages/$', views.beverage_item, name='beverages'),
url(r'^frozen/$', views.frozen_item, name='frozen'),
url(r'^snacks/$', views.snacks_item, name='snacks'),
url(r'^alcohol/$', views.alcohol_item, name='alcohol'),
url(r'^dairy/$', views.dairy_item, name='dairy'),
url(r'^meat/$', views.meat_item, name='meat'),
url(r'^pasta/$', views.pasta_item, name='pasta'),
url(r'^babycare/(?P<item_name>\d+)/$', views.add_to_cart, name='add_to_cart')

    # url(r'^aisle/$', views.aisle, name='aisle'),
]