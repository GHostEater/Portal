from django.conf.urls import url
from payment import views

urlpatterns = [
    url(r'^payment/$', views.PaymentAPIView.as_view()),
    url(r'^payment/new/$', views.PaymentCreateAPIView.as_view()),
    url(r'^payment/student/$', views.PaymentStudentAPIView.as_view()),
    url(r'^payment/application/$', views.PaymentApplicationAPIView.as_view()),
    url(r'^payment/transaction/(?P<transaction_id>[A-Za-z0-9_@./#&+-]*)/$', views.PaymentTransactionDetailAPIView.as_view()),
    url(r'^payment/(?P<pk>[0-9]+)/$', views.PaymentDetailAPIView.as_view()),
    url(r'^payment/student-paid-list/$', views.student_paid_list),
    url(r'^payment/student-unpaid-list/$', views.student_unpaid_list),
    url(r'^payment/application-unpaid-list/$', views.application_unpaid_list),
    url(r'^payment/application-paid-list/$', views.application_paid_list),

    url(r'^xpress-response/$', views.xpress_response),
    url(r'^xpress-pay-cashier/$', views.xpress_pay_cashier),
    url(r'^xpress-notification/$', views.xpress_notification),

    url(r'^hasher/$', views.hasher),
    url(r'^test/$', views.email_test)
]
