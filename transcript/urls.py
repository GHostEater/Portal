# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf.urls import url
from transcript import views

urlpatterns = [
    url(r'^transcript-application/$', views.ApplicationAPIView.as_view()),
    url(r'^transcript-application/(?P<pk>[0-9]+)/$', views.ApplicationDetailAPIView.as_view()),
    url(r'^transcript-application/new/$', views.ApplicationCreateAPIView.as_view()),
    url(r'^transcript-application/student/$', views.ApplicationStudentAPIView.as_view()),
    url(r'^transcript/email/$', views.notify_registrar),
]
