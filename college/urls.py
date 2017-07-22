from django.conf.urls import url
from college import views

urlpatterns = [
    url(r'^college/$', views.CollegeAPIView.as_view(), name='college'),
    url(r'^college/(?P<pk>[0-9]+)/$', views.CollegeDetailAPIView.as_view(), name='college_detail'),
]
