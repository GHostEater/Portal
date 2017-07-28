from django.conf.urls import url
from paymentWaving import views

urlpatterns = [
    url(r'^payment-waving/$', views.WavedPaymentAPIView.as_view(), name='payment_waving'),
    url(r'^payment-waving/new/$', views.WavedPaymentCreateAPIView.as_view()),
    url(r'^payment-waving/student/$', views.WavedPaymentStudentAPIView.as_view(), name='payment_waving_student'),
    url(r'^payment-waving/(?P<pk>[0-9]+)/$', views.WavedPaymentDetailAPIView.as_view(), name='payment_waving_detail'),
]
