# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework.generics import ListCreateAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from systemlog.serializers import LogSerializer
from systemlog.models import Log

# Create your views here.


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
