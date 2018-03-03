# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated
from courseresultgpa.serializers import CourseResultGPASerializer, CourseResultCreateGPASerializer
from courseresultgpa.models import CourseResultGPA

# Create your views here.


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


class CourseResultGPAStudentAPIView(ListAPIView):
    serializer_class = CourseResultGPASerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = CourseResultGPA.objects.filter(student=self.request.GET['student'])
        queryset = self.get_serializer_class().setup_eager_loading(queryset)
        return queryset


class CourseResultGPADeptAPIView(ListAPIView):
    serializer_class = CourseResultGPASerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = CourseResultGPA.objects.filter(dept=self.request.GET['dept'], session=self.request.GET['session'])
        queryset = self.get_serializer_class().setup_eager_loading(queryset)
        return queryset


class CourseResultGPADetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = CourseResultGPASerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = CourseResultGPA.objects.all()
        queryset = self.get_serializer_class().setup_eager_loading(queryset)
        return queryset
