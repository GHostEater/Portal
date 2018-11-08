from django.conf.urls import url
from hod import views

urlpatterns = [
    url(r'^hod/$', views.HodAPIView.as_view(), name='hod'),
    url(r'^hod/(?P<lecturer>[0-9]+)/$', views.HodDetailAPIView.as_view(), name='hod_detail'),
]
