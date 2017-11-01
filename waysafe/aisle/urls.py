from django.conf.urls import url
from . import views

urlpatterns = [
    #^$ means this is the default homepage page of the section..
    #/aisle/
    url(r'^$', views.index, name='index'),
    url(r'^babycare/$', views.baby_care_subcategory, name='babycare'),
    url(r'^beverages/$', views.beverages_subcategory, name='beverages'),
    url(r'^frozen_subcategory/$', views.frozen_subcategory, name='frozen_subcategory'),
    url(r'^meat_subcategory/$', views.meat_subcategory, name='meat_subcategory'),
    url(r'^pasta_and_grains_subcategory/$', views.pasta_and_grains_subcategory, name='pasta_and_grains_subcategory'),
    url(r'^babycare/babycare_item/$', views.babycare_item, name='babycare_item'),

    url(r'^aisle/$', views.aisle, name='aisle'),
]