from django.conf.urls import url
from major import views

urlpatterns = [
    url(r'^major/$', views.MajorAPIView.as_view(), name='major'),
    url(r'^major/(?P<pk>[0-9]+)/$', views.MajorDetailAPIView.as_view(), name='major_detail'),
]
