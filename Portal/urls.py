"""Portal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('core.urls')),
    url(r'^api/', include('accounts.urls')),
    url(r'^api/', include('session.urls')),
    url(r'^api/', include('semester.urls')),
    url(r'^api/', include('level.urls')),
    url(r'^api/', include('modeOfEntry.urls')),
    url(r'^api/', include('college.urls')),
    url(r'^api/', include('dept.urls')),
    url(r'^api/', include('major.urls')),
    url(r'^api/', include('course.urls')),
    url(r'^api/', include('courseToMajor.urls')),
    url(r'^api/', include('hod.urls')),
    url(r'^api/', include('courseAllocation.urls')),
    url(r'^api/', include('levelAdviser.urls')),
    url(r'^api/', include('courseReg.urls')),
    url(r'^api/', include('courseWaving.urls')),
    url(r'^api/', include('courseResult.urls')),
    url(r'^api/', include('courseResultGpa.urls')),
    url(r'^api/', include('courseResultEditRequest.urls')),
    url(r'^api/', include('examOfficer.urls')),
    url(r'^api/', include('systemLog.urls')),
    url(r'^api/', include('lateReg.urls')),
    url(r'^api/', include('payment.urls')),
    url(r'^api/', include('paymentType.urls')),
    url(r'^api/', include('paymentToMajor.urls')),
    url(r'^api/', include('paymentWaving.urls')),
]
