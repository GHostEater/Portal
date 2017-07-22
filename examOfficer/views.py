# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework.generics import ListCreateAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from examOfficer.serializers import ExamOfficerSerializer
from examOfficer.models import ExamOfficer

# Create your views here.


class ExamOfficerAPIView(ListCreateAPIView):
    serializer_class = ExamOfficerSerializer
    permission_classes = [IsAuthenticated]
    queryset = ExamOfficer.objects.all()


class ExamOfficerDetailAPIView(RetrieveAPIView):
    lookup_field = 'lecturer'
    serializer_class = ExamOfficerSerializer
    queryset = ExamOfficer.objects.all()
