from django.conf.urls import url
from payment import views

urlpatterns = [
    url(r'^payment/$', views.PaymentAPIView.as_view()),
    url(r'^payment/new/$', views.PaymentCreateAPIView.as_view()),
    url(r'^payment/student/$', views.PaymentStudentAPIView.as_view()),
    url(r'^payment/dept/$', views.PaymentDeptAPIView.as_view()),
    url(r'^payment/course/$', views.PaymentCourseAPIView.as_view()),
    url(r'^payment/(?P<pk>[0-9]+)/$', views.PaymentDetailAPIView.as_view()),
]
