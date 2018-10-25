# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import hashlib
import json

import requests
from django.db import IntegrityError
from rest_framework.decorators import api_view
from rest_framework.response import Response

from payment.models import Payment


@api_view(['POST'])
def remita_notification(request):
    remita_status = "https://login.remita.net/remita/ecomm"
    data = request.data
    payments = []
    if isinstance(data, list):
        p = len(data)
        pr = 0
        fail = 0

        for d in data:
            payment = Payment.objects.get(order_id=d['orderRef'])
            rrr = d['rrr']
            payment.rrr = rrr
            payment.save()

            hsh = hashlib.sha512()
            hsh.update(payment.rrr+payment.payment_type.api_key+payment.payment_type.merchant_id)
            hsh_dig = hsh.hexdigest()

            r = requests.get(
                remita_status+"/"+payment.payment_type.merchant_id+"/"+payment.rrr+"/"+hsh_dig+"/status.reg")
            dat = json.loads(r.text)
            if (dat['status'] == '00') or (dat['status'] == '01'):
                payment.paid = True
                payment.status = dat['message']
                payment.amount = dat['amount']
                try:
                    payment.save()
                    pr += 1
                except IntegrityError:
                    fail += 1
            else:
                payment.status = dat['message']
                payment.amount = dat['amount']
                payment.paid = False
                try:
                    payment.save()
                    pr += 1
                except IntegrityError:
                    fail += 1
            payments.append(payment)
        serial = {
            'payments_sent': p,
            'payments_processed_success': pr,
            'payments_processed_fail': fail
        }

        return Response(serial)

    else:
        p = 1
        pr = 0
        fail = 0

        payment = Payment.objects.get(order_id=data['orderRef'])
        rrr = data['rrr']
        payment.rrr = rrr
        payment.save()

        hsh = hashlib.sha512()
        hsh.update(payment.rrr + payment.payment_type.api_key + payment.payment_type.merchant_id)
        hsh_dig = hsh.hexdigest()

        r = requests.get(
            remita_status + "/" + payment.payment_type.merchant_id + "/" + payment.rrr + "/" + hsh_dig + "/status.reg")
        dat = json.loads(r.text)
        if (dat['status'] == '00') or (dat['status'] == '01'):
            payment.paid = True
            payment.status = dat['message']
            payment.amount = dat['amount']
            try:
                payment.save()
                pr += 1
            except IntegrityError:
                fail += 1
        else:
            payment.status = dat['message']
            payment.amount = dat['amount']
            payment.paid = False
            try:
                payment.save()
                pr += 1
            except IntegrityError:
                fail += 1
        payments.append(payment)
    serial = {
        'payments_sent': p,
        'payments_processed_success': pr,
        'payments_processed_fail': fail
    }

    return Response(serial)
