from django.conf.urls import url
from courseResultGpa import views

urlpatterns = [
    url(r'^gpa/$', views.CourseResultGPAAPIView.as_view(), name='course_result_gpa'),
    url(r'^gpa/student/$', views.CourseResultGPAStudentAPIView.as_view(), name='course_result_gpa_student'),
    url(r'^gpa/dept/$', views.CourseResultGPADeptAPIView.as_view(), name='course_result_gpa_dept'),
    url(r'^gpa/(?P<pk>[0-9]+)/$', views.CourseResultGPADetailAPIView.as_view(), name='course_result_gpa_detail'),
]
