# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

from courseresultgpa.models import CourseResultGPA
from courseresultgpa.serializers import CourseResultGPASerializer


class CourseResultGPAStudentAPIView(ListAPIView):
    serializer_class = CourseResultGPASerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = CourseResultGPA.objects.filter(student=self.request.GET['student'])
        queryset = self.get_serializer_class().setup_eager_loading(queryset)
        return queryset
