# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework.generics import ListCreateAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from sitelog.serializers import LogSerializer
from sitelog.models import Log

# Create your views here.


class LogAPIView(ListCreateAPIView):
    serializer_class = LogSerializer
    queryset = Log.objects.all()


class LogDetailAPIView(RetrieveAPIView):
    serializer_class = LogSerializer
    permission_classes = [IsAuthenticated]
    queryset = Log.objects.all()
