# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from modeofentry.serializers import ModeOfEntrySerializer
from modeofentry.models import ModeOfEntry

# Create your views here.


class ModeOfEntryAPIView(ListAPIView):
    serializer_class = ModeOfEntrySerializer
    permission_classes = [IsAuthenticated]
    queryset = ModeOfEntry.objects.all()


class ModeOfEntryDetailAPIView(RetrieveAPIView):
    serializer_class = ModeOfEntrySerializer
    permission_classes = [IsAuthenticated]
    queryset = ModeOfEntry.objects.all()
