# -*- coding: utf-8 -*-
from rest_framework.generics import ListAPIView, RetrieveDestroyAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated
from courseToMajor.serializers import CourseToMajorSerializer, CourseToMajorCreateSerializer
from courseToMajor.models import CourseToMajor

# Create your views here.


class CourseToMajorAPIView(ListAPIView):
    serializer_class = CourseToMajorSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return CourseToMajor.objects.filter(major=self.request.GET['majorId'])


class CourseToMajorDetailAPIView(RetrieveDestroyAPIView):
    serializer_class = CourseToMajorSerializer
    permission_classes = [IsAuthenticated]
    queryset = CourseToMajor.objects.all()


class CourseToMajorCreateAPIView(CreateAPIView):
    serializer_class = CourseToMajorCreateSerializer
    permission_classes = [IsAuthenticated]
    queryset = CourseToMajor
