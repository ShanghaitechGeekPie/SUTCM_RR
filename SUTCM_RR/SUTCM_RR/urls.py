"""SUTCM_RR URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from SUTCM_RR_db import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^resources/(?P<category_id>\d{1})/$', views.ResourcesList),
    url(r'^resource/(?P<resource_id>\d+)/$', views.ResourceInfo),
    url(r'^time/(?P<from>\d+)/(?P<to>\d+)/$', views.time_check),
    url(r'^reserve/.../$', views.article_detail),
    url(r'^result/(?P<reserve_sn>\d|\w{6})/$', views.result)
]
