# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import hashlib
import hmac
import json

import datetime
import requests
from django.shortcuts import render
from django.template.loader import get_template
from mailqueue.models import MailerMessage
from rest_framework.decorators import api_view

from payment.models import Payment


@api_view(['GET'])
def xpress_response(request):
    xpress_status = "https://payxpress.com/xp-gateway/ws/v2/query"
    transaction_id = request.GET['transaction-id']
    merchant_id = request.GET['merchant-id']

    payment = Payment.objects.get(transaction_id=transaction_id)

    hsh_msg = str("merchant-id="+merchant_id+"&public-key="+payment.payment_type.public_key+"&transaction-id="+transaction_id)
    hsh = hmac.new(key=str(payment.payment_type.private_key.decode('hex')), msg=hsh_msg, digestmod=hashlib.sha256)
    hsh_dig = hsh.hexdigest()

    d = {
        "transaction-id": transaction_id,
        "merchant-id": merchant_id,
        "public-key": payment.payment_type.public_key,
        "hash": hsh_dig,
        "hash-type": "SHA256",
    }
    r = requests.post(xpress_status, json=d, verify=False)
    data = json.loads(r.text)
    print data

    response = data['responseCode']
    status = data['responseMsg']

    if response == '000':
        payment.paid = True
        payment.status = status
        payment.date = datetime.datetime.now()
        payment.amount = data['amount']
        payment.save()
        subject = str(
            "Successful Web Payment of " + payment.payment_type.name + str(" NGN") + str(payment.amount) +
            " (Transaction ID- " + str(payment.transaction_id) + ")")
    else:
        payment.status = status
        payment.paid = False
        payment.date = datetime.datetime.now()
        payment.amount = data['amount']
        payment.save()
        subject = str(
            "Failed Web Payment of " + payment.payment_type.name + str(" NGN") + str(payment.amount) +
            " (Transaction ID- " + str(payment.transaction_id) + ")")

    if payment.application:
        receiver = payment.application.email
    else:
        receiver = payment.student.email

    template = get_template('email.html')
    context = {'payment': payment}
    content = template.render(context)

    message = MailerMessage()
    message.subject = subject
    message.to_address = receiver
    message.bcc_address = 'payments@fuo.edu.ng'
    message.from_address = 'payments@fuo.edu.ng'
    message.content = ""
    message.html_content = content
    message.app = "Fountain University Mailing System"
    message.save()

    return render(request, 'xpress.html', context={'payment': payment})
