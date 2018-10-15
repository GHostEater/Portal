# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import hashlib
import json

from django.shortcuts import render

import requests
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView

from payment.serializers import PaymentSerializer, PaymentCreateSerializer
from payment.models import Payment


@csrf_exempt
def remita_notification(request):
    remita_status = "http://www.remitademo.net/remita/ecomm"
    body_unicode = request.body.decode('utf-8')
    data = json.loads(body_unicode)
    payments = []

    for d in data:
        payment = Payment.objects.filter(order_id=d['orderRef']).first()
        rrr = d['rrr']
        payment.rrr = rrr
        payment.save()

        hsh = hashlib.sha512()
        hsh.update(payment.rrr+payment.payment_type.api_key+payment.payment_type.merchant_id)
        hsh_dig = hsh.hexdigest()

        r = requests.get(remita_status+"/"+payment.payment_type.merchant_id+"/"+payment.rrr+"/"+hsh_dig+"/status.reg")
        dat = json.loads(r.text)
        if (dat['status'] == '00') or (dat['status'] == '01'):
            payment.paid = True
            payment.status = dat['message']
            payment.save()
        else:
            payment.status = dat['message']
            payment.paid = False
            payment.save()
        payment.payment_type.amount += 350
        payments.append(payment)
    serial = 'ok'

    return HttpResponse(serial)
