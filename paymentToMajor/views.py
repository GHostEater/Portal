# -*- coding: utf-8 -*-
from rest_framework.generics import ListAPIView, RetrieveDestroyAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated
from paymentToMajor.serializers import PaymentToMajorSerializer, PaymentToMajorCreateSerializer
from paymentToMajor.models import PaymentToMajor

# Create your views here.


class PaymentToMajorAPIView(ListAPIView):
    serializer_class = PaymentToMajorSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return PaymentToMajor.objects.filter(major=self.request.GET['majorId'])


class PaymentToMajorDetailAPIView(RetrieveDestroyAPIView):
    serializer_class = PaymentToMajorSerializer
    permission_classes = [IsAuthenticated]
    queryset = PaymentToMajor.objects.all()


class PaymentToMajorCreateAPIView(CreateAPIView):
    serializer_class = PaymentToMajorCreateSerializer
    permission_classes = [IsAuthenticated]
    queryset = PaymentToMajor
