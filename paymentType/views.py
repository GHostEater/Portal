# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from paymentType.serializers import PaymentTypeSerializer
from paymentType.models import PaymentType

# Create your views here.


class PaymentTypeAPIView(ListAPIView):
    serializer_class = PaymentTypeSerializer
    permission_classes = [IsAuthenticated]
    queryset = PaymentType.objects.all()


class PaymentTypeDetailAPIView(RetrieveAPIView):
    serializer_class = PaymentTypeSerializer
    permission_classes = [IsAuthenticated]
    queryset = PaymentType.objects.all()
