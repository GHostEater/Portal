# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import url
from sysinfo import views

urlpatterns = [
    url(r'^sysinfo/(?P<pk>[0-9]+)/$', views.SysInfoAPIView.as_view()),
]
