# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView

from payment.models import Payment
from payment.serializers import PaymentSerializer, PaymentCreateSerializer


# class PaymentAPIView(ListAPIView):
#     serializer_class = PaymentSerializer
#
#     def get_queryset(self):
#         queryset = Payment.objects.all()
#         queryset = self.get_serializer_class().setup_eager_loading(queryset)
#         return queryset
#
#
# class PaymentCreateAPIView(CreateAPIView):
#     serializer_class = PaymentCreateSerializer
#     queryset = Payment.objects.all()
#
#
# class PaymentDetailAPIView(RetrieveUpdateDestroyAPIView):
#     serializer_class = PaymentSerializer
#
#     def get_queryset(self):
#         queryset = Payment.objects.all()
#         queryset = self.get_serializer_class().setup_eager_loading(queryset)
#         return queryset


class PaymentAPIView(ListAPIView):
    serializer_class = PaymentSerializer

    def get_queryset(self):
        queryset = Payment.objects.all().exclude(rrr=None)
        queryset = self.get_serializer_class().setup_eager_loading(queryset)
        return queryset


class PaymentDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = PaymentSerializer

    def get_queryset(self):
        queryset = Payment.objects.all().exclude(rrr=None)
        queryset = self.get_serializer_class().setup_eager_loading(queryset)
        return queryset


class PaymentCreateAPIView(CreateAPIView):
    serializer_class = PaymentCreateSerializer
    queryset = Payment.objects.all().exclude(rrr=None)
