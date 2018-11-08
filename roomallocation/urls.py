from django.conf.urls import url
from roomallocation import views

urlpatterns = [
    url(r'^room-allocation/$', views.RoomAllocationAPIView.as_view()),
    url(r'^room-allocation/session-hostel/$', views.RoomAllocationSessionHostelAPIView.as_view()),
    url(r'^room-allocation/student/$', views.RoomAllocationStudentAPIView.as_view()),
    url(r'^room-allocation/(?P<pk>[0-9]+)/$', views.RoomAllocationDetailAPIView.as_view()),
    url(r'^room-allocation/new/$', views.RoomAllocationCreateAPIView.as_view()),
]
