# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from admission.models import Application
from level.models import Level
from paymenttype.models import PaymentType
from accounts.models import Student
from session.models import Session

# Create your models here.


class Payment(models.Model):
    type_choices = (
        ("Web", "Web"),
        ("eCashier", "eCashier"),
    )

    payment_type = models.ForeignKey(PaymentType)
    type = models.CharField(max_length=256, choices=type_choices, default="Web")
    student = models.ForeignKey(Student, null=True, blank=True)
    application = models.ForeignKey(Application, null=True, blank=True)
    session = models.ForeignKey(Session, null=True, blank=True)
    level = models.ForeignKey(Level, null=True, blank=True)
    transaction_id = models.CharField(max_length=256, null=True, blank=True)
    prn = models.TextField(null=True, blank=True)
    date = models.DateTimeField(null=True, blank=True)
    status = models.TextField(null=True, blank=True)
    paid = models.BooleanField(default=False)
    amount = models.FloatField(null=True, blank=True)

    def __str__(self):
        return str(str(self.student)+" "+str(self.application)+" "+str(self.payment_type)+" Type:"+str(self.type)
                   + " PRN:"+str(self.prn)+" Paid: "+str(self.paid)+", Status:"+str(self.status)
                   + ", Date:"+str(self.date))
