# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework.generics import CreateAPIView, RetrieveDestroyAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated
from paymentWaving.serializers import WavedPaymentSerializer, WavedPaymentCreateSerializer
from paymentWaving.models import WavedPayment

# Create your views here.


class WavedPaymentAPIView(ListAPIView):
    serializer_class = WavedPaymentSerializer
    permission_classes = [IsAuthenticated]
    queryset = WavedPayment.objects.all()


class WavedPaymentCreateAPIView(CreateAPIView):
    serializer_class = WavedPaymentCreateSerializer
    permission_classes = [IsAuthenticated]
    queryset = WavedPayment.objects.all()


class WavedPaymentStudentAPIView(ListAPIView):
    serializer_class = WavedPaymentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return WavedPayment.objects.filter(student=self.request.GET['student'])


class WavedPaymentDetailAPIView(RetrieveDestroyAPIView):
    serializer_class = WavedPaymentSerializer
    permission_classes = [IsAuthenticated]
    queryset = WavedPayment.objects.all()
