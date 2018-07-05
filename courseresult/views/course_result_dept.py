# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

from courseresult.models import CourseResult
from courseresult.serializers import CourseResultSerializer


class CourseResultDeptAPIView(ListAPIView):
    serializer_class = CourseResultSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = CourseResult.objects.filter(
            student__major__dept=self.request.GET['dept'],
            session=self.request.GET['session'])
        queryset = self.get_serializer_class().setup_eager_loading(queryset)
        return queryset
