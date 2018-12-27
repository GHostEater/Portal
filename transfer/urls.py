# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import url
from transfer import views

urlpatterns = [
    url(r'^intra-uni/$', views.IntraUniAPIView.as_view()),
    url(r'^intra-uni/new/$', views.IntraUniCreateAPIView.as_view()),
    url(r'^intra-uni/transfer-student/$', views.transfer_student),
    url(r'^intra-uni/(?P<pk>[0-9]+)/$', views.IntraUniDetailAPIView.as_view()),
]
