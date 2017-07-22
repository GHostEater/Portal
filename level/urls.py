from django.conf.urls import url
from level import views

urlpatterns = [
    url(r'^level/$', views.LevelAPIView.as_view(), name='level'),
    url(r'^level/(?P<pk>[0-9]+)/$', views.LevelDetailAPIView.as_view(), name='level_detail'),
]
