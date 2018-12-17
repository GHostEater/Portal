# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import hashlib
import json

import requests
from rest_framework.decorators import api_view
from rest_framework.response import Response

import transcript.models
from accounts.models import Student
from admission.models import Application
from level.models import Level
from payment.models import Payment
from payment.serializers import PaymentSerializer
from paymenttype.models import PaymentType
from session.models import Session


@api_view(['POST'])
def generate_rrr(request):
    gen_rrr = "https://login.remita.net/remita/exapp/api/v1/send/api/echannelsvc/merchant/api/paymentinit"
    req = request.data

    matric_no = ''
    dept = ''
    level = ''
    student = None
    app = None
    trans_app = None

    if request.data.get('matricNo'):
        matric_no = req['matricNo']
    if request.data.get('dept'):
        dept = req['dept']

    if request.data.get('level'):
        level = Level.objects.get(pk=req['level'])
    else:
        level = Level()
        level.level = ''

    if request.data.get('student'):
        student = Student.objects.get(pk=req['student'])
    if request.data.get('application'):
        app = Application.objects.get(pk=req['application'])
    if request.data.get('transcript_app'):
        trans_app = transcript.models.Application.objects.get(pk=req['transcript_app'])

    payment_type = PaymentType.objects.get(pk=req['payment_type'])
    session = Session.objects.get(pk=req['session'])

    payment = Payment()
    payment.payment_type = payment_type
    if student is not None:
        payment.student = student
    if app is not None:
        payment.application = app
    if trans_app is not None:
        payment.transcript_app = trans_app
    payment.session = session
    if level.level != '':
        payment.level = level
    payment.order_id = req['order_id']
    payment.status = req['status']
    payment.date = req['date']

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
            "value": matric_no,
            "type": "ALL"
        },
            {
                "name": "Department",
                "value": dept,
                "type": "ALL"
            },
            {
                "name": "Level",
                "value": level.level,
                "type": "ALL"
            },
            {
                "name": "Purpose of Payment",
                "value": payment.payment_type.name,
                "type": "ALL"
            }
        ]
    }

    header = {
        "Authorization": "remitaConsumerKey=" + payment.payment_type.merchant_id + ",remitaConsumerToken=" + hsh_dig,
        "Content-Type": "application/json"
        }

    r = requests.post(url=gen_rrr, headers=header, json=request)

    data = json.loads(r.text.split("(")[1].strip(")"))
    status = data['status']
    if data['statuscode'] == '025':
        payment.status = status
        payment.amount = req['amount']
        payment.rrr = data['RRR']
        payment.save()

    return Response(PaymentSerializer(payment).data)
