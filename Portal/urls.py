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
from django.conf import settings

import debug_toolbar

from django.conf.urls.static import static


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('core.urls')),
    url(r'^mail-queue/', include('mailqueue.urls')),
    url(r'^api/', include('accounts.urls')),
    url(r'^api/', include('session.urls')),
    url(r'^api/', include('semester.urls')),
    url(r'^api/', include('level.urls')),
    url(r'^api/', include('modeofentry.urls')),
    url(r'^api/', include('college.urls')),
    url(r'^api/', include('dept.urls')),
    url(r'^api/', include('major.urls')),
    url(r'^api/', include('course.urls')),
    url(r'^api/', include('coursetomajor.urls')),
    url(r'^api/', include('hod.urls')),
    url(r'^api/', include('courseallocation.urls')),
    url(r'^api/', include('leveladviser.urls')),
    url(r'^api/', include('coursereg.urls')),
    url(r'^api/', include('coursewaving.urls')),
    url(r'^api/', include('courseresult.urls')),
    url(r'^api/', include('courseresultgpa.urls')),
    url(r'^api/', include('courseresulteditrequest.urls')),
    url(r'^api/', include('examofficer.urls')),
    url(r'^api/', include('systemlog.urls')),
    url(r'^api/', include('latereg.urls')),
    url(r'^api/', include('payment.urls')),
    url(r'^api/', include('paymenttype.urls')),
    url(r'^api/', include('paymenttomajor.urls')),
    url(r'^api/', include('paymentwaving.urls')),
    url(r'^api/', include('admission.urls')),
    url(r'^api/', include('sitelog.urls')),
    url(r'^api/', include('courseware.urls')),
    url(r'^api/', include('publication.urls')),
    url(r'^api/', include('nysc.urls')),
    url(r'^api/', include('hostel.urls')),
    url(r'^api/', include('room.urls')),
    url(r'^api/', include('roomallocation.urls')),
    url(r'^api/', include('coursereview.urls')),
    url(r'^api/', include('voting.urls')),
    url(r'^api/', include('transcript.urls')),
    url(r'^api/', include('transfer.urls')),
    url(r'^api/', include('courseresultuploadlog.urls')),
    url(r'^api/', include('grade.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
