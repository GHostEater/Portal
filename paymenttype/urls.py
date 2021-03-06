from django.conf.urls import url
from paymenttype import views

urlpatterns = [
    url(r'^payment-type/$', views.PaymentTypeAPIView.as_view()),
    url(r'^payment-type/student/$', views.PaymentTypeStudentAPIView.as_view()),
    url(r'^payment-type/admission/$', views.PaymentTypeAdmissionAPIView.as_view()),
    url(r'^payment-type/(?P<pk>[0-9]+)/$', views.PaymentTypeDetailAPIView.as_view()),
    
    url(r'^tuition-fee/$', views.TuitionFeeAPIView.as_view()),
    url(r'^tuition-fee/single/$', views.tuition_fee_detail),
]
