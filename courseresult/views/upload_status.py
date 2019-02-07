# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated

from courseresult.models import UploadStatus
from courseresult.serializers import UploadStatusSerializer


class UploadStatusAPIView(RetrieveUpdateAPIView):
    serializer_class = UploadStatusSerializer
    permission_classes = [IsAuthenticated]
    queryset = UploadStatus.objects.all()
