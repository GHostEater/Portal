from django.conf.urls import url
from courseResultEditRequest import views

urlpatterns = [
    url(r'^result-edit-request/$', views.RequestAPIView.as_view()),
    url(r'^result-edit-request/new/$', views.RequestCreateAPIView.as_view()),
    url(r'^result-edit-request/(?P<pk>[0-9]+)/$', views.RequestDetailAPIView.as_view()),
    url(r'^result-edit-log/$', views.LogAPIView.as_view()),
    url(r'^result-edit-log/new/$', views.LogCreateAPIView.as_view()),
    url(r'^result-edit-log/(?P<pk>[0-9]+)/$', views.LogDetailAPIView.as_view()),
]
