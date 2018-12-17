# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import hashlib
import json

import datetime
import requests
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from payment.models import Payment
from systemlog.models import Log


@csrf_exempt
def remita_final_response(request):
    remita_status = "https://login.remita.net/remita/ecomm"
    rrr = request.GET['RRR']

    payment = Payment.objects.get(rrr=rrr)

    payment.rrr = rrr
    payment.save()

    hsh = hashlib.sha512()
    hsh.update(rrr+payment.payment_type.api_key+payment.payment_type.merchant_id)
    hsh_dig = hsh.hexdigest()

    r = requests.get(remita_status+"/"+payment.payment_type.merchant_id+"/"+rrr+"/"+hsh_dig+"/status.reg")
    data = json.loads(r.text)
    if hasattr(request.GET, 'status'):
        status = request.GET['status']
    else:
        status = data['message']
    if (data['status'] == '00') or (data['status'] == '01'):
        payment.paid = True
        payment.status = status
        payment.amount = data['amount']
        payment.save()

        if payment.student:
            log = Log()
            log.user = payment.student.user.last_name + ", " + payment.student.user.first_name
            log.action = "Paid For " + payment.payment_type.name
            log.role = "Student"
            log.location = "System"
            log.date = datetime.datetime.now()
            log.save()
    else:
        payment.status = status
        payment.paid = False
        payment.amount = data['amount']
        payment.save()

    return render(request, 'remita.html', context={'payment': payment})
