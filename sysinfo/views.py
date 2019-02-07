# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Create your views here.
from rest_framework.generics import RetrieveUpdateAPIView

from sysinfo.models import SysInfo
from sysinfo.serializers import SysInfoSerializer


class SysInfoAPIView(RetrieveUpdateAPIView):
    serializer_class = SysInfoSerializer
    queryset = SysInfo.objects.all()
