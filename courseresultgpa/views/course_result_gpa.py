# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated

from courseresultgpa.models import CourseResultGPA
from courseresultgpa.serializers import CourseResultGPASerializer, CourseResultCreateGPASerializer


class CourseResultGPAAPIView(ListAPIView):
    serializer_class = CourseResultGPASerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = CourseResultGPA.objects.all()
        queryset = self.get_serializer_class().setup_eager_loading(queryset)
        return queryset


class CourseResultGPACreateAPIView(CreateAPIView):
    serializer_class = CourseResultCreateGPASerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = CourseResultGPA.objects.all()
        return queryset


class CourseResultGPADetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = CourseResultGPASerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = CourseResultGPA.objects.all()
        queryset = self.get_serializer_class().setup_eager_loading(queryset)
        return queryset
