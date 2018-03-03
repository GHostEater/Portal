# -*- coding: utf-8 -*-
from rest_framework.generics import CreateAPIView, RetrieveDestroyAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated
from coursereg.serializers import CourseRegSerializer, CourseRegCreateSerializer
from coursereg.models import CourseReg

# Create your views here.


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


class CourseRegStudentAPIView(ListAPIView):
    serializer_class = CourseRegSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = CourseReg.objects.filter(student=self.request.GET['student'])
        queryset = self.get_serializer_class().setup_eager_loading(queryset)
        return queryset


class CourseRegCourseAPIView(ListAPIView):
    serializer_class = CourseRegSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = CourseReg.objects.filter(course=self.request.GET['course'], session=self.request.GET['session'])
        queryset = self.get_serializer_class().setup_eager_loading(queryset)
        return queryset
