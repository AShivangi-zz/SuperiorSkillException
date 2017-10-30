"""waysafe URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

"""
this is basically the table of contents for your website.

This manages the urls
"""

from django.conf.urls import include, url #Include imports from the other url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^home/', include('homepage.urls')), #TB set this so that when you go to xxx.x.x.x:8000 it directs directly to homepage page
    url(r'^aisle/', include('aisle.urls')),
    url(r'^history/', include('history.urls')),
    url(r'^index/', include('index.urls')),
    url(r'^savings/', include('savings.urls')),
    url(r'^payment/', include('payment.urls')),

]

# if settings.DEBUG:
#     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)