# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime

from django.template.loader import get_template
from mailqueue.models import MailerMessage
from rest_framework.decorators import api_view
from rest_framework.response import Response

from payment.models import Payment


@api_view(['POST'])
def xpress_notification(request):
    data = request.data
    payments = []
    p = 0
    q = 0
    r = 0

    for d in data:
        payment = Payment.objects.get(prn=d['prn'])
        if payment.application:
            receiver = payment.application.email
        else:
            receiver = payment.student.email

        if (d['status'] == '00') or (d['status'] == '01'):
            payment.paid = True
            payment.status = d['message']
            payment.date = datetime.datetime.now()
            payment.amount = d['amount']
            payment.save()
            subject = str("Successful eCashier Payment of " + payment.payment_type.name + str(" NGN") + str(
                payment.amount) + " (Transaction ID- " + str(payment.transaction_id) + ")")
            q += 1
        else:
            payment.status = d['message']
            payment.paid = False
            payment.amount = d['amount']
            payment.save()
            subject = str("Failed eCashier Payment of " + payment.payment_type.name + str(" NGN") +
                          str(payment.amount) + " (Transaction ID- " + str(payment.transaction_id) + ")")
            r += 1
        payments.append(payment)

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
        p += 1
    serial = {"payments processed": p, "successful payments": q, "failed payments": r}

    return Response(serial)
