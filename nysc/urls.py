from django.conf.urls import url
from nysc import views

urlpatterns = [
    url(r'^nysc/$', views.NyscAPIView.as_view()),
    url(r'^nysc/(?P<pk>[0-9]+)/$', views.NyscDetailAPIView.as_view()),
]