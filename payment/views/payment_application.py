# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework.generics import ListAPIView

from payment.models import Payment
from payment.serializers import PaymentSerializer


# class PaymentApplicationAPIView(ListAPIView):
#     serializer_class = PaymentSerializer
#
#     def get_queryset(self):
#         queryset = Payment.objects.filter(application=self.request.GET['application'])
#         queryset = self.get_serializer_class().setup_eager_loading(queryset)
#         return queryset


class PaymentApplicationAPIView(ListAPIView):
    serializer_class = PaymentSerializer

    def get_queryset(self):
        queryset = Payment.objects.filter(application=self.request.GET['application']).exclude(rrr=None)
        queryset = self.get_serializer_class().setup_eager_loading(queryset)
        return queryset
