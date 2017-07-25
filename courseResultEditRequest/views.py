# -*- coding: utf-8 -*-
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated
from courseResultEditRequest.serializers import LogSerializer, RequestSerializer, LogCreateSerializer, RequestCreateSerializer
from courseResultEditRequest.models import Log, Request

# Create your views here.


class RequestAPIView(ListAPIView):
    serializer_class = RequestSerializer
    permission_classes = [IsAuthenticated]
    queryset = Request.objects.all()


class RequestCreateAPIView(CreateAPIView):
    serializer_class = RequestCreateSerializer
    permission_classes = [IsAuthenticated]
    queryset = Request.objects.all()


class RequestDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = RequestSerializer
    permission_classes = [IsAuthenticated]
    queryset = Request.objects.all()


class LogAPIView(ListAPIView):
    serializer_class = LogSerializer
    permission_classes = [IsAuthenticated]
    queryset = Log.objects.all()


class LogCreateAPIView(CreateAPIView):
    serializer_class = LogCreateSerializer
    permission_classes = [IsAuthenticated]
    queryset = Log.objects.all()


class LogDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = LogSerializer
    permission_classes = [IsAuthenticated]
    queryset = Log.objects.all()
