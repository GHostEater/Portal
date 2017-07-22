# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from college.serializers import CollegeSerializer
from college.models import College

# Create your views here.


class CollegeAPIView(ListAPIView):
    serializer_class = CollegeSerializer
    permission_classes = [IsAuthenticated]
    queryset = College.objects.all()


class CollegeDetailAPIView(RetrieveAPIView):
    serializer_class = CollegeSerializer
    permission_classes = [IsAuthenticated]
    queryset = College.objects.all()
