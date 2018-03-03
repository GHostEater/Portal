# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from paymenttype.models import PaymentType
from accounts.models import Student, Lecturer

# Create your models here.


class WavedPayment(models.Model):
    payment_type = models.ForeignKey(PaymentType)
    student = models.ForeignKey(Student)
    waved_by = models.ForeignKey(Lecturer)
