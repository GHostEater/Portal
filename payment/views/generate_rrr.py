# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import hashlib
import json

import requests
from rest_framework.decorators import api_view
from rest_framework.response import Response

from payment.models import Payment
from payment.serializers import PaymentSerializer


@api_view(['POST'])
def generate_rrr(request):
    gen_rrr = "https://login.remita.net/remita/exapp/api/v1/send/api/echannelsvc/merchant/api/paymentinit"
    req = request.data

    payment = Payment.objects.get(pk=req['payment'])

    hsh = hashlib.sha512()
    hsh.update(
        payment.payment_type.merchant_id
        + payment.payment_type.service_type_id + payment.order_id + str(req['amount']) + payment.payment_type.api_key)
    hsh_dig = hsh.hexdigest()

    request = {
        "serviceTypeId": payment.payment_type.service_type_id,
        "amount": str(req['amount']),
        "orderId": payment.order_id,
        "payerName": req['payerName'],
        "payerEmail": req['payerEmail'],
        "payerPhone": req['payerPhone'],
        "description": payment.payment_type.name,
        "customFields": [{
            "name": "Matric No",
            "value": req['matricNo'],
            "type": "ALL"
        },
            {
            "name": "Department",
            "value": req['dept'],
            "type": "ALL"
        },
            {
            "name": "Level",
            "value": req['level'],
            "type": "ALL"
        },
            {
            "name": "Purpose of Payment",
            "value": payment.payment_type.name,
            "type": "ALL"
        }
        ]
    }

    header = {"Authorization": "remitaConsumerKey="+payment.payment_type.merchant_id+",remitaConsumerToken="+hsh_dig,
              "Content-Type": "application/json"
            }

    r = requests.post(url=gen_rrr, headers=header, json=request)
    print r.text

    data = json.loads(r.text.split("(")[1].strip(")"))
    status = data['status']
    if data['statuscode'] == '025':
        payment.status = status
        payment.amount = req['amount']
        payment.rrr = data['RRR']
        payment.save()

    return Response(PaymentSerializer(payment).data)
