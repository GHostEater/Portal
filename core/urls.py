from django.conf.urls import url
from django.contrib.auth.views import login, logout

from core import views

urlpatterns = [
    url(r'^$', login, {'template_name': 'login.html', 'redirect_authenticated_user': True}),
    url(r'^logout/$', logout, name='logout'),

    url(r'^app/$', views.app, name='app'),
]
