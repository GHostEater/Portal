# -*- coding: utf-8 -*-
from rest_framework.generics import ListAPIView, RetrieveDestroyAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated
from paymenttomajor.serializers import PaymentToMajorSerializer, PaymentToMajorCreateSerializer
from paymenttomajor.models import PaymentToMajor

# Create your views here.


class PaymentToMajorAPIView(ListAPIView):
    serializer_class = PaymentToMajorSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = PaymentToMajor.objects.filter(major=self.request.GET['majorId'])
        queryset = self.get_serializer_class().setup_eager_loading(queryset)
        return queryset


class PaymentToMajorDetailAPIView(RetrieveDestroyAPIView):
    serializer_class = PaymentToMajorSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = PaymentToMajor.objects.all()
        queryset = self.get_serializer_class().setup_eager_loading(queryset)
        return queryset


class PaymentToMajorCreateAPIView(CreateAPIView):
    serializer_class = PaymentToMajorCreateSerializer
    permission_classes = [IsAuthenticated]
    queryset = PaymentToMajor
