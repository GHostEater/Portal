# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from latereg.serializers import LateRegSerializer, LogSerializer, RegStatusSerializer, LateRegCreateSerializer, LogCreateSerializer
from latereg.models import RegStatus, LateReg, Log

# Create your views here.


class RegStatusAPIView(RetrieveAPIView):
    serializer_class = RegStatusSerializer
    permission_classes = [IsAuthenticated]
    queryset = RegStatus.objects.all()


class LateRegAPIView(ListAPIView):
    serializer_class = LateRegSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = LateReg.objects.all()
        queryset = self.get_serializer_class().setup_eager_loading(queryset)
        return queryset


class LateRegCreateAPIView(CreateAPIView):
    serializer_class = LateRegCreateSerializer
    permission_classes = [IsAuthenticated]
    queryset = LateReg.objects.all()


class LateRegDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = LateRegSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = LateReg.objects.all()
        queryset = self.get_serializer_class().setup_eager_loading(queryset)
        return queryset


class LogAPIView(ListAPIView):
    serializer_class = LogSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Log.objects.all()
        queryset = self.get_serializer_class().setup_eager_loading(queryset)
        return queryset


class LogCreateAPIView(CreateAPIView):
    serializer_class = LogCreateSerializer
    permission_classes = [IsAuthenticated]
    queryset = Log.objects.all()


class LogDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = LateRegSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Log.objects.all()
        queryset = self.get_serializer_class().setup_eager_loading(queryset)
        return queryset
