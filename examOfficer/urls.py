from django.conf.urls import url
from examOfficer import views

urlpatterns = [
    url(r'^exam-officer/$', views.ExamOfficerAPIView.as_view(), name='exam_officer'),
    url(r'^exam-officer/(?P<lecturer>[0-9]+)/$', views.ExamOfficerDetailAPIView.as_view(), name='exam_officer_detail'),
]
