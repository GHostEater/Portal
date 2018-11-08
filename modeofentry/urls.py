from django.conf.urls import url
from modeofentry import views

urlpatterns = [
    url(r'^mode-of-entry/$', views.ModeOfEntryAPIView.as_view(), name='mode_of_entry'),
    url(r'^mode-of-entry/(?P<pk>[0-9]+)/$', views.ModeOfEntryDetailAPIView.as_view(), name='mode_of_entry_detail'),
]
