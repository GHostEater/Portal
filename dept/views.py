# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from dept.serializers import DeptSerializer
from dept.models import Dept

# Create your views here.


class DeptAPIView(ListAPIView):
    serializer_class = DeptSerializer
    permission_classes = [IsAuthenticated]
    queryset = Dept.objects.all()


class DeptDetailAPIView(RetrieveAPIView):
    serializer_class = DeptSerializer
    permission_classes = [IsAuthenticated]
    queryset = Dept.objects.all()
