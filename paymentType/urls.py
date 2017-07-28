from django.conf.urls import url
from paymentType import views

urlpatterns = [
    url(r'^payment-type/$', views.PaymentTypeAPIView.as_view()),
    url(r'^payment-type/(?P<pk>[0-9]+)/$', views.PaymentTypeDetailAPIView.as_view()),
]
