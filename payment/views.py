# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import hashlib
import hmac
import json
import datetime

from django.shortcuts import render

from mailqueue.models import MailerMessage

from django.template.loader import get_template

import requests
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView

from payment.serializers import PaymentSerializer, PaymentCreateSerializer
from payment.models import Payment

# Create your views here.


class PaymentAPIView(ListAPIView):
    serializer_class = PaymentSerializer

    def get_queryset(self):
        queryset = Payment.objects.all()
        queryset = self.get_serializer_class().setup_eager_loading(queryset)
        return queryset


class PaymentCreateAPIView(CreateAPIView):
    serializer_class = PaymentCreateSerializer
    queryset = Payment.objects.all()


class PaymentStudentAPIView(ListAPIView):
    serializer_class = PaymentSerializer

    def get_queryset(self):
        queryset = Payment.objects.filter(student=self.request.GET['student'])
        queryset = self.get_serializer_class().setup_eager_loading(queryset)
        return queryset


class PaymentDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = PaymentSerializer

    def get_queryset(self):
        queryset = Payment.objects.all()
        queryset = self.get_serializer_class().setup_eager_loading(queryset)
        return queryset


class PaymentTransactionDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = PaymentSerializer
    lookup_field = 'transaction_id'

    def get_queryset(self):
        queryset = Payment.objects.all()
        queryset = self.get_serializer_class().setup_eager_loading(queryset)
        return queryset


class PaymentApplicationAPIView(ListAPIView):
    serializer_class = PaymentSerializer

    def get_queryset(self):
        queryset = Payment.objects.filter(application=self.request.GET['application'])
        queryset = self.get_serializer_class().setup_eager_loading(queryset)
        return queryset


@csrf_exempt
def hasher(request):
    body_unicode = request.body.decode('utf-8')
    data = json.loads(body_unicode)
    key = str(data['key'].decode('hex'))
    enc = str(data['enc'])

    hsh = hmac.new(key=key, msg=enc, digestmod=hashlib.sha256)
    hsh_dig = hsh.hexdigest()

    serial = {"hex": hsh_dig}

    return JsonResponse(serial, safe=False, status=200)


@csrf_exempt
def xpress_response(request):
    xpress_status = "https://staging.payxpress.com/xp-gateway/ws/v2/query"
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

    response = data['responseCode']
    status = data['responseMsg']

    if response == '000':
        payment.paid = True
        payment.status = status
        payment.date = datetime.datetime.now()
        payment.save()
        subject = str(
            "Successful Web Payment of " + payment.payment_type.name + str(" NGN") + str(payment.payment_type.amount) +
            " (Transaction ID- " + str(payment.transaction_id) + ")")
    else:
        payment.status = status
        payment.paid = False
        payment.save()
        subject = str(
            "Failed Web Payment of " + payment.payment_type.name + str(" NGN") + str(payment.payment_type.amount) +
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


@csrf_exempt
def xpress_pay_cashier(request):
    url = "http://80.88.8.245:8090/api/payment/GeneratePRN"
    body_unicode = request.body.decode('utf-8')
    data = json.loads(body_unicode)

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
        payment.save()
        subject = str("Successful Generation of Payment Reference for eCashier Payment of " + payment.payment_type.name + str(" NGN") + str(
            payment.payment_type.amount) + " (Transaction ID- " + str(payment.transaction_id) + ")")
    else:
        payment.status = message
        payment.save()
        subject = str("Failed Generation of Payment Reference for eCashier Payment of " + payment.payment_type.name + str(" NGN") + str(
            payment.payment_type.amount) + " (Transaction ID- " + str(payment.transaction_id) + ")")

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

    return JsonResponse(serial, safe=False, status=200)


@csrf_exempt
def xpress_notification(request):
    body_unicode = request.body.decode('utf-8')
    data = json.loads(body_unicode)
    payments = []
    p = 0

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
            payment.save()
            subject = str("Successful eCashier Payment of " + payment.payment_type.name + str(" NGN") + str(
                payment.payment_type.amount) + " (Transaction ID- " + str(payment.transaction_id) + ")")
        else:
            payment.status = d['message']
            payment.paid = False
            payment.save()
            subject = str("Failed eCashier Payment of " + payment.payment_type.name + str(" NGN") +
                str(payment.payment_type.amount) + " (Transaction ID- " + str(payment.transaction_id) + ")")
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
    serial = {"payments processed": p}

    return JsonResponse(serial, safe=False, status=200)


@csrf_exempt
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
