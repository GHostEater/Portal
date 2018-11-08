# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated

from courseresult.models import ReleaseStatus
from courseresult.serializers import ReleaseStatusSerializer


class ReleaseStatusAPIView(RetrieveUpdateAPIView):
    serializer_class = ReleaseStatusSerializer
    permission_classes = [IsAuthenticated]
    queryset = ReleaseStatus.objects.all()
