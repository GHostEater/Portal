from django.conf.urls import url
from django.contrib.auth.views import login, logout

urlpatterns = [
    url(r'^$', login, {'template_name': 'login.html', 'redirect_authenticated_user': True}),
    url(r'^logout/$', logout, name='logout'),
]
