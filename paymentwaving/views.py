# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework.generics import CreateAPIView, RetrieveDestroyAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated
from paymentwaving.serializers import WavedPaymentSerializer, WavedPaymentCreateSerializer
from paymentwaving.models import WavedPayment

# Create your views here.


class WavedPaymentAPIView(ListAPIView):
    serializer_class = WavedPaymentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = WavedPayment.objects.all()
        queryset = self.get_serializer_class().setup_eager_loading(queryset)
        return queryset


class WavedPaymentCreateAPIView(CreateAPIView):
    serializer_class = WavedPaymentCreateSerializer
    permission_classes = [IsAuthenticated]
    queryset = WavedPayment.objects.all()


class WavedPaymentStudentAPIView(ListAPIView):
    serializer_class = WavedPaymentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = WavedPayment.objects.filter(student=self.request.GET['student'])
        queryset = self.get_serializer_class().setup_eager_loading(queryset)
        return queryset


class WavedPaymentDetailAPIView(RetrieveDestroyAPIView):
    serializer_class = WavedPaymentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = WavedPayment.objects.all()
        queryset = self.get_serializer_class().setup_eager_loading(queryset)
        return queryset
