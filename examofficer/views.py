# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated
from examofficer.serializers import ExamOfficerSerializer, ExamOfficerCreateSerializer
from examofficer.models import ExamOfficer

# Create your views here.


class ExamOfficerAPIView(ListAPIView):
    serializer_class = ExamOfficerSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = ExamOfficer.objects.all()
        queryset = self.get_serializer_class().setup_eager_loading(queryset)
        return queryset


class ExamOfficerDetailAPIView(RetrieveUpdateDestroyAPIView):
    lookup_field = 'lecturer'
    serializer_class = ExamOfficerSerializer

    def get_queryset(self):
        queryset = ExamOfficer.objects.all()
        queryset = self.get_serializer_class().setup_eager_loading(queryset)
        return queryset


class ExamOfficerCreateAPIView(CreateAPIView):
    serializer_class = ExamOfficerCreateSerializer
    permission_classes = [IsAuthenticated]
    queryset = ExamOfficer.objects.all()
