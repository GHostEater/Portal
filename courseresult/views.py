# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated
from courseresult.serializers import CourseResultSerializer, CourseResultCreateSerializer
from courseresult.models import CourseResult

# Create your views here.


class CourseResultAPIView(ListAPIView):
    serializer_class = CourseResultSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = CourseResult.objects.all()
        queryset = self.get_serializer_class().setup_eager_loading(queryset)
        return queryset


class CourseResultCreateAPIView(CreateAPIView):
    serializer_class = CourseResultCreateSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = CourseResult.objects.all()
        return queryset


class CourseResultStudentAPIView(ListAPIView):
    serializer_class = CourseResultSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = CourseResult.objects.filter(student=self.request.GET['student'])
        queryset = self.get_serializer_class().setup_eager_loading(queryset)
        return queryset


class CourseResultDeptAPIView(ListAPIView):
    serializer_class = CourseResultSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = CourseResult.objects.filter(
            student__major__dept=self.request.GET['dept'],
            session=self.request.GET['session'])
        queryset = self.get_serializer_class().setup_eager_loading(queryset)
        return queryset


class CourseResultCourseAPIView(ListAPIView):
    serializer_class = CourseResultSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = CourseResult.objects.filter(
            course=self.request.GET['course'],
            session=self.request.GET['session'])
        queryset = self.get_serializer_class().setup_eager_loading(queryset)
        return queryset


class CourseResultDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = CourseResultSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = CourseResult.objects.all()
        queryset = self.get_serializer_class().setup_eager_loading(queryset)
        return queryset
