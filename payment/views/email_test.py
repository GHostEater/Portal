# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from mailqueue.models import MailerMessage

from django.template.loader import get_template

from django.http import HttpResponse
from rest_framework.decorators import api_view

from payment.models import Payment


@api_view(['GET'])
def email_test(request):
    payment = Payment.objects.get(application__email='v@gmail.com')
    template = get_template('email.html')
    context = {'payment': payment}
    content = template.render(context)

    if payment.paid:
        subject = str("Successful Web Payment of "+payment.payment_type.name+str(" NGN")+str(payment.payment_type.amount) +
                      " (Transaction ID- "+str(payment.transaction_id)+")")
    else:
        subject = str("Failed Web Payment of " + payment.payment_type.name + str(" NGN") + str(payment.payment_type.amount) +
                      " (Transaction ID- " + str(payment.transaction_id) + ")")

    message = MailerMessage()
    message.subject = subject
    message.to_address = 'lasisi28@gmail.com'
    message.bcc_address = 'payments@fuo.edu.ng'
    message.from_address = 'payments@fuo.edu.ng'
    message.content = ""
    message.html_content = content
    message.app = "Fountain University Mailing System"
    message.save()
    return HttpResponse('ok')
