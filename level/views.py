# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from level.serializers import LevelSerializer
from level.models import Level

# Create your views here.


class LevelAPIView(ListAPIView):
    serializer_class = LevelSerializer
    permission_classes = [IsAuthenticated]
    queryset = Level.objects.all()


class LevelDetailAPIView(RetrieveAPIView):
    serializer_class = LevelSerializer
    permission_classes = [IsAuthenticated]
    queryset = Level.objects.all()
