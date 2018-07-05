# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework.generics import ListAPIView

from payment.models import Payment
from payment.serializers import PaymentSerializer


class PaymentStudentAPIView(ListAPIView):
    serializer_class = PaymentSerializer

    def get_queryset(self):
        queryset = Payment.objects.filter(student=self.request.GET['student'])
        queryset = self.get_serializer_class().setup_eager_loading(queryset)
        return queryset
