# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from accounts.models import Student
from payment.models import Payment
from payment.serializers import PaymentSerializer
from paymenttomajor.models import PaymentToMajor


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def tuition_fee_clearance(request):
    req = request.GET

    student = Student.objects.get(pk=req['student'])

    payments = Payment.objects.filter(student=student, level=student.level, paid=True)

    pays = []

    pay_status = {
        'p60': False,
        'p40': False,
        'p100': False
    }

    for p in payments:
        if p.payment_type.name == ("Tuition Fees 60% " + student.major.dept.college.acronym):
            pay_status['p60'] = True
            if p not in pays:
                pays.append(p)

        if p.payment_type.name == ("Tuition Fees 40% " + student.major.dept.college.acronym):
            pay_status['p40'] = True
            if p not in pays:
                pays.append(p)

        if p.payment_type.name == ("Tuition Fees 100% " + student.major.dept.college.acronym):
            pay_status['p100'] = True
            if p not in pays:
                pays.append(p)

        if (p.payment_type.name == ("Tuition Fees 60% " + student.major.dept.college.acronym)) and (
                    p.payment_type.name == ("Tuition Fees 40% " + student.major.dept.college.acronym)):
            pay_status['p100'] = True

    try:
        partial_payments = payments.filter(payment_type__name="Tuition Fees Partial",
                                           paid=True,
                                           level=student.level.id)
        p_payments_total = 0
        for pay in partial_payments:
            p_payments_total += pay.amount
            if p not in pays:
                pays.append(pay)

        if student.mode_of_entry.name == "JME":
            tuition_fee_60 = PaymentToMajor.objects.get(
                payment_type__name="Tuition Fees 60% " + student.major.dept.college.acronym,
                level=student.level,
                jme=True)
            tuition_fee_40 = PaymentToMajor.objects.get(
                payment_type__name="Tuition Fees 40% " + student.major.dept.college.acronym,
                level=student.level,
                jme=True)
            tuition_fee_100 = PaymentToMajor.objects.get(
                payment_type__name="Tuition Fees 100% " + student.major.dept.college.acronym,
                level=student.level,
                jme=True)

        if student.mode_of_entry.name == "D/E":
            tuition_fee_60 = PaymentToMajor.objects.get(
                payment_type__name="Tuition Fees 60% " + student.major.dept.college.acronym,
                level=student.level,
                de=True)
            tuition_fee_40 = PaymentToMajor.objects.get(
                payment_type__name="Tuition Fees 40% " + student.major.dept.college.acronym,
                level=student.level,
                de=True)
            tuition_fee_100 = PaymentToMajor.objects.get(
                payment_type__name="Tuition Fees 100% " + student.major.dept.college.acronym,
                level=student.level,
                de=True)

        if student.mode_of_entry.name == "D/E 300":
            tuition_fee_60 = PaymentToMajor.objects.get(
                payment_type__name="Tuition Fees 60% " + student.major.dept.college.acronym,
                level=student.level,
                conversion=True)
            tuition_fee_40 = PaymentToMajor.objects.get(
                payment_type__name="Tuition Fees 40% " + student.major.dept.college.acronym,
                level=student.level,
                conversion=True)
            tuition_fee_100 = PaymentToMajor.objects.get(
                payment_type__name="Tuition Fees 100% " + student.major.dept.college.acronym,
                level=student.level,
                conversion=True)

        if student.programme_type == "Part Time":
            if student.mode_of_entry.name == "JME":
                tuition_fee_60 = PaymentToMajor.objects.get(
                    payment_type__name="Tuition Fees 60% " + student.major.dept.college.acronym,
                    level=student.level,
                    pt=True,
                    jme=True)
                tuition_fee_40 = PaymentToMajor.objects.get(
                    payment_type__name="Tuition Fees 40% " + student.major.dept.college.acronym,
                    level=student.level,
                    pt=True,
                    jme=True)
                tuition_fee_100 = PaymentToMajor.objects.get(
                    payment_type__name="Tuition Fees 100% " + student.major.dept.college.acronym,
                    level=student.level,
                    pt=True,
                    jme=True)

            if student.mode_of_entry.name == "D/E":
                tuition_fee_60 = PaymentToMajor.objects.get(
                    payment_type__name="Tuition Fees 60% " + student.major.dept.college.acronym,
                    level=student.level,
                    pt=True,
                    de=True)
                tuition_fee_40 = PaymentToMajor.objects.get(
                    payment_type__name="Tuition Fees 40% " + student.major.dept.college.acronym,
                    level=student.level,
                    pt=True,
                    de=True)
                tuition_fee_100 = PaymentToMajor.objects.get(
                    payment_type__name="Tuition Fees 100% " + student.major.dept.college.acronym,
                    level=student.level,
                    pt=True,
                    de=True)

            if student.mode_of_entry.name == "D/E 300":
                tuition_fee_60 = PaymentToMajor.objects.get(
                    payment_type__name="Tuition Fees 60% " + student.major.dept.college.acronym,
                    level=student.level,
                    pt=True,
                    conversion=True)
                tuition_fee_40 = PaymentToMajor.objects.get(
                    payment_type__name="Tuition Fees 40% " + student.major.dept.college.acronym,
                    level=student.level,
                    pt=True,
                    conversion=True)
                tuition_fee_100 = PaymentToMajor.objects.get(
                    payment_type__name="Tuition Fees 100% " + student.major.dept.college.acronym,
                    level=student.level,
                    pt=True,
                    conversion=True)

        if p_payments_total >= tuition_fee_60.payment_type.amount:
            pay_status['p60'] = True
        if p_payments_total >= tuition_fee_40.payment_type.amount:
            pay_status['p40'] = True
        if p_payments_total >= tuition_fee_100.payment_type.amount:
            pay_status['p100'] = True

    except Payment.DoesNotExist:
        no_partial_payment = True

    response = {
        'payments': PaymentSerializer(pays, many=True).data,
        'pay_status': pay_status
    }
    return Response(response)
