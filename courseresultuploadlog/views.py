# -*- coding: utf-8 -*-
from __future__ import unicode_literals


# Create your views here.
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated

from courseresultuploadlog.models import Log
from courseresultuploadlog.serializers import LogSerializer


class LogAPIView(ListCreateAPIView):
    serializer_class = LogSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Log.objects.filter(date__gte=self.request.GET['min'], date__lte=self.request.GET['max'])
        return queryset


class LogDetailAPIView(RetrieveAPIView):
    serializer_class = LogSerializer
    permission_classes = [IsAuthenticated]
    queryset = Log.objects.all()
