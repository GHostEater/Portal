from django.conf.urls import url
from session import views

urlpatterns = [
    url(r'^session/$', views.SessionAPIView.as_view(), name='session'),
    url(r'^session/(?P<pk>[0-9]+)/$', views.SessionDetailAPIView.as_view(), name='session_detail'),
    url(r'^session/new/$', views.add_session),
    url(r'^session/set-current/$', views.set_current),
    url(r'^session/set-admission/$', views.set_admission),

    url(r'^session-current/(?P<is_current>[0-9]+)/$', views.SessionCurrentAPIView.as_view(), name='session_current'),
    url(r'^session-admission/(?P<is_admission>[0-9]+)/$', views.SessionAdmissionAPIView.as_view()),
    url(r'^session-actions/$', views.session_actions),
]
