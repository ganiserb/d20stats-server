# coding=utf-8
__author__ = 'gabriel'

from django.conf.urls import include, url

urlpatterns = [
    url('^test/$', 'api.views.test', name="test")
]
