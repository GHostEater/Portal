from django.conf.urls import url

from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token
from accounts import views

urlpatterns = [
    url(r'^login/$', views.UserLoginAPIView.as_view(), name='user_login'),
    url(r'^auth/token/get/$', obtain_jwt_token, name='get_token'),
    url(r'^auth/token/verify/$', verify_jwt_token, name='verify_token'),
    url(r'^auth/token/refresh/$', refresh_jwt_token, name='refresh_token'),
    url(r'^auth/pass-reset/$', views.pass_reset),

    url(r'^user/$', views.UserAPIView.as_view()),
    url(r'^user/(?P<pk>[0-9]+)/$', views.UserDetailAPIView.as_view()),
    url(r'^user/email/(?P<email>[A-Za-z0-9_@./#&+-]*)/$', views.UserEmailAPIView.as_view()),

    url(r'^unit/$', views.UnitAPIView.as_view()),
    url(r'^unit/(?P<pk>[0-9]+)/$', views.UnitDetailAPIView.as_view()),

    url(r'^student/$', views.StudentAPIView.as_view(), name='student'),
    url(r'^student/dept/$', views.StudentDeptAPIView.as_view(), name='student_dept'),
    url(r'^student/(?P<user>[0-9]+)/$', views.StudentDetailAPIView.as_view(), name='student_detail'),
    url(r'^student/new/$', views.student_upload, name='student_create'),
    url(r'^student/auto-withdraw/$', views.student_auto_withdraw, name='student_auto_withdraw'),
    url(r'^student/graduate/$', views.student_graduate),

    url(r'^college-officer/$', views.CollegeOfficerAPIView.as_view(), name='college_officer'),
    url(r'^college-officer/(?P<user>[0-9]+)/$', views.CollegeOfficerDetailAPIView.as_view()),

    url(r'^bursar/$', views.BursarAPIView.as_view()),
    url(r'^bursar/(?P<user>[0-9]+)/$', views.BursarDetailAPIView.as_view()),

    url(r'^dean/$', views.DeanAPIView.as_view()),
    url(r'^dean/(?P<user>[0-9]+)/$', views.DeanDetailAPIView.as_view()),

    url(r'^student-affairs/$', views.StudentAffairsAPIView.as_view(), name='student_affairs'),
    url(r'^student-affairs/(?P<user>[0-9]+)/$', views.StudentAffairsDetailAPIView.as_view()),

    url(r'^lecturer/$', views.LecturerAPIView.as_view(), name='lecturer'),
    url(r'^lecturer/(?P<user>[0-9]+)/$', views.LecturerDetailAPIView.as_view(), name='lecturer_detail'),
]
