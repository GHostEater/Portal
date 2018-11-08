# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework.generics import ListAPIView, RetrieveDestroyAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated
from courseallocation.serializers import CourseAllocationSerializer, CourseAllocationCreateSerializer
from courseallocation.models import CourseAllocation

# Create your views here.


class CourseAllocationAPIView(ListAPIView):
    serializer_class = CourseAllocationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = CourseAllocation.objects.filter(session=self.request.GET['session'])
        queryset = self.get_serializer_class().setup_eager_loading(queryset)
        return queryset


class CourseAllocationDetailAPIView(RetrieveDestroyAPIView):
    serializer_class = CourseAllocationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = CourseAllocation.objects.all()
        queryset = self.get_serializer_class().setup_eager_loading(queryset)
        return queryset


class CourseAllocationCreateAPIView(CreateAPIView):
    serializer_class = CourseAllocationCreateSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = CourseAllocation.objects.all()
        return queryset
