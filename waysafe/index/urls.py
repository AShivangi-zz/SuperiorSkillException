from django.conf.urls import url
from . import views

urlpatterns = [
    #^$ means this is the default homepage page of the section..
    #/homepage/
    url(r'^$', views.index, name='index'),
    url(r'^myOrders/$', views.myOrders, name='myOrders'),
    url(r'^myAccount/$', views.myAccount, name='myAccount'),
    url(r'^help/$', views.help, name='help'),
    url(r'^myCart/$', views.myCart, name='myCart'),
    url(r'^aisles/$', views.aisles, name='aisles'),
    url(r'^searchresults/$', views.searchresults, name='searchresults'),
    url(r'^login.html/$', views.login_view, name='login'),
    url(r'^guest.html/$', views.guest, name='guest'),
    url(r'^logout/$', views.logout_view, name='logout'),
    url(r'^index/register.html/$', views.register_view, name='register')

]