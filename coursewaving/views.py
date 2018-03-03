# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework.generics import CreateAPIView, RetrieveDestroyAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated
from coursewaving.serializers import WavedCoursesSerializer, WavedCoursesCreateSerializer
from coursewaving.models import WavedCourses

# Create your views here.


class WavedCourseAPIView(ListAPIView):
    serializer_class = WavedCoursesSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = WavedCourses.objects.all()
        queryset = self.get_serializer_class().setup_eager_loading(queryset)
        return queryset


class WavedCourseCreateAPIView(CreateAPIView):
    serializer_class = WavedCoursesCreateSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = WavedCourses.objects.all()
        return queryset


class WavedCourseStudentAPIView(ListAPIView):
    serializer_class = WavedCoursesSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = WavedCourses.objects.filter(student=self.request.GET['student'])
        queryset = self.get_serializer_class().setup_eager_loading(queryset)
        return queryset


class WavedCourseDetailAPIView(RetrieveDestroyAPIView):
    serializer_class = WavedCoursesSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = WavedCourses.objects.all()
        queryset = self.get_serializer_class().setup_eager_loading(queryset)
        return queryset
