# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from courseware.serializers import CoursewareSerializer, CoursewareCreateSerializer
from courseware.models import Courseware

# Create your views here.


class CoursewareAPIView(ListAPIView):
    serializer_class = CoursewareSerializer

    def get_queryset(self):
        queryset = Courseware.objects.all()
        queryset = self.get_serializer_class().setup_eager_loading(queryset)
        return queryset


class CoursewareDeptAPIView(ListAPIView):
    serializer_class = CoursewareSerializer

    def get_queryset(self):
        queryset = Courseware.objects.filter(course__dept=self.request.GET['dept'])
        queryset = self.get_serializer_class().setup_eager_loading(queryset)
        return queryset


class CoursewareCreateAPIView(CreateAPIView):
    serializer_class = CoursewareCreateSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Courseware.objects.all()
        return queryset


class CoursewareDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = CoursewareSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Courseware.objects.all()
        queryset = self.get_serializer_class().setup_eager_loading(queryset)
        return queryset
