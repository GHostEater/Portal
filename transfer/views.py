# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveDestroyAPIView
from rest_framework.permissions import IsAuthenticated

from transfer.models import IntraUni
from transfer.serializers import IntraUniSerializer, IntraUniCreateSerializer


class IntraUniAPIView(ListAPIView):
    serializer_class = IntraUniSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = IntraUni.objects.all()
        queryset = self.get_serializer_class().setup_eager_loading(queryset)
        return queryset


class IntraUniCreateAPIView(CreateAPIView):
    serializer_class = IntraUniCreateSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = IntraUni.objects.all()
        return queryset


class IntraUniDetailAPIView(RetrieveDestroyAPIView):
    serializer_class = IntraUniSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = IntraUni.objects.all()
        queryset = self.get_serializer_class().setup_eager_loading(queryset)
        return queryset
