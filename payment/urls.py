from django.conf.urls import url
from payment import views

urlpatterns = [
    url(r'^payment/$', views.PaymentAPIView.as_view()),
    url(r'^payment/new/$', views.PaymentCreateAPIView.as_view()),
    url(r'^payment/student/$', views.PaymentStudentAPIView.as_view()),
    url(r'^payment/application/$', views.PaymentApplicationAPIView.as_view()),
    url(r'^payment/order/(?P<order_id>[A-Za-z0-9_@./#&+-]*)/$', views.PaymentTransactionDetailAPIView.as_view()),
    url(r'^payment/(?P<pk>[0-9]+)/$', views.PaymentDetailAPIView.as_view()),
    url(r'^payment/student-paid-list/$', views.student_paid_list),
    url(r'^payment/student-unpaid-list/$', views.student_unpaid_list),
    url(r'^payment/application-unpaid-list/$', views.application_unpaid_list),
    url(r'^payment/application-paid-list/$', views.application_paid_list),

    url(r'^generate-rrr/$', views.generate_rrr),
    url(r'^remita-rrrgen-response/$', views.remita_rrrgen_response, name='rrrgen_response'),
    url(r'^remita-final-response/$', views.remita_final_response, name='final_response'),
    url(r'^remita-notification/$', views.remita_notification),

    url(r'^hasher/$', views.hasher),
    url(r'^test/$', views.email_test)

    # url(r'^xpress-rrrgen-response/$', views.xpress_response, name='rrrgen_response'),
    # url(r'^xpress-final-response/$', views.xpress_response, name='final_response'),
    # url(r'^xpress-pay-cashier/$', views.xpress_pay_cashier),
    # url(r'^xpress-notification/$', views.xpress_notification),
]
