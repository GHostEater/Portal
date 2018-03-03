# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated
from roomallocation.serializers import RoomAllocationSerializer, RoomAllocationCreateSerializer
from roomallocation.models import RoomAllocation

# Create your views here.


class RoomAllocationAPIView(ListAPIView):
    serializer_class = RoomAllocationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = RoomAllocation.objects.all()
        queryset = self.get_serializer_class().setup_eager_loading(queryset)
        return queryset


class RoomAllocationSessionHostelAPIView(ListAPIView):
    serializer_class = RoomAllocationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = RoomAllocation.objects.filter(session=self.request.GET['session'],
                                                 room__hostel=self.request.GET['hostel'])
        queryset = self.get_serializer_class().setup_eager_loading(queryset)
        return queryset


class RoomAllocationStudentAPIView(ListAPIView):
    serializer_class = RoomAllocationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = RoomAllocation.objects.filter(student=self.request.GET['student'])
        queryset = self.get_serializer_class().setup_eager_loading(queryset)
        return queryset


class RoomAllocationDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = RoomAllocationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = RoomAllocation.objects.all()
        queryset = self.get_serializer_class().setup_eager_loading(queryset)
        return queryset


class RoomAllocationCreateAPIView(CreateAPIView):
    serializer_class = RoomAllocationCreateSerializer
    permission_classes = [IsAuthenticated]
    queryset = RoomAllocation.objects.all()
