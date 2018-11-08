from django.conf.urls import url
from publication import views

urlpatterns = [
    url(r'^publication/$', views.PublicationAPIView.as_view()),
    url(r'^publication/user/$', views.PublicationUserAPIView.as_view()),
    url(r'^publication/new/$', views.PublicationCreateAPIView.as_view()),
    url(r'^publication/(?P<pk>[0-9]+)/$', views.PublicationDetailAPIView.as_view()),
]
