# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from dept.models import Dept


class PaymentType(models.Model):
    name = models.CharField(max_length=100)
    amount = models.FloatField()
    merchant_id = models.CharField(max_length=256, null=True, blank=True)
    service_type_id = models.CharField(max_length=256, null=True, blank=True)
    api_key = models.CharField(max_length=256, null=True, blank=True)
    public_key = models.CharField(max_length=256, null=True, blank=True)
    private_key = models.CharField(max_length=256, null=True, blank=True)
    code = models.CharField(max_length=256, null=True, blank=True)
    admission = models.BooleanField(default=False)
    incur_charges = models.BooleanField(default=True)

    def __str__(self):
        return str(self.name+" "+str(self.amount))


class TuitionFee(models.Model):
    first = models.FloatField()
    second = models.FloatField()
    total = models.FloatField()
    dept = models.ForeignKey(Dept)
