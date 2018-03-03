# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated
from room.serializers import RoomSerializer, RoomCreateSerializer
from room.models import Room

# Create your views here.


class RoomAPIView(ListAPIView):
    serializer_class = RoomSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Room.objects.all()
        queryset = self.get_serializer_class().setup_eager_loading(queryset)
        return queryset


class RoomDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = RoomSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Room.objects.all()
        queryset = self.get_serializer_class().setup_eager_loading(queryset)
        return queryset


class RoomCreateAPIView(CreateAPIView):
    serializer_class = RoomCreateSerializer
    permission_classes = [IsAuthenticated]
    queryset = Room.objects.all()
