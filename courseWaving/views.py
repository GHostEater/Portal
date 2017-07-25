# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework.generics import CreateAPIView, RetrieveDestroyAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated
from courseWaving.serializers import WavedCoursesSerializer, WavedCoursesCreateSerializer
from courseWaving.models import WavedCourses

# Create your views here.


class WavedCourseAPIView(ListAPIView):
    serializer_class = WavedCoursesSerializer
    permission_classes = [IsAuthenticated]
    queryset = WavedCourses.objects.all()


class WavedCourseCreateAPIView(CreateAPIView):
    serializer_class = WavedCoursesCreateSerializer
    permission_classes = [IsAuthenticated]
    queryset = WavedCourses.objects.all()


class WavedCourseStudentAPIView(ListAPIView):
    serializer_class = WavedCoursesSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return WavedCourses.objects.filter(student=self.request.GET['student'])


class WavedCourseDetailAPIView(RetrieveDestroyAPIView):
    serializer_class = WavedCoursesSerializer
    permission_classes = [IsAuthenticated]
    queryset = WavedCourses.objects.all()
