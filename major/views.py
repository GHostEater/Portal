# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework.generics import ListAPIView, RetrieveAPIView
from major.serializers import MajorSerializer
from major.models import Major

# Create your views here.


class MajorAPIView(ListAPIView):
    serializer_class = MajorSerializer

    def get_queryset(self):
        queryset = Major.objects.all()
        queryset = self.get_serializer_class().setup_eager_loading(queryset)
        return queryset


class MajorDetailAPIView(RetrieveAPIView):
    serializer_class = MajorSerializer

    def get_queryset(self):
        queryset = Major.objects.all()
        queryset = self.get_serializer_class().setup_eager_loading(queryset)
        return queryset
