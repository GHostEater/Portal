# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework.generics import ListAPIView, RetrieveDestroyAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated
from courseAllocation.serializers import CourseAllocationSerializer, CourseAllocationCreateSerializer
from courseAllocation.models import CourseAllocation

# Create your views here.


class CourseAllocationAPIView(ListAPIView):
    serializer_class = CourseAllocationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return CourseAllocation.objects.filter(session=self.request.GET['session'])


class CourseAllocationDetailAPIView(RetrieveDestroyAPIView):
    serializer_class = CourseAllocationSerializer
    permission_classes = [IsAuthenticated]
    queryset = CourseAllocation.objects.all()


class CourseAllocationCreateAPIView(CreateAPIView):
    serializer_class = CourseAllocationCreateSerializer
    permission_classes = [IsAuthenticated]
    queryset = CourseAllocation.objects.all()
