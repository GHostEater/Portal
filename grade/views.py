# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework.generics import ListAPIView, RetrieveAPIView
from grade.serializers import GradePointSerializer
from grade.models import GradePoint

# Create your views here.


class GradePointAPIView(ListAPIView):
    serializer_class = GradePointSerializer
    queryset = GradePoint.objects.all()


class GradePointDetailAPIView(RetrieveAPIView):
    serializer_class = GradePointSerializer
    queryset = GradePoint.objects.all()
