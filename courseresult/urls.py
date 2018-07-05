from django.conf.urls import url
from courseresult import views

urlpatterns = [
    url(r'^result/$', views.CourseResultAPIView.as_view()),
    url(r'^result/student/$', views.CourseResultStudentAPIView.as_view(), name='course_result_student'),
    url(r'^result/dept/$', views.CourseResultDeptAPIView.as_view(), name='course_result_dept'),
    url(r'^result/course/$', views.CourseResultCourseAPIView.as_view(), name='course_result_course'),
    url(r'^result/(?P<pk>[0-9]+)/$', views.CourseResultDetailAPIView.as_view(), name='course_result_detail'),

    url(r'^result/upload-ca/$', views.upload_ca),
    url(r'^result/upload-exam/$', views.upload_exam),
    url(r'^result/edit-exam/$', views.edit_exam),
    url(r'^result/edit-ca/$', views.edit_ca),

    url(r'^release-status/(?P<pk>[0-9]+)/$', views.ReleaseStatusAPIView.as_view()),
]
