# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import hashlib
import json

import requests
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from payment.models import Payment


@csrf_exempt
def remita_response(request):
    remita_status = "http://www.remitademo.net/remita/ecomm"
    rrr = request.GET['RRR']
    order_id = request.GET['orderID']

    payment = Payment.objects.find(order_id=order_id)
    payment.rrr = rrr
    payment.status = ''
    payment.save()

    hsh = hashlib.sha512()
    hsh.update(rrr+payment.payment_type.api_key+payment.payment_type.merchant_id)
    hsh_dig = hsh.hexdigest()

    r = requests.get(remita_status+"/"+payment.payment_type.merchant_id+"/"+rrr+"/"+hsh_dig+"/status.reg")
    data = json.loads(r.text)
    if request.GET['status']:
        status = request.GET['status']
    else:
        status = data['message']
    if (data['status'] == '00') or (data['status'] == '01'):
        payment.paid = True
        payment.status = status
        payment.save()
    else:
        payment.status = status
        payment.paid = False
        payment.save()
    payment.payment_type.amount += 350

    return render(request, 'remita.html', context={'payment': payment})
