# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import hashlib
import json

import requests
from rest_framework.decorators import api_view
from rest_framework.response import Response

from payment.models import Payment
from payment.serializers import PaymentSerializer


@api_view(['GET'])
def remita_status(request):
    remita_stat = "https://login.remita.net/remita/ecomm"
    req = request.GET

    payment = Payment.objects.get(rrr=req['rrr'])

    hsh = hashlib.sha512()
    hsh.update(payment.rrr+payment.payment_type.api_key+payment.payment_type.merchant_id)
    hsh_dig = hsh.hexdigest()

    r = requests.get(remita_stat+"/"+payment.payment_type.merchant_id+"/"+payment.rrr+"/"+hsh_dig+"/status.reg")
    data = json.loads(r.text)

    print data

    status = data['message']
    if (data['status'] == '00') or (data['status'] == '01'):
        payment.paid = True
        payment.status = status
        payment.amount = data['amount']
        payment.save()
    else:
        payment.status = status
        payment.paid = False
        payment.amount = data['amount']
        payment.save()

    return Response(PaymentSerializer(payment).data)
