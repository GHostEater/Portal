# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

from coursereg.models import CourseReg
from coursereg.serializers import CourseRegSerializer


class CourseRegCourseAPIView(ListAPIView):
    serializer_class = CourseRegSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = CourseReg.objects.filter(course=self.request.GET['course'], session=self.request.GET['session'])
        queryset = self.get_serializer_class().setup_eager_loading(queryset)
        return queryset
