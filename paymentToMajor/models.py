# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from paymentType.models import PaymentType
from major.models import Major
from level.models import Level
# Create your models here.


class PaymentToMajor(models.Model):
    paymentType = models.ForeignKey(PaymentType)
    major = models.ForeignKey(Major)
    level = models.ForeignKey(Level)
