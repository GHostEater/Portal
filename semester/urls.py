from django.conf.urls import url
from semester import views

urlpatterns = [
    url(r'^semester/(?P<pk>[0-9]+)/$', views.SemesterAPIView.as_view(), name='semester'),
]
