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


class PaymentAPIView(ListAPIView):
    serializer_class = PaymentSerializer

    def get_queryset(self):
        queryset = Payment.objects.all().exclude(rrr=None)
        queryset = self.get_serializer_class().setup_eager_loading(queryset)
        return queryset


class PaymentCreateAPIView(CreateAPIView):
    serializer_class = PaymentCreateSerializer
    queryset = Payment.objects.all().exclude(rrr=None)


class PaymentStudentAPIView(ListAPIView):
    serializer_class = PaymentSerializer

    def get_queryset(self):
        queryset = Payment.objects.filter(student=self.request.GET['student']).exclude(rrr=None)
        queryset = self.get_serializer_class().setup_eager_loading(queryset)
        return queryset


class PaymentDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = PaymentSerializer

    def get_queryset(self):
        queryset = Payment.objects.all().exclude(rrr=None)
        queryset = self.get_serializer_class().setup_eager_loading(queryset)
        return queryset


class PaymentApplicationDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = PaymentSerializer
    lookup_field = 'application'

    def get_queryset(self):
        queryset = Payment.objects.all().exclude(rrr=None)
        queryset = self.get_serializer_class().setup_eager_loading(queryset)
        return queryset


@csrf_exempt
def remita_response(request):
    remita_status = "http://www.remitademo.net/remita/ecomm"
    rrr = request.GET['RRR']
    order_id = request.GET['orderID']

    payment = Payment.objects.filter(order_id=order_id).first()
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
    print data

    return render(request, 'remita.html', context={'payment': payment})


@csrf_exempt
def remita_response_json(request):
    remita_status = "http://www.remitademo.net/remita/ecomm"
    body_unicode = request.body.decode('utf-8')
    data = json.loads(body_unicode)

    try:
        payment = Payment.objects.get(rrr=data['rrr'])

        rrr = payment.rrr
        payment.status = ''
        payment.save()

        hsh = hashlib.sha512()
        hsh.update(rrr+payment.payment_type.api_key+payment.payment_type.merchant_id)
        hsh_dig = hsh.hexdigest()

        r = requests.get(remita_status+"/"+payment.payment_type.merchant_id+"/"+rrr+"/"+hsh_dig+"/status.reg")
        data = json.loads(r.text)
        if (data['status'] == '00') or (data['status'] == '01'):
            payment.paid = True
            payment.status = data['message']
            payment.save()
        else:
            payment.status = data['message']
            payment.paid = False
            payment.save()
        payment.payment_type.amount += 350
        serial = PaymentSerializer(payment)

        return JsonResponse(serial.data, safe=False, status=200)
    except ObjectDoesNotExist:
        payment = Payment.objects.filter(order_id=data['rrr']).first()

        order_id = payment.order_id
        payment.status = ''
        payment.save()

        hsh = hashlib.sha512()
        hsh.update(order_id + payment.payment_type.api_key + payment.payment_type.merchant_id)
        hsh_dig = hsh.hexdigest()

        r = requests.get(
            remita_status + "/" + payment.payment_type.merchant_id + "/" + order_id + "/" + hsh_dig + "/orderstatus.reg")
        data = json.loads(r.text)
        if (data['status'] == '00') or (data['status'] == '01'):
            payment.paid = True
            payment.status = data['message']
            payment.rrr = data['RRR']
            payment.save()
        else:
            payment.status = data['message']
            payment.paid = False
            payment.rrr = data['RRR']
            payment.save()
        payment.payment_type.amount += 350
        serial = PaymentSerializer(payment)

        return JsonResponse(serial.data, safe=False, status=200)


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
