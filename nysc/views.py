# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from nysc.serializers import NyscSerializer
from nysc.models import Nysc

# Create your views here.


class NyscAPIView(ListCreateAPIView):
    serializer_class = NyscSerializer
    queryset = Nysc.objects.all()


class NyscDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = NyscSerializer
    queryset = Nysc.objects.all()
