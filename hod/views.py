# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from hod.serializers import HodSerializer
from hod.models import Hod

# Create your views here.


class HodAPIView(ListAPIView):
    serializer_class = HodSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Hod.objects.all()
        queryset = self.get_serializer_class().setup_eager_loading(queryset)
        return queryset


class HodDetailAPIView(RetrieveAPIView):
    lookup_field = 'lecturer'
    serializer_class = HodSerializer

    def get_queryset(self):
        queryset = Hod.objects.all()
        queryset = self.get_serializer_class().setup_eager_loading(queryset)
        return queryset
