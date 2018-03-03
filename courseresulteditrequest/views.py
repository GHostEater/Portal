# -*- coding: utf-8 -*-
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated
from courseresulteditrequest.serializers import LogSerializer, RequestSerializer, LogCreateSerializer, RequestCreateSerializer
from courseresulteditrequest.models import Log, Request

# Create your views here.


class RequestAPIView(ListAPIView):
    serializer_class = RequestSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Request.objects.all()
        queryset = self.get_serializer_class().setup_eager_loading(queryset)
        return queryset


class RequestCreateAPIView(CreateAPIView):
    serializer_class = RequestCreateSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Request.objects.all()
        return queryset


class RequestDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = RequestSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Request.objects.all()
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

    def get_queryset(self):
        queryset = Log.objects.all()
        return queryset


class LogDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = LogSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Log.objects.all()
        queryset = self.get_serializer_class().setup_eager_loading(queryset)
        return queryset
