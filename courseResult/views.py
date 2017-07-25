# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated
from courseResult.serializers import CourseResultSerializer, CourseResultCreateSerializer
from courseResult.models import CourseResult

# Create your views here.


class CourseResultAPIView(ListAPIView):
    serializer_class = CourseResultSerializer
    permission_classes = [IsAuthenticated]
    queryset = CourseResult.objects.all()


class CourseResultCreateAPIView(CreateAPIView):
    serializer_class = CourseResultCreateSerializer
    permission_classes = [IsAuthenticated]
    queryset = CourseResult.objects.all()


class CourseResultStudentAPIView(ListAPIView):
    serializer_class = CourseResultSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return CourseResult.objects.filter(student=self.request.GET['student'])


class CourseResultDeptAPIView(ListAPIView):
    serializer_class = CourseResultSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return CourseResult.objects.filter(dept=self.request.GET['dept'], session=self.request.GET['session'])


class CourseResultCourseAPIView(ListAPIView):
    serializer_class = CourseResultSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return CourseResult.objects.filter(
            course=self.request.GET['course'],
            session=self.request.GET['session'])


class CourseResultDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = CourseResultSerializer
    permission_classes = [IsAuthenticated]
    queryset = CourseResult.objects.all()
