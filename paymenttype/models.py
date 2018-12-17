# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from major.models import Major


class PaymentType(models.Model):
    sex_choices = (
        ("Male", "Male"),
        ("Female", "Female"),
        ("Both", "Both")
    )
    
    name = models.CharField(max_length=100)
    amount = models.FloatField()
    merchant_id = models.CharField(max_length=256, null=True, blank=True)
    service_type_id = models.CharField(max_length=256, null=True, blank=True)
    api_key = models.CharField(max_length=256, null=True, blank=True)
    public_key = models.CharField(max_length=256, null=True, blank=True)
    private_key = models.CharField(max_length=256, null=True, blank=True)
    code = models.CharField(max_length=256, null=True, blank=True)
    admission = models.BooleanField(default=False)
    tuition = models.BooleanField(default=False)
    sex = models.CharField(max_length=256, default="Both", choices=sex_choices)
    incur_charges = models.BooleanField(default=True)
    tag = models.CharField(max_length=256, null=True, blank=True)

    def __str__(self):
        return str(self.name+" "+str(self.amount))


class TuitionFee(models.Model):
    first = models.FloatField()
    second = models.FloatField()
    total = models.FloatField()
    major = models.ForeignKey(Major)
    jme = models.BooleanField(default=False)
    de = models.BooleanField(default=False)
    conversion = models.BooleanField(default=False)
    ft = models.BooleanField(default=True)
    pt = models.BooleanField(default=False)
