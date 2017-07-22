from django.conf.urls import url
from courseAllocation import views

urlpatterns = [
    url(r'^course-allocation/$', views.CourseAllocationAPIView.as_view(), name='course_allocation'),
    url(r'^course-allocation/(?P<pk>[0-9]+)/$', views.CourseAllocationDetailAPIView.as_view(), name='course_allocation_detail'),
    url(r'^course-allocation/new/$', views.CourseAllocationCreateAPIView.as_view(), name='course_allocation_create'),
]
