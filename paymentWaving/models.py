# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from paymentType.models import PaymentType
from accounts.models import Student, Lecturer

# Create your models here.


class WavedPayment(models.Model):
    paymentType = models.ForeignKey(PaymentType)
    student = models.ForeignKey(Student)
    wavedBy = models.ForeignKey(Lecturer)
