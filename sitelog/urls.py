from django.conf.urls import url
from sitelog import views

urlpatterns = [
    url(r'^site-log/$', views.LogAPIView.as_view()),
    url(r'^site-log/(?P<pk>[0-9]+)/$', views.LogDetailAPIView.as_view()),
]
