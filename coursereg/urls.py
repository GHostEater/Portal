from django.conf.urls import url
from coursereg import views

urlpatterns = [
    url(r'^course-reg/$', views.CourseRegAPIView.as_view(), name='course_reg'),
    url(r'^course-reg/new/$', views.CourseRegCreateAPIView.as_view(), name='course_reg_create'),
    url(r'^course-reg/course/$', views.CourseRegCourseAPIView.as_view(), name='course_reg_course'),
    url(r'^course-reg/student/$', views.CourseRegStudentAPIView.as_view()),
    url(r'^course-reg/(?P<pk>[0-9]+)/$', views.CourseRegDetailAPIView.as_view(), name='course_reg_detail'),
    url(r'^course-reg/reg-and-raw-result/$', views.reg_and_raw_results),
    url(r'^course-reg/register-courses/$', views.register_courses),
    url(r'^course-reg/registrable-courses/$', views.registrable_courses),

    url(r'^extra-unit-request/$', views.ExtraUnitRequestAPIView.as_view()),
    url(r'^extra-unit-request/new/$', views.ExtraUnitRequestCreateAPIView.as_view()),
    url(r'^extra-unit-request/(?P<pk>[0-9]+)/$', views.ExtraUnitRequestDetailAPIView.as_view()),
]
