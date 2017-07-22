from django.conf.urls import url

from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token
from accounts import views

urlpatterns = [
    url(r'^login/$', views.UserLoginAPIView.as_view(), name='user_login'),
    url(r'^auth/token/get/$', obtain_jwt_token, name='get_token'),
    url(r'^auth/token/verify/$', verify_jwt_token, name='verify_token'),
    url(r'^auth/token/refresh/$', refresh_jwt_token, name='refresh_token'),


    url(r'^student/$', views.StudentAPIView.as_view(), name='student'),
    url(r'^student/dept/$', views.StudentDeptAPIView.as_view(), name='student_dept'),
    url(r'^student/(?P<user>[0-9]+)/$', views.StudentDetailAPIView.as_view(), name='student_detail'),
    url(r'^student/new/$', views.student_create, name='student_create'),
    url(r'^student/auto-withdraw/$', views.student_auto_withdraw, name='student_auto_withdraw'),

    url(r'^college-officer/$', views.CollegeOfficerAPIView.as_view(), name='college_officer'),
    url(r'^college-officer/(?P<user>[0-9]+)/$', views.CollegeOfficerDetailAPIView.as_view(), name='college_officer_detail'),

    url(r'^student-affairs/$', views.StudentAffairsAPIView.as_view(), name='student_affairs'),
    url(r'^student-affairs/(?P<user>[0-9]+)/$', views.StudentAffairsDetailAPIView.as_view(), name='student_affairs_detail'),

    url(r'^lecturer/$', views.LecturerAPIView.as_view(), name='lecturer'),
    url(r'^lecturer/(?P<user>[0-9]+)/$', views.LecturerDetailAPIView.as_view(), name='lecturer_detail'),
]
