# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework.generics import ListCreateAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from hostel.serializers import HostelSerializer
from hostel.models import Hostel


# Create your views here.


class HostelAPIView(ListCreateAPIView):
    serializer_class = HostelSerializer
    permission_classes = [IsAuthenticated]
    queryset = Hostel.objects.all()


class HostelDetailAPIView(RetrieveAPIView):
    serializer_class = HostelSerializer
    permission_classes = [IsAuthenticated]
    queryset = Hostel.objects.all()
