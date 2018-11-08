# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveDestroyAPIView
from rest_framework.permissions import IsAuthenticated

from coursereg.models import CourseReg
from coursereg.serializers import CourseRegSerializer, CourseRegCreateSerializer


class CourseRegAPIView(ListAPIView):
    serializer_class = CourseRegSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = CourseReg.objects.all()
        queryset = self.get_serializer_class().setup_eager_loading(queryset)
        return queryset


class CourseRegCreateAPIView(CreateAPIView):
    serializer_class = CourseRegCreateSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = CourseReg.objects.all()
        return queryset


class CourseRegDetailAPIView(RetrieveDestroyAPIView):
    serializer_class = CourseRegSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = CourseReg.objects.all()
        queryset = self.get_serializer_class().setup_eager_loading(queryset)
        return queryset
