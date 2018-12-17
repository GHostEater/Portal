# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from grade.serializers import GradePointSerializer
from grade.models import GradePoint

# Create your views here.


class GradePointAPIView(ListAPIView):
    serializer_class = GradePointSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = GradePoint.objects.all()
        queryset = self.get_serializer_class().setup_eager_loading(queryset)
        return queryset


class GradePointDetailAPIView(RetrieveAPIView):
    serializer_class = GradePointSerializer

    def get_queryset(self):
        queryset = GradePoint.objects.all()
        queryset = self.get_serializer_class().setup_eager_loading(queryset)
        return queryset
