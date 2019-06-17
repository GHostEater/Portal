from django.conf.urls import url
from admission import views

urlpatterns = [
    url(r'^pin/$', views.PinAPIView.as_view()),
    url(r'^pin/(?P<pin>[0-9]+)/$', views.PinDetailAPIView.as_view()),
    url(r'^pin/new/$', views.PinCreateAPIView.as_view()),

    url(r'^application/$', views.ApplicationAPIView.as_view()),
    url(r'^application/(?P<pk>[0-9]+)/$', views.ApplicationDetailAPIView.as_view()),
    url(r'^application/single/(?P<email>[A-Za-z0-9_@./#&+-]*)/$', views.ApplicationSingleDetailAPIView.as_view()),
    url(r'^application/new/$', views.ApplicationCreateAPIView.as_view()),
    url(r'^application/transfer-email/$', views.transfer_email),
    url(r'^application/postgrad-email/$', views.postgrad_email),
]
