from django.conf.urls import url
from systemLog import views

urlpatterns = [
    url(r'^system-log/$', views.LogAPIView.as_view(), name='system_log'),
    url(r'^system-log/(?P<pk>[0-9]+)/$', views.LogDetailAPIView.as_view(), name='system_log_detail'),
]
