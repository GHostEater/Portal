from django.conf.urls import url
from paymenttomajor import views

urlpatterns = [
    url(r'^payment-to-major/$', views.PaymentToMajorAPIView.as_view()),
    url(r'^payment-to-major/(?P<pk>[0-9]+)/$', views.PaymentToMajorDetailAPIView.as_view()),
    url(r'^payment-to-major/new/$', views.PaymentToMajorCreateAPIView.as_view()),
]
