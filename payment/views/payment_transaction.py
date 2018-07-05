# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework.generics import RetrieveUpdateDestroyAPIView

from payment.models import Payment
from payment.serializers import PaymentSerializer


class PaymentTransactionDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = PaymentSerializer
    lookup_field = 'transaction_id'

    def get_queryset(self):
        queryset = Payment.objects.all()
        queryset = self.get_serializer_class().setup_eager_loading(queryset)
        return queryset
