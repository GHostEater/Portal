# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.db.models.signals import post_save

# Create your models here.


class Session(models.Model):
    session = models.CharField(max_length=20, default='')
    start_date = models.DateField(null=True, blank=True)
    is_current = models.BooleanField(default='1')
    is_admission = models.BooleanField(default='0')
    actions = models.BooleanField(default='0')

    def __str__(self):
        return str(self.session)
