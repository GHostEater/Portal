# -*- coding: utf-8 -*-
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

    if student.mode_of_entry.name == "JME":
        payment_to_major = PaymentToMajor.objects.filter(major=student.major.id,
                                                         jme=True,
                                                         level__level__lte=student.level.level)
    if student.mode_of_entry.name == "D/E":
        payment_to_major = PaymentToMajor.objects.filter(major=student.major.id,
                                                         de=True,
                                                         level__level__lte=student.level.level)
    if student.mode_of_entry.name == "D/E 300":
        payment_to_major = PaymentToMajor.objects.filter(major=student.major.id,
                                                         conversion=True,
                                                         level__level__lte=student.level.level)
    if student.programme_type == "Part Time":
        if student.mode_of_entry.name == "JME":
            payment_to_major = PaymentToMajor.objects.filter(major=student.major.id,
                                                             jme=True,
                                                             pt=True,
                                                             level__level__lte=student.level.level)
        if student.mode_of_entry.name == "D/E":
            payment_to_major = PaymentToMajor.objects.filter(major=student.major.id,
                                                             de=True,
                                                             pt=True,
                                                             level__level__lte=student.level.level)
        if student.mode_of_entry.name == "D/E 300":
            payment_to_major = PaymentToMajor.objects.filter(major=student.major.id,
                                                             conversion=True,
                                                             pt=True,
                                                             level__level__lte=student.level.level)

    return Response(PaymentToMajorSerializer(payment_to_major, many=True).data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def student_payment(request):
    req = request.GET

    student = Student.objects.get(pk=req['student'])
    payment_to_major = PaymentToMajor()

    if student.mode_of_entry.name == "JME":
        payment_to_major = PaymentToMajor.objects.filter(major=student.major.id,
                                                         jme=True,
                                                         level__level__lte=student.level.level)
    if student.mode_of_entry.name == "D/E":
        payment_to_major = PaymentToMajor.objects.filter(major=student.major.id,
                                                         de=True,
                                                         level__level__lte=student.level.level)
    if student.mode_of_entry.name == "D/E 300":
        payment_to_major = PaymentToMajor.objects.filter(major=student.major.id,
                                                         conversion=True,
                                                         level__level__lte=student.level.level)
    if student.programme_type == "Part Time":
        if student.mode_of_entry.name == "JME":
            payment_to_major = PaymentToMajor.objects.filter(major=student.major.id,
                                                             jme=True,
                                                             pt=True,
                                                             level__level__lte=student.level.level)
        if student.mode_of_entry.name == "D/E":
            payment_to_major = PaymentToMajor.objects.filter(major=student.major.id,
                                                             de=True,
                                                             pt=True,
                                                             level__level__lte=student.level.level)
        if student.mode_of_entry.name == "D/E 300":
            payment_to_major = PaymentToMajor.objects.filter(major=student.major.id,
                                                             conversion=True,
                                                             pt=True,
                                                             level__level__lte=student.level.level)
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
            # If payment to major is 60% or 40% Tuition only show if 100% not paid in that level
            if (p.payment_type.name == ("Tuition Fees 60% " + student.major.dept.college.acronym)) or (
                        p.payment_type.name == ("Tuition Fees 40% " + student.major.dept.college.acronym)):
                try:
                    std_payments.get(payment_type__name="Tuition Fees 100% " + student.major.dept.college.acronym,
                                     paid=True, level=p.level.id)
                    no_100_payment = False
                except Payment.DoesNotExist:
                    no_100_payment = True

                try:
                    partial_payments = std_payments.filter(payment_type__name="Tuition Fees Partial",
                                                           paid=True,
                                                           level=p.level.id)
                    p_payments_total = 0
                    for pay in partial_payments:
                        p_payments_total += pay.amount
                    if p_payments_total >= p.payment_type.amount:
                        no_partial_payment = False
                    else:
                        no_partial_payment = True
                except Payment.DoesNotExist:
                    no_partial_payment = True
                if no_100_payment and no_partial_payment:
                    payments.append(p)
            elif p.payment_type.name == ("Tuition Fees 100% " + student.major.dept.college.acronym):
                try:
                    partial_payments = std_payments.filter(payment_type__name="Tuition Fees Partial",
                                                           paid=True,
                                                           level=p.level.id)
                    p_payments_total = 0
                    for pay in partial_payments:
                        p_payments_total += pay.amount
                    if p_payments_total > 0:
                        no_partial_payment = False
                    else:
                        no_partial_payment = True
                except Payment.DoesNotExist:
                    no_partial_payment = True

                try:
                    std_payments.get(payment_type__name="Tuition Fees 60% " + student.major.dept.college.acronym,
                                     paid=True, level=p.level.id,
                                     session=req['session'])
                    no_60_payment = False
                except Payment.DoesNotExist:
                    no_60_payment = True

                try:
                    std_payments.get(payment_type__name="Tuition Fees 40% " + student.major.dept.college.acronym,
                                     paid=True, level=p.level.id,
                                     session=req['session'])
                    no_40_payment = False
                except Payment.DoesNotExist:
                    no_40_payment = True

                if no_partial_payment and no_60_payment and no_40_payment:
                    payments.append(p)
            elif p.payment_type.name == "Tuition Fees Partial":
                continue
            else:
                payments.append(p)

    return Response(PaymentToMajorSerializer(payments, many=True).data)
