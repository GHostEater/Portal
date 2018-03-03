from django.conf.urls import url
from courseresult import views

urlpatterns = [
    url(r'^result/$', views.CourseResultAPIView.as_view()),
    url(r'^result/new/$', views.CourseResultCreateAPIView.as_view()),
    url(r'^result/student/$', views.CourseResultStudentAPIView.as_view(), name='course_result_student'),
    url(r'^result/dept/$', views.CourseResultDeptAPIView.as_view(), name='course_result_dept'),
    url(r'^result/course/$', views.CourseResultCourseAPIView.as_view(), name='course_result_course'),
    url(r'^result/(?P<pk>[0-9]+)/$', views.CourseResultDetailAPIView.as_view(), name='course_result_detail'),
]
