# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from paymentType.models import PaymentType
from accounts.models import Student
from session.models import Session

# Create your models here.


class Payment(models.Model):
    paymentType = models.ForeignKey(PaymentType)
    student = models.ForeignKey(Student)
    session = models.ForeignKey(Session)
    rrr = models.CharField(max_length=500)
    date = models.DateTimeField(null=True, blank=True)
    status = models.IntegerField(default=0)
