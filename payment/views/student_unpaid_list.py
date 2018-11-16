# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from accounts.models import Student
from accounts.serializers import StudentSerializer
from payment.models import Payment
from paymenttype.models import PaymentType, TuitionFee
from paymentwaving.models import WavedPayment


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def student_unpaid_list(request):
    req = request.GET
    response = []
    pay_status = {
        'p_first': False,
        'p_second': False,
        'p_total': False
    }
    
    students = Student.objects.filter(major=req['major'], level=req['level'])
    
    for student in students:
        payment_type = PaymentType.objects.get(pk=req['payment_type'])
        payment_wavings = WavedPayment.objects.filter(student=student.id)
        payments = Payment.objects.filter(student=student.id,
                                          payment_type=req['payment_type'],
                                          session=req['session'])

        try:
            payment_wavings.get(level=req['level'], payment_type=payment_type.id)
            in_wavings = True
        except WavedPayment.DoesNotExist:
            in_wavings = False

        if payment_type.tuition:
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
            tuition_payments = payments.filter(payment_type__tuition=True,
                                               paid=True,
                                               session=req['session'])
            try:
                level = tuition_payments[0].level.level
            except IndexError:
                level = ''
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
                'owing': tuition.total - t_payments_total,
                'level': level
            }
            if not pay_status['p_total'] and not in_wavings:
                response.append(obj)
        else:
            try:
                Payment.objects.get(student=student.id, payment_type=req['payment_type'], session=req['session'],
                                    paid=True)
            except Payment.DoesNotExist:
                if not in_wavings:
                    obj = {
                        'student': StudentSerializer(student).data,
                        'owing': payment_type.amount
                    }
                    response.append(obj)
    
    return Response(response)
