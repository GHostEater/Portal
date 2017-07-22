# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated
from semester.serializers import SemesterSerializer
from semester.models import Semester

# Create your views here.


class SemesterAPIView(RetrieveUpdateAPIView):
    serializer_class = SemesterSerializer
    permission_classes = [IsAuthenticated]
    queryset = Semester.objects.all()
