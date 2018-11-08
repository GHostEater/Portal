# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from accounts.models import Student
from payment.models import Payment


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def access_fee_restrict(request):
    req = request.GET

    student = Student.objects.get(pk=req['student'])

    paid = False

    try:
        Payment.objects.get(student=req['student'], payment_type__name="Portal Access Fee", level=student.level,
                            paid=True)
        paid = True
    except Payment.DoesNotExist:
        paid = False

    return Response({'paid': paid})
