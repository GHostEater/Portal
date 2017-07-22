from django.conf.urls import url
from levelAdviser import views

urlpatterns = [
    url(r'^level-adviser/$', views.LevelAdviserAPIView.as_view(), name='level_adviser'),
    url(r'^level-adviser/(?P<lecturer>[0-9]+)/$', views.LevelAdviserDetailAPIView.as_view(), name='level_adviser_detail'),
]
