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
    queryset = Log.objects.all()


class LogDetailAPIView(RetrieveAPIView):
    serializer_class = LogSerializer
    permission_classes = [IsAuthenticated]
    queryset = Log.objects.all()
