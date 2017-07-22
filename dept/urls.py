from django.conf.urls import url
from dept import views

urlpatterns = [
    url(r'^dept/$', views.DeptAPIView.as_view(), name='dept'),
    url(r'^dept/(?P<pk>[0-9]+)/$', views.DeptDetailAPIView.as_view(), name='dept_detail'),
]
