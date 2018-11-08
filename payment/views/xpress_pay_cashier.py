# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import hashlib
import json

import requests
from django.template.loader import get_template
from mailqueue.models import MailerMessage
from rest_framework.decorators import api_view
from rest_framework.response import Response

from payment.models import Payment
from payment.serializers import PaymentSerializer


@api_view(['POST'])
def xpress_pay_cashier(request):
    url = "https://www.ecashier.com/PaymentReferenceService/api/payment/GeneratePRN"
    data = request.data

    hsh = hashlib.sha256()
    hsh.update(data['hash'])
    hsh_dig = hsh.hexdigest()

    d = {
        "Name": data['name'],
        "Email": data['email'],
        "PhoneNo": data['phone'],
        "Amount": data['amount'],
        "Narration": data['narration'],
        "PaymentType": data['payment_type'],
        "CallBackURL": data['callback'],
        "TransactionId": data['transaction_id'],
        "HashString": hsh_dig,
        "HashType": "SHA256",
        "MerchantId": data['merchant_id'],
    }
    r = requests.post(url, json=d, verify=False)
    dat = json.loads(r.text)

    status = dat['status']
    message = dat['message']
    payment = Payment.objects.get(transaction_id=dat['TransactionId'])
    payment.prn = dat['PRN']
    if status == "00":
        payment.status = 'Pending Payment'
        payment.amount = data['amount']
        payment.save()
        subject = str("Successful Generation of Payment Reference for eCashier Payment of " + payment.payment_type.name
                      + str(" NGN") + str(payment.amount) + " (Transaction ID- " + str(payment.transaction_id) + ")")
    else:
        payment.status = message
        payment.amount = data['amount']
        payment.save()
        subject = str("Failed Generation of Payment Reference for eCashier Payment of " + payment.payment_type.name +
                      str(" NGN") + str(payment.amount) + " (Transaction ID- " + str(payment.transaction_id) + ")")

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

    serial = PaymentSerializer(payment).data

    return Response(serial)
