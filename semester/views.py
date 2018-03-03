# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework.generics import RetrieveUpdateAPIView
from semester.serializers import SemesterSerializer
from semester.models import Semester

# Create your views here.


class SemesterAPIView(RetrieveUpdateAPIView):
    serializer_class = SemesterSerializer
    queryset = Semester.objects.all()
