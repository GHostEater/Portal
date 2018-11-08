# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from level.models import Level
from paymenttype.models import PaymentType
from accounts.models import Student, Bursar


# Create your models here.


class WavedPayment(models.Model):
    payment_type = models.ForeignKey(PaymentType)
    student = models.ForeignKey(Student)
    level = models.ForeignKey(Level)
    waved_by = models.ForeignKey(Bursar)
