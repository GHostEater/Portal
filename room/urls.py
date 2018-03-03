from django.conf.urls import url
from room import views

urlpatterns = [
    url(r'^room/$', views.RoomAPIView.as_view()),
    url(r'^room/new/$', views.RoomCreateAPIView.as_view()),
    url(r'^room/(?P<pk>[0-9]+)/$', views.RoomDetailAPIView.as_view()),
]
