from django.conf.urls import url
from courseToMajor import views

urlpatterns = [
    url(r'^course-to-major/$', views.CourseToMajorAPIView.as_view(), name='course_to_major'),
    url(r'^course-to-major/(?P<pk>[0-9]+)/$', views.CourseToMajorDetailAPIView.as_view(), name='course_to_major_detail'),
    url(r'^course-to-major/new/$', views.CourseToMajorCreateAPIView.as_view(), name='course_to_major_create'),
]
