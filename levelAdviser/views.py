# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework.generics import ListCreateAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from levelAdviser.serializers import LevelAdviserSerializer
from levelAdviser.models import LevelAdviser

# Create your views here.


class LevelAdviserAPIView(ListCreateAPIView):
    serializer_class = LevelAdviserSerializer
    permission_classes = [IsAuthenticated]
    queryset = LevelAdviser.objects.all()


class LevelAdviserDetailAPIView(RetrieveAPIView):
    lookup_field = 'lecturer'
    serializer_class = LevelAdviserSerializer
    queryset = LevelAdviser.objects.all()
