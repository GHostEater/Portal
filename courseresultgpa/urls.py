from django.conf.urls import url
from courseresultgpa import views

urlpatterns = [
    url(r'^gpa/$', views.CourseResultGPAAPIView.as_view(), name='course_result_gpa'),
    url(r'^gpa/new/$', views.CourseResultGPACreateAPIView.as_view()),
    url(r'^gpa/student/$', views.CourseResultGPAStudentAPIView.as_view(), name='course_result_gpa_student'),
    url(r'^gpa/dept/$', views.CourseResultGPADeptAPIView.as_view(), name='course_result_gpa_dept'),
    url(r'^gpa/(?P<pk>[0-9]+)/$', views.CourseResultGPADetailAPIView.as_view(), name='course_result_gpa_detail'),

    url(r'^gpa/raw-result-and-cgpa/$', views.raw_result_and_cgpa),
    url(r'^gpa/raw-result-and-cgpa-specific/$', views.raw_result_and_cgpa_specific),
    url(r'^gpa/release-result-and-cgpa/$', views.release_result_and_cgpa),
    url(r'^gpa/result-test/$', views.result_test),
]
