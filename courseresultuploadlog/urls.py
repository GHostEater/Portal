# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf.urls import url
from courseresultuploadlog import views

urlpatterns = [
    url(r'^upload-log/$', views.LogAPIView.as_view()),
    url(r'^upload-log/(?P<pk>[0-9]+)/$', views.LogDetailAPIView.as_view()),
]