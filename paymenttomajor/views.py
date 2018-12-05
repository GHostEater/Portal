# -*- coding: utf-8 -*-
from django.db.models import Q
from rest_framework.decorators import api_view, permission_classes
from rest_framework.generics import (ListAPIView, RetrieveDestroyAPIView, CreateAPIView)
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from accounts.models import Student
from payment.models import Payment
from paymenttomajor.serializers import PaymentToMajorSerializer, PaymentToMajorCreateSerializer
from paymenttomajor.models import PaymentToMajor

# Create your views here.
from paymentwaving.models import WavedPayment


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


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def student_payment_unedited(request):
    data = request.GET

    student = Student.objects.get(pk=data['student'])
    payment_to_major = PaymentToMajor()

    if student.programme_type == "Full Time":
        if student.mode_of_entry.name == "JME":
            payment_to_major = PaymentToMajor.objects.filter(major=student.major.id,
                                                             jme=True,
                                                             ft=True,
                                                             level__level__lte=student.level.level)
            payment_to_major = payment_to_major.filter(
                Q(payment_type__sex=student.user.sex) | Q(payment_type__sex="Both"))
        if student.mode_of_entry.name == "D/E":
            payment_to_major = PaymentToMajor.objects.filter(major=student.major.id,
                                                             de=True,
                                                             ft=True,
                                                             level__level__lte=student.level.level)
            payment_to_major = payment_to_major.filter(
                Q(payment_type__sex=student.user.sex) | Q(payment_type__sex="Both"))
        if student.mode_of_entry.name == "D/E 300":
            payment_to_major = PaymentToMajor.objects.filter(major=student.major.id,
                                                             conversion=True,
                                                             ft=True,
                                                             level__level__lte=student.level.level)
            payment_to_major = payment_to_major.filter(
                Q(payment_type__sex=student.user.sex) | Q(payment_type__sex="Both"))

    if student.programme_type == "Part Time":
        if student.mode_of_entry.name == "JME":
            payment_to_major = PaymentToMajor.objects.filter(major=student.major.id,
                                                             jme=True,
                                                             pt=True,
                                                             level__level__lte=student.level.level)
            payment_to_major = payment_to_major.filter(
                Q(payment_type__sex=student.user.sex) | Q(payment_type__sex="Both"))
        if student.mode_of_entry.name == "D/E":
            payment_to_major = PaymentToMajor.objects.filter(major=student.major.id,
                                                             de=True,
                                                             pt=True,
                                                             level__level__lte=student.level.level)
            payment_to_major = payment_to_major.filter(
                Q(payment_type__sex=student.user.sex) | Q(payment_type__sex="Both"))
        if student.mode_of_entry.name == "D/E 300":
            payment_to_major = PaymentToMajor.objects.filter(major=student.major.id,
                                                             conversion=True,
                                                             pt=True,
                                                             level__level__lte=student.level.level)
            payment_to_major = payment_to_major.filter(
                Q(payment_type__sex=student.user.sex) | Q(payment_type__sex="Both"))

    return Response(PaymentToMajorSerializer(payment_to_major, many=True).data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def student_payment(request):
    req = request.GET

    student = Student.objects.get(pk=req['student'])
    payment_to_major = PaymentToMajor()

    if student.programme_type == "Full Time":
        if student.mode_of_entry.name == "JME":
            payment_to_major = PaymentToMajor.objects.filter(major=student.major.id,
                                                             jme=True,
                                                             ft=True,
                                                             level__level__lte=student.level.level)
            payment_to_major = payment_to_major.filter(
                Q(payment_type__sex=student.user.sex) | Q(payment_type__sex="Both"))
        if student.mode_of_entry.name == "D/E":
            payment_to_major = PaymentToMajor.objects.filter(major=student.major.id,
                                                             de=True,
                                                             ft=True,
                                                             level__level__lte=student.level.level)
            payment_to_major = payment_to_major.filter(
                Q(payment_type__sex=student.user.sex) | Q(payment_type__sex="Both"))
        if student.mode_of_entry.name == "D/E 300":
            payment_to_major = PaymentToMajor.objects.filter(major=student.major.id,
                                                             conversion=True,
                                                             ft=True,
                                                             level__level__lte=student.level.level)
            payment_to_major = payment_to_major.filter(
                Q(payment_type__sex=student.user.sex) | Q(payment_type__sex="Both"))

    if student.programme_type == "Part Time":
        if student.mode_of_entry.name == "JME":
            payment_to_major = PaymentToMajor.objects.filter(major=student.major.id,
                                                             jme=True,
                                                             pt=True,
                                                             level__level__lte=student.level.level)
            payment_to_major = payment_to_major.filter(
                Q(payment_type__sex=student.user.sex) | Q(payment_type__sex="Both"))
        if student.mode_of_entry.name == "D/E":
            payment_to_major = PaymentToMajor.objects.filter(major=student.major.id,
                                                             de=True,
                                                             pt=True,
                                                             level__level__lte=student.level.level)
            payment_to_major = payment_to_major.filter(
                Q(payment_type__sex=student.user.sex) | Q(payment_type__sex="Both"))
        if student.mode_of_entry.name == "D/E 300":
            payment_to_major = PaymentToMajor.objects.filter(major=student.major.id,
                                                             conversion=True,
                                                             pt=True,
                                                             level__level__lte=student.level.level)
            payment_to_major = payment_to_major.filter(
                Q(payment_type__sex=student.user.sex) | Q(payment_type__sex="Both"))
    try:
        std_payment_wavings = WavedPayment.objects.filter(student=student.id)
    except WavedPayment.DoesNotExist:
        std_payment_wavings = None

    try:
        std_payments = Payment.objects.filter(student=student.id)
    except Payment.DoesNotExist:
        std_payments = None

    payments = []

    for p in payment_to_major:
        try:
            std_payments.get(payment_type=p.payment_type.id, paid=True, level=p.level.id)
            not_in_payments = False
        except Payment.DoesNotExist:
            not_in_payments = True

        try:
            std_payment_wavings.get(payment_type=p.payment_type.id, level=p.level.id)
            not_in_wavings = False
        except WavedPayment.DoesNotExist:
            not_in_wavings = True

        if not_in_payments and not_in_wavings:
            payments.append(p)

    return Response(PaymentToMajorSerializer(payments, many=True).data)
