# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from accounts.models import Student
from payment.models import Payment
from payment.serializers import PaymentSerializer
from paymenttype.models import TuitionFee
from paymentwaving.models import WavedPayment
from paymentwaving.serializers import WavedPaymentSerializer


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def tuition_fee_clearance(request):
    req = request.GET

    student = Student.objects.get(pk=req['student'])

    payments = Payment.objects.filter(student=student, level=student.level, paid=True)
    payment_wavings = WavedPayment.objects.filter(student=student.id, level=student.level)

    try:
        payment_wavings.get(level=student.level, payment_type__tuition=True)
        in_wavings = True
    except WavedPayment.DoesNotExist:
        in_wavings = False

    tuition = TuitionFee()

    if student.programme_type == "Full Time":
        if student.mode_of_entry.name == "JME":
            tuition = TuitionFee.objects.get(major=student.major.id, jme=True, ft=True)
        if student.mode_of_entry.name == "D/E":
            tuition = TuitionFee.objects.get(major=student.major.id, de=True, ft=True)
        if student.mode_of_entry.name == "D/E 300":
            tuition = TuitionFee.objects.get(major=student.major.id, conversion=True, ft=True)

    if student.programme_type == "Part Time":
        if student.mode_of_entry.name == "JME":
            tuition = TuitionFee.objects.get(major=student.major.id, jme=True, pt=True)
        if student.mode_of_entry.name == "D/E":
            tuition = TuitionFee.objects.get(major=student.major.id, de=True, pt=True)
        if student.mode_of_entry.name == "D/E 300":
            tuition = TuitionFee.objects.get(major=student.major.id, conversion=True, pt=True)

    pay_status = {
        'p_first': False,
        'p_second': False,
        'p_total': False
    }

    try:
        tuition_payments = payments.filter(payment_type__tuition=True,
                                           paid=True,
                                           level=student.level.id)
        t_payments_total = 0
        for pay in tuition_payments:
            t_payments_total += pay.amount

        if t_payments_total >= int(tuition.first):
            pay_status['p_first'] = True
        if t_payments_total >= int(tuition.second):
            pay_status['p_second'] = True
        if t_payments_total >= int(tuition.total):
            pay_status['p_total'] = True

    except Payment.DoesNotExist:
        no_payment = True

    if in_wavings:
        pay_status = {
            'p_first': True,
            'p_second': True,
            'p_total': True
        }

    response = {
        'payments': PaymentSerializer(payments, many=True).data,
        'pay_status': pay_status,
        'waved_payments': WavedPaymentSerializer(payment_wavings, many=True).data
    }
    return Response(response)
