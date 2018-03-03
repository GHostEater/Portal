# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from paymenttype.serializers import PaymentTypeSerializer
from paymenttype.models import PaymentType

# Create your views here.


class PaymentTypeAPIView(ListAPIView):
    serializer_class = PaymentTypeSerializer
    queryset = PaymentType.objects.all()


class PaymentTypeDetailAPIView(RetrieveAPIView):
    serializer_class = PaymentTypeSerializer
    queryset = PaymentType.objects.all()
