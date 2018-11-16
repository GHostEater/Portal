# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response

from accounts.models import Student
from paymenttype.serializers import PaymentTypeSerializer, TuitionFeeSerializer
from paymenttype.models import PaymentType, TuitionFee


# Create your views here.


class PaymentTypeAPIView(ListAPIView):
    serializer_class = PaymentTypeSerializer
    queryset = PaymentType.objects.all()


class PaymentTypeDetailAPIView(RetrieveAPIView):
    serializer_class = PaymentTypeSerializer
    queryset = PaymentType.objects.all()


class PaymentTypeStudentAPIView(ListAPIView):
    serializer_class = PaymentTypeSerializer

    def get_queryset(self):
        return PaymentType.objects.filter(admission=False)


class PaymentTypeAdmissionAPIView(ListAPIView):
    serializer_class = PaymentTypeSerializer

    def get_queryset(self):
        return PaymentType.objects.filter(admission=True)


class TuitionFeeAPIView(ListAPIView):
    serializer_class = TuitionFeeSerializer
    queryset = TuitionFee.objects.all()


@api_view(['GET'])
def tuition_fee_detail(request):
    req = request.GET

    student = Student.objects.get(pk=req['student'])
    tuition = TuitionFee()

    if student.mode_of_entry.name == "JME":
        tuition = TuitionFee.objects.get(major=student.major.id, jme=True)
    if student.mode_of_entry.name == "D/E":
        tuition = TuitionFee.objects.get(major=student.major.id, de=True)
    if student.mode_of_entry.name == "D/E 300":
        tuition = TuitionFee.objects.get(major=student.major.id, conversion=True)

    if student.programme_type == "Part Time":
        if student.mode_of_entry.name == "JME":
            tuition = TuitionFee.objects.get(major=student.major.id, jme=True, pt=True)
        if student.mode_of_entry.name == "D/E":
            tuition = TuitionFee.objects.get(major=student.major.id, de=True, pt=True)
        if student.mode_of_entry.name == "D/E 300":
            tuition = TuitionFee.objects.get(major=student.major.id, conversion=True, pt=True)

    return Response(TuitionFeeSerializer(tuition).data)
