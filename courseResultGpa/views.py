# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated
from courseResultGpa.serializers import CourseResultGPASerializer
from courseResultGpa.models import CourseResultGPA

# Create your views here.


class CourseResultGPAAPIView(ListCreateAPIView):
    serializer_class = CourseResultGPASerializer
    permission_classes = [IsAuthenticated]
    queryset = CourseResultGPA.objects.all()


class CourseResultGPAStudentAPIView(ListAPIView):
    serializer_class = CourseResultGPASerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return CourseResultGPA.objects.filter(student=self.request.GET['student'])


class CourseResultGPADeptAPIView(ListAPIView):
    serializer_class = CourseResultGPASerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return CourseResultGPA.objects.filter(dept=self.request.GET['dept'], session=self.request.GET['session'])


class CourseResultGPADetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = CourseResultGPASerializer
    permission_classes = [IsAuthenticated]
    queryset = CourseResultGPA.objects.all()
