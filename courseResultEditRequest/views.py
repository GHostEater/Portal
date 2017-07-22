# -*- coding: utf-8 -*-
from rest_framework.generics import ListCreateAPIView, RetrieveDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from courseResultEditRequest.serializers import LogSerializer, RequestSerializer
from courseResultEditRequest.models import Log, Request

# Create your views here.


class RequestAPIView(ListCreateAPIView):
    serializer_class = RequestSerializer
    permission_classes = [IsAuthenticated]
    queryset = Request.objects.all()


class RequestDetailAPIView(RetrieveDestroyAPIView):
    serializer_class = RequestSerializer
    permission_classes = [IsAuthenticated]
    queryset = Request.objects.all()


class LogAPIView(ListCreateAPIView):
    serializer_class = LogSerializer
    permission_classes = [IsAuthenticated]
    queryset = Log.objects.all()


class LogDetailAPIView(RetrieveDestroyAPIView):
    serializer_class = LogSerializer
    permission_classes = [IsAuthenticated]
    queryset = Log.objects.all()
