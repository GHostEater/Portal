# -*- coding: utf-8 -*-
from rest_framework.generics import CreateAPIView, RetrieveDestroyAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated
from courseReg.serializers import CourseRegSerializer, CourseRegCreateSerializer
from courseReg.models import CourseReg

# Create your views here.


class CourseRegAPIView(ListAPIView):
    serializer_class = CourseRegSerializer
    permission_classes = [IsAuthenticated]
    queryset = CourseReg


class CourseRegCreateAPIView(CreateAPIView):
    serializer_class = CourseRegCreateSerializer
    permission_classes = [IsAuthenticated]
    queryset = CourseReg


class CourseRegDetailAPIView(RetrieveDestroyAPIView):
    serializer_class = CourseRegSerializer
    permission_classes = [IsAuthenticated]
    queryset = CourseReg.objects.all()


class CourseRegStudentAPIView(ListAPIView):
    serializer_class = CourseRegSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return CourseReg.objects.filter(student=self.request.GET['student'])


class CourseRegCourseAPIView(ListAPIView):
    serializer_class = CourseRegSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return CourseReg.objects.filter(course=self.request.GET['course'], session=self.request.GET['session'])
