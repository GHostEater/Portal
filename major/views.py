# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from major.serializers import MajorSerializer
from major.models import Major

# Create your views here.


class MajorAPIView(ListAPIView):
    serializer_class = MajorSerializer
    permission_classes = [IsAuthenticated]
    queryset = Major.objects.all()


class MajorDetailAPIView(RetrieveAPIView):
    serializer_class = MajorSerializer
    permission_classes = [IsAuthenticated]
    queryset = Major.objects.all()
