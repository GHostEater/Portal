# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated

from coursereg.models import ExtraUnitRequest
from coursereg.serializers import ExtraUnitRequestSerializer, ExtraUnitRequestCreateSerializer


class ExtraUnitRequestAPIView(ListAPIView):
    serializer_class = ExtraUnitRequestSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = ExtraUnitRequest.objects.all()
        queryset = self.get_serializer_class().setup_eager_loading(queryset)
        return queryset


class ExtraUnitRequestCreateAPIView(CreateAPIView):
    serializer_class = ExtraUnitRequestCreateSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = ExtraUnitRequest.objects.all()
        return queryset


class ExtraUnitRequestDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = ExtraUnitRequestSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = ExtraUnitRequest.objects.all()
        queryset = self.get_serializer_class().setup_eager_loading(queryset)
        return queryset
