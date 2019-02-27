# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from accounts.models import Student
from accounts.serializers import StudentSerializer
from courseresult.models import CourseResult
from payment.models import Payment
from payment.serializers import PaymentSerializer
from paymenttype.models import PaymentType, TuitionFee
from paymentwaving.models import WavedPayment


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def student_paid_list(request):
    req = request.GET
    response = []
    pay_status = {
        'p_first': False,
        'p_second': False,
        'p_total': False
    }
    college = ''
    dept = ''
    major = ''
    level = ''
    if request.GET.get('college'):
        college = req['college']
    if request.GET.get('dept'):
        dept = req['dept']
    if request.GET.get('major'):
        major = req['major']
    if request.GET.get('level'):
        level = req['level']

    if college == '' and dept == '' and major == '' and level == '':
        students = Student.objects.all().exclude(status='8')
    if college == '' and dept == '' and major == '' and level != '':
        students = Student.objects.filter(level=level)
    if college != '' and dept == '' and major == '' and level == '':
        students = Student.objects.filter(major__dept__college=college)
    if college != '' and dept == '' and major == '' and level != '':
        students = Student.objects.filter(major__dept__college=college, level=level)
    if dept != '' and major == '' and level == '':
        students = Student.objects.filter(major__dept=dept)
    if dept != '' and major == '' and level != '':
        students = Student.objects.filter(major__dept=dept, level=level)
    if major != '' and level == '':
        students = Student.objects.filter(major=major)
    if major != '' and level != '':
        students = Student.objects.filter(major=major, level=level)

    for student in students:
        payment_type = PaymentType.objects.get(pk=req['payment_type'])
        payment_wavings = WavedPayment.objects.filter(student=student.id)
        payments = Payment.objects.filter(student=student.id,
                                          payment_type=req['payment_type'],
                                          session=req['session'])

        try:
            waved_payment = payment_wavings.get(level=req['level'], payment_type=payment_type.id)
            in_wavings = True
        except WavedPayment.DoesNotExist:
            in_wavings = False

        if payment_type.tuition:
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
            tuition_payments = payments.filter(payment_type__tuition=True,
                                               paid=True,
                                               session=req['session'])
            try:
                level = tuition_payments[0].level.level
                date = tuition_payments[0].date
            except IndexError:
                level = ''
                date = ''
            t_payments_total = 0
            for pay in tuition_payments:
                t_payments_total += pay.amount

            if t_payments_total >= int(tuition.first):
                pay_status['p_first'] = True
            if t_payments_total >= int(tuition.second):
                pay_status['p_second'] = True
            if t_payments_total >= int(tuition.total):
                pay_status['p_total'] = True
            obj = {
                'student': StudentSerializer(student).data,
                'pay_status': pay_status,
                'paid': pay_status['p_total'],
                'amount': t_payments_total,
                'level': level,
                'owing': tuition.total - t_payments_total,
                'date': date,
                'payments': PaymentSerializer(tuition_payments, many=True).data,
            }
            if pay_status['p_total']:
                response.append(obj)

            if in_wavings:
                obj = {
                    'student': StudentSerializer(student).data,
                    'waved': True,
                    'amount': waved_payment.payment_type.amount,
                    'level': waved_payment.level.level
                }
                response.append(obj)

        elif in_wavings:
            obj = {
                'student': StudentSerializer(student).data,
                'waved': True,
                'amount': waved_payment.payment_type.amount,
                'level': waved_payment.level.level
            }
            response.append(obj)

        else:
            try:
                payment = payments.get(paid=True)
            except Payment.DoesNotExist:
                payment = Payment()

            if payment.paid:
                owing = float(payment.amount) - float(payment_type.amount)
                obj = {
                    'student': StudentSerializer(student).data,
                    'paid': payment.paid,
                    'amount': payment.amount,
                    'level': payment.level.level,
                    'owing': owing,
                    'date': payment.date,
                    'rrr': payment.rrr
                }
                response.append(obj)
    
    return Response(response)
