from django.conf.urls import url
from coursetomajor import views

urlpatterns = [
    url(r'^course-to-major/$', views.CourseToMajorAPIView.as_view()),
    url(r'^course-to-major/(?P<pk>[0-9]+)/$', views.CourseToMajorDetailAPIView.as_view()),
    url(r'^course-to-major/new/$', views.CourseToMajorCreateAPIView.as_view()),
]
