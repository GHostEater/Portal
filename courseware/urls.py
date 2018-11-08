from django.conf.urls import url
from courseware import views

urlpatterns = [
    url(r'^courseware/$', views.CoursewareAPIView.as_view()),
    url(r'^courseware/dept/$', views.CoursewareDeptAPIView.as_view()),
    url(r'^courseware/new/$', views.CoursewareCreateAPIView.as_view()),
    url(r'^courseware/(?P<pk>[0-9]+)/$', views.CoursewareDetailAPIView.as_view()),
]
