# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework.decorators import api_view
from rest_framework.response import Response

from admission.models import Application
from admission.serializers import ApplicationSerializer
from payment.models import Payment


@api_view(['GET'])
def access_fee_restrict(request):
    req = request.GET
