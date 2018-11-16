# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from admission.models import Application
from admission.serializers import ApplicationSerializer
from payment.models import Payment


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def application_unpaid_list(request):
    req = request.GET
    std = []

    apps = Application.objects.filter(session=req['session'])

    for app in apps:
        try:
            Payment.objects.get(application=app.id, payment_type=req['payment_type'], session=req['session'])
        except Payment.DoesNotExist:
            std.append(app)

    return Response(ApplicationSerializer(std, many=True).data)
