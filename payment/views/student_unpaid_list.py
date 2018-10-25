# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from accounts.models import Student
from accounts.serializers import StudentSerializer
from payment.models import Payment


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def student_unpaid_list(request):
    req = request.GET
    std = []
    
    students = Student.objects.filter(major=req['major'], level=req['level'])
    
    for s in students:
        try:
            Payment.objects.get(student=s.id, payment_type=req['payment_type'], session=req['session'])
        except Payment.DoesNotExist:
            std.append(s)
    
    return Response(StudentSerializer(std, many=True).data)
