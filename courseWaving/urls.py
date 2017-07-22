from django.conf.urls import url
from courseWaving import views

urlpatterns = [
    url(r'^course-waving/$', views.WavedCourseAPIView.as_view(), name='course_waving'),
    url(r'^course-waving/student/$', views.WavedCourseStudentAPIView.as_view(), name='course_waving_student'),
    url(r'^course-waving/(?P<pk>[0-9]+)/$', views.WavedCourseDetailAPIView.as_view(), name='course_waving_detail'),
]
