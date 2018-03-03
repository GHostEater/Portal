# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveDestroyAPIView, UpdateAPIView
from rest_framework.permissions import IsAuthenticated
from leveladviser.serializers import LevelAdviserSerializer, LevelAdviserCreateSerializer
from leveladviser.models import LevelAdviser

# Create your views here.


class LevelAdviserAPIView(ListAPIView):
    serializer_class = LevelAdviserSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = LevelAdviser.objects.all()
        queryset = self.get_serializer_class().setup_eager_loading(queryset)
        return queryset


class LevelAdviserCreateAPIView(CreateAPIView):
    serializer_class = LevelAdviserCreateSerializer
    permission_classes = [IsAuthenticated]
    queryset = LevelAdviser.objects.all()


class LevelAdviserDetailAPIView(RetrieveDestroyAPIView):
    lookup_field = 'lecturer'
    serializer_class = LevelAdviserSerializer

    def get_queryset(self):
        queryset = LevelAdviser.objects.all()
        queryset = self.get_serializer_class().setup_eager_loading(queryset)
        return queryset


class LevelAdviserUpdateAPIView(UpdateAPIView):
    lookup_field = 'lecturer'
    permission_classes = [IsAuthenticated]
    serializer_class = LevelAdviserCreateSerializer
    queryset = LevelAdviser.objects.all()
