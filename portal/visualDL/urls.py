"""portal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url

from portal import url_helper


import views

urlpatterns = [
    url(r'^$', views.home_root, name='visualdl-home'),
    url(r'^docs/(?P<version>[^/]+)/(?P<path>.*)$', views.content_sub_path, name=url_helper.URL_NAME_CONTENT),
    url(r'^change-lang$', views.change_lang, name='change_lang'),
]
