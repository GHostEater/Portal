from django.conf.urls import url
from session import views

urlpatterns = [
    url(r'^session/$', views.SessionAPIView.as_view(), name='session'),
    url(r'^session/(?P<pk>[0-9]+)/$', views.SessionDetailAPIView.as_view(), name='session_detail'),

    url(r'^session-current/(?P<is_current>[0-9]+)/$', views.SessionCurrentAPIView.as_view(), name='session_current'),
    url(r'^session-actions/$', views.session_actions),
]
