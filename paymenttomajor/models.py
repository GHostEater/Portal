# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from paymenttype.models import PaymentType
from major.models import Major
from level.models import Level
# Create your models here.


class PaymentToMajor(models.Model):
    payment_type = models.ForeignKey(PaymentType)
    major = models.ForeignKey(Major)
    level = models.ForeignKey(Level)
    jme = models.BooleanField(default=False)
    de = models.BooleanField(default=False)
    conversion = models.BooleanField(default=False)
    pt = models.BooleanField(default=False)

    def __str__(self):
        return str(str(self.payment_type)+str(self.major)+str(self.level)+" JME:"+str(self.jme)+" D/E:"+str(self.de) +
                   " Conversion:"+str(self.conversion)+" Part Time:"+str(self.pt))
