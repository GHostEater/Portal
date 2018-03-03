from django.conf.urls import url
from leveladviser import views

urlpatterns = [
    url(r'^level-adviser/$', views.LevelAdviserAPIView.as_view()),
    url(r'^level-adviser/new/$', views.LevelAdviserCreateAPIView.as_view()),
    url(r'^level-adviser/(?P<lecturer>[0-9]+)/$', views.LevelAdviserDetailAPIView.as_view()),
    url(r'^level-adviser/update/(?P<lecturer>[0-9]+)/$', views.LevelAdviserUpdateAPIView.as_view()),
]
