# coding=utf-8
__author__ = 'gabriel'

urlpatterns = [
    url('^test/$', 'registrator.views.test', name="test"),
    url('^v1/$', include(v1_api.urls)),
]
