from django.conf.urls import url
from course import views

urlpatterns = [
    url(r'^course/$', views.CourseAPIView.as_view(), name='course'),
    url(r'^course/(?P<pk>[0-9]+)/$', views.CourseDetailAPIView.as_view(), name='course_detail'),
]
