from django.conf.urls import url
from grade import views

urlpatterns = [
    url(r'^grade-point/$', views.GradePointAPIView.as_view()),
    url(r'^grade-point/(?P<lecturer>[0-9]+)/$', views.GradePointDetailAPIView.as_view()),
]
