# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework.decorators import api_view
from rest_framework.response import Response

from payment.models import Payment
from payment.serializers import PaymentSerializer


@api_view(['GET'])
def student_paid_list(request):
    req = request.GET

    payments = Payment.objects.filter(student__major=req['major'], 
                                      student__level=req['level'], 
                                      payment_type=req['payment_type'],
                                      session=req['session'])
    
    return Response(PaymentSerializer(payments, many=True).data)
