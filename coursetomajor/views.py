# -*- coding: utf-8 -*-
from rest_framework.generics import ListAPIView, RetrieveDestroyAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated
from coursetomajor.serializers import CourseToMajorSerializer, CourseToMajorCreateSerializer
from coursetomajor.models import CourseToMajor

# Create your views here.


class CourseToMajorAPIView(ListAPIView):
    serializer_class = CourseToMajorSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = CourseToMajor.objects.filter(major=self.request.GET['major'])
        queryset = self.get_serializer_class().setup_eager_loading(queryset)
        return queryset


class CourseToMajorDetailAPIView(RetrieveDestroyAPIView):
    serializer_class = CourseToMajorSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = CourseToMajor.objects.all()
        queryset = self.get_serializer_class().setup_eager_loading(queryset)
        return queryset


class CourseToMajorCreateAPIView(CreateAPIView):
    serializer_class = CourseToMajorCreateSerializer
    permission_classes = [IsAuthenticated]
    queryset = CourseToMajor
