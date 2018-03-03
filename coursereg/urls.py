from django.conf.urls import url
from coursereg import views

urlpatterns = [
    url(r'^course-reg/$', views.CourseRegAPIView.as_view(), name='course_reg'),
    url(r'^course-reg/new/$', views.CourseRegCreateAPIView.as_view(), name='course_reg_create'),
    url(r'^course-reg/course/$', views.CourseRegCourseAPIView.as_view(), name='course_reg_course'),
    url(r'^course-reg/student/$', views.CourseRegStudentAPIView.as_view(), name='course_reg'),
    url(r'^course-reg/(?P<pk>[0-9]+)/$', views.CourseRegDetailAPIView.as_view(), name='course_reg_detail'),
]
