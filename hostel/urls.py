from django.conf.urls import url
from hostel import views

urlpatterns = [
    url(r'^hostel/$', views.HostelAPIView.as_view()),
    url(r'^hostel/(?P<pk>[0-9]+)/$', views.HostelDetailAPIView.as_view()),
]
